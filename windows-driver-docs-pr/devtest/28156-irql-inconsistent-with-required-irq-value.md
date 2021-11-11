---
title: C28156 warning
description: Warning C28156 The actual IRQL is inconsistent with the required IRQL.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium 
f1_keywords: 
  - "C28156"
---

# C28156


warning C28156: The actual IRQL is inconsistent with the required IRQL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>The value at exit was not set to the expected value.</p></td>
</tr>
</tbody>
</table>

 

An **\_IRQL\_requires\_** annotation specifies that the driver should be executing at a particular IRQL when the function completes, but there is at least one path in which the driver is executing at a different IRQL when the function completes.

 

 





