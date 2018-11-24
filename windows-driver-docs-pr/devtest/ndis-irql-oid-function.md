---
title: Irql\_OID\_Function rule (ndis)
description: The Irql\_OID\_Function rule specifies that the NDIS OID request DDIs must be called at correct IRQL levels.
ms.assetid: 450afd4e-ba01-45e8-a866-6cd9b3190bb7
ms.date: 05/21/2018
keywords: ["Irql_OID_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_OID_Function
api_type:
- NA
ms.localizationpriority: medium
---

# Irql\_OID\_Function rule (ndis)


The **Irql\_OID\_Function** rule specifies that the NDIS OID request DDIs must be called at correct IRQL levels.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>Irql_OID_Function</strong> rule.</p>
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

[**NdisAllocateCloneOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff560706)
[**NdisCancelOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561622)
[**NdisFCancelOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561792)
[**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830)
[**NdisFOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561833)
[**NdisFreeCloneOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561845)
[**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622)
[**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710)
 

 





