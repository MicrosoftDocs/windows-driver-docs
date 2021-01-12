---
title: Overview of NDIS packet timestamping
description: NDIS packet timestamping supports NICs' hardware timestamping capabilities
ms.date: 12/31/2020
ms.localizationpriority: medium
---

# Overview of NDIS packet timestamping

)This API is a part of changes which enable Windows...) 

Starting with NDIS 6.82, the NDIS packet timestamping interface enables Windows to support the hardware timestamping capability of network cards for the Precision Time Protocol (PTP) version 2 protocol. 

Overall these changes include providing the ability to drivers of network cards to support timestamps, for user mode applications to query timestamp configuration (through iphlpapi) and consume timestamps associated with packets (through Winsock). In addition, an ability to generate software timestamps is also introduced as part of these changes which allows a network driver to generate timestamps in software.

The APIs provide the following abilities:

- Provide ability to discover NIC hardware’s timestamping capabilities.

- Provide ability to associate NIC hardware clock’s timestamps to PTP version 2 traffic running over UDP (using the standard UDP ports defined for PTP, for example 319 and 320).

- Provide ability to use the network hardware’s clock as a free running clock by being able to query the network hardware’s clock to enable establishment of a relation between the network hardware clock and a system clock.

The target of these APIs is Ethernet hardware. The API is intended to work both with NICs which have support specifically for generating hardware timestamps for PTP traffic, as well as with NICs which can generate hardware timestamps for all traffic and so would work with PTP traffic as well.

(As mentioned above, the main scenario intended to be supported is PTP version 2. All references to PTP throughout the document should be assumed to apply to PTP version 2 wherever the version of PTP is not explicitly specified.) - remove, though wording helpful

From INF page: "**Exactly which hardware timestamping capabilities should be enabled** depends on the capabilities of the NIC hardware. As outlined on (ADD LINK), **the main scenario** which needs to be addressed is PTP version 2 over UDP (for both IPv4 and IPv6) operating in 2 step mode. This is the scenario that the **\*PtpHardwareTimestamp** keyword addresses. Supporting hardware timestamping for PTP version 2 over UDP (in 2 step mode) for both Rx and Tx direction should be the main consideration when determining which hardware timestamping capabilities in hardware should be enabled when this keyword is set to enabled." (Maybe just add second sentence)

## Miscellaneous implementation notes (add elsewhere)

- Cross timestamps must be supported when supporting hardware timestamps.

- When recognizing PTPv2 packets to generate hardware timestamps, the implementation should aim as much as possible to not restrict timestamp generation to only those packets which are using the multicast addresses (both IPv4 and IPv6) which are specified by the PTP specification. The implementation should try to recognize PTP packets in other ways, e.g. based on the UDP header, or the PTP payload. This would help in scenarios where a PTP implementation might not be using the multicast addresses specified in the PTP specification e.g. unicast address are being used.
-  
- An implementation must support hardware timestamps. Software timestamps are optional.

- If an implementation finds both hardware and software timestamps as enabled through the keywords, then the miniport should only generate hardware timestamps and disable software timestamps. NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG should take this into account.


# Reporting NDIS timestamping capabilities (and current configuration)

Miniport drivers need to indicate the NIC's hardware timestamping capabilities and the miniport driver's software timestamping capabilities (as well as the current configuration of the timestamping capabilities) to NDIS and overlying drivers. (Both of these would be reported to the operating system through status indications). 

(For more information on indicating (?) the driver's current configuration of the timestamping capabilities, see (ADD LINK).)

The support for NDIS timestamping capabilities is enabled or disabled through the setting of the **\*PtpHardwareTimestamp** and **\*SoftwareTimestamp** standardized INF keywords. For more information about these keywords, see [**Standardized INF Keywords for NDIS packet timestamping**](standardized-inf-keywords-for-ndis-packet-timestamping.md).

When NDIS calls the miniport driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function, the driver indicates its hardware and software timestamp capabilities by following these steps:

**All the info in this second is on the status indication page anyway. IS this topic repetiive? Move the below back. just keep this high level, rules to do with both...**
1. The driver initializes an [**NDIS_TIMESTAMP_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_timestamp_capabilities) structure with the NIC's hardware and software timestamp capabilities.
The  driver sets the members of the **NDIS_TIMESTAMP_CAPABILITIES** structure  as follows:
    * The miniport driver uses the **TimestampFlags** field to indicate the hardware and software timestamp capabilities of the NIC hardware and miniport.

    * The **CrossTimestamp** field should be set to **TRUE** if hardware cross timestamps are supported or **FALSE** if they are not.

    * The **HardwareClockFrequencyHz** field should contain the nominal operating frequency of the hardware clock used for timestamping by the NIC. This data may be used to display the nominal clock frequency to end users for informational purposes.

    * The **Type** field in the **Header** field should be set to **NDIS_OBJECT_TYPE_DEFAULT** and the **Revision** to **NDIS_TIMESTAMP_CAPABILITIES_REVISION_1**.

1. Once it has initialized the [**NDIS_TIMESTAMP_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_timestamp_capabilities) structure, the driver generates an [**NDIS_STATUS_TIMESTAMP_CAPABILITY**](ndis-status-timestamp-capability.md) status indication by calling [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex) to report the timestamping capabilities. The **StatusBuffer** field of the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure should point to the initialized **NDIS_TIMESTAMP_CAPABILITIES** structure.

> [!NOTE] 
> The miniport driver must also generate the [**NDIS_STATUS_TIMESTAMP_CAPABILITY**](ndis-status-timestamp-capability.md) status indication whenever it detects a change in underlying hardware capabilities.

# Indicating the timestamping current configuration? / reporting?
determingin, getting, setting, obtaining

Miniport drivers need to indicate the the current configuration of the NIC's hardware timestamping capabilities and the miniport driver's software timestamping capabilities to NDIS and overlying drivers. (Both of these would be reported to the operating system through status indications). 

For more information on reporting the driver's timestamping capabilities, see (ADD LINK). (MAybe have this on the page above. in an overview, say first it reports capabilites, second it reports current configuration. < **Ya. Again, all of the below is alread on the other page. break it down o the other page into steps as well. keep it true to original spec** )

During initialization, the miniport driver should indicate its current timestamping configuration from within its [**MiniportInitializeEx**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function.

Miniport drivers generate **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indications by calling the [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex) function. The **StatusBuffer** field of the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure should point to an [**NDIS_TIMESTAMP_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_timestamp_capabilities) structure.

Info about setting the structure.

The miniport driver must generate an [**NDIS_STATUS_TIMESTAMP_CAPABILITY**](ndis-status-timestamp-capability.md) indication at least once before indicating **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG**. Otherwise NDIS will reject the **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indication and it will not be indicated to overlying drivers.

If the miniport driver indicates a change in the NIC’s hardware timestamping *capability* using the [**NDIS_STATUS_TIMESTAMP_CAPABILITY**](ndis-status-timestamp-capability.md) status indication (for example, a change in the **HardwareClockFrequencyHz** field in the **NDIS_TIMESTAMP_CAPABILITIES** structure because of an underlying change in the NIC hardware), then it must also report the corresponding change in the current configuration using the **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indication.

The miniport driver must also generate the **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indication whenever it detects a change in current timestamping configuration.



# Querying packet timestamping capabilities and current configuration

(For example:

Once the miniport driver is initialized, overlying drivers and applications can issue the following OID query requests to obtain the packet coalescing capabilities of the network adapter:

-   [OID\_RECEIVE\_FILTER\_HARDWARE\_CAPABILITIES](./oid-receive-filter-hardware-capabilities.md)

-   [OID\_RECEIVE\_FILTER\_CURRENT\_CAPABILITIES](./oid-receive-filter-current-capabilities.md)

-   [OID\_RECEIVE\_FILTER\_GLOBAL\_PARAMETERS](./oid-receive-filter-global-parameters.md)

NDIS handles these OID query requests for miniport drivers and returns the packet coalescing capabilities that the miniport driver registered when NDIS called the driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. Therefore, these OID query requests are not handled by miniport drivers.

For more information about how the miniport driver registers its packet coalescing capabilities, see [Determining Receive Filtering Capabilities](determining-receive-filtering-capabilities.md).

end)

An overlying driver issues an object identifier (OID) query request of OID_TIMESTAMP_CAPABILITY to obtain the hardware timestamping capabilities of the NIC and software timestamping capabilities of the miniport driver.

An overlying driver issues an object identifier (OID) query request of OID_TIMESTAMP_GET_CROSSTIMESTAMP to obtain the cross timestamp from the NIC hardware. Precision Time Protocol (PTP) version 2 applications use the information provided in this OID to establish a relation between the NIC’s hardware clock and a system clock. 

# NDIS packet timestamping implementation guidelines?

