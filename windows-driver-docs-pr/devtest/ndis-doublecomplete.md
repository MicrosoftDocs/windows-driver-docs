---
title: DoubleComplete rule (ndis)
description: The DoubleComplete rule specifies that NDIS drivers must not complete an object identifier (OID) request multiple times.
ms.assetid: b79aaf92-3536-4409-ac8d-420a5999409c
ms.date: 05/21/2018
keywords: ["DoubleComplete rule (ndis)"]
topic_type:
- apiref
api_name:
- DoubleComplete
api_type:
- NA
ms.localizationpriority: medium
---

# DoubleComplete rule (ndis)


The DoubleComplete rule specifies that NDIS drivers must not complete an object identifier (OID) request multiple times.

This rule verifies that when the **MiniportOidRequest** callback function returns NDIS\_STATUS\_SUCCESS, the **NdisMOidRequestComplete** function must not be called for that request. The rule also specifies that when **MiniportOidRequest** returns status pending, the driver must not call the **NdisMOidRequestComplete** function multiple times for that request.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>DoubleComplete</strong> rule.</p>
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

[**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622)
 

 





