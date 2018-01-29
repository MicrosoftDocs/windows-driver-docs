---
title: IrqlExAllocatePool rule (wdm)
description: The IrqlExAllocatePool rule specifies that the driver calls ExAllocatePoolWithTag and ExAllocatePoolWithTagPriority only when it is executing at IRQL DISPATCH\_LEVEL.
ms.assetid: 0bb179c5-e76b-46bc-b497-8639328d2eb2
keywords: ["IrqlExAllocatePool rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlExAllocatePool
api_type:
- NA
---

# IrqlExAllocatePool rule (wdm)


The **IrqlExAllocatePool** rule specifies that the driver calls [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) and [**ExAllocatePoolWithTagPriority**](https://msdn.microsoft.com/library/windows/hardware/ff544523) only when it is executing at IRQL&lt;=DISPATCH\_LEVEL.

A caller executing at DISPATCH\_LEVEL must specify a NonPaged*Xxx* value for *PoolType*. A caller executing at IRQL &lt;= APC\_LEVEL can specify any [**POOL\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559707) value.

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                                                                                                                        |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00020004), [**Bug Check 0xA: IRQL\_NOT\_LESS\_OR\_EQUAL**](https://msdn.microsoft.com/library/windows/hardware/ff560129) |

Example
-------

In the following example, the [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) routine is called after the [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917) routine, which sets IRQL to DISPATCH\_LEVEL. The **ExAllocatePoolWithTag** routine is called with **PagedPool**, which violates the rule.

```ManagedCPlusPlus
NTSTATUS
DispatchRequest (
    __in PDEVICE_REQUEST DeviceRequest
    )
{  
    KIRQL OldIrql;
    KSPIN_LOCK SpinLock;
    NTSTATUS Status;
    ...

    KeInitializeSpinLock(&amp;SpinLock);

    //
    // KeAcquireSpinLock sets IRQL to DISPATCH_LEVEL and the previous IRQL is 
    // written to OldIrql after the lock is acquired.
    //

    KeAcquireSpinLock(&amp;SpinLock, &amp;OldIrql);
    ...

    Status = ProcessRequest(DeviceRequest);

    //
    // KeReleaseSpinLock sets IRQL to the OldIrql returned by KeAcquireSpinLock.
    //

    KeReleaseSpinLock(&amp;SpinLock, &amp;OldIrql);
    ...
}

NTSTATUS
ProcessRequest (
    __in PDEVICE_REQUEST DeviceRequest
    )
{
    NTSTATUS Status;
    ...

    //
    // RULE VIOLATION! - IrqlExAllocatePool executing at DISPATCH_LEVEL must specify 
    //                   a NonPagedXxx value for PoolType. 
    //

    DeviceRequest->Context = ExAllocatePool(PagedPool, sizeof(REQUEST_CONTEXT));
    if (DeviceRequest->Context == NULL) {
        Status = STATUS_INSUFFICIENT_RESOURCES;
    }
    ...

    return Status;
}
```

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlExAllocatePool</strong> rule.</p>
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

[**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520)
[**ExAllocatePoolWithTagPriority**](https://msdn.microsoft.com/library/windows/hardware/ff544523)
See also
--------

[**Managing Hardware Priorities**](https://msdn.microsoft.com/library/windows/hardware/ff554368)
[**Preventing Errors and Deadlocks While Using Spin Locks**](https://msdn.microsoft.com/library/windows/hardware/ff559854)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20IrqlExAllocatePool%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




