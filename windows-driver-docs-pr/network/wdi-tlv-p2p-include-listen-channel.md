---
title: WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL
description: WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL is a TLV that specifies whether the probe request should include the Listen Channel attribute during discovery.
ms.assetid: 75662669-102A-4186-951C-58D1B36D1686
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_INCLUDE\_LISTEN\_CHANNEL


WDI\_TLV\_P2P\_INCLUDE\_LISTEN\_CHANNEL is a TLV that specifies whether the probe request should include the Listen Channel attribute during discovery.

**Note**  This TLV was added in Windows 10, version 1607, WDI version 1.0.21.

 

## TLV Type


0x128

## Length


The size (in bytes) of a UINT8.

## Values


| Type  | Description                                                                                                                                                           |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8 | This parameter specifies whether the probe request should include the Listen Channel attribute during discovery. Valid values are 0 (do not include) and 1 (include). |

 

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

 

 




