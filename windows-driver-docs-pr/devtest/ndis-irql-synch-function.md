---
title: Irql\_Synch\_Function rule (ndis)
description: The Irql\_Synch\_Function rule specifies that the NDIS interrupt and synchronization DDIs must be called at correct IRQL levels.
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

## How to test

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>Irql_Synch_Function</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](./using-static-driver-verifier-to-find-defects-in-drivers.md#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](./using-static-driver-verifier-to-find-defects-in-drivers.md#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](./using-static-driver-verifier-to-find-defects-in-drivers.md#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

## Applies to

[**NDIS\_RELEASE\_MUTEX**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndis_release_mutex)
[**NDIS\_WAIT\_FOR\_MUTEX**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndis_wait_for_mutex)
[**NdisAcquireReadWriteLock**](/previous-versions/ff560696(v=vs.85))
[**NdisAcquireSpinLock**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisacquirespinlock)
[**NdisDprAcquireSpinLock**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisdpracquirespinlock)
[**NdisDprReleaseSpinLock**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisdprreleasespinlock)
[**NdisReleaseReadWriteLock**](/previous-versions/ff564521(v=vs.85))
[**NdisReleaseSpinLock**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreleasespinlock)
[**NdisResetEvent**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisresetevent)
[**NdisSetEvent**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetevent)
