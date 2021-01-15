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


# NDIS packet timestamping implementation guidelines?

put this somewhere? in overview? 
CrossTimestamp: A value of TRUE indicates that the miniport\hardware combination is capable of generating a hardware cross timestamp by handling the OID_TIMESTAMP_GET_CROSSTIMESTAMP OID to generate a cross timestamp. A cross timestamp refers to a set of NIC hardware timestamp and system timestamp(s) obtained very close to each other. How these timestamps are obtained is described in more detail further down in the document. A value of FALSE for the CrossTimestamp field indicates this capability does not exist (alread in capabilities struc)

To determine which timestamping capabilities are currently enabled or disabled, the miniport reads the current values of the timestamping related keywords **\*PtpHardwareTimestamp** and **\*SoftwareTimestamp**. For more information on  using these keywords to enable the timestamping capabilities that the miniport and NIC hardware support, see [Standardized INF keywords for NDIS packet timestamping](standardized-inf-keywords-for-ndis-packet-timestamping.md). (already in cofig indiation)

The flags within the **TimestampFlags** field in the [**NDIS_TIMESTAMP_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_timestamp_capabilities) structure that correspond to hardware timestamping are `PtpV2OverUdpIPv4EventMsgReceiveHw`, `PtpV2OverUdpIPv4AllMsgReceiveHw`, `PtpV2OverUdpIPv4EventMsgTransmitHw`, `PtpV2OverUdpIPv4AllMsgTransmitHw`, `PtpV2OverUdpIPv6EventMsgReceiveHw`, `PtpV2OverUdpIPv6AllMsgReceiveHw`, `PtpV2OverUdpIPv6EventMsgTransmitHw`, `PtpV2OverUdpIPv6AllMsgTransmitHw`, `AllReceiveHw`, `AllTransmitHw` and `TaggedTransmitHw`. The **CrossTimestamp** field in the [**NDIS_TIMESTAMP_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_timestamp_capabilities) structure for **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indicates if hardware cross timestamping is enabled. -* add list to overview? with descriptions.. separatee hw, sw, cross* (from INF page)


Fix PTPv2 over UDP references.
