---
title: C28162 warning
description: Warning C28162 Exiting while holding the right to use floating-point hardware.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium 
f1_keywords: 
  - "C28162"
---

# C28162


warning C28162: Exiting while holding the right to use floating-point hardware

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>This function was annotated to exit with floating point restored.</p></td>
</tr>
</tbody>
</table>

 

The **\_Kernel\_float\_restored\_** annotation was used to release the right to use floating point, but a path through the function was detected where no function known to perform that operation was successfully called. This warning might indicate that a conditional (**\_When\_**) annotation is needed, or it might indicate a coding error.

 

 





