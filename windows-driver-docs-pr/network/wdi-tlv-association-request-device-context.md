---
title: WDI_TLV_ASSOCIATION_REQUEST_DEVICE_CONTEXT
description: WDI_TLV_ASSOCIATION_REQUEST_DEVICE_CONTEXT is a TLV that contains vendor-specific information that is passed down to the port if the host decides to send a response to a incoming association request.
ms.assetid: 5C684769-77A0-446D-81F6-A90E54806A1F
ms.date: 07/18/2017
keywords:
 - WDI_TLV_ASSOCIATION_REQUEST_DEVICE_CONTEXT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ASSOCIATION\_REQUEST\_DEVICE\_CONTEXT


WDI\_TLV\_ASSOCIATION\_REQUEST\_DEVICE\_CONTEXT is a TLV that contains vendor-specific information that is passed down to the port if the host decides to send a response to a incoming association request.

## TLV Type


0x72

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                           |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | Vendor-specific information that is passed down to the port if the host decides to send a response to a incoming association request. |

 

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

 

 




