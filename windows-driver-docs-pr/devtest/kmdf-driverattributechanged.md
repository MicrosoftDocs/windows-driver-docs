---
title: DriverAttributeChanged rule (kmdf)
description: The DriverAttributeChanged rule specifies that a driver must not change the execution level or synchronization scope of a KMDF driver.
ms.assetid: 9a11e06b-d663-4b1b-89bc-b3631e9928ce
ms.date: 05/21/2018
keywords: ["DriverAttributeChanged rule (kmdf)"]
topic_type:
- apiref
api_name:
- DriverAttributeChanged
api_type:
- NA
ms.localizationpriority: medium
---

# DriverAttributeChanged rule (kmdf)


The **DriverAttributeChanged** rule specifies that a driver must not change the execution level or synchronization scope of a KMDF driver.

|              |      |
|--------------|------|
| Driver model | KMDF |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>DriverAttributeChanged</strong> rule.</p>
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

[**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175)
 

 





