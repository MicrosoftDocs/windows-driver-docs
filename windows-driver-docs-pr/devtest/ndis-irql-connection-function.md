---
title: Irql\_Connection\_Function rule (ndis)
description: The Irql\_Connection\_Function rule specifies that the NDIS connection functions for protocol drivers must be called at correct IRQL levels.
ms.assetid: 9721cb8a-ac70-4f2b-8bbd-809dc06548dc
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["Irql_Connection_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_Connection_Function
api_type:
- NA
ms.localizationpriority: medium
---

# Irql\_Connection\_Function rule (ndis)


The **Irql\_Connection\_Function** rule specifies that the NDIS connection functions for protocol drivers must be called at correct IRQL levels.

This rule verifies the following NDIS functions:

**NdisCoAssignInstanceNam**
**NdisCoCreateVc**
**NdisCoDeleteVc**
**NdisCoGetTapiCallId**
**NdisCoOidRequest**
**NdisCoOidRequestComplete**
**NdisCoSendNetBufferLists**
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Irql_Connection_Function</strong> rule.</p>
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

[**NdisCoAssignInstanceName**](https://msdn.microsoft.com/library/windows/hardware/ff561692)
[**NdisCoCreateVc**](https://msdn.microsoft.com/library/windows/hardware/ff561696)
[**NdisCoDeleteVc**](https://msdn.microsoft.com/library/windows/hardware/ff561698)
[**NdisCoGetTapiCallId**](https://msdn.microsoft.com/library/windows/hardware/ff561700)
[**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711)
[**NdisCoOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561716)
[**NdisCoSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561728)
 

 





