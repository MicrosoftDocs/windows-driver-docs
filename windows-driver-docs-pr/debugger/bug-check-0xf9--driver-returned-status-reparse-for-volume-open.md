---
title: Bug Check 0xF9 DRIVER_RETURNED_STATUS_REPARSE_FOR_VOLUME_OPEN
description: The DRIVER_RETURNED_STATUS_REPARSE_FOR_VOLUME_OPEN bug check that indicates that a driver returned STATUS_REPARSE to an IRP_MJ_CREATE request with no trailing names.
keywords: ["Bug Check 0xF9 DRIVER_RETURNED_STATUS_REPARSE_FOR_VOLUME_OPEN", "DRIVER_RETURNED_STATUS_REPARSE_FOR_VOLUME_OPEN"]
ms.date: 07/21/2020
topic_type:
- apiref
ms.topic: reference
api_name:
- DRIVER_RETURNED_STATUS_REPARSE_FOR_VOLUME_OPEN
api_type:
- NA
---

# Bug Check 0xF9: DRIVER\_RETURNED\_STATUS\_REPARSE\_FOR\_VOLUME\_OPEN

The DRIVER\_RETURNED\_STATUS\_REPARSE\_FOR\_VOLUME\_OPEN bug check has a value of 0x000000F9. This indicates that a driver returned STATUS\_REPARSE to an IRP\_MJ\_CREATE request with no trailing names.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


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

## Remarks

The [**!analyze**](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

STATUS\_REPARSE should be returned only for IRP\_MJ\_CREATE requests with trailing names, as that indicates the driver is supporting name spaces. 

For more information about working with file system drivers, see [File systems driver design guide](../ifs/index.md). For information about IRP\_MJ\_CREATE requests see [IRP_MJ_CREATE (IFS)](../ifs/irp-mj-create.md).
