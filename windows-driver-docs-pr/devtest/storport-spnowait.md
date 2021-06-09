---
title: SpNoWait rule (storport)
description: This rule verifies that waits or data allocation are not performed inside StartIo.
ms.date: 05/21/2018
keywords: ["SpNoWait rule (storport)"]
topic_type:
- apiref
api_name:
- SpNoWait
api_type:
- NA
ms.localizationpriority: medium
---

# SpNoWait rule (storport)


This rule verifies that waits or data allocation are not performed inside **StartIo**.

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>SpNoWait</strong> rule.</p>
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

[**StorPortStallExecution**](/windows-hardware/drivers/ddi/storport/nf-storport-storportstallexecution)
[**ExAcquireSharedWaitForExclusive**](/previous-versions/ff544370(v=vs.85))
[**ExAllocatePool**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool)
[**ExAllocatePoolWithQuota**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithquota)
[**ExAllocatePoolWithQuotaTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithquotatag)
[**ExAllocatePoolWithTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtag)
[**ExAllocatePoolWithTagPriority**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtagpriority)
[**ExWaitForRundownProtectionRelease**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exwaitforrundownprotectionrelease)
[**IoAllocateController**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioallocatecontroller)
[**IoAllocateIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp)
[**IoWMIAllocateInstanceIds**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iowmiallocateinstanceids)
[**KeWaitForMultipleObjects**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitformultipleobjects)
[**KeWaitForMutexObject**](https://msdn.microsoft.com/library/windows/hardware/ff553344)
[**KeWaitForSingleObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitforsingleobject)
[**MmAllocateNonCachedMemory**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-mmallocatenoncachedmemory)
[**MmAllocatePagesForMdl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmallocatepagesformdl)
[**ZwAllocateLocallyUniqueId**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwallocatelocallyuniqueid)
[**ZwAllocateVirtualMemory**](/previous-versions/ff566416(v=vs.85))
[**ZwWaitForSingleObject**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwwaitforsingleobject)
