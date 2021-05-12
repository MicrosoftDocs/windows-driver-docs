---
title: NdisAllocateMdl rule (ndis)
description: The NdisAllocateMdl rule specifies that NdisAllocateMdl and NdisFreeMdl are called in alternate order. The ultimate goal is to make sure all MDLs are freed when MiniportHaltEx ends.
ms.date: 05/21/2018
keywords: ["NdisAllocateMdl rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisAllocateMdl
api_type:
- NA
ms.localizationpriority: medium
---

# NdisAllocateMdl rule (ndis)


The **NdisAllocateMdl** rule specifies that [**NdisAllocateMdl**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatemdl) and [**NdisFreeMdl**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreemdl) are called in alternate order. The ultimate goal is to make sure all MDLs are freed when [*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt) ends.

The rule uses three different states. The state changes when an MDL is allocated or freed. If an MDL is still allocated when the [*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt) exits, the rule reports the defect.

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>NdisAllocateMdl</strong> rule.</p>
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

[**NdisAllocateMdl**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatemdl)
[**NdisFreeMdl**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreemdl)
