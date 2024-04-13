---
title: WDI_TLV_OPERATION_MODE
ms.topic: reference
description: WDI_TLV_OPERATION_MODE is a TLV that contains the desired operation mode.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_OPERATION_MODE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_OPERATION\_MODE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_OPERATION\_MODE is a TLV that contains the desired operation mode.

## TLV Type


0x95

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                        |
|--------|----------------------------------------------------------------------------------------------------|
| UINT32 | The desired operation mode, as defined in [**WDI\_OPERATION\_MODE**](/windows-hardware/drivers/ddi/dot11wdi/ne-dot11wdi-_wdi_operation_mode). |

 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

