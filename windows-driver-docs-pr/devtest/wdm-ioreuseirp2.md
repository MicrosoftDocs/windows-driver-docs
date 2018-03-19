---
title: IoReuseIrp2 rule (wdm)
description: The IoReuseIrp2 rule specifies that a driver should use IoReuseIrp only on IRPs that it previously allocated within the driver.
ms.assetid: 707E14EA-96C2-4B50-B381-C3FCF45FA26C
keywords: ["IoReuseIrp2 rule (wdm)"]
topic_type:
- apiref
api_name:
- IoReuseIrp2
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IoReuseIrp2</strong> rule.</p>
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

[**IoReuseIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549661)
 

 





