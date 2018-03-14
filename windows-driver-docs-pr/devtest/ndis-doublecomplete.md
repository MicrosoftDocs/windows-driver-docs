---
title: DoubleComplete rule (ndis)
description: The DoubleComplete rule specifies that NDIS drivers must not complete an object identifier (OID) request multiple times.
ms.assetid: b79aaf92-3536-4409-ac8d-420a5999409c
keywords: ["DoubleComplete rule (ndis)"]
topic_type:
- apiref
api_name:
- DoubleComplete
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>DoubleComplete</strong> rule.</p>
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
 

 





