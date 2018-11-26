---
title: WDI_TLV_DISCONNECT_DEAUTH_FRAME
description: WDI_TLV_DISCONNECT_DEAUTH_FRAME is a TLV that contains the received deauthentication frame.
ms.assetid: 394B83C7-D001-4816-BC38-42325469863C
ms.date: 07/18/2017
keywords:
 - WDI_TLV_DISCONNECT_DEAUTH_FRAME Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_DISCONNECT\_DEAUTH\_FRAME


WDI\_TLV\_DISCONNECT\_DEAUTH\_FRAME is a TLV that contains the received deauthentication frame.

## TLV Type


0x37

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                   |
|-----------|-------------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that contains the received deauthentication frame. |

 

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

 

 




