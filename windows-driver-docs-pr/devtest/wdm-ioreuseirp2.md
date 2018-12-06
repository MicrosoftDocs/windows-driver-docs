---
title: IoReuseIrp2 rule (wdm)
description: The IoReuseIrp2 rule specifies that a driver should use IoReuseIrp only on IRPs that it previously allocated within the driver.
ms.assetid: 707E14EA-96C2-4B50-B381-C3FCF45FA26C
ms.date: 05/21/2018
keywords: ["IoReuseIrp2 rule (wdm)"]
topic_type:
- apiref
api_name:
- IoReuseIrp2
api_type:
- NA
ms.localizationpriority: medium
---

# IoReuseIrp2 rule (wdm)


The **IoReuseIrp2** rule specifies that a driver should use [**IoReuseIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549661) only on IRPs that it previously allocated within the driver.

|              |     |
|--------------|-----|
| Driver model | WDM |

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>IoReuseIrp2</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh454281" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**IoReuseIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549661)
 

 





