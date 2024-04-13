---
title: MIB_IFSTACK_ROW structure (Windows Drivers)
description: Learn more about the MIB_IFSTACK_ROW structure.
keywords:
- MIB_IFSTACK_ROW
- PMIB_IFSTACK_ROW
- netioapi/MIB_IFSTACK_ROW
- netioapi/PMIB_IFSTACK_ROW
ms.date: 10/25/2022
ms.topic: reference
---

# MIB\_IFSTACK\_ROW structure

The MIB\_IFSTACK\_ROW structure represents the relationship between two network interfaces.

## Syntax

``` c++
typedef struct _MIB_IFSTACK_ROW {
  NET_IFINDEX HigherLayerInterfaceIndex;
  NET_IFINDEX LowerLayerInterfaceIndex;
} MIB_IFSTACK_ROW, *PMIB_IFSTACK_ROW;
```

## Members

- **HigherLayerInterfaceIndex**  
   The network interface index for the interface that is higher in the interface stack table.

- **LowerLayerInterfaceIndex**  
   The network interface index for the interface that is lower in the interface stack table.

## Remarks

The relationship between the interfaces in the interface stack is that the interface with the index in the **HigherLayerInterfaceIndex** member is immediately above the interface with the index in the **LowerLayerInterfaceIndex** member.

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

[**MIB\_IFSTACK\_TABLE**](mib-ifstack-table.md)

[**MIB\_INVERTEDIFSTACK\_ROW**](mib-invertedifstack-row.md)

[**MIB\_INVERTEDIFSTACK\_TABLE**](mib-invertedifstack-table.md)
