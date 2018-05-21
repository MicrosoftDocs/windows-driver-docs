---
title: Irql\_MCO\_Function rule (ndis)
description: The Irql\_MCO\_Function rule specifies that the NDIS MCO DDIs for miniport drivers must be called at correct IRQL levels.
ms.assetid: 4a6643a2-d831-4b60-a9d6-decf494a2ffc
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["Irql_MCO_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_MCO_Function
api_type:
- NA
---

# Irql\_MCO\_Function rule (ndis)


The **Irql\_MCO\_Function** rule specifies that the NDIS MCO DDIs for miniport drivers must be called at correct IRQL levels.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Irql_MCO_Function</strong> rule.</p>
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

[**NdisMCoActivateVcComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563558)
[**NdisMCoDeactivateVcComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563559)
[**NdisMCoIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563561)
[**NdisMCoIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563562)
[**NdisMCompleteDmaTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff563564)
[**NdisMCoOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563568)
[**NdisMCoSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563570)
 

 





