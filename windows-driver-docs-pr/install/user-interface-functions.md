---
title: User Interface Functions
description: User Interface Functions
ms.date: 04/20/2017
---

# User Interface Functions


You can use the following general Setup functions in class installers and co-installers to determine whether the current process can interact with a user.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupgetnoninteractivemode" data-raw-source="[&lt;strong&gt;SetupGetNonInteractiveMode&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupgetnoninteractivemode)"><strong>SetupGetNonInteractiveMode</strong></a></p></td>
<td align="left"><p>Returns the value of a SetupAPI non-interactive flag that indicates whether the caller's process can interact with a user through user interface components, such as dialog boxes.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupsetnoninteractivemode" data-raw-source="[&lt;strong&gt;SetupSetNonInteractiveMode&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupsetnoninteractivemode)"><strong>SetupSetNonInteractiveMode</strong></a></p></td>
<td align="left"><p>Sets a non-interactive SetupAPI flag that determines whether SetupAPI can interact with a user in the caller's context.</p></td>
</tr>
</tbody>
</table>

 

