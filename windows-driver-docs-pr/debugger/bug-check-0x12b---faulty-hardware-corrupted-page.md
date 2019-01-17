---
title: Bug Check 0x12B FAULTY_HARDWARE_CORRUPTED_PAGE
description: The FAULTY_HARDWARE_CORRUPTED_PAGE bug check has a value of 0x0000012B. This bug check indicates either a memory manager or store manager memory error has occurred.
ms.assetid: caa57d76-946f-4394-bfcf-1dbf3813a55b
keywords: ["Bug Check 0x12B FAULTY_HARDWARE_CORRUPTED_PAGE", "FAULTY_HARDWARE_CORRUPTED_PAGE"]
ms.date: 01/17/2019
topic_type:
- apiref
api_name:
- FAULTY_HARDWARE_CORRUPTED_PAGE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x12B: FAULTY\_HARDWARE\_CORRUPTED\_PAGE

The FAULTY\_HARDWARE\_CORRUPTED\_PAGE bug check has a value of 0x0000012B. This bug check indicates that either a memory manager or store manager memory error has occurred.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## FAULTY\_HARDWARE\_CORRUPTED\_PAGE Parameters

There are two different types of FAULTY\_HARDWARE\_CORRUPTED\_PAGE bug checks with two different sets of parameters. One can happen with memory manager and one is for store manager.

If parameters 3 and 4 are both zero, this bug check is caused by memory manager. If parameters 3 and 4 are non-zero, the bug check is caused by store manager. 

### Memory Manager Parameters

This bug check indicates that a single-bit error was found in this page. This is a hardware memory error.

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
<td align="left"><p>Virtual address maps to the corrupted page</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Physical page number</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Zero</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Zero</p></td>
</tr>
</tbody>
</table>


### Store Manager Parameters 

 This bug check indicates that a store manager memory error has occurred. It may be an authentication failure, a CRC failure, or a decompression failure.

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
<td align="left"><p>FailStatus - Indicates the type of failure</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The CompressedSize of the page that is being read</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Source Buffer</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Target Buffer</p></td>
</tr>
</tbody>
</table>

 

 




