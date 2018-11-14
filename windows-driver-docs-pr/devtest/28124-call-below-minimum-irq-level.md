---
title: C28124
description: Warning C28124 The call to causes the IRQ Level to be set below the minimum acceptable for the function being analyzed.
ms.assetid: d0540a52-2252-49d5-ba03-3d026e07670a
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28124


warning C28124: The call to causes the IRQ Level to be set below the minimum acceptable for the function being analyzed.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>Minimum legal IRQL was last set to &lt;<em>IRQL</em>&gt; at line &lt;<em>line-number</em>&gt;. The level limits come from annotations on the current function.</p></td>
</tr>
</tbody>
</table>

 

The driver is calling a function that changes the IRQL to a level less than the minimum IRQL for the current function type. The Code Analysis tool infers this information from the function type or from annotations.

This warning occurs inside a function that has been annotated with the **\_\_drv\_minIRQL** annotation and indicates either a coding error in the function or a misunderstanding of the function's contract in the annotations.

 

 





