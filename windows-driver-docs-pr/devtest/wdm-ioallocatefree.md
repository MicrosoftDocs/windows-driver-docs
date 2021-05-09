---
title: IoAllocateFree rule
description: The IoAllocateFree rule specifies that a driver should use IoFreeIrp only on IRPs that were previously allocated with IoAllocateIrp.
ms.date: 05/21/2018
keywords: ["IoAllocateFree rule"]
topic_type:
- apiref
api_name:
- IoAllocateFree
api_type:
- NA
ms.localizationpriority: medium
---

# IoAllocateFree rule


The **IoAllocateFree** rule specifies that a driver should use [**IoFreeIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iofreeirp) only on IRPs that were previously allocated with [**IoAllocateIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp).

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>IoAllocateFree</strong> rule.</p>
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

[**ExInterlockedInsertHeadList**](/previous-versions/ff545397(v=vs.85))
[**ExInterlockedInsertTailList**](/previous-versions/ff545402(v=vs.85))
[**ExInterlockedPushEntryList**](/previous-versions/ff545418(v=vs.85))
[**InsertHeadList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-insertheadlist)
[**IoAllocateIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp)
[**IoCsqInsertIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocsqinsertirp)
[**IoCsqInsertIrpEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocsqinsertirpex)
[**IoFreeIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iofreeirp)
[**RemoveHeadList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-removeheadlist)
