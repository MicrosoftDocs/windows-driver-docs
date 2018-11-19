---
title: WDI_TLV_ADAPTER_NLO_SCAN_MODE
description: WDI_TLV_ADAPTER_NLO_SCAN_MODE is a TLV that indicates whether scans should be performed in active or passive mode.
ms.assetid: 4294AF4D-587E-4978-9C54-E11D7368FBB8
ms.date: 07/18/2017
keywords:
 - WDI_TLV_ADAPTER_NLO_SCAN_MODE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ADAPTER\_NLO\_SCAN\_MODE


WDI\_TLV\_ADAPTER\_NLO\_SCAN\_MODE is a TLV that indicates whether scans should be performed in active or passive mode.

## TLV Type


0x125

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                                     |
|--------|---------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | [**WDI\_SCAN\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/dn926115) value that indicates whether scans should be performed in active or passive mode. |

 

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

 

 




