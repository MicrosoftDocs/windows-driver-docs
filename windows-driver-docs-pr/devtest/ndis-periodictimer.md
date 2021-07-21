---
title: PeriodicTimer rule (ndis)
description: The PeriodicTimer rule specifies that the caller of NdisCancelTimerObject must be running at IRQL PASSIVE\_LEVEL if a nonzero value was specified in the MillisecondsPeriod parameter of the NdisSetTimerObject function.
ms.date: 05/21/2018
keywords: ["PeriodicTimer rule (ndis)"]
topic_type:
- apiref
api_name:
- PeriodicTimer
api_type:
- NA
ms.localizationpriority: medium
---

# PeriodicTimer rule (ndis)


The **PeriodicTimer** rule specifies that the caller of [**NdisCancelTimerObject**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscanceltimerobject) must be running at **IRQL = PASSIVE\_LEVEL** if a nonzero value was specified in the *MillisecondsPeriod* parameter of the [**NdisSetTimerObject**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissettimerobject) function. If the *MillisecondsPeriod* parameter of the **NdisSetTimerObject** function was zero, callers of **NdisCancelTimerObject** can be running at **IRQL &lt;= DISPATCH\_LEVEL**.

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>PeriodicTimer</strong> rule.</p>
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

[**NdisCancelTimerObject**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscanceltimerobject)
[**NdisSetTimerObject**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissettimerobject)
