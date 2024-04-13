---
title: WDI_TLV_BSS_ENTRY_DEVICE_CONTEXT
ms.topic: reference
description: WDI_TLV_BSS_ENTRY_DEVICE_CONTEXT is a TLV that contains device context for the BSS entry.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_BSS_ENTRY_DEVICE_CONTEXT Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_BSS\_ENTRY\_DEVICE\_CONTEXT

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_BSS\_ENTRY\_DEVICE\_CONTEXT is a TLV that contains device context for the BSS entry.

## TLV Type


0xD

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                                                                                                                                                                                |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that specifies the context data. This context is provided by the IHV component and can be used to store per-BSS entry state that the IHV component wants to maintain. To avoid lifetime management issues, the IHV component must not use pointers in this TLV. |

 

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

 

 




