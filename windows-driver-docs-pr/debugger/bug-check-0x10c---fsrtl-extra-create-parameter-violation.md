---
title: Bug Check 0x10C FSRTL_EXTRA_CREATE_PARAMETER_VIOLATION
description: The FSRTL_EXTRA_CREATE_PARAMETER_VIOLATION bug check has a value of 0x0000010C that indicates that a violation was detected in the FsRtl ECP package.
keywords: ["Bug Check 0x10C FSRTL_EXTRA_CREATE_PARAMETER_VIOLATION", "FSRTL_EXTRA_CREATE_PARAMETER_VIOLATION"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- FSRTL_EXTRA_CREATE_PARAMETER_VIOLATION
api_type:
- NA
---

# Bug Check 0x10C: FSRTL\_EXTRA\_CREATE\_PARAMETER\_VIOLATION


The FSRTL\_EXTRA\_CREATE\_PARAMETER\_VIOLATION bug check has a value of 0x0000010C. This indicates that a violation was detected in the File system Run-time library (FsRtl) Extra Create Parameter (ECP) package.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## FSRTL\_EXTRA\_CREATE\_PARAMETER\_VIOLATION Parameters


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
<td align="left"><p>The type of violation. (See the following table later on this page for more details).</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The address of the ECP.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The starting address of the ECP list.</p></td>
</tr>
</tbody>
</table>

 

The value of Parameter 1 indicates the type of violation.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Type of Violation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1</p></td>
<td align="left"><p>The ECP signature is invalid, due to either a bad pointer or memory corruption.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2</p></td>
<td align="left"><p>The ECP has undefined flags set.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3</p></td>
<td align="left"><p>The ECP was not allocated by the FsRtl.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x4</p></td>
<td align="left"><p>The ECP has flags set that are illegal for a parameter passed by a create caller.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x5</p></td>
<td align="left"><p>The ECP is corrupted; its size is smaller than the header size.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x6</p></td>
<td align="left"><p>The ECP that is being freed has non-empty list pointers; it might still be part of an ECP list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x11</p></td>
<td align="left"><p>The ECP list signature is invalid, due to either a bad pointer or memory corruption.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x12</p></td>
<td align="left"><p>The ECP list has undefined flags set.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x13</p></td>
<td align="left"><p>The ECP list was not allocated by the FsRtl.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x14</p></td>
<td align="left"><p>The ECP list has flags set that are illegal for a parameter list passed by a create caller.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x15</p></td>
<td align="left"><p>The ECP list passed by the create caller is empty.</p></td>
</tr>
</tbody>
</table>

 

 

 




