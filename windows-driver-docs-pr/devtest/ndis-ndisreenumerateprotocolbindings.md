---
title: NdisReEnumerateProtocolBindings rule (ndis)
description: Protocol drivers cannot call NdisReEnumerateProtocolBindings from within the context of the ProtocolBindAdapterEx or ProtocolUnbindAdapterEx functions.
ms.assetid: A6BB5B25-B8F4-4D90-B325-DFEED9C4AA6A
ms.date: 05/21/2018
keywords: ["NdisReEnumerateProtocolBindings rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisReEnumerateProtocolBindings
api_type:
- NA
ms.localizationpriority: medium
---

# NdisReEnumerateProtocolBindings rule (ndis)


Protocol drivers cannot call [**NdisReEnumerateProtocolBindings**](https://msdn.microsoft.com/library/windows/hardware/ff564516) from within the context of the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) or [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) functions. Also, protocol drivers cannot call **NdisReEnumerateProtocolBindings** from within the context of the [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function if the *ProtocolBindingContext* parameter of *ProtocolNetPnPEvent* is not NULL. However, protocol drivers can call **NdisReEnumerateProtocolBindings** from within the context of *ProtocolNetPnPEvent* if *ProtocolBindingContext* is NULL. A NULL *ProtocolBindingContext* value indicates that the event applies to all bindings.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>NdisReEnumerateProtocolBindings</strong> rule.</p>
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

[**NdisReEnumerateProtocolBindings**](https://msdn.microsoft.com/library/windows/hardware/ff564516)
 

 





