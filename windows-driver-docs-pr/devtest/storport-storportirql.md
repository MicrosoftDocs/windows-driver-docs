---
title: StorPortIrql rule (storport)
description: The StorPortIrql rule checks that StorPort routines are called at the correct IRQL levels.
ms.date: 05/21/2018
keywords: ["StorPortIrql rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortIrql
api_type:
- NA
ms.localizationpriority: medium
---

# StorPortIrql rule (storport)


The **StorPortIrql** rule checks that StorPort routines are called at the correct IRQL levels.

**Driver model: Storport**

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>StorPortIrql</strong> rule.</p>
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

[**StorPortAllocateContiguousMemorySpecifyCacheNode**](/windows-hardware/drivers/ddi/storport/nf-storport-storportallocatecontiguousmemoryspecifycachenode)
[**StorPortAllocateMdl**](/windows-hardware/drivers/ddi/storport/nf-storport-storportallocatemdl)
[**StorPortAllocatePool**](/windows-hardware/drivers/ddi/storport/nf-storport-storportallocatepool)
[**StorPortBuildMdlForNonPagedPool**](/windows-hardware/drivers/ddi/storport/nf-storport-storportbuildmdlfornonpagedpool)
[**StorPortFreeContiguousMemorySpecifyCache**](/windows-hardware/drivers/ddi/storport/nf-storport-storportfreecontiguousmemoryspecifycache)
[**StorPortFreeMdl**](/windows-hardware/drivers/ddi/storport/nf-storport-storportfreemdl)
[**StorPortFreePool**](/windows-hardware/drivers/ddi/storport/nf-storport-storportfreepool)
[**StorPortGetActiveGroupCount**](/windows-hardware/drivers/ddi/storport/nf-storport-storportgetactivegroupcount)
[**StorPortGetActiveNodeCount**](/windows-hardware/drivers/ddi/storport/nf-storport-storportgetactivenodecount)
[**StorPortGetCurrentProcessorNumber**](/windows-hardware/drivers/ddi/storport/nf-storport-storportgetcurrentprocessornumber)
[**StorPortGetGroupAffinity**](/windows-hardware/drivers/ddi/storport/nf-storport-storportgetgroupaffinity)
[**StorPortGetHighestNodeNumber**](/windows-hardware/drivers/ddi/storport/nf-storport-storportgethighestnodenumber)
[**StorPortGetLogicalProcessorRelationship**](/windows-hardware/drivers/ddi/storport/nf-storport-storportgetlogicalprocessorrelationship)
[**StorPortGetNodeAffinity**](/windows-hardware/drivers/ddi/storport/nf-storport-storportgetnodeaffinity)
[**StorPortGetSystemAddress**](/windows-hardware/drivers/ddi/storport/nf-storport-storportgetsystemaddress)
[**StorPortLogSystemEvent**](/windows-hardware/drivers/ddi/storport/nf-storport-storportlogsystemevent)
[**StorPortPutScatterGatherList**](/windows-hardware/drivers/ddi/storport/nf-storport-storportputscattergatherlist)
[**StorPortRegistryRead**](/windows-hardware/drivers/ddi/storport/nf-storport-storportregistryread)
[**StorPortRegistryWrite**](/windows-hardware/drivers/ddi/storport/nf-storport-storportregistrywrite)
