---
title: C28127
description: Warning C28127 The function being used as a routine does not exactly match the type expected.
ms.assetid: ae8f554b-c1e1-42a7-b1ad-c5554af25953
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28127


warning C28127: The function being used as a routine does not exactly match the type expected.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>It is likely that the difference is that the actual function returns a value, and the expected function type is void</p></td>
</tr>
</tbody>
</table>

 

The driver is passing or assigning a function (pointer) of an unexpected type (that is, function signature). This often occurs in C when the expected return type of a function is VOID and a function with an (implied) **int** return value is actually supplied. It can also happen when the parameters are compatible but not identical. In general, callback functions should match the expected type exactly, which is most easily accomplished using a function typedef.

This type mismatch message is designed primarily to verify that the Code Analysis tool can recognize callbacks.

 

 





