---
title: Irql\_Interrupt\_Function rule (ndis)
description: The Irql\_Interrupt\_Function rule specifies that the NDIS functions for interrupts must be called at correct IRQL levels.
ms.assetid: a71eaa14-b1f8-4ef6-8dc4-5c0c0d168685
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["Irql_Interrupt_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_Interrupt_Function
api_type:
- NA
---

# Irql\_Interrupt\_Function rule (ndis)


The Irql\_Interrupt\_Function rule specifies that the NDIS functions for interrupts must be called at correct IRQL levels.

This rule verifies the following NDIS functions:

**NdisMDeregisterInterruptEx**
**NdisMRegisterInterruptEx**
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Irql_Interrupt_Function</strong> rule.</p>
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
 

 





