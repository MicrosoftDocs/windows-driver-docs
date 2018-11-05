---
title: Bug Check 0x10F RESOURCE_MANAGER_EXCEPTION_NOT_HANDLED
description: The RESOURCE_MANAGER_EXCEPTION_NOT_HANDLED bug check has a value of 0x0000010F.
ms.assetid: d2589163-8c82-4416-a378-a0c72360a9fb
keywords: ["Bug Check 0x10F RESOURCE_MANAGER_EXCEPTION_NOT_HANDLED", "RESOURCE_MANAGER_EXCEPTION_NOT_HANDLED"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- RESOURCE_MANAGER_EXCEPTION_NOT_HANDLED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x10F: RESOURCE\_MANAGER\_EXCEPTION\_NOT\_HANDLED


The RESOURCE\_MANAGER\_EXCEPTION\_NOT\_HANDLED bug check has a value of 0x0000010F. This indicates that the kernel transaction manager detected that a kernel-mode resource manager has raised an exception in response to a direct call-back. The resource manager is in an unexpected and unrecoverable state.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## RESOURCE\_MANAGER\_EXCEPTION\_NOT\_HANDLED Parameters


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
<td align="left"><p>The address of the exception record</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The address of the context record</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The address of the exception code</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The address of the resource manager</p></td>
</tr>
</tbody>
</table>

 

 

 




