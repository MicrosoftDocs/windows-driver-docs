---
title: Bug Check 0xF9 DRIVER_RETURNED_STATUS_REPARSE_FOR_VOLUME_OPEN
description: The DRIVER_RETURNED_STATUS_REPARSE_FOR_VOLUME_OPEN bug check that indicates that a driver returned STATUS_REPARSE to an IRP_MJ_CREATE request with no trailing names.
ms.assetid: 60eeb24a-accf-4db8-ba5b-1738a9aa4b46
keywords: ["Bug Check 0xF9 DRIVER_RETURNED_STATUS_REPARSE_FOR_VOLUME_OPEN", "DRIVER_RETURNED_STATUS_REPARSE_FOR_VOLUME_OPEN"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DRIVER_RETURNED_STATUS_REPARSE_FOR_VOLUME_OPEN
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xF9: DRIVER\_RETURNED\_STATUS\_REPARSE\_FOR\_VOLUME\_OPEN


The DRIVER\_RETURNED\_STATUS\_REPARSE\_FOR\_VOLUME\_OPEN bug check has a value of 0x000000F9. This indicates that a driver returned STATUS\_REPARSE to an IRP\_MJ\_CREATE request with no trailing names.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## DRIVER\_RETURNED\_STATUS\_REPARSE\_FOR\_VOLUME\_OPEN Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>The device object that was opened</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The device object to which the IRP_MJ_CREATE request was issued</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Address of the Unicode string containing the new name of the file (to be reparsed)</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Information returned by the driver for the IRP_MJ_CREATE request</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

STATUS\_REPARSE should be returned only for IRP\_MJ\_CREATE requests with trailing names, as that indicates the driver is supporting name spaces.

 

 




