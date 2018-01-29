---
title: RemoveLockMnRemove2 rule (wdm)
description: The RemoveLockMnRemove2 rule verifies that calls to IoAcquireRemoveLock and IoReleaseRemoveLockAndWait are used correctly when processing IRP\_MN\_REMOVE\_DEVICE request before the IRP is forwarded to lower drivers.
ms.assetid: 69CCB0CB-86E0-4994-AC3E-44A4B9993EBC
keywords: ["RemoveLockMnRemove2 rule (wdm)"]
topic_type:
- apiref
api_name:
- RemoveLockMnRemove2
api_type:
- NA
---

# RemoveLockMnRemove2 rule (wdm)


The **RemoveLockMnRemove2** rule verifies that calls to [**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [**IoReleaseRemoveLockAndWait**](https://msdn.microsoft.com/library/windows/hardware/ff549567) are used correctly when processing IRP\_MN\_REMOVE\_DEVICE request before the IRP is forwarded to lower drivers.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>RemoveLockMnRemove2</strong> rule.</p>
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

[**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204)
[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560)
[**IoReleaseRemoveLockAndWait**](https://msdn.microsoft.com/library/windows/hardware/ff549567)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20RemoveLockMnRemove2%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




