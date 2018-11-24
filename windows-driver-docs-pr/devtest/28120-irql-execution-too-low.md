---
title: C28120
description: Warning C28120 The function is not permitted to be called at the current IRQ level. The current level is too low.
ms.assetid: a31a7c97-e27a-4a6a-a172-41d87cab236d
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28120


warning C28120: The function is not permitted to be called at the current IRQ level. The current level is too low.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>IRQL was last set to &lt;<em>value</em>&gt; at line &lt;<em>line-number</em>&gt;. The level might have been inferred from the function signature.</p></td>
</tr>
</tbody>
</table>

 

The driver is executing at an IRQL that is too low for the function that it is calling.

When the Code Analysis tool reports this warning, consult the WDK documentation for the function and verify the IRQL at which the function can be called.

The Code Analysis tool infers the current IRQL and reports this warning only when it has inferred enough about the IRQL to detect the error. This inference might be based on the *function signature* (the arguments and result type) of the function being analyzed, or from prior calls along the current path.

If the Code Analysis tool cannot determine the IRQL at which the driver is running, it will not report this warning, even if the function is being called at the wrong IRQL.

For a description of a similar situation, see [Warning 28121](28121-irq-execution-too-high.md).

 

 





