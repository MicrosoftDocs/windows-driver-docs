---
title: MIB_UNICASTIPADDRESS_TABLE structure (Windows Drivers)
description: Learn more about the MIB_UNICASTIPADDRESS_TABLE structure.
keywords:
- MIB_UNICASTIPADDRESS_TABLE
- PMIB_UNICASTIPADDRESS_TABLE
- netioapi/MIB_UNICASTIPADDRESS_TABLE
- netioapi/PMIB_UNICASTIPADDRESS_TABLE
ms.date: 10/25/2022
ms.topic: reference
---

# MIB\_UNICASTIPADDRESS\_TABLE structure

The MIB\_UNICASTIPADDRESS\_TABLE structure contains a table of unicast IP address entries.

## Syntax

``` c++
typedef struct _MIB_UNICASTIPADDRESS_TABLE {
  ULONG                    NumEntries;
  MIB_UNICASTIPADDRESS_ROW Table[ANY_SIZE];
} MIB_UNICASTIPADDRESS_TABLE, *PMIB_UNICASTIPADDRESS_TABLE;
```

## Members

- **NumEntries**  
   A value that specifies the number of unicast IP address entries in the array.

- **Table**  
   An array of [**MIB\_UNICASTIPADDRESS\_ROW**](mib-unicastipaddress-row.md) structures that contains unicast IP address entries.

## Remarks

The [**GetUnicastIpAddressTable**](getunicastipaddresstable.md) function enumerates the unicast IP addresses on a local computer and returns this information in an MIB\_UNICASTIPADDRESS\_TABLE structure.

The MIB\_UNICASTIPADDRESS\_TABLE structure might contain padding for alignment between the **NumEntries** member and the first [**MIB\_UNICASTIPADDRESS\_ROW**](mib-unicastipaddress-row.md) array entry in the **Table** member. Padding for alignment might also be present between the MIB\_UNICASTIPADDRESS\_ROW array entries in the **Table** member. Any access to a MIB\_UNICASTIPADDRESS\_ROW array entry should assume padding might exist.

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

[**GetUnicastIpAddressTable**](getunicastipaddresstable.md)

[**MIB\_UNICASTIPADDRESS\_ROW**](mib-unicastipaddress-row.md)
