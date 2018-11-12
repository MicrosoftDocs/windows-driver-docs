---
title: Bug Check 0x127 PAGE_NOT_ZERO
description: The PAGE_NOT_ZERO bug check has a value of 0x00000127.
ms.assetid: b6485307-191d-401a-8f2e-7f4a54a630f9
keywords: ["Bug Check 0x127 PAGE_NOT_ZERO", "PAGE_NOT_ZERO"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- PAGE_NOT_ZERO
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x127: PAGE\_NOT\_ZERO


The PAGE\_NOT\_ZERO bug check has a value of 0x00000127. This bug check indicates that a page that should have been filled with zeros was not. This bug check might occur because of a hardware error or because a privileged component of the operating system modified a page after freeing it.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## PAGE\_NOT\_ZERO Parameters


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
<td align="left"><p>Virtual address that maps the corrupted page</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Physical page number</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Zero (Reserved)</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Zero (Reserved)</p></td>
</tr>
</tbody>
</table>

 

 

 




