---
title: WDI_TLV_INDICATION_STOP_AP
description: WDI_TLV_INDICATION_STOP_AP is a TLV that contains the reason for a Stop AP indication.
ms.assetid: 49FA6AF6-68BE-437B-9715-5090F52F0109
ms.date: 07/18/2017
keywords:
 - WDI_TLV_INDICATION_STOP_AP Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_INDICATION\_STOP\_AP


WDI\_TLV\_INDICATION\_STOP\_AP is a TLV that contains the reason for a Stop AP indication.

## TLV Type


0xE6

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                  |
|--------|--------------------------------------------------------------------------------------------------------------|
| UINT32 | The Stop AP reason. See [**WDI\_STOP\_AP\_REASON**](https://msdn.microsoft.com/library/windows/hardware/dn926116) for possible reason values. |

 

Requirements
------------

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

## See also


[NDIS\_STATUS\_WDI\_INDICATION\_STOP\_AP](https://msdn.microsoft.com/library/windows/hardware/dn925661)

 

 




