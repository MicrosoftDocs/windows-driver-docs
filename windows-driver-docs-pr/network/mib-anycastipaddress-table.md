---
title: MIB_ANYCASTIPADDRESS_TABLE structure (Windows Drivers)
description: Learn more about the MIB_ANYCASTIPADDRESS_TABLE structure.
keywords:
- MIB_ANYCASTIPADDRESS_TABLE
- PMIB_ANYCASTIPADDRESS_TABLE
- netioapi/MIB_ANYCASTIPADDRESS_TABLE
- netioapi/PMIB_ANYCASTIPADDRESS_TABLE
ms.date: 10/25/2022
ms.topic: reference
---

# MIB\_ANYCASTIPADDRESS\_TABLE structure

The MIB\_ANYCASTIPADDRESS\_TABLE structure contains a table of anycast IP address entries.

## Syntax

``` c++
typedef struct _MIB_ANYCASTIPADDRESS_TABLE {
  ULONG                    NumEntries;
  MIB_ANYCASTIPADDRESS_ROW Table[ANY_SIZE];
} MIB_ANYCASTIPADDRESS_TABLE, *PMIB_ANYCASTIPADDRESS_TABLE;
```

## Members

- **NumEntries**  
   A value that specifies the number of anycast IP address entries in the array.

- **Table**  
   An array of [**MIB\_ANYCASTIPADDRESS\_ROW**](mib-anycastipaddress-row.md) structures that contain anycast IP address entries.

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

[**GetAnycastIpAddressTable**](getanycastipaddresstable.md)

[**MIB\_ANYCASTIPADDRESS\_ROW**](mib-anycastipaddress-row.md)
