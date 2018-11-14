---
title: Bug Check 0xCB DRIVER_LEFT_LOCKED_PAGES_IN_PROCESS
description: The DRIVER_LEFT_LOCKED_PAGES_IN_PROCESS bug check has a value of 0x000000CB. This indicates that a driver or the I/O manager failed to release locked pages after an I/O operation.
ms.assetid: e97d114e-c6f1-44f1-a2ad-bfa8d03dc3c7
keywords: ["Bug Check 0xCB DRIVER_LEFT_LOCKED_PAGES_IN_PROCESS", "DRIVER_LEFT_LOCKED_PAGES_IN_PROCESS"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DRIVER_LEFT_LOCKED_PAGES_IN_PROCESS
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xCB: DRIVER\_LEFT\_LOCKED\_PAGES\_IN\_PROCESS


The DRIVER\_LEFT\_LOCKED\_PAGES\_IN\_PROCESS bug check has a value of 0x000000CB. This indicates that a driver or the I/O manager failed to release locked pages after an I/O operation.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## DRIVER\_LEFT\_LOCKED\_PAGES\_IN\_PROCESS Parameters


The four parameters listed in the message can have two possible meanings.

If a driver locked these pages, the parameters have the following meaning.

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
<td align="left"><p>Calling address in the driver that locked the pages</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Caller of the calling address in driver that locked the pages</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Address of the MDL containing the locked pages</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Number of locked pages</p></td>
</tr>
</tbody>
</table>

 

If the driver responsible for the error can be identified, its name is printed on the blue screen and stored in memory at the location (PUNICODE\_STRING) **KiBugCheckDriver**.

If the I/O manager locked these pages, the parameters have the following meaning.

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
<td align="left"><p>Address of the dispatch routine of the top driver on the stack to which the IRP was sent</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Address of the device object of the top driver on the stack to which the IRP was sent</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Address of the MDL containing the locked pages</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Number of locked pages</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This bug check is issued only if the registry value **\\\\HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\TrackLockedPages** is equal to DWORD 1. If this value is not set, the system will issue the less-informative [**bug check 0x76**](bug-check-0x76--process-has-locked-pages.md) (PROCESS\_HAS\_LOCKED\_PAGES).

Starting with Windows Vista, this bug check can also be issued by Driver Verifier when the Pool Tracking option is enabled.

 

 




