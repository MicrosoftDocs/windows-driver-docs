---
title: C28150
description: Warning C28150 The function causes the IRQ Level to be set above the maximum acceptable for the function being analyzed.
ms.assetid: 7ad53801-fa7f-49c1-a1f0-715c9f4951d1
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28150


warning C28150: The function causes the IRQ Level to be set above the maximum acceptable for the function being analyzed

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>The level limits come from annotations on the current function.</p></td>
</tr>
</tbody>
</table>

 

The specified function has raised the IRQL above the maximum IRQL permitted for the current function call.

This warning occurs inside a function that has been annotated with the **\_\_drv\_maxIRQL** annotation and indicates either a coding error in the function or a misunderstanding of the function's contract in the annotations.

 

 





