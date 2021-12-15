---
title: C28146 warning
description: Warning C28146 Kernel Mode drivers should use ntstrsafe.h, not strsafe.h. Found in source file.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
f1_keywords: 
  - "C28146"
---

# C28146


warning C28146: Kernel Mode drivers should use ntstrsafe.h, not strsafe.h. Found in source file

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>The header ntstrsafe.h contains versions of the functions found in strsafe.h that are suitable for use in kernel mode code.</p></td>
</tr>
</tbody>
</table>

 

A kernel-mode driver includes Strsafe.h, instead of Ntstrsafe.h. For information about Ntstrsafe.h and Strsafe.h, see [Using Safe String Functions](../kernel/using-safe-string-functions.md).

 

