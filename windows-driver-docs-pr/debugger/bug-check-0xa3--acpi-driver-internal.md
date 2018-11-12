---
title: Bug Check 0xA3 ACPI_DRIVER_INTERNAL
description: The ACPI_DRIVER_INTERNAL bug check has a value of 0x000000A3. This bug check indicates that the ACPI driver detected an internal inconsistency.
ms.assetid: 599c09a9-5c13-404e-b68f-5fa68bd801ed
keywords: ["Bug Check 0xA3 ACPI_DRIVER_INTERNAL", "ACPI_DRIVER_INTERNAL"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ACPI_DRIVER_INTERNAL
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xA3: ACPI\_DRIVER\_INTERNAL


The ACPI\_DRIVER\_INTERNAL bug check has a value of 0x000000A3. This bug check indicates that the ACPI driver detected an internal inconsistency.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## ACPI\_DRIVER\_INTERNAL Parameters


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
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Reserved</p></td>
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

 

Cause
-----

An inconsistency in the ACPI driver is so severe that continuing to run would cause serious problems.

One possible source of this problem is a BIOS error.

 

 




