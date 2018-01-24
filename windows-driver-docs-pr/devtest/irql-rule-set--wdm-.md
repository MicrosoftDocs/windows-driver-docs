---
title: Irql rule set (WDM)
description: Use these rules to verify that your driver makes DDI calls at the required IRQL.A driver that does not follow the IRQL rules can cause serious problems during operation that can lead to deadlock conditions or computer crashes.
ms.assetid: 40C17906-58D5-4023-A549-0164C3A92A06
---

# Irql rule set (WDM)


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
<td align="left"><p>[<strong>ForwardedAtBadIrql</strong>](wdm-forwardedatbadirql.md)</p></td>
<td align="left"><p>The [<strong>ForwardedAtBadIrql</strong>](wdm-forwardedatbadirql.md) rule specifies that the driver should call [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336) and [<strong>PoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559654) at IRQL&lt;DISPATCH_LEVEL unless the IRP major function code being forwarded is one of the following:</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ForwardedAtBadIrqlAllocate</strong>](wdm-forwardedatbadirqlallocate.md)</p></td>
<td align="left"><p>The [<strong>ForwardedAtBadIrqlAllocate</strong>](wdm-forwardedatbadirqlallocate.md) rule specifies that the driver should call [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336) and [<strong>PoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559654) at IRQL&lt;DISPATCH_LEVEL, unless the IRP major function code being forwarded is one of the following:</p>
<ul>
<li>[<strong>IRP_MJ_POWER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550784)</li>
<li>[<strong>IRP_MJ_READ</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550794)</li>
<li>[<strong>IRP_MJ_WRITE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550819)</li>
<li>[<strong>IRP_MJ_DEVICE_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550744)</li>
<li>[<strong>IRP_MJ_INTERNAL_DEVICE_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550766)</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ForwardedAtBadIrqlFsdAsync</strong>](wdm-forwardedatbadirqlfsdasync.md)</p></td>
<td align="left"><p>The [<strong>ForwardedAtBadIrqlFsdAsync</strong>](wdm-forwardedatbadirqlfsdasync.md) rule specifies that the driver call [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336) and [<strong>PoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559654) at IRQL&lt;DISPATCH_LEVEL, unless the IRP major function code being forwarded is one of the following:</p>
<ul>
<li>[<strong>IRP_MJ_POWER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550784)</li>
<li>[<strong>IRP_MJ_READ</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550794)</li>
<li>[<strong>IRP_MJ_WRITE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550819)</li>
<li>[<strong>IRP_MJ_DEVICE_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550744)</li>
<li>[<strong>IRP_MJ_INTERNAL_DEVICE_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550766)</li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ForwardedAtBadIrqlFsdSync</strong>](wdm-forwardedatbadirqlfsdsync.md)</p></td>
<td align="left"><p>The [<strong>ForwardedAtBadIrqlFsdSync</strong>](wdm-forwardedatbadirqlfsdsync.md) rule specifies that the driver call [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336) and [<strong>PoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559654) at IRQL&lt;DISPATCH_LEVEL, unless the IRP major function code being forwarded is one of the following:</p>
<ul>
<li>[<strong>IRP_MJ_POWER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550784)</li>
<li>[<strong>IRP_MJ_READ</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550794)</li>
<li>[<strong>IRP_MJ_WRITE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550819)</li>
<li>[<strong>IRP_MJ_DEVICE_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550744)</li>
<li>[<strong>IRP_MJ_INTERNAL_DEVICE_CONTROL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550766)</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IrqlApcLte</strong>](wdm-irqlapclte.md)</p></td>
<td align="left"><p>The [<strong>IrqlApcLte</strong>](wdm-irqlapclte.md) rule specifies that the driver calls [<strong>ObGetObjectSecurity</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557738) and [<strong>ObReleaseObjectSecurity</strong>](https://msdn.microsoft.com/library/windows/hardware/ff558695) only when it is executing at IRQL &lt;= APC_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrqlDispatch</strong>](wdm-irqldispatch.md)</p></td>
<td align="left"><p>The [<strong>IrqlDispatch</strong>](wdm-irqldispatch.md) rule specifies that the driver calls the following DDIs only when it is executing at IRQL = DISPATCH_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IrqlExAllocatePool</strong>](wdm-irqlexallocatepool.md)</p></td>
<td align="left"><p>The [<strong>IrqlExAllocatePool</strong>](wdm-irqlexallocatepool.md) rule specifies that the driver calls [<strong>ExAllocatePoolWithTag</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544520) and [<strong>ExAllocatePoolWithTagPriority</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544523) only when it is executing at IRQL&lt;=DISPATCH_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrqlExApcLte1</strong>](wdm-irqlexapclte1.md)</p></td>
<td align="left"><p>The [<strong>IrqlExApcLte1</strong>](wdm-irqlexapclte1.md) rule specifies that the driver calls [<strong>ExAcquireFastMutex</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544337) and [<strong>ExTryToAcquireFastMutex</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545647) only at IRQL &lt;= APC_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IrqlExApcLte2</strong>](wdm-irqlexapclte2.md)</p></td>
<td align="left"><p>The [<strong>IrqlExApcLte2</strong>](wdm-irqlexapclte2.md) rule specifies that the driver calls the following routines only at IRQL &lt;= APC_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrqlExApcLte3</strong>](wdm-irqlexapclte3.md)</p></td>
<td align="left"><p>The [<strong>IrqlExApcLte3</strong>](wdm-irqlexapclte3.md) rule specifies that the driver calls the following executive support routines only at IRQL &lt;= APC_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IrqlExApcLteInline</strong>](wdm-irqlexapclteinline.md)</p></td>
<td align="left"><p>The [<strong>IrqlExApcLteInline</strong>](wdm-irqlexapclteinline.md) rule specifies that DDIs are only called at proper IRQL levels</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrqlExFree1</strong>](wdm-irqlexfree1.md)</p></td>
<td align="left"><p>The [<strong>IrqlExFree1</strong>](wdm-irqlexfree1.md) rule specifies that [<strong>ExFreePool</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544590) and [<strong>ExFreePoolWithTag</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544593) are called at proper IRQL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IrqlExFree2</strong>](wdm-irqlexfree2.md)</p></td>
<td align="left"><p>The [<strong>IrqlExFree2</strong>](wdm-irqlexfree2.md) rule specifies that [<strong>ExFreePool</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544590) and [<strong>ExFreePoolWithTag</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544593) are called at proper IRQL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrqlExFree3</strong>](wdm-irqlexfree3.md)</p></td>
<td align="left"><p>The [<strong>IrqlExFree3</strong>](wdm-irqlexfree3.md) rule specifies that [<strong>ExFreePool</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544590) and [<strong>ExFreePoolWithTag</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544593) are called at proper IRQL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IrqlExPassive</strong>](wdm-irqlexpassive.md)</p></td>
<td align="left"><p>The [<strong>IrqlExPassive</strong>](wdm-irqlexpassive.md) rule specifies that the driver calls the following executive support routines only at IRQL = PASSIVE_LEVEL:</p>
<ul>
<li><p>[<strong>ExCreateCallback</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544560)</p></li>
<li><p>[<strong>ExIsProcessorFeaturePresent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545442)</p></li>
<li><p>[<strong>ExRaiseAccessViolation</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545509)</p></li>
<li><p>[<strong>ExRaiseDatatypeMisalignment</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545524)</p></li>
<li><p>[<strong>ExRaiseStatus</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545529)</p></li>
<li><p>[<strong>ExUuidCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545658)</p></li>
</ul>
<p>The [<strong>IrqlExPassive</strong>](wdm-irqlexpassive.md) rule also specifies that the driver calls [<strong>ExRaiseStatus</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545529) at IRQL &lt;= APC_LEVEL</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrqlIoApcLte</strong>](wdm-irqlioapclte.md)</p></td>
<td align="left"><p>The [<strong>IrqlIoApcLte</strong>](wdm-irqlioapclte.md) rule specifies that the driver calls the following I/O manager routines only when it is executing at IRQL &lt;= APC_LEVEL:</p>
<ul>
<li><p>[<strong>IoDeleteDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549083)</p></li>
<li><p>[<strong>IoGetInitialStack</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549247)</p></li>
<li><p>[<strong>IoRaiseHardError</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549482)</p></li>
<li><p>[<strong>IoRaiseInformationalHardError</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549488)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IrqlIoDispatch</strong>](wdm-irqliodispatch.md)</p></td>
<td align="left"><p>The [<strong>IrqlIoDispatch</strong>](wdm-irqliodispatch.md) rule specifies that the driver calls the following I/O Manager routines only when it is executing at IRQL &lt;= DISPATCH_LEVEL: [<strong>IoGetDeviceToVerify</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549212), [<strong>IoSetDeviceToVerify</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548529).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrqlIoPassive1</strong>](wdm-irqliopassive1.md)</p></td>
<td align="left"><p>The [<strong>IrqlIoPassive1</strong>](wdm-irqliopassive1.md) rule specifies that the driver calls the following routines only when it is executing at IRQL = PASSIVE_LEVEL:</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IrqlIoPassive2</strong>](wdm-irqliopassive2.md)</p></td>
<td align="left"><p>The [<strong>IrqlIoPassive2</strong>](wdm-irqliopassive2.md) rule specifies that the driver calls the following I/O Manager routines only at IRQL = PASSIVE_LEVEL:</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrqlIoPassive3</strong>](wdm-irqliopassive3.md)</p></td>
<td align="left"><p>The IrqlIoPassive3 rule specifies that the driver calls the following routines only when it is executing at IRQL = PASSIVE_LEVEL:</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IrqlIoPassive4</strong>](wdm-irqliopassive4.md)</p></td>
<td align="left"><p>The [<strong>IrqlIoPassive4</strong>](wdm-irqliopassive4.md) rule specifies that the driver calls the following routines only when it is executing at IRQL = PASSIVE_LEVEL:</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrqlIoPassive5</strong>](wdm-irqliopassive5.md)</p></td>
<td align="left"><p>The [<strong>IrqlIoPassive5</strong>](wdm-irqliopassive5.md) rule specifies that the driver calls specific I/O Manager routines only when it is executing at IRQL = PASSIVE_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IrqlKeApcLte1</strong>](wdm-irqlkeapclte1.md)</p></td>
<td align="left"><p>The [<strong>IrqlKeApcLte1</strong>](wdm-irqlkeapclte1.md) rule specifies that the driver calls the following kernel routines only when it is executing at IRQL &lt;= APC_LEVEL:</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrqlKeApcLte2</strong>](wdm-irqlkeapclte2.md)</p></td>
<td align="left"><p>The [<strong>IrqlKeApcLte2</strong>](wdm-irqlkeapclte2.md) rule specifies that the driver calls the following kernel routines only when it is executing at IRQL &lt;= APC_LEVEL:</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IrqlKeDispatchLte</strong>](wdm-irqlkedispatchlte.md)</p></td>
<td align="left"><p>The [<strong>IrqlKeDispatchLte</strong>](wdm-irqlkedispatchlte.md) rule specifies that the driver calls the following kernel routines only when it is executing at IRQL &lt;= DISPATCH_LEVEL:</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrqlKeRaiseLower</strong>](wdm-irqlkeraiselower.md)</p></td>
<td align="left"><p>The [<strong>IrqlKeRaiseLower</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547817) rule specifies that the driver does the following when raising and lowering the IRQL:</p>
When the driver calls [<strong>KeRaiseIrql</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553079), it is executing at an IRQL that is lower than or equal to the value of the <em>NewIrql</em> parameter.<br />
The driver calls [<strong>KeLowerIrql</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552968) only after calling <strong>KeRaiseIrql</strong> or [<strong>KeRaiseIrqlToDpcLevel</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553084).<br />
</td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IrqlKeRaiseLower2</strong>](wdm-irqlkeraiselower2.md)</p></td>
<td align="left"><p>The [<strong>IrqlKeRaiseLower2</strong>](wdm-irqlkeraiselower2.md) rule specifies that drivers use [<strong>KeLowerIrql</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552968) to restore the original IRQL raised by a preceding call to [<strong>KeRaiseIrql</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553079) or [<strong>KeRaiseIrqlToDpcLevel</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553084).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrqlKeReleaseSpinLock</strong>](wdm-irqlkereleasespinlock.md)</p></td>
<td align="left"><p>The [<strong>IrqlKeReleaseSpinLock</strong>](wdm-irqlkereleasespinlock.md) rule specifies that the driver calls [<strong>KeReleaseSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553145) only when it is executing at IRQL = DISPATCH_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IrqlKeSetEvent</strong>](wdm-irqlkesetevent.md)</p></td>
<td align="left"><p>The [<strong>IrqlKeSetEvent</strong>](wdm-irqlkesetevent.md) rule specifies that the [<strong>KeSetEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553253) routine is only called at IRQL &lt;= DISPATCH_LEVEL when <em>Wait</em> is set to <strong>FALSE</strong>, and at IRQL &lt;= APC_LEVEL when <em>Wait</em> is set to <strong>TRUE</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrqlKeWaitForMutexObject</strong>](wdm-irqlkewaitformutexobject.md)</p></td>
<td align="left"><p>The [<strong>IrqlKeWaitForMutexObject</strong>](wdm-irqlkewaitformutexobject.md) rule specifies the driver to call the [<strong>KeWaitForMutexObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553344) routine at the proper IRQL based on the value of the <em>Timeout</em> parameter:</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IrqlKeWaitForMultipleObjects</strong>](wdm-irqlkewaitformultipleobjects.md)</p></td>
<td align="left"><p>The [<strong>IrqlKeWaitForMultipleObjects</strong>](wdm-irqlkewaitformultipleobjects.md) rule specifies that callers of the [<strong>KeWaitForMultipleObjects</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553324) routine must be running at proper IRQL based upon the <em>Timeout</em> parameter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrqlMmApcLte</strong>](wdm-irqlmmapclte.md)</p></td>
<td align="left"><p>The [<strong>IrqlMmApcLte</strong>](wdm-irqlmmapclte.md) rule specifies that the driver calls the following memory manager routines only when it is executing at IRQL &lt;= APC_LEVEL:</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IrqlMmDispatch</strong>](wdm-irqlmmdispatch.md)</p></td>
<td align="left"><p>The [<strong>IrqlMmDispatch</strong>](wdm-irqlmmdispatch.md) rule specifies that the driver calls [<strong>MmFreeContiguousMemory</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554503) only when it is executing at <strong>IRQL &lt;= DISPATCH_LEVEL</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrqlObPassive</strong>](wdm-irqlobpassive.md)</p></td>
<td align="left"><p>The [<strong>IrqlObPassive</strong>](wdm-irqlobpassive.md) rule specifies that the driver calls [<strong>ObReferenceObjectByHandle</strong>](https://msdn.microsoft.com/library/windows/hardware/ff558679) only when it is executing at IRQL = PASSIVE_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IrqlPsPassive</strong>](wdm-irqlpspassive.md)</p></td>
<td align="left"><p>The [<strong>IrqlPsPassive</strong>](wdm-irqlpspassive.md) rule specifies that the driver calls the following [<strong>Process Structure routines</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559917) only when it is executing at IRQL = PASSIVE_LEVEL:</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrqlReturn</strong>](wdm-irqlreturn.md)</p></td>
<td align="left"><p>The [<strong>IrqlReturn</strong>](wdm-irqlreturn.md) rule specifies that the driver's dispatch routines return at the same IRQL at which they were called.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IrqlRtlPassive</strong>](wdm-irqlrtlpassive.md)</p></td>
<td align="left"><p>The IrqlRtlPassive rule specifies that the driver calls [<strong>RtlDeleteRegistryValue</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561829) only when it is executing at IRQL = PASSIVE_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrqlZwPassive</strong>](wdm-irqlzwpassive.md)</p></td>
<td align="left"><p>The [<strong>IrqlZwPassive</strong>](wdm-irqlzwpassive.md) rule specifies that the driver calls [<strong>ZwClose</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566417) only when it is executing at IRQL = PASSIVE_LEVEL.</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Irql%20rule%20set%20%28WDM%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




