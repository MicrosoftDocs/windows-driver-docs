---
title: StartIoCancel rule (wdm)
description: The StartIoCancel rule specifies that the driver must not call IoSetStartIoAttributes with the NonCancelable parameter set to FALSE before calling IoSetCancelRoutine with a non-NULLCancel routine.
ms.date: 05/21/2018
keywords: ["StartIoCancel rule (wdm)"]
topic_type:
- apiref
api_name:
- StartIoCancel
api_type:
- NA
ms.localizationpriority: medium
---

# StartIoCancel rule (wdm)


The **StartIoCancel** rule specifies that the driver must not call [**IoSetStartIoAttributes**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iosetstartioattributes) with the *NonCancelable* parameter set to **FALSE** before calling [**IoSetCancelRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcancelroutine) with a non-**NULL**[**Cancel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) routine.

Setting the *NonCancelable* parameter to **FALSE** before registering the [**Cancel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) routine can result in a cancellation race condition.

Because a driver's [**Cancel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) routine must include a call to [**IoReleaseCancelSpinLock**](/previous-versions/windows/hardware/drivers/ff549550(v=vs.85)) (to release the spin lock that the I/O Manager acquires before calling the **Cancel** routine), consider verifying your driver with both the **StartIoCancel** rule and the [**CancelSpinLock**](wdm-cancelspinlock.md) rule.

**Driver model: WDM**

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>StartIoCancel</strong> rule.</p>
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

[**IoSetCancelRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcancelroutine)
[**IoSetStartIoAttributes**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iosetstartioattributes)
## See also

[**CancelSpinLock**](wdm-cancelspinlock.md)
