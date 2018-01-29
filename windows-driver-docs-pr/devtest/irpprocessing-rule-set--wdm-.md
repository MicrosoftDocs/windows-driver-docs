---
title: IrpProcessing rule set (WDM)
description: Use these rules to verify that your driver correctly processes I/O request packets (IRP).
ms.assetid: C11F1FD7-DA41-4A72-A0EB-97C1D79ECC21
---

# IrpProcessing rule set (WDM)


Use these rules to verify that your driver correctly processes I/O request packets (IRP).

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
<td align="left"><p>[<strong>CompleteRequest</strong>](wdm-completerequest.md)</p></td>
<td align="left"><p>The [<strong>CompleteRequest</strong>](wdm-completerequest.md) rule verifies that the [<strong>IoCompleteRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548343) routine is not called after a completion routine runs and that it does not return STATUS_MORE_PROCESSING_REQUIRED.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>CompleteRequestStatusCheck</strong>](wdm-completerequeststatuscheck.md)</p></td>
<td align="left"><p>The [<strong>CompleteRequestStatusCheck</strong>](wdm-completerequeststatuscheck.md) rule verifies that the I/O status value in the IRP matches the status value returned by the lower driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>CompletionRoutineRegistered</strong>](wdm-completionroutineregistered.md)</p></td>
<td align="left"><p>The [<strong>CompletionRoutineRegistered</strong>](wdm-completionroutineregistered.md) rule specifies that if the dispatch routine registers an [<strong>IoCompletion</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine using [<strong>IoSetCompletionRoutineEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549686), the dispatch routine must thereafter call [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336) or [<strong>PoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559654).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DoubleCompletion</strong>](wdm-doublecompletion.md)</p></td>
<td align="left"><p>The [<strong>DoubleCompletion (WDM)</strong>](wdm-doublecompletion.md) rule specifies that the driver must not call the [<strong>IoCompleteRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548343) routine twice for the same IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IoReuseIrp</strong>](wdm-ioreuseirp.md)</p></td>
<td align="left"><p>The [<strong>IoReuseIrp</strong>](wdm-ioreuseirp.md) rule specifies that a driver should use [<strong>IoReuseIrp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549661) only on IRPs that it previously allocated with [<strong>IoAllocateIrp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548257).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IoReuseIrp2</strong>](wdm-ioreuseirp2.md)</p></td>
<td align="left"><p>The [<strong>IoReuseIrp2</strong>](wdm-ioreuseirp2.md) rule specifies that a driver should use [<strong>IoReuseIrp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549661) only on IRPs that it previously allocated within the driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IoSetCompletionExCompleteIrp</strong>](wdm-iosetcompletionexcompleteirp.md)</p></td>
<td align="left"><p>The [<strong>IoSetCompletionExCompleteIrp</strong>](wdm-iosetcompletionexcompleteirp.md) rule specifies that the [<strong>IoSetCompletionRoutineEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549686) routine returns an NTSTATUS value. The driver must check this value to determine if the [<em>IoCompletion</em>](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine was successfully registered before calling [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336) or [<strong>PoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559654) and if <strong>IoSetCompletionRoutineEx</strong> fails then the IRP should be completed and the dispatch routine should return.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IoSetCompletionRoutineExCheck</strong>](wdm-iosetcompletionroutineexcheck.md)</p></td>
<td align="left"><p>The [<strong>IoSetCompletionRoutineExCheck</strong>](wdm-iosetcompletionroutineexcheck.md) rule specifies that the [<strong>IoSetCompletionRoutineEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549686) routine returns an NTSTATUS value. The driver must check this value to determine if the [<em>IoCompletion</em>](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine was successfully registered before calling [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336) or [<strong>PoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559654).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IoSetCompletionRoutineExCheckDeviceObject</strong>](wdm-iosetcompletionroutineexcheckdeviceobject.md)</p></td>
<td align="left"><p>The [<strong>IoSetCompletionRoutineExCheckDeviceObject</strong>](wdm-iosetcompletionroutineexcheckdeviceobject.md) rule specifies that if the current device object is not passed to [<strong>IoSetCompletionRoutineEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549686) and the lower device object is, this can lead to a race condition where the current device object could be unloaded even though the completion routine has not run.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IoSetCompletionRoutineNonPnpDriver</strong>](wdm-iosetcompletionroutinenonpnpdriver.md)</p></td>
<td align="left"><p>The [<strong>IoSetCompletionRoutineNonPnpDriver</strong>](wdm-iosetcompletionroutinenonpnpdriver.md) rule specifies that drivers that are not PnP drivers should use [<strong>IoSetCompletionRoutineEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549686) not [<strong>IoSetCompletionRoutine</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549679).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IrpCancelField</strong>](wdm-irpcancelfield.md)</p></td>
<td align="left"><p>The [<strong>IrpCancelField</strong>](wdm-irpcancelfield.md) rule specifies that the driver check the value of the <strong>Irp-&gt;Cancel</strong> member when setting a cancel routine on an IRP that it has pended.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IrpProcessingComplete</strong>](wdm-irpprocessingcomplete.md)</p></td>
<td align="left"><p>The [<strong>IrpProcessingComplete</strong>](wdm-irpprocessingcomplete.md) rule specifies that if a dispatch routine returns STATUS_SUCCESS, the IRP must have been completed by either the driver itself or by a lower-level driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>LowerDriverReturn</strong>](wdm-lowerdriverreturn.md)</p></td>
<td align="left"><p>The [<strong>LowerDriverReturn</strong>](wdm-lowerdriverreturn.md) rule specifies that after using [<strong>PoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559654) or [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336) to call a lower driver, the driver saves the return status from the call and passes the return status that it received to the dispatch routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SignalEventInCompletion</strong>](wdm-signaleventincompletion.md)</p></td>
<td align="left"><p>The [<strong>SignalEventInCompletion</strong>](wdm-signaleventincompletion.md) rule specifies that when processing an asynchronous IRP, the driver needs to call the [<strong>KeSetEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553253) in the completion routine when the <strong>Irp-&gt;PendingReturned</strong> flag is set.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SignalEventInCompletion2</strong>](wdm-signaleventincompletion2.md)</p></td>
<td align="left"><p>The [<strong>SignalEventInCompletion2</strong>](wdm-signaleventincompletion2.md) rule specifies that when processing an asynchronous IRP, the driver needs to call the [<strong>KeSetEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553253) in the completion routine when the <strong>Irp-&gt;PendingReturned</strong> flag is set.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SignalEventInCompletion3</strong>](wdm-signaleventincompletion3.md)</p></td>
<td align="left"><p>The [<strong>SignalEventInCompletion3</strong>](wdm-signaleventincompletion3.md) rule specifies that when processing a asynchronous IRP, the driver needs to call the [<strong>KeSetEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553253) in the completion routine when the <strong>Irp-&gt;PendingReturned</strong> flag is set.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>StartIoCancel</strong>](wdm-startiocancel.md)</p></td>
<td align="left"><p>The [<strong>StartIoCancel</strong>](wdm-startiocancel.md) rule specifies that the driver must not call [<strong>IoSetStartIoAttributes</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550330) with the <em>NonCancelable</em> parameter set to <strong>FALSE</strong> before calling [<strong>IoSetCancelRoutine</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549674) with a non-<strong>NULL</strong>[<strong>Cancel</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>StartIoRecursion</strong>](wdm-startiorecursion.md)</p></td>
<td align="left"><p>The [<strong>StartIoRecursion</strong>](wdm-startiorecursion.md) rule specifies that if a driver's [<strong>StartIo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine includes a call to [<strong>IoStartNextPacket</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550358), the driver must first call [<strong>IoSetStartIoAttributes</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550330) with the <em>DeferredStartIo</em> attribute set to <strong>TRUE</strong>. Otherwise, infinite recursion can result.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PnpRemove</strong>](wdm-pnpremove.md)</p></td>
<td align="left"><p>The [<strong>PnpRemove</strong>](wdm-pnpremove.md) rule specifies that the driver cannot complete IRP_MN_SURPRISE_REMOVAL, IRP_MN_CANCEL_REMOVE_DEVICE, IRP_MN_CANCEL_STOP_DEVICE, or IRP_MN_REMOVE_DEVICE requests with a failure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PnpSurpriseRemove</strong>](wdm-pnpsurpriseremove.md)</p></td>
<td align="left"><p>The [<strong>PnpSurpriseRemove</strong>](wdm-pnpsurpriseremove.md) rule specifies that the driver does not call IoDeleteDevice or IoDetachDevice while processing an [<strong>IRP_MN_SURPRISE_REMOVAL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551760) request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PowerDownAllocate</strong>](wdm-powerdownallocate.md)</p></td>
<td align="left"><p>The [<strong>PowerDownAllocate</strong>](wdm-powerdownallocate.md) rule specifies that an FDO and FIDO driver should not allocate memory when processing an IRP_MN_SET_POWER request for a <strong>SystemPowerState</strong> transition that goes from s0 to [S1...S5].</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PowerDownFail</strong>](wdm-powerdownfail.md)</p></td>
<td align="left"><p>The [<strong>PowerDownFail</strong>](wdm-powerdownfail.md) rule specifies that a FDO or FIDO driver should not fail an IRP_MN_SET_POWER request when the device is powering down. This rule only applies to FDO and FIDO drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PowerIrpDDIs</strong>](wdm-powerirpddis.md)</p></td>
<td align="left"><p>The [<strong>PowerIrpDDIs</strong>](wdm-powerirpddis.md) rule specifies that when a driver is processing a system or a device IRP_MJ_POWER with IRP_MN_SET_POWER, it should not call DDIs that can only be call at PASSIVE_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PowerUpFail</strong>](wdm-powerupfail.md)</p></td>
<td align="left"><p>The PowerUpFail rule specifies a FDO or FIDO driver should not fail a IRP_MN_SET_POWER request when the device is powering up.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PnpIrpCompletion</strong>](wdm-pnpirpcompletion.md)</p></td>
<td align="left"><p>The [<strong>PnpIrpCompletion</strong>](wdm-pnpirpcompletion.md) rule verifies that an FDO driver passes PnP IRPs to the lower driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WmiComplete</strong>](wdm-wmicomplete.md)</p></td>
<td align="left"><p>The [<strong>WmiComplete</strong>](wdm-wmicomplete.md) rule specifies that when processing a [<strong>WMI minor IRP</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566361), the driver calls [<strong>IoCompleteRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548343) before returning from the [<strong>DispatchSystemControl</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543412) routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WmiForward</strong>](wdm-wmiforward.md)</p></td>
<td align="left"><p>The [<strong>WmiForward</strong>](wdm-wmiforward.md) rule specifies that the driver must forward [<strong>WMI minor IRPs</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566361) when forwarding is required.</p></td>
</tr>
</tbody>
</table>

 

**To select the IrpProcessing rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **IrpProcessing**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **IrpProcessing.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:IrpProcessing.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20IrpProcessing%20rule%20set%20%28WDM%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




