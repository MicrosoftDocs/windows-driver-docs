---
title: Bug Check 0xE8 INVALID_CANCEL_OF_FILE_OPEN
description: The INVALID_CANCEL_OF_FILE_OPEN bug check has a value of 0x000000E8. This indicates that an invalid file object was passed to IoCancelFileOpen.
keywords: ["Bug Check 0xE8 INVALID_CANCEL_OF_FILE_OPEN", "INVALID_CANCEL_OF_FILE_OPEN"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- INVALID_CANCEL_OF_FILE_OPEN
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xE8: INVALID\_CANCEL\_OF\_FILE\_OPEN


The INVALID\_CANCEL\_OF\_FILE\_OPEN bug check has a value of 0x000000E8. This indicates that an invalid file object was passed to **IoCancelFileOpen**.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## INVALID\_CANCEL\_OF\_FILE\_OPEN Parameters


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
<td align="left"><p>The file object passed to <strong>IoCancelFileOpen</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The device object passed to <strong>IoCancelFileOpen</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

## Cause

The file object passed to **IoCancelFileOpen** is invalid. It should have reference of one. The driver that called **IoCancelFileOpen** is at fault.

 

 




