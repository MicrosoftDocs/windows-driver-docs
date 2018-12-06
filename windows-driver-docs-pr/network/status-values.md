---
title: Status Values
description: Status Values
ms.assetid: 1d5cce4a-9830-4e2e-af90-fc1fecfb0fc9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Status Values





The Remote NDIS status values are generally equivalent to the 32-bit status values that are defined in the Microsoft Windows 2000 Driver Development Kit (DDK). The specific Remote NDIS status values used in this specification are listed below, others can be inferred from the Windows 2000 DDK or online documentation. A device may return any semantically correct Remote NDIS status value in a *Status* field of a message that it generates.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Status Identifier</th>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>RNDIS_STATUS_SUCCESS</p></td>
<td align="left"><p>0x00000000</p></td>
<td align="left"><p>Success</p></td>
</tr>
<tr class="even">
<td align="left"><p>RNDIS_STATUS_FAILURE</p></td>
<td align="left"><p>0xC00000001</p></td>
<td align="left"><p>Unspecified error (equivalent to STATUS_UNSUCCESSFUL)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>RNDIS_STATUS_INVALID_DATA</p></td>
<td align="left"><p>0xC0010015</p></td>
<td align="left"><p>Invalid data error</p></td>
</tr>
<tr class="even">
<td align="left"><p>RNDIS_STATUS_NOT_SUPPORTED</p></td>
<td align="left"><p>0xC00000BB</p></td>
<td align="left"><p>Unsupported request error</p></td>
</tr>
<tr class="odd">
<td align="left"><p>RNDIS_STATUS_MEDIA_CONNECT</p></td>
<td align="left"><p>0x4001000B</p></td>
<td align="left"><p>Device is connected to network medium (equivalent to NDIS_STATUS_MEDIA_CONNECT from Windows 2000 DDK)</p></td>
</tr>
<tr class="even">
<td align="left"><p>RNDIS_STATUS_MEDIA_DISCONNECT</p></td>
<td align="left"><p>0x4001000C</p></td>
<td align="left"><p>Device is disconnected from network medium (equivalent to NDIS_STATUS_MEDIA_DISCONNECT from Windows 2000 DDK)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>RNDIS_STATUS_Xxx</p></td>
<td align="left"><p>...</p></td>
<td align="left"><p>Equal to NDIS_STATUS_Xxx values defined in Windows 2000 DDK or online documentation</p></td>
</tr>
</tbody>
</table>

 

 

 





