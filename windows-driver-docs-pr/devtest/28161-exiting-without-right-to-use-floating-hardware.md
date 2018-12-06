---
title: C28161
description: Warning C28161 Exiting without acquiring the right to use floating hardware.
ms.assetid: 4132409d-10aa-4014-a2d9-77c62e137795
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28161


warning C28161: Exiting without acquiring the right to use floating hardware

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>This function was annotated to exit with floating point available.</p></td>
</tr>
</tbody>
</table>

 

The **\_Kernel\_float\_saved\_** annotation was used to acquire the right to use floating point, but a path through the function was detected where no function known to perform that operation was successfully called. This warning might indicate that a conditional (**\_When\_**) annotation is needed, or it might indicate a coding error.

 

 





