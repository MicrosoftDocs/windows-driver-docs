---
title: Init\_RegisterSG rule (ndis)
description: The Init\_RegisterSG rule specifies that the registration of the scatter-gather list (SG), which usually happens during initialization, must be undone if something goes wrong in the initialization process or during the halting of the miniport driver.If NdisMRegisterScatterGatherDma is called at least one time during MiniportInitializeEx, the NdisMDeregisterScatterGatherDma function should be called at least one time in MiniportHaltEx.
ms.date: 05/21/2018
keywords: ["Init_RegisterSG rule (ndis)"]
topic_type:
- apiref
api_name:
- Init_RegisterSG
api_type:
- NA
ms.localizationpriority: medium
---

# Init\_RegisterSG rule (ndis)


The Init\_RegisterSG rule specifies that the registration of the scatter-gather list (SG), which usually happens during initialization, must be undone if something goes wrong in the initialization process or during the halting of the miniport driver.

If **NdisMRegisterScatterGatherDma** is called at least one time during **MiniportInitializeEx**, the **NdisMDeregisterScatterGatherDma** function should be called at least one time in **MiniportHaltEx**.

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>Init_RegisterSG</strong> rule.</p>
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

[**NdisMDeregisterScatterGatherDma**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismderegisterscattergatherdma)
[**NdisMRegisterScatterGatherDma**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterscattergatherdma)
