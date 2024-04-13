---
title: Bug Check 0x14A KERNEL_WMI_INTERNAL
description: The KERNEL_WMI_INTERNAL bug check has a value of 0x0000014A. This indicates that the internal kernel WMI subsystem has encountered a fatal error.
keywords: ["Bug Check 0x14A KERNEL_WMI_INTERNAL", "KERNEL_WMI_INTERNAL"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- KERNEL_WMI_INTERNAL
api_type:
- NA
---

# Bug Check 0x14A: KERNEL\_WMI\_INTERNAL


The KERNEL\_WMI\_INTERNAL bug check has a value of 0x0000014A. This indicates that the internal kernel WMI subsystem has encountered a fatal error.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## KERNEL\_WMI\_INTERNAL Parameters


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
<td align="left">1</td>
<td align="left"><p>0 : A kernel WMI entry reference count was incremented from 0.</p>
Parameter 2: Pointer to the kernel WMI entry.
<p>1 : A kernel WMI datasource was removed prematurely.</p>
Parameter 2: Pointer to the kernel WMI datasource.</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">See parameter 1</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">Reserved</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">Reserved</td>
</tr>
</tbody>
</table>

 

 

 




