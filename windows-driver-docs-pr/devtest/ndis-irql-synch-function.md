---
title: Irql\_Synch\_Function rule (ndis)
description: The Irql\_Synch\_Function rule specifies that the NDIS interrupt and synchronization DDIs must be called at correct IRQL levels.
ms.assetid: 5d0e862a-89e6-493d-a102-83430c5140e4
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["Irql_Synch_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_Synch_Function
api_type:
- NA
---

# Irql\_Synch\_Function rule (ndis)


The **Irql\_Synch\_Function** rule specifies that the NDIS interrupt and synchronization DDIs must be called at correct IRQL levels.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Irql_Synch_Function</strong> rule.</p>
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

[**NDIS\_RELEASE\_MUTEX**](https://msdn.microsoft.com/library/windows/hardware/ff567247)
[**NDIS\_WAIT\_FOR\_MUTEX**](https://msdn.microsoft.com/library/windows/hardware/ff567897)
[**NdisAcquireReadWriteLock**](https://msdn.microsoft.com/library/windows/hardware/ff560696)
[**NdisAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff560699)
[**NdisDprAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff561749)
[**NdisDprReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff561753)
[**NdisReleaseReadWriteLock**](https://msdn.microsoft.com/library/windows/hardware/ff564521)
[**NdisReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff564524)
[**NdisResetEvent**](https://msdn.microsoft.com/library/windows/hardware/ff564526)
[**NdisSetEvent**](https://msdn.microsoft.com/library/windows/hardware/ff564539)
 

 





