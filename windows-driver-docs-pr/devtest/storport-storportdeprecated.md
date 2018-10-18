---
title: StorPortDeprecated rule (storport)
description: This rule verifies that the driver does not call either of these deprecated routines StorPortValidateRange or StorPortLogError.
ms.assetid: 90223719-91AB-4D10-88A0-0DBD2D99C5B2
ms.date: 05/21/2018
keywords: ["StorPortDeprecated rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortDeprecated
api_type:
- NA
ms.localizationpriority: medium
---

# StorPortDeprecated rule (storport)


This rule verifies that the driver does not call either of these deprecated routines: **StorPortValidateRange** or **StorPortLogError**.

|              |          |
|--------------|----------|
| Driver model | Storport |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>StorPortDeprecated</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li>[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)</li>
<li>[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)</li>
<li>[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)</li>
</ol>
<p>For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281).</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**StorPortLogError**](https://msdn.microsoft.com/library/windows/hardware/ff567426)
[**StorPortValidateRange**](https://msdn.microsoft.com/library/windows/hardware/ff567513)
 

 





