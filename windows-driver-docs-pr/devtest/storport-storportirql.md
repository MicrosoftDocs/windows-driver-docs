---
title: StorPortIrql rule (storport)
description: The StorPortIrql rule checks that StorPort routines are called at the correct IRQL levels.
ms.assetid: 6A3946AB-DFB6-4447-9EF3-F0A003DB58E9
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

|              |          |
|--------------|----------|
| Driver model | Storport |

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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier)">Static Driver Verifier</a> and specify the <strong>StorPortIrql</strong> rule.</p>
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

[**StorPortAllocateContiguousMemorySpecifyCacheNode**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportallocatecontiguousmemoryspecifycachenode)
[**StorPortAllocateMdl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportallocatemdl)
[**StorPortAllocatePool**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportallocatepool)
[**StorPortBuildMdlForNonPagedPool**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportbuildmdlfornonpagedpool)
[**StorPortFreeContiguousMemorySpecifyCache**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportfreecontiguousmemoryspecifycache)
[**StorPortFreeMdl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportfreemdl)
[**StorPortFreePool**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportfreepool)
[**StorPortGetActiveGroupCount**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportgetactivegroupcount)
[**StorPortGetActiveNodeCount**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportgetactivenodecount)
[**StorPortGetCurrentProcessorNumber**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportgetcurrentprocessornumber)
[**StorPortGetGroupAffinity**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportgetgroupaffinity)
[**StorPortGetHighestNodeNumber**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportgethighestnodenumber)
[**StorPortGetLogicalProcessorRelationship**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportgetlogicalprocessorrelationship)
[**StorPortGetNodeAffinity**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportgetnodeaffinity)
[**StorPortGetSystemAddress**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportgetsystemaddress)
[**StorPortLogSystemEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportlogsystemevent)
[**StorPortPutScatterGatherList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportputscattergatherlist)
[**StorPortRegistryRead**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportregistryread)
[**StorPortRegistryWrite**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/storport/nf-storport-storportregistrywrite)
 

 





