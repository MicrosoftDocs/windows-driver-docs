---
title: C28123
description: Warning C28123 The function is not permitted to be called at a high IRQ level. Prior function calls are inconsistent with this constraint.
ms.assetid: 6b40a485-f4f7-4c68-8575-960faa8cb87b
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28123


warning C28123: The function is not permitted to be called at a high IRQ level. Prior function calls are inconsistent with this constraint.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>It may be that the error is actually in some prior call that limited the range.</p></td>
</tr>
</tbody>
</table>

 

The driver is executing at an IRQL that is too high for the function that it is calling and the lowest permissible IRQL for prior calls within the function is greater than the maximum IRQL required for this call.

When the Code Analysis tool reports this warning, consult the WDK documentation for the function sequence and verify the IRQL at which each function can be called.

The Code Analysis tool infers the current IRQL and reports this warning only when it has inferred enough about the IRQL to detect the error. This inference might be based on the *function signature* (the arguments and result type) of the function being analyzed, or from prior calls in the execution path.

 

 





