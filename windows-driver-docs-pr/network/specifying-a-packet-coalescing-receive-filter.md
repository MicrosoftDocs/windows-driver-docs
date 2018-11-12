---
title: Specifying a Packet Coalescing Receive Filter
description: Specifying a Packet Coalescing Receive Filter
ms.assetid: 0369A63D-4CDE-448A-8472-EEEB7B859B8D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying a Packet Coalescing Receive Filter


An overlying driver can set one or more receive filters on a miniport driver that support NDIS packet coalescing. The overlying driver can specify up to the maximum number of receive filters that the miniport driver specified in the **MaxPacketCoalescingFilters** member of the [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure.

**Note**  The overlying protocol driver obtains the [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure within the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure. The overlying filter driver obtains the **NDIS\_RECEIVE\_FILTER\_CAPABILITIES** structure within the [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481) structure.

 

The overlying driver downloads receive filters to the miniport driver by issuing OID method requests of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795). The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure for this OID request contains a pointer to a caller-allocated buffer. This buffer is formatted to contain the following:

-   An [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure that specifies the parameters for an NDIS receive filter.

    For more information about how to initialize this structure, see [Specifying a Receive Filter](#specifying-receive-filter).

-   An array of [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567169) structures that specifies the filter test criterion for a field in a network packet header.

    For more information about how to initialize these structures, see [Specifying Header Field Tests](#specifying-header-field-test).

## Specifying a Receive Filter


An overlying driver specifies a packet coalescing receive filter by initializing an [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure with the configuration parameters for the filter. When it initializes the **NDIS\_RECEIVE\_FILTER\_PARAMETERS** structure, the overlying driver must follow these rules:

-   The **FilterType** member must be set to the [**NDIS\_RECEIVE\_FILTER\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff567186) enumeration value of **NdisReceiveFilterTypePacketCoalescing**.

-   The **QueueId** member must be set to NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.

    **Note**  Starting with NDIS 6.30, packet coalescing receive filter are only supported on the default receive queue of the network adapter. This receive queue has an identifier of NDIS\_DEFAULT\_RECEIVE\_QUEUE\_ID.

     

-   If the overlying driver is creating a new receive filter, it must set the **FilterId** member to NDIS\_DEFAULT\_RECEIVE\_FILTER\_ID.

    **Note**  NDIS will generate a unique filter identifier (ID) for the receive filter before it forwards the OID method request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795) to the miniport driver.     

-  If the overlying driver is modifying an existing receive filter, it must set the **FilterId** member to the nonzero filter ID of the receive filter. The overlying driver obtains the filter ID for the receive filter when it issues an OID method request of [OID\_RECEIVE\_FILTER\_ENUM\_FILTERS](https://msdn.microsoft.com/library/windows/hardware/ff569787). For more information about how to modify a receive filter, see [Modifying Packet Coalescing Receive Filters](modifying-packet-coalescing-receive-filters.md).

-   The **FieldParametersArrayOffset**, **FieldParametersArrayNumElements**, and **FieldParametersArrayElementSize** members of the [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure must be set to define a field parameter's array. Each element in the array is an [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567169) structure that specifies the parameters for a header field test of a receive filter.

-   The **RequestedFilterIdBitCount** member must be set to zero.

-   The **MaxCoalescingDelay** must be set to the maximum time, in units of milliseconds, that the first packet that matches the receive filter is saved and coalesced on the network adapter. As soon as the first packet that matches the filter is received, the network adapter coalesces the packet and starts a hardware timer whose expiration time is set to the value of the **MaxCoalescingDelay** member.

The overlying driver must order the header field tests in the field parameters array to be in the same order that the associated MAC and protocol headers would exist in a packet.

For example, before the overlying driver specifies the filter parameters for an IP version 4 (IPv4) protocol field, it must first specify the filter parameters for a MAC header protocol field (NdisMacHeaderFieldProtocol). In this manner, the driver specifies a header field test that verifies the field is set to the correct EtherType value (0x0800) for IPv4 packets. If the test fails, the adapter does not have to perform the test of the IPV4 protocol field.

## Specifying Header Field Tests


Each receive filter can specify one or more test criteria (*header field tests*). The network adapter performs these tests to determine whether a received packet should be coalesced in a hardware coalescing buffer on the adapter. Also, the overlying driver can specify separate filter tests for various media access control (MAC), IP version 4 (IPv4), and IP version 6 (IPv6) header fields.

To optimize filtering on the network adapter, header field tests are based on standardized header field names instead of byte offset/length specifications within the packet data. By using header/field names, the network adapter's hardware or firmware can optimize how multiple header field tests are performed on a received packet.

Each receive filter can contain one or more header field tests specified by an [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567169) structure. Each **NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS** structure is an element of the field parameters array that is referenced by the **FieldParametersArrayOffset**, **FieldParametersArrayNumElements**, and **FieldParametersArrayElementSize** members of the [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure.

The miniport driver must follow these guidelines when it handles an OID method request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795):

-   If the **NDIS\_RECEIVE\_FILTER\_FIELD\_MAC\_HEADER\_VLAN\_UNTAGGED\_OR\_ZERO** flag is set in the **Flags** member of the [**NDIS\_RECEIVE\_FILTER\_FIELD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567169) structure, the network adapter must only indicate received packets with a matching MAC address and untagged packets or packets with a VLAN identifier of zero. That is, the network adapter must not indicate packets with a matching MAC address and a nonzero VLAN identifier.

-   If the **NDIS\_RECEIVE\_FILTER\_FIELD\_MAC\_HEADER\_VLAN\_UNTAGGED\_OR\_ZERO** flag is not set and there is no VLAN identifier filter configured by an OID set request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795), the miniport driver must do one of the following:

    -   If the miniport driver supports NDIS 6.20, it must return a failed status for the OID request of [OID\_RECEIVE\_FILTER\_SET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569795).

    -   If the miniport driver supports NDIS 6.30 or later versions of NDIS, it must configure the network adapter to inspect and filter the specified MAC address fields. If a VLAN tag is present in the received packet, the network adapter must remove it from the packet data. The miniport driver must put the VLAN tag in an [**NDIS\_NET\_BUFFER\_LIST\_8021Q\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566565) that is associated with the packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

-   If the overlying driver sets a MAC address filter and a VLAN identifier filter in the [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567181) structure, it does not set the **NDIS\_RECEIVE\_FILTER\_FIELD\_MAC\_HEADER\_VLAN\_UNTAGGED\_OR\_ZERO** flag in either of the filter fields. In this case, the miniport driver should indicate packets that match both the specified MAC address and the VLAN identifier. That is, the miniport driver should not indicate packets with a matching MAC address that have a zero VLAN identifier or are untagged packets.

 

 





