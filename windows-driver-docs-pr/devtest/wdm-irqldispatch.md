---
title: IrqlDispatch rule (wdm)
description: The IrqlDispatch rule specifies that the driver calls the following DDIs only when it is executing at IRQL�  DISPATCH\_LEVEL.
ms.assetid: f72d4f27-b488-4d0a-97b7-9cb40f00e346
ms.date: 05/21/2018
keywords: ["IrqlDispatch rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlDispatch
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlDispatch rule (wdm)


The **IrqlDispatch** rule specifies that the driver calls the following DDIs only when it is executing at IRQL = DISPATCH\_LEVEL.

-   [**FreeAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff546507)

-   [**FreeMapRegisters**](https://msdn.microsoft.com/library/windows/hardware/ff546513)

-   [**GetScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff546531)

-   [**IoAllocateAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff548216)

-   [**IoAllocateController**](https://msdn.microsoft.com/library/windows/hardware/ff548224)

-   [**IoFreeController**](https://msdn.microsoft.com/library/windows/hardware/ff549104)

-   [**IoStartNextPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550358)

-   [**KeAcquireSpinLockAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff551921)

-   [**KeInsertByKeyDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff552178)

-   [**KeInsertDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff552180)

-   [**KeReleaseSpinLockFromDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553150)

-   [**KeRemoveByKeyDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff553152)

-   [**KeRemoveDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff553156)

-   [**PutScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff559967)

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                                                                                                                         |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xA: IRQL\_NOT\_LESS\_OR\_EQUAL**](https://msdn.microsoft.com/library/windows/hardware/ff560129) , [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00020003) |

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>IrqlDispatch</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh454281" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff545448" data-raw-source="[Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448)">Driver Verifier</a> and select the <a href="https://msdn.microsoft.com/library/windows/hardware/hh454208" data-raw-source="[DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208)">DDI compliance checking</a> option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**AllocateAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff540573)
[**AllocateCommonBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff540575)
[**BuildMdlFromScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff540686)
[**BuildScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff540689)
[**FlushAdapterBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff545917)
[**FreeAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff546507)
[**FreeCommonBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff546511)
[**FreeMapRegisters**](https://msdn.microsoft.com/library/windows/hardware/ff546513)
[**GetDmaAlignment**](https://msdn.microsoft.com/library/windows/hardware/ff546530)
[**GetScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff546531)
[**IoAllocateController**](https://msdn.microsoft.com/library/windows/hardware/ff548224)
[**IoFreeController**](https://msdn.microsoft.com/library/windows/hardware/ff549104)
[**IoStartNextPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550358)
[**IoWriteErrorLogEntry**](https://msdn.microsoft.com/library/windows/hardware/ff550527)
[**KeInsertByKeyDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff552178)
[**KeInsertDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff552180)
[**KeRemoveByKeyDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff553152)
[**KeRemoveDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff553156)
[**MapTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff554402)
[**PutDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff559965)
[**PutScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff559967)
[**ReadDmaCounter**](https://msdn.microsoft.com/library/windows/hardware/ff560782)
See also
--------

[**Managing Hardware Priorities**](https://msdn.microsoft.com/library/windows/hardware/ff554368)
[**Preventing Errors and Deadlocks While Using Spin Locks**](https://msdn.microsoft.com/library/windows/hardware/ff559854)
 

 





