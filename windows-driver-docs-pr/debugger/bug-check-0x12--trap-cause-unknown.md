---
title: Bug Check 0x12 TRAP_CAUSE_UNKNOWN
description: The TRAP_CAUSE_UNKNOWN bug check has a value of 0x00000012. This indicates that an unknown exception has occurred.
ms.assetid: 43cbcc34-9df0-4d5f-b823-1cc3cafaa811
keywords: ["Bug Check 0x12 TRAP_CAUSE_UNKNOWN", "TRAP_CAUSE_UNKNOWN"]
ms.author: domars
ms.date: 06/26/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- TRAP_CAUSE_UNKNOWN
api_type:
- NA
---

# Bug Check 0x12: TRAP\_CAUSE\_UNKNOWN


The TRAP\_CAUSE\_UNKNOWN bug check has a value of 0x00000012. This indicates that an unknown exception has occurred.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](http://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## TRAP\_CAUSE\_UNKNOWN Parameters


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
<td align="left"><p>Type of TRAP_CAUSE_UNKNOWN</p>
<p><B>VALUES</B></p>
<p>1 - Unexpected interrupt. (Parameter 2 – Interrupt Vector)</p>
<p>2 - Unknown floating point exception. </p>
<p>3 - The enabled and asserted status bits (see processor definition).</p>
</td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Dependent on Arg1</p></td>
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

 

 

 




