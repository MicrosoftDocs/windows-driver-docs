---
title: DoubleCompleteWorkItem rule (ndis)
description: The DoubleCompleteWorkItem rule specifies that NDIS drivers must not complete an OID request multiple times when the completion is deferred in a work item.
ms.assetid: 7add7473-0324-42e9-83bc-8f563410e44f
ms.date: 05/21/2018
keywords: ["DoubleCompleteWorkItem rule (ndis)"]
topic_type:
- apiref
api_name:
- DoubleCompleteWorkItem
api_type:
- NA
ms.localizationpriority: medium
---

# DoubleCompleteWorkItem rule (ndis)


The DoubleCompleteWorkItem rule specifies that NDIS drivers must not complete an OID request multiple times when the completion is deferred in a work item.

This rule tracks the OID and verifies that when the driver queues a work item, the driver does not call **NdisMOidRequestComplete** multiple times on the same OID.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>DoubleCompleteWorkItem</strong> rule.</p>
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

[**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622)
 

 





