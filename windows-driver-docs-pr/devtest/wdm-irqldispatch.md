---
title: IrqlDispatch rule (wdm)
description: The IrqlDispatch rule specifies that the driver calls the following DDIs only when it is executing at IRQL�  DISPATCH\_LEVEL.
ms.assetid: f72d4f27-b488-4d0a-97b7-9cb40f00e346
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
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20IrqlDispatch%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




