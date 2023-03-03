---
title: MIB_MULTICASTIPADDRESS_TABLE structure (Windows Drivers)
description: Learn more about the MIB_MULTICASTIPADDRESS_TABLE structure.
keywords:
- MIB_MULTICASTIPADDRESS_TABLE
- PMIB_MULTICASTIPADDRESS_TABLE
- netioapi/MIB_MULTICASTIPADDRESS_TABLE
- netioapi/PMIB_MULTICASTIPADDRESS_TABLE
ms.date: 10/25/2022
ms.topic: reference
---

# MIB\_MULTICASTIPADDRESS\_TABLE structure

The MIB\_MULTICASTIPADDRESS\_TABLE structure contains a table of multicast IP address entries.

## Syntax

``` c++
typedef struct _MIB_MULTICASTIPADDRESS_TABLE {
  ULONG                      NumEntries;
  MIB_MULTICASTIPADDRESS_ROW Table[ANY_SIZE];
} MIB_MULTICASTIPADDRESS_TABLE, *PMIB_MULTICASTIPADDRESS_TABLE;
```

## Members

- **NumEntries**  
   A value that specifies the number of multicast IP address entries in the array.

- **Table**  
   An array of [**MIB\_MULTICASTIPADDRESS\_ROW**](mib-multicastipaddress-row.md) structures that contain multicast IP address entries.

## Remarks

The [**GetMulticastIpAddressTable**](getmulticastipaddresstable.md) function enumerates the multicast IP addresses on a local computer and returns this information in an MIB\_MULTICASTIPADDRESS\_TABLE structure.

The MIB\_MULTICASTIPADDRESS\_TABLE structure might contain padding for alignment between the **NumEntries** member and the first [**MIB\_MULTICASTIPADDRESS\_ROW**](mib-multicastipaddress-row.md) array entry in the **Table** member. Padding for alignment might also be present between the MIB\_MULTICASTIPADDRESS\_ROW array entries in the **Table** member. Any access to a MIB\_MULTICASTIPADDRESS\_ROW array entry should assume padding might exist.

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

[**GetMulticastIpAddressTable**](getmulticastipaddresstable.md)

[**MIB\_MULTICASTIPADDRESS\_ROW**](mib-multicastipaddress-row.md)
