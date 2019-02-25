---
title: WDI_TLV_EXTRA_ASSOCIATION_REQUEST_IES
description: WDI_TLV_EXTRA_ASSOCIATION_REQUEST_IES is a TLV that contains Information Elements (IEs) that must be included in association requests sent by the port.
ms.assetid: 2275B8F2-1FE4-4518-AD67-E9A65F2F37DA
ms.date: 07/18/2017
keywords:
 - WDI_TLV_EXTRA_ASSOCIATION_REQUEST_IES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_EXTRA\_ASSOCIATION\_REQUEST\_IES


WDI\_TLV\_EXTRA\_ASSOCIATION\_REQUEST\_IES is a TLV that contains Information Elements (IEs) that must be included in association requests sent by the port.

## TLV Type


0x40

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                                                                                                                                               |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that contains the IEs that must be included in association requests sent by the port. These are applicable to any BSSID that the device associates with. They should be used in addition to the common and BSSID specific IEs. |

 

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

 

 




