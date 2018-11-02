---
title: RemoveLockQueryMnRemove rule (wdm)
description: The RemoveLockQueryMnRemove rule verifies that calls to IoAcquireRemoveLock and IoReleaseRemoveLock are used correctly when processing IRP\_MJ\_PNP with MinorFunction IRP\_MN\_QUERY\_REMOVE\_DEVICE.
ms.assetid: 593B8305-EA61-4857-9304-A8319A8E0017
ms.date: 05/21/2018
keywords: ["RemoveLockQueryMnRemove rule (wdm)"]
topic_type:
- apiref
api_name:
- RemoveLockQueryMnRemove
api_type:
- NA
ms.localizationpriority: medium
---

# RemoveLockQueryMnRemove rule (wdm)


The **RemoveLockQueryMnRemove** rule verifies that calls to [**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used correctly when processing IRP\_MJ\_PNP with MinorFunction IRP\_MN\_QUERY\_REMOVE\_DEVICE. The driver should acquire the remove lock before forwarding the IRP down the stack.

This rule only applies to FDO and FIDO drivers.

For example, consider a PnP driver stack that consists of a filter driver, a FDO, and a PDO.

The PnP manager sends a query remove through the stack. The FDO is enabled to idle while the system is running. The FDO decides to power down in the query removed state, so it requests a d0 IRP. Before the d0 IRP arrives, the PnP manager sends a PnP remove IRP and that IRP is processed by the filter driver. The filter driver detaches from the stack and cleans up its state. The d0 arrives at the top of the stack, but the filter driver does not send it down the stack because it has no context or data to know where to send it anymore. The FDO is hung waiting for the d0 IRP to arrive but that IRP never will.

**To avoid this error**

1.  Before a device is detached from the device stack, [**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204) must succeed before the IRP is forwarded down the stack for the following IRP types:

    -   IRP\_MN\_QUERY\_REMOVE
    -   IRP\_MN\_SUPRISE\_REMOVAL
    -   IRP\_MN\_REMOVE\_DEVICE

2.  [**IoReleaseRemoveLockAndWait**](https://msdn.microsoft.com/library/windows/hardware/ff549567) should be called before calling [**IoDetachDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549087) or [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083). (This makes sure that all remove locks are released in device drivers).

|              |     |
|--------------|-----|
| Driver model | WDM |

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>RemoveLockQueryMnRemove</strong> rule.</p>
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

Applies to
----------

[**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204)
[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
 

 





