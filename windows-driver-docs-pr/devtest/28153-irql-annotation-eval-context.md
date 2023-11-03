---
title: C28153 warning
description: Warning C28153 The value for an IRQL from annotation could not be evaluated in this context.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
f1_keywords: 
  - "C28153"
---

# C28153


warning C28153: The value for an IRQL from annotation could not be evaluated in this context.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>Probable annotation error.</p>
<p>The following was computed: &lt;<em>val</em>&gt;</p></td>
</tr>
</tbody>
</table>

 

This warning indicates that the Code Analysis tool cannot interpret the function annotation because the annotation is not coded correctly. As a result, the Code Analysis tool cannot determine the specified IRQL value.

This warning can occur with any of the driver-specific annotations that mention an IRQL when the Code Analysis tool cannot evaluate the expression for the IRQL.

