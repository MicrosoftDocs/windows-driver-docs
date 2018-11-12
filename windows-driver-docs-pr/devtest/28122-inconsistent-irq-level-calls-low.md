---
title: C28122
description: Warning C28122 The function is not permitted to be called at a low IRQ level. Prior function calls are inconsistent with this constraint.
ms.assetid: 4bc2f85e-055c-4821-9260-a223be787daf
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28122


warning C28122: The function is not permitted to be called at a low IRQ level. Prior function calls are inconsistent with this constraint.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>Maximum legal IRQL was last set to &lt;<em>IRQL</em>&gt; at line &lt;<em>line-number</em>&gt;. It may be that the error is actually in some prior call that limited the range.</p></td>
</tr>
</tbody>
</table>

 

The driver is executing at an IRQL that is too low for the function that it is calling, and the highest permissible IRQL for prior calls in the current function is below the minimum IRQL that is required for this call.

When the Code Analysis tool reports this warning, consult the WDK documentation for the function sequence and verify the IRQL at which each function can be called.

The Code Analysis tool infers the current IRQL and reports this warning only when it has inferred enough about the IRQL to detect the error. This inference might be based on the *function signature* (the arguments and result type) of the function being analyzed, or from prior calls in the execution path.

For a description of a similar situation, see[Warning 28123](28123-inconsistent-irq-level-calls-high.md).

 

 





