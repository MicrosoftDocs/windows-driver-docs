---
title: Init\_DeRegisterInterrupt rule (ndis)
description: The Init\_DeRegisterInterrupt rule specifies that if NdisMRegisterInterruptEx is called at least once during MPInitilize, NdisMDeregisterInterruptEx should be called at least once in MPHaltEx.
ms.assetid: C7436321-43DD-4B38-A0A3-9888CFDDA284
keywords: ["Init_DeRegisterInterrupt rule (ndis)"]
topic_type:
- apiref
api_name:
- Init_DeRegisterInterrupt
api_type:
- NA
---

# Init\_DeRegisterInterrupt rule (ndis)


The **Init\_DeRegisterInterrupt** rule specifies that if [**NdisMRegisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563649) is called at least once during MPInitilize, [**NdisMDeregisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563575) should be called at least once in MPHaltEx.

Register of interrupts, which usually happen during initialization, should be undone (deregister) if something goes wrong in the initialization process or during the halting of the miniport.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Init_DeRegisterInterrupt</strong> rule.</p>
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

[**NdisMDeregisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563575)
[**NdisMRegisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563649)
 

 





