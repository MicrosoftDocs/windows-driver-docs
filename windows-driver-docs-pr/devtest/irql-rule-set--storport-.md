---
title: Irql rule set (Storport)
description: Use these rules to verify that your driver makes DDI calls at the required IRQL.A driver that does not follow the IRQL rules can cause serious problems during operation that can lead to deadlock conditions or computer crashes.
ms.assetid: 3322200A-2073-4568-B1FC-481B216D8F61
---

# Irql rule set (Storport)


Use these rules to verify that your driver makes DDI calls at the required IRQL.

A driver that does not follow the IRQL rules can cause serious problems during operation that can lead to deadlock conditions or computer crashes.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>IrqlDispatch</strong>](storport-irqldispatch.md)</p></td>
<td align="left"><p>This rule verifies that the following routines are only called at <strong>IRQL = DISPATCH_LEVEL</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrqlKeReleaseSpinLock</strong>](storport-irqlkereleasespinlock.md)</p></td>
<td align="left"><p>This rule verifies that <strong>KeReleaseSpinLock</strong> is called at <strong>IRQL = DISPATCH_LEVEL</strong> only. It must also set the IRQL to the previous IRQL level. Typically this call would be preceded by a call to <strong>KeAcquireSpinLock</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SpChangeIrql</strong>](storport-spchangeirql.md)</p></td>
<td align="left"><p>This rule verifies that the StorPort callback routines return at the same IRQL level as the level at which they are called.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SpIrql</strong>](storport-spirql.md)</p></td>
<td align="left"><p>This rule verifies that the routines <strong>TdiRegisterPnPHandlers</strong> and <strong>TdiDeregisterPnPHandlers</strong> are only called at IRQL lower than <strong>DISPATCH_LEVEL</strong>. However, if <strong>ExFreeToNPagedLookasideList</strong> is called, the rule passes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>StorPortIrql</strong>](storport-storportirql.md)</p></td>
<td align="left"><p>The [<strong>StorPortIrql</strong>](storport-storportirql.md) rule checks that StorPort routines are called at the correct IRQL levels.</p></td>
</tr>
</tbody>
</table>

 

**To select the Irql rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **Irql**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **Irql.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:Irql.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Irql%20rule%20set%20%28Storport%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




