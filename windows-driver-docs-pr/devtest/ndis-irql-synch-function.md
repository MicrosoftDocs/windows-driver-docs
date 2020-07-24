---
title: Irql\_Synch\_Function rule (ndis)
description: The Irql\_Synch\_Function rule specifies that the NDIS interrupt and synchronization DDIs must be called at correct IRQL levels.
ms.assetid: 5d0e862a-89e6-493d-a102-83430c5140e4
ms.date: 05/21/2018
keywords: ["Irql_Synch_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_Synch_Function
api_type:
- NA
ms.localizationpriority: medium
---

# Irql\_Synch\_Function rule (ndis)


The **Irql\_Synch\_Function** rule specifies that the NDIS interrupt and synchronization DDIs must be called at correct IRQL levels.

**Driver model: NDIS**

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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier)">Static Driver Verifier</a> and specify the <strong>Irql_Synch_Function</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**NDIS\_RELEASE\_MUTEX**](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-release-mutex)
[**NDIS\_WAIT\_FOR\_MUTEX**](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-wait-for-mutex)
[**NdisAcquireReadWriteLock**](https://msdn.microsoft.com/library/windows/hardware/ff560696)
[**NdisAcquireSpinLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisacquirespinlock)
[**NdisDprAcquireSpinLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisdpracquirespinlock)
[**NdisDprReleaseSpinLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisdprreleasespinlock)
[**NdisReleaseReadWriteLock**](https://msdn.microsoft.com/library/windows/hardware/ff564521)
[**NdisReleaseSpinLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreleasespinlock)
[**NdisResetEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisresetevent)
[**NdisSetEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetevent)
 

 





