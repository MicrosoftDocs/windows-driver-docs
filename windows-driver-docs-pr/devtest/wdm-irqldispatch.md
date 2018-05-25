---
title: IrqlDispatch rule (wdm)
description: The IrqlDispatch rule specifies that the driver calls the following DDIs only when it is executing at IRQL�  DISPATCH\_LEVEL.
ms.assetid: f72d4f27-b488-4d0a-97b7-9cb40f00e346
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IrqlDispatch rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlDispatch
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlDispatch</strong> rule.</p>
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
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208) option.</p></td>
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
 

 





