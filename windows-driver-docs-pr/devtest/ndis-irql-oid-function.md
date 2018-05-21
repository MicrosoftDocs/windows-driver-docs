---
title: Irql\_OID\_Function rule (ndis)
description: The Irql\_OID\_Function rule specifies that the NDIS OID request DDIs must be called at correct IRQL levels.
ms.assetid: 450afd4e-ba01-45e8-a866-6cd9b3190bb7
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["Irql_OID_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_OID_Function
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Irql_OID_Function</strong> rule.</p>
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

[**NdisAllocateCloneOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff560706)
[**NdisCancelOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561622)
[**NdisFCancelOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561792)
[**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830)
[**NdisFOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561833)
[**NdisFreeCloneOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561845)
[**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622)
[**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710)
 

 





