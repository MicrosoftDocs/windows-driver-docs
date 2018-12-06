---
title: C28750
description: Warning C28750 Banned usage of lstrlen and its variants.
ms.assetid: 5057FE71-286A-4710-922F-DFC639717C75
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28750


warning C28750: Banned usage of lstrlen and its variants

This warning indicates that a function is being used that has been banned, and has better replacements.

The lstrlen function and related variations fail to transmit exceptions that occur during operation. This can cause error conditions to happen much later, potentially on a different thread, making the error conditions harder to diagnose. In addition, equivalent substitute functions can be optimized by the compiler, and avoid the performance overhead of exception handlers (**\_try** and **\_except** blocks).

The lstrlen function and its variants are banned because they fail to transmit exceptions. The correct mitigation is to convert them to another string length function (usually strlen, wcslen, \_tcslen). However, while you review the lstrlen changes, you should confirm that the string buffer is coming from trusted code. If you are dealing with untrusted data, you should instead switch from the strlen family of functions to the strnlen family (or StringCchLength family), which will ensure they don't go past the bounds of the untrusted data block.

Unlike lstrlen, none of the replacements catch exceptions. In addition, lstrlen allows NULL pointers, so if NULL pointers are possible at that point in the code, an explicit NULL check is required when replacing lstrlen with strlen or strnlen.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">API</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="lstrlen"></span><span id="LSTRLEN"></span>lstrlen</p></td>
<td align="left"><p>Trusted data replacement options: _tcslen</p>
<p>Untrusted data replacement: _tcsnlen, StringCchLength</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="lstrlenA"></span><span id="lstrlena"></span><span id="LSTRLENA"></span>lstrlenA</p></td>
<td align="left"><p>Trusted data replacement options: strlen</p>
<p>Untrusted data replacement: strnlen, StringCchLengthA</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="lstrlenW"></span><span id="lstrlenw"></span><span id="LSTRLENW"></span>lstrlenW</p></td>
<td align="left"><p>Trusted data replacement options: wcslen</p>
<p>Untrusted data replacement: wcsnlen, StringCchLengthW</p></td>
</tr>
</tbody>
</table>

 

 

 





