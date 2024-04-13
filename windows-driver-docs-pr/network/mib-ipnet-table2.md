---
title: MIB_IPNET_TABLE2 structure (Windows Drivers)
description: Learn more about the MIB_IPNET_TABLE2 structure.
keywords:
- MIB_IPNET_TABLE2
- PMIB_IPNET_TABLE2
- netioapi/MIB_IPNET_TABLE2
- netioapi/PMIB_IPNET_TABLE2
ms.date: 10/25/2022
ms.topic: reference
---

# MIB\_IPNET\_TABLE2 structure

The MIB\_IPNET\_TABLE2 structure contains a table of neighbor IP address entries.

## Syntax

``` c++
typedef struct _MIB_IPNET_TABLE2 {
  ULONG          NumEntries;
  MIB_IPNET_ROW2 Table[ANY_SIZE];
} MIB_IPNET_TABLE2, *PMIB_IPNET_TABLE2;
```

## Members

- **NumEntries**  
   A value that specifies the number of IP network neighbor address entries in the array.

- **Table**  
   An array of [**MIB\_IPNET\_ROW2**](mib-ipnet-row2.md) structures that contain IP network neighbor address entries.

## Remarks

The [**GetIpNetTable2**](getipnettable2.md) function enumerates the neighbor IP addresses on a local computer and returns this information in an MIB\_IPNET\_TABLE2 structure. For IPv4, this information includes addresses determined by using the Address Resolution Protocol (ARP). For IPv6, this information includes addresses determined by using the Neighbor Discovery (ND) protocol for IPv6 as specified in RFC 2461. For more information, see [Neighbor Discovery for IP Version 6 (IPv6)](https://go.microsoft.com/fwlink/p/?linkid=84044).

The MIB\_IPNET\_TABLE2 structure might contain padding for alignment between the **NumEntries** member and the first [**MIB\_IPNET\_ROW2**](mib-ipnet-row2.md) array entry in the **Table** member. Padding for alignment might also be present between the MIB\_IPNET\_ROW2 array entries in the **Table** member. Any access to a MIB\_IPNET\_ROW2 array entry should assume that padding might exist.

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

[**GetIpNetTable2**](getipnettable2.md)

[**MIB\_IPNET\_ROW2**](mib-ipnet-row2.md)
