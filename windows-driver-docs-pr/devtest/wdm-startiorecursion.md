---
title: StartIoRecursion rule (wdm)
description: The StartIoRecursion rule specifies that if a driver's StartIo routine includes a call to IoStartNextPacket, the driver must first call IoSetStartIoAttributes with the DeferredStartIo attribute set to TRUE. Otherwise, infinite recursion can result.
ms.assetid: 997df0a3-1222-435d-9c61-e97a2b6185cf
ms.date: 05/21/2018
keywords: ["StartIoRecursion rule (wdm)"]
topic_type:
- apiref
api_name:
- StartIoRecursion
api_type:
- NA
ms.localizationpriority: medium
---

# StartIoRecursion rule (wdm)


The **StartIoRecursion** rule specifies that if a driver's [**StartIo**](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine includes a call to [**IoStartNextPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550358), the driver must first call [**IoSetStartIoAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff550330) with the *DeferredStartIo* attribute set to **TRUE**. Otherwise, infinite recursion can result.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>StartIoRecursion</strong> rule.</p>
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

[**IoSetStartIoAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff550330)
[**IoStartNextPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550358)
 

 





