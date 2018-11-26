---
title: WDI_TLV_ADDITIONAL_BEACON_IES
description: WDI_TLV_ADDITIONAL_BEACON_IES is a TLV that contains additional beacon IEs.
ms.assetid: 7B4D863A-1480-4283-A5E9-5F4F043B0CDE
ms.date: 07/18/2017
keywords:
 - WDI_TLV_ADDITIONAL_BEACON_IES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ADDITIONAL\_BEACON\_IES


WDI\_TLV\_ADDITIONAL\_BEACON\_IES is a TLV that contains additional beacon IEs.

## TLV Type


0x98

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                                                                                                                |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | The array of beacon IEs. The Wi-Fi Direct port must add these additional IEs to the beacon packets when it is acting as a Group Owner. These are ignored when the Wi-Fi Direct port is operating in device or client mode. |

 

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

 

 




