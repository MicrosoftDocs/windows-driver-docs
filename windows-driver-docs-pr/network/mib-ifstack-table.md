---
title: MIB_IFSTACK_TABLE structure (Windows Drivers)
description: Learn more about the MIB_IFSTACK_TABLE structure.
keywords:
- MIB_IFSTACK_TABLE
- PMIB_IFSTACK_TABLE
- netioapi/MIB_IFSTACK_TABLE
- netioapi/PMIB_IFSTACK_TABLE
ms.date: 10/25/2022
---

# MIB\_IFSTACK\_TABLE structure

The MIB\_IFSTACK\_TABLE structure contains a table of network interface stack row entries. This table specifies the relationship of the network interfaces on an interface stack.

## Syntax

``` c++
typedef struct _MIB_IFSTACK_TABLE {
  ULONG           NumEntries;
  MIB_IFSTACK_ROW Table[ANY_SIZE];
} MIB_IFSTACK_TABLE, *PMIB_IFSTACK_TABLE;
```

## Members

- **NumEntries**  
   The number of interface stack row entries in the array.

- **Table**  
   An array of [**MIB\_IFSTACK\_ROW**](mib-ifstack-row.md) structures that contain interface stack row entries.

## Remarks

The relationship between the interfaces in the interface stack is that the interface with the index in the **HigherLayerInterfaceIndex** member of the MIB\_IFSTACK\_ROW structure is immediately above the interface with the index in the **LowerLayerInterfaceIndex** member of the MIB\_IFSTACK\_ROW structure.

The [**GetIfStackTable**](getifstacktable.md) function enumerates the network interface stack row entries on a local computer and returns this information in a MIB\_IFSTACK\_TABLE structure.

The MIB\_IFSTACK\_TABLE structure might contain padding for alignment between the **NumEntries** member and the first MIB\_IFSTACK\_ROW array entry in the **Table** member. Padding for alignment might also be present between the MIB\_IFSTACK\_ROW array entries in the **Table** member. Any access to a MIB\_IFSTACK\_ROW array entry should assume padding might exist.

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

[**GetIfStackTable**](getifstacktable.md)

[**GetInvertedIfStackTable**](getinvertedifstacktable.md)

[**MIB\_IFSTACK\_ROW**](mib-ifstack-row.md)

[**MIB\_INVERTEDIFSTACK\_ROW**](mib-invertedifstack-row.md)

[**MIB\_INVERTEDIFSTACK\_TABLE**](mib-invertedifstack-table.md)
