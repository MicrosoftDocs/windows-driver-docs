---
title: StorPortIrql rule (storport)
description: The StorPortIrql rule checks that StorPort routines are called at the correct IRQL levels.
ms.assetid: 6A3946AB-DFB6-4447-9EF3-F0A003DB58E9
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>StorPortIrql</strong> rule.</p>
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

[**StorPortAllocateContiguousMemorySpecifyCacheNode**](https://msdn.microsoft.com/library/windows/hardware/ff567027)
[**StorPortAllocateMdl**](https://msdn.microsoft.com/library/windows/hardware/ff567028)
[**StorPortAllocatePool**](https://msdn.microsoft.com/library/windows/hardware/ff567031)
[**StorPortBuildMdlForNonPagedPool**](https://msdn.microsoft.com/library/windows/hardware/ff567036)
[**StorPortFreeContiguousMemorySpecifyCache**](https://msdn.microsoft.com/library/windows/hardware/ff567059)
[**StorPortFreeMdl**](https://msdn.microsoft.com/library/windows/hardware/ff567063)
[**StorPortFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff567065)
[**StorPortGetActiveGroupCount**](https://msdn.microsoft.com/library/windows/hardware/ff567071)
[**StorPortGetActiveNodeCount**](https://msdn.microsoft.com/library/windows/hardware/ff567073)
[**StorPortGetCurrentProcessorNumber**](https://msdn.microsoft.com/library/windows/hardware/ff567077)
[**StorPortGetGroupAffinity**](https://msdn.microsoft.com/library/windows/hardware/ff567084)
[**StorPortGetHighestNodeNumber**](https://msdn.microsoft.com/library/windows/hardware/ff567085)
[**StorPortGetLogicalProcessorRelationship**](https://msdn.microsoft.com/library/windows/hardware/ff567087)
[**StorPortGetNodeAffinity**](https://msdn.microsoft.com/library/windows/hardware/ff567091)
[**StorPortGetSystemAddress**](https://msdn.microsoft.com/library/windows/hardware/ff567100)
[**StorPortLogSystemEvent**](https://msdn.microsoft.com/library/windows/hardware/ff567428)
[**StorPortPutScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff567463)
[**StorPortRegistryRead**](https://msdn.microsoft.com/library/windows/hardware/ff567491)
[**StorPortRegistryWrite**](https://msdn.microsoft.com/library/windows/hardware/ff567492)
 

 





