---
title: StorPortIrql rule (storport)
description: The StorPortIrql rule checks that StorPort routines are called at the correct IRQL levels.
ms.assetid: 6A3946AB-DFB6-4447-9EF3-F0A003DB58E9
keywords: ["StorPortIrql rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortIrql
api_type:
- NA
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
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20StorPortIrql%20rule%20%28storport%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




