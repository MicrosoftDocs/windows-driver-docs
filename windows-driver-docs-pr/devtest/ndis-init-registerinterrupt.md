---
title: Init\_RegisterInterrupt rule (ndis)
description: The Init\_RegisterInterrupt rule specifies that the registration of interrupts, which usually happens during initialization, must be undone if something goes wrong in the initialization process or during the halting of the miniport driver.If NdisMRegisterInterruptEx is called at least one time during MiniportInitializeEx, the NdisMDeregisterInterruptEx function must be called at least one time in MiniportHaltEx.
ms.assetid: f12cc1b9-396b-4351-ad13-c1750b54b709
ms.date: 05/21/2018
keywords: ["Init_RegisterInterrupt rule (ndis)"]
topic_type:
- apiref
api_name:
- Init_RegisterInterrupt
api_type:
- NA
ms.localizationpriority: medium
---

# Init\_RegisterInterrupt rule (ndis)


The Init\_RegisterInterrupt rule specifies that the registration of interrupts, which usually happens during initialization, must be undone if something goes wrong in the initialization process or during the halting of the miniport driver.

If **NdisMRegisterInterruptEx** is called at least one time during **MiniportInitializeEx**, the **NdisMDeregisterInterruptEx** function must be called at least one time in **MiniportHaltEx**.

|              |      |
|--------------|------|
| Driver model | NDIS |

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>Init_RegisterInterrupt</strong> rule.</p>
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

[**NdisMDeregisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563575)
[**NdisMRegisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563649)
 

 





