---
title: MIB_ANYCASTIPADDRESS_ROW structure (Windows Drivers)
description: Learn more about the MIB_ANYCASTIPADDRESS_ROW structure.
keywords:
- MIB_ANYCASTIPADDRESS_ROW
- PMIB_ANYCASTIPADDRESS_ROW
- netioapi/MIB_ANYCASTIPADDRESS_ROW
- netioapi/PMIB_ANYCASTIPADDRESS_ROW
ms.date: 10/25/2022
---

# MIB\_ANYCASTIPADDRESS\_ROW structure

The MIB\_ANYCASTIPADDRESS\_ROW structure stores information about an anycast IP address.

## Syntax

``` c++
typedef struct _MIB_ANYCASTIPADDRESS_ROW {
  SOCKADDR_INET Address;
  NET_LUID      InterfaceLuid;
  NET_IFINDEX   InterfaceIndex;
  SCOPE_ID      ScopeId;
} MIB_ANYCASTIPADDRESS_ROW, *PMIB_ANYCASTIPADDRESS_ROW;
```

## Members

- **Address**  
   The anycast IP address. This member can be an IPv6 address or an IPv4 address.

- **InterfaceLuid**  
   The locally unique identifier (LUID) for the network interface that is associated with this IP address.

- **InterfaceIndex**  
   The local index value for the network interface that is associated with this IP address. This index value might change when a network adapter is disabled and then enabled, or under other circumstances, and should not be considered persistent.

- **ScopeId**  
   The scope ID of the anycast IP address. This member is applicable only to an IPv6 address. Your driver cannot set this member. This member is automatically determined by the interface that the address was added on.

## Remarks

The [**GetAnycastIpAddressTable**](getanycastipaddresstable.md) function enumerates the anycast IP addresses on a local computer and returns this information in a [**MIB\_ANYCASTIPADDRESS\_TABLE**](mib-anycastipaddress-table.md) structure.

The MIB\_ANYCASTIPADDRESS\_TABLE structure might contain padding for alignment between the **NumEntries** member and the first MIB\_ANYCASTIPADDRESS\_ROW array entry in the **Table** member. Padding for alignment might also be present between the MIB\_ANYCASTIPADDRESS\_ROW array entries in the **Table** member. Any access to a MIB\_ANYCASTIPADDRESS\_ROW array entry should assume padding might exist.

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

[**CreateAnycastIpAddressEntry**](createanycastipaddressentry.md)

[**DeleteAnycastIpAddressEntry**](deleteanycastipaddressentry.md)

[**GetAnycastIpAddressTable**](getanycastipaddresstable.md)

[**GetAnycastIpAddressEntry**](getanycastipaddressentry.md)

[**MIB\_ANYCASTIPADDRESS\_TABLE**](mib-anycastipaddress-table.md)
