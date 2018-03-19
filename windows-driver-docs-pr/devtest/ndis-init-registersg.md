---
title: Init\_RegisterSG rule (ndis)
description: The Init\_RegisterSG rule specifies that the registration of the scatter-gather list (SG), which usually happens during initialization, must be undone if something goes wrong in the initialization process or during the halting of the miniport driver.If NdisMRegisterScatterGatherDma is called at least one time during MiniportInitializeEx, the NdisMDeregisterScatterGatherDma function should be called at least one time in MiniportHaltEx.
ms.assetid: c4d00be1-b44b-4769-bbe6-6128a742d088
keywords: ["Init_RegisterSG rule (ndis)"]
topic_type:
- apiref
api_name:
- Init_RegisterSG
api_type:
- NA
---

# Init\_RegisterSG rule (ndis)


The Init\_RegisterSG rule specifies that the registration of the scatter-gather list (SG), which usually happens during initialization, must be undone if something goes wrong in the initialization process or during the halting of the miniport driver.

If **NdisMRegisterScatterGatherDma** is called at least one time during **MiniportInitializeEx**, the **NdisMDeregisterScatterGatherDma** function should be called at least one time in **MiniportHaltEx**.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Init_RegisterSG</strong> rule.</p>
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

[**NdisMDeregisterScatterGatherDma**](https://msdn.microsoft.com/library/windows/hardware/ff563581)
[**NdisMRegisterScatterGatherDma**](https://msdn.microsoft.com/library/windows/hardware/ff563659)
 

 





