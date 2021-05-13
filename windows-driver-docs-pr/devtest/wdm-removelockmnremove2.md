---
title: RemoveLockMnRemove2 rule (wdm)
description: The RemoveLockMnRemove2 rule verifies that calls to IoAcquireRemoveLock and IoReleaseRemoveLockAndWait are used correctly when processing IRP\_MN\_REMOVE\_DEVICE request before the IRP is forwarded to lower drivers.
ms.date: 05/21/2018
keywords: ["RemoveLockMnRemove2 rule (wdm)"]
topic_type:
- apiref
api_name:
- RemoveLockMnRemove2
api_type:
- NA
ms.localizationpriority: medium
---

# RemoveLockMnRemove2 rule (wdm)


The **RemoveLockMnRemove2** rule verifies that calls to [**IoAcquireRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioacquireremovelock) and [**IoReleaseRemoveLockAndWait**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreleaseremovelockandwait) are used correctly when processing IRP\_MN\_REMOVE\_DEVICE request before the IRP is forwarded to lower drivers.

This rule only applies to FDO and FIDO drivers.

For example, consider a PnP driver stack that consists of a filter driver, a FDO, and a PDO.

The PnP manager sends a query remove through the stack. The FDO is enabled to idle while the system is running. The FDO decides to power down in the query removed state, so it requests a d0 IRP. Before the d0 IRP arrives, the PnP manager sends a PnP remove IRP and that IRP is processed by the filter driver. The filter driver detaches from the stack and cleans up its state. The d0 arrives at the top of the stack, but the filter driver does not send it down the stack because it has no context or data to know where to send it anymore. The FDO is hung waiting for the d0 IRP to arrive but that IRP never will.

**To avoid this error**

1.  Before a device is detached from the device stack, [**IoAcquireRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioacquireremovelock) must succeed before the IRP is forwarded down the stack for the following IRP types:

    -   IRP\_MN\_QUERY\_REMOVE
    -   IRP\_MN\_SUPRISE\_REMOVAL
    -   IRP\_MN\_REMOVE\_DEVICE

2.  [**IoReleaseRemoveLockAndWait**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreleaseremovelockandwait) should be called before calling [**IoDetachDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodetachdevice) or [**IoDeleteDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodeletedevice). (This makes sure that all remove locks are released in device drivers).

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>RemoveLockMnRemove2</strong> rule.</p>
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

[**IoAcquireRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioacquireremovelock)
[**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)
[**IoReleaseRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreleaseremovelock)
[**IoReleaseRemoveLockAndWait**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreleaseremovelockandwait)
[**PoCallDriver**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver)
