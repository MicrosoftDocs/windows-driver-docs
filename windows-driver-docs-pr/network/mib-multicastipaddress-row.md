---
title: MIB_MULTICASTIPADDRESS_ROW structure (Windows Drivers)
description: Learn more about the MIB_MULTICASTIPADDRESS_ROW structure.
keywords:
- MIB_MULTICASTIPADDRESS_ROW
- PMIB_MULTICASTIPADDRESS_ROW
- netioapi/MIB_MULTICASTIPADDRESS_ROW
- netioapi/PMIB_MULTICASTIPADDRESS_ROW
ms.date: 10/25/2022
ms.topic: reference
---

# MIB\_MULTICASTIPADDRESS\_ROW structure

The MIB\_MULTICASTIPADDRESS\_ROW structure stores information about a multicast IP address.

## Syntax

``` c++
typedef struct _MIB_MULTICASTIPADDRESS_ROW {
  SOCKADDR_INET Address;
  NET_IFINDEX   InterfaceIndex;
  NET_LUID      InterfaceLuid;
  SCOPE_ID      ScopeId;
} MIB_MULTICASTIPADDRESS_ROW, *PMIB_MULTICASTIPADDRESS_ROW;
```

## Members

- **Address**  
   The multicast IP address. This member can be an IPv6 address or an IPv4 address.

- **InterfaceIndex**  
   The local index value for the network interface that is associated with this IP address. This index value might change when a network adapter is disabled and then enabled, or under other circumstances, and should not be considered persistent.

- **InterfaceLuid**  
   The locally unique identifier (LUID) for the network interface that is associated with this IP address.

- **ScopeId**  
   The scope ID of the multicast IP address. This member is applicable only to an IPv6 address. Your driver cannot set this member. This member is automatically determined by the interface that the address was added on.

## Remarks

The [**GetMulticastIpAddressTable**](getmulticastipaddresstable.md) function enumerates the multicast IP addresses on a local computer and returns this information in a [**MIB\_MULTICASTIPADDRESS\_TABLE**](mib-multicastipaddress-table.md) structure. The **GetMulticastIpAddressEntry** function retrieves a single multicast IP address and returns this information in a MIB\_MULTICASTIPADDRESS\_ROW structure.

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Netioapi.h (include Netioapi.h)</td>
</tr>
</tbody>
</table>

## See also

[**FlushIpPathTable**](flushippathtable.md)

[**GetIpPathEntry**](getippathentry.md)

[**GetIpPathTable**](getippathtable.md)

[**GetMulticastIpAddressTable**](getmulticastipaddresstable.md)

[**MIB\_IPPATH\_ROW**](mib-ippath-row.md)

[**MIB\_MULTICASTIPADDRESS\_TABLE**](mib-multicastipaddress-table.md)
