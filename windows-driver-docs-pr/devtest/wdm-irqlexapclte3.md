---
title: IrqlExApcLte3 rule (wdm)
description: The IrqlExApcLte3 rule specifies that the driver calls the following executive support routines only at IRQL APC_LEVEL.
ms.date: 05/21/2018
keywords: ["IrqlExApcLte3 rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlExApcLte3
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlExApcLte3 rule (wdm)


The **IrqlExApcLte3** rule specifies that the driver calls the following executive support routines only at IRQL &lt;= APC\_LEVEL.

-   [**ExAcquireResourceExclusiveLite**](/previous-versions/ff544351(v=vs.85))

-   [**ExAcquireResourceSharedLite**](/previous-versions/ff544363(v=vs.85))

-   [**ExAcquireSharedStarveExclusive**](/previous-versions/ff544367(v=vs.85))

-   [**ExAcquireSharedWaitForExclusive**](/previous-versions/ff544370(v=vs.85))

-   [**ExConvertExclusiveToSharedLite**](/previous-versions/ff544558(v=vs.85))

-   [**ExDeleteResourceLite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exdeleteresourcelite)

Drivers that have errors related to IRQL can cause serious problems and could cause a computer to crash.

**Driver model: WDM**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x20007), [**Bug Check 0xA: IRQL\_NOT\_LESS\_OR\_EQUAL**](../debugger/bug-check-0xa--irql-not-less-or-equal.md)


## Example

The following code violates this rule:

```ManagedCPlusPlus
NTSTATUS
DispatchRequest (
    _In_ PDEVICE_REQUEST DeviceRequest
    )
{  
    KIRQL OldIrql;
    KSPIN_LOCK SpinLock;
    NTSTATUS Status;
    ...

    KeInitializeSpinLock(&SpinLock);

    //
    // KeAcquireSpinLock sets IRQL to DISPATCH_LEVEL and the previous IRQL is 
    // written to OldIrql after the lock is acquired.
    //

    KeAcquireSpinLock(&SpinLock, &OldIrql);
    ...

    Status = ProcessRequest(DeviceRequest);

    //
    // KeReleaseSpinLock sets IRQL to the OldIrql returned by KeAcquireSpinLock.
    //

    KeReleaseSpinLock(&SpinLock, &OldIrql);
    ...
}

NTSTATUS
ProcessRequest (
    _In_ PDEVICE_REQUEST DeviceRequest
    )
{
    ERESOURCE Resource;
    NTSTATUS Status;
    ...

    Resource = DeviceRequest->GetTableLock();

    //
    // RULE VIOLATION! - ExAcquireSharedStarveExclusive can be called only at 
    //                   IRQL <= APC_LEVEL. 
    //

    if(!ExAcquireSharedStarveExclusive(&Resource, FALSE)) {
        return STATUS_UNSUCCESSFUL;
    }

    ...

    ExReleaseResourceLite(&Resource);
    ...
    return Status;
}
```

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>IrqlExApcLte3</strong> rule.</p>
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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](./driver-verifier.md)">Driver Verifier</a> and select the <a href="/windows-hardware/drivers/devtest/ddi-compliance-checking" data-raw-source="[DDI compliance checking](./ddi-compliance-checking.md)">DDI compliance checking</a> option.</p></td>
</tr>
</tbody>
</table>

 

## Applies to

[**ExAcquireResourceExclusiveLite**](/previous-versions/ff544351(v=vs.85))
[**ExAcquireResourceSharedLite**](/previous-versions/ff544363(v=vs.85))
[**ExAcquireSharedStarveExclusive**](/previous-versions/ff544367(v=vs.85))
[**ExAcquireSharedWaitForExclusive**](/previous-versions/ff544370(v=vs.85))
[**ExConvertExclusiveToSharedLite**](/previous-versions/ff544558(v=vs.85))
[**ExDeleteResourceLite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exdeleteresourcelite)
## See also

[Managing Hardware Priorities](../kernel/managing-hardware-priorities.md)
[Preventing Errors and Deadlocks While Using Spin Locks](../kernel/preventing-errors-and-deadlocks-while-using-spin-locks.md)
