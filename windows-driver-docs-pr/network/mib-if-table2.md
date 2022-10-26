---
title: MIB_IF_TABLE2 structure (Windows Drivers)
description: Learn more about the MIB_IF_TABLE2 structure.
keywords:
- MIB_IF_TABLE2
- PMIB_IF_TABLE2
- netioapi/MIB_IF_TABLE2
- netioapi/PMIB_IF_TABLE2
ms.date: 10/25/2022
---

# MIB\_IF\_TABLE2 structure

The MIB\_IF\_TABLE2 structure contains a table of logical and physical interface entries.

## Syntax

``` c++
typedef struct _MIB_IF_TABLE2 {
  ULONG       NumEntries;
  MIB_IF_ROW2 Table[ANY_SIZE];
} MIB_IF_TABLE2, *PMIB_IF_TABLE2;
```

## Members

- **NumEntries**  
   The number of interface entries in the array.

- **Table**  
   An array of [**MIB\_IF\_ROW2**](mib-if-row2.md) structures that contain interface entries.

## Remarks

The [**GetIfTable2**](getiftable2.md) and [**GetIfTable2Ex**](getiftable2ex.md) functions enumerate the logical and physical interfaces on a local computer and return this information in a MIB\_IF\_TABLE2 structure.

The MIB\_IF\_TABLE2 structure might contain padding for alignment between the **NumEntries** member and the first MIB\_IF\_ROW2 array entry in the **Table** member. Padding for alignment might also be present between the MIB\_IF\_ROW2 array entries in the **Table** member. Any access to a MIB\_IF\_ROW2 array entry should assume padding might exist.

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

[**GetIfTable2**](getiftable2.md)

[**GetIfTable2Ex**](getiftable2ex.md)

[**MIB\_IF\_ROW2**](mib-if-row2.md)
