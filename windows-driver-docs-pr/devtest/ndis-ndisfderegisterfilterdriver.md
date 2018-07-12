---
title: NdisFDeregisterFilterDriver rule (ndis)
description: A filter driver must call NdisFDeregisterFilterDriver from its FilterDriverUnload routine.
ms.assetid: 24EEB6F6-EEBC-482B-BCAE-DE43277DE899
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["NdisFDeregisterFilterDriver rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisFDeregisterFilterDriver
api_type:
- NA
---

# NdisFDeregisterFilterDriver rule (ndis)


A filter driver must call [**NdisFDeregisterFilterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff561800) from its [**FilterDriverUnload**](https://msdn.microsoft.com/library/windows/hardware/ff549936) routine.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>NdisFDeregisterFilterDriver</strong> rule.</p>
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

[**NdisFDeregisterFilterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff561800)
[**NdisFRegisterFilterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562608)
 

 





