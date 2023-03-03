---
title: MIB_UNICASTIPADDRESS_ROW structure (Windows Drivers)
description: Learn more about the MIB_UNICASTIPADDRESS_ROW structure.
keywords:
- MIB_UNICASTIPADDRESS_ROW
- PMIB_UNICASTIPADDRESS_ROW
- netioapi/MIB_UNICASTIPADDRESS_ROW
- netioapi/PMIB_UNICASTIPADDRESS_ROW
ms.date: 10/25/2022
ms.topic: reference
---

# MIB\_UNICASTIPADDRESS\_ROW structure

The MIB\_UNICASTIPADDRESS\_ROW structure stores information about a unicast IP address.

## Syntax

``` c++
typedef struct _MIB_UNICASTIPADDRESS_ROW {
  SOCKADDR_INET    Address;
  NET_LUID         InterfaceLuid;
  NET_IFINDEX      InterfaceIndex;
  NL_PREFIX_ORIGIN PrefixOrigin;
  NL_SUFFIX_ORIGIN SuffixOrigin;
  ULONG            ValidLifetime;
  ULONG            PreferredLifetime;
  UINT8            OnLinkPrefixLength;
  BOOLEAN          SkipAsSource;
  NL_DAD_STATE     DadState;
  SCOPE_ID         ScopeId;
  LARGE_INTEGER    CreationTimeStamp;
} MIB_UNICASTIPADDRESS_ROW, *PMIB_UNICASTIPADDRESS_ROW;
```

## Members

- **Address**  
   The unicast IP address. This member can be an IPv6 address or an IPv4 address.

- **InterfaceLuid**  
   The locally unique identifier (LUID) for the network interface that is associated with this IP address.

- **InterfaceIndex**  
   The local index value for the network interface that is associated with this IP address. This index value might change when a network adapter is disabled and then enabled, or under other circumstances, and should not be considered persistent.

- **PrefixOrigin**  
   An [**NL\_PREFIX\_ORIGIN**](nl-prefix-origin.md) type that specifies the origin of the prefix or network part of the IP address.

- **SuffixOrigin**  
   An [**NL\_SUFFIX\_ORIGIN**](nl-suffix-origin.md) type that specifies the origin of the suffix or host part of the IP address.

- **ValidLifetime**  
   The maximum time, in seconds, that the IP address is valid. A value of 0xffffffff is considered to be infinite.

- **PreferredLifetime**  
   The preferred time, in seconds, that the IP address is valid. A value of 0xffffffff is considered to be infinite.

- **OnLinkPrefixLength**  
   The length, in bits, of the prefix or network part of the IP address. For a unicast IPv4 address, any value that is greater than 32 is an illegal value. For a unicast IPv6 address, any value that is greater than 128 is an illegal value. A value of 255 is typically used to represent an illegal value.

- **SkipAsSource**  
   A value that specifies if the address can be used as an IP source address.

- **DadState**  
   A [**NL\_DAD\_STATE**](nl-dad-state.md) duplicate address detection (DAD) type.

- **ScopeId**  
   The scope ID of the IP address. This member is applicable only to an IPv6 address. Your driver cannot set this member. This member is automatically determined by the interface that the address was added on.

- **CreationTimeStamp**  
   The time stamp when the IP address was created.

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

[**CreateUnicastIpAddressEntry**](createunicastipaddressentry.md)

[**DeleteUnicastIpAddressEntry**](deleteunicastipaddressentry.md)

[**GetUnicastIpAddressEntry**](getunicastipaddressentry.md)

[**GetUnicastIpAddressTable**](getunicastipaddresstable.md)

[**InitializeUnicastIpAddressEntry**](initializeunicastipaddressentry.md)

[**MIB\_UNICASTIPADDRESS\_TABLE**](mib-unicastipaddress-table.md)

[**NL\_DAD\_STATE**](nl-dad-state.md)

[**NL\_PREFIX\_ORIGIN**](nl-prefix-origin.md)

[**NL\_SUFFIX\_ORIGIN**](nl-suffix-origin.md)

[**SetUnicastIpAddressEntry**](setunicastipaddressentry.md)
