---
title: IrpTracking rule set (WDM)
description: Use these rules to verify that your driver correctly tracks I/O request packets (IRP) so that the device is not removed while IRPs are outstanding.
ms.assetid: 9AD62397-6840-42FF-ADEC-6836EDD16647
---

# IrpTracking rule set (WDM)


Use these rules to verify that your driver correctly tracks I/O request packets (IRP) so that the device is not removed while IRPs are outstanding.

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
<td align="left"><p>[<strong>IoReleaseRemoveLockAndWaitOutsideRemoveDevice</strong>](wdm-ioreleaseremovelockandwaitoutsideremovedevice.md)</p></td>
<td align="left"><p>The [<strong>IoReleaseRemoveLockAndWaitOutsideRemoveDevice</strong>](wdm-ioreleaseremovelockandwaitoutsideremovedevice.md) rule specifies that [<strong>IoReleaseRemoveLockAndWait</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549567) should not be called outside IRP_MJ_PNP with IRP_MN_REMOVE_DEVICE for a PnP driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NsRemoveLockMnRemove</strong>](wdm-nsremovelockmnremove.md)</p></td>
<td align="left"><p>The [<strong>NsRemoveLockMnRemove</strong>](wdm-nsremovelockmnremove.md) rule verifies a driver does not return STATUS_NOT_SUPPORTED when processing IRP_MJ_PNP with MinorFunction IRP_MN_REMOVE_DEVICE. This rule only applies to FDO and FIDO drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NsRemoveLockMnSurpriseRemove</strong>](wdm-nsremovelockmnsurpriseremove.md)</p></td>
<td align="left"><p>The [<strong>NsRemoveLockMnSurpriseRemove</strong>](wdm-nsremovelockmnsurpriseremove.md) rule verifies that a driver does not return STATUS_NOT_SUPPORTED when processing an IRP_MJ_PNP request with minorFunction IRP_MN_SUPRISE_REMOVAL. This rule only applies to FDO and FIDO drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NsRemoveLockQueryMnRemove</strong>](wdm-nsremovelockquerymnremove.md)</p></td>
<td align="left"><p>The [<strong>NsRemoveLockQueryMnRemove</strong>](wdm-nsremovelockquerymnremove.md) rule verifies a driver does not return STATUS_NOT_SUPPORTED when processing IRP_MJ_PNP with MinorFunction IRP_MN_QUERY_REMOVE. This rule only applies to FDO and FIDO drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RemoveLock</strong>](wdm-removelock.md)</p></td>
<td align="left"><p>The [<strong>RemoveLock</strong>](wdm-removelock.md) rule specifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used correctly. Moreover, at the end of the IRP_MJ_PNP or IRP_MJ_POWER routine, the driver should not hold the <strong>RemoveLock</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RemoveLockCheck</strong>](wdm-removelockcheck.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockCheck</strong>](wdm-removelockcheck.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLockAndWait</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549567) are used correctly when processing IRP_MJ_PNP with MinorFunction IRP_MN_REMOVE_DEVICE.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RemoveLockForward</strong>](wdm-removelockforward.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockForward</strong>](wdm-removelockforward.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used correctly when forwarding a IRP to another device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RemoveLockForward2</strong>](wdm-removelockforward2.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockForward2</strong>](wdm-removelockforward2.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used correctly when forwarding the IRP to another device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RemoveLockForwardDeviceControl</strong>](wdm-removelockforwarddevicecontrol.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockForwardDeviceControl</strong>](wdm-removelockforwarddevicecontrol.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used correctly when the driver uses [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336) to forward an IRP to a another device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RemoveLockForwardDeviceControl2</strong>](wdm-removelockforwarddevicecontrol2.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockForwardDeviceControl2</strong>](wdm-removelockforwarddevicecontrol2.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used correctly when the driver uses [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336) to forward an IRP to a another device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RemoveLockForwardDeviceControlInternal</strong>](wdm-removelockforwarddevicecontrolinternal.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockForwardDeviceControlInternal</strong>](wdm-removelockforwarddevicecontrolinternal.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used in correctly when forwarding a IRP using [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336) to a another device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RemoveLockForwardDeviceControlInternal2</strong>](wdm-removelockforwarddevicecontrolinternal2.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockForwardDeviceControlInternal2</strong>](wdm-removelockforwarddevicecontrolinternal2.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used in correctly when forwarding a IRP using [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336) to a another device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RemoveLockForwardRead</strong>](wdm-removelockforwardread.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockForwardRead</strong>](wdm-removelockforwardread.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used in correctly.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RemoveLockForwardRead2</strong>](wdm-removelockforwardread2.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockForwardRead2</strong>](wdm-removelockforwardread2.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used correctly when forwarding a IRP using [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336) to a another device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RemoveLockForwardWrite</strong>](wdm-removelockforwardwrite.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockForwardWrite</strong>](wdm-removelockforwardwrite.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used correctly when forwarding a IRP using [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336) to a another device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RemoveLockForwardWrite2</strong>](wdm-removelockforwardwrite2.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockForwardWrite2</strong>](wdm-removelockforwardwrite2.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used correctly when forwarding a IRP using [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336) to a another device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RemoveLockMnRemove</strong>](wdm-removelockmnremove.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockMnRemove</strong>](wdm-removelockmnremove.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLockAndWait</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549567) are used correctly when processing IRP_MJ_PNP with MinorFunction IRP_MN_REMOVE_DEVICE.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RemoveLockMnRemove2</strong>](wdm-removelockmnremove2.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockMnRemove2</strong>](wdm-removelockmnremove2.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLockAndWait</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549567) are used correctly when processing IRP_MN_REMOVE_DEVICE request before the IRP is forwarded to lower drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RemoveLockMnSurpriseRemove</strong>](wdm-removelockmnsurpriseremove.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockMnSurpriseRemove</strong>](wdm-removelockmnsurpriseremove.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLockAndWait</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549567) are used correctly when processing IRP_MJ_PNP with MinorFunction IRP_MN_SUPRISE_REMOVAL. The driver should acquire the remove lock before forwarding the IRP down the stack.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RemoveLockQueryMnRemove</strong>](wdm-removelockquerymnremove.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockQueryMnRemove</strong>](wdm-removelockquerymnremove.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used correctly when processing IRP_MJ_PNP with MinorFunction IRP_MN_QUERY_REMOVE_DEVICE. The driver should acquire the remove lock before forwarding the IRP down the stack.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RemoveLockRelease2</strong>](wdm-removelockrelease2.md)</p></td>
<td align="left"><p>The rule [<strong>RemoveLockRelease2</strong>](wdm-removelockrelease2.md) verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used in strict alternation. Moreover, at the end of the dispatch routine the driver should not hold the remove lock.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RemoveLockReleaseCleanup</strong>](wdm-removelockreleasecleanup.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockReleaseCleanup</strong>](wdm-removelockreleasecleanup.md) rule specifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used in strict alternation. Each call to <strong>IoAcquireRemoveLock</strong> must have a matching call to <strong>IoReleaseRemoveLock</strong>. Moreover, at the end of the dispatch routine the driver should not hold the remove lock.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RemoveLockReleaseClose</strong>](wdm-removelockreleaseclose.md)</p></td>
<td align="left"><p>The rule [<strong>RemoveLockReleaseClose</strong>](wdm-removelockreleaseclose.md) verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used in strict alternation. Moreover, at the end of the dispatch routine the driver should not hold the remove lock.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RemoveLockReleaseCreate</strong>](wdm-removelockreleasecreate.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockReleaseCreate</strong>](wdm-removelockreleasecreate.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used in strict alternation. Moreover, at the end of the dispatch routine the driver should not hold the remove lock.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RemoveLockReleaseDeviceControl</strong>](wdm-removelockreleasedevicecontrol.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockReleaseDeviceControl</strong>](wdm-removelockreleasedevicecontrol.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used in strict alternation. Moreover, at the end of the dispatch routine the driver should not hold the remove lock.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RemoveLockReleaseInternalDeviceControl</strong>](wdm-removelockreleaseinternaldevicecontrol.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockReleaseInternalDeviceControl</strong>](wdm-removelockreleaseinternaldevicecontrol.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used in strict alternation. Moreover, at the end of the dispatch routine the driver should not hold the remove lock.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RemoveLockReleasePnp</strong>](wdm-removelockreleasepnp.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockReleasePnp</strong>](wdm-removelockreleasepnp.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used in strict alternation. Moreover, at the end of the dispatch routine the driver should not hold the remove lock.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RemoveLockReleasePower</strong>](wdm-removelockreleasepower.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockReleasePower</strong>](wdm-removelockreleasepower.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used in strict alternation. Moreover, at the end of the dispatch routine the driver should not hold the remove lock.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RemoveLockReleaseRead</strong>](wdm-removelockreleaseread.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockReleaseRead</strong>](wdm-removelockreleaseread.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used in strict alternation. Moreover, at the end of the dispatch routine the driver should not hold the remove lock.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RemoveLockReleaseShutdown</strong>](wdm-removelockreleaseshutdown.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockReleaseShutdown</strong>](wdm-removelockreleaseshutdown.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used in strict alternation. Moreover, at the end of the dispatch routine the driver should not hold the remove lock.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RemoveLockReleaseSystemControl</strong>](wdm-removelockreleasesystemcontrol.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockReleaseSystemControl</strong>](wdm-removelockreleasesystemcontrol.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used in strict alternation. Moreover, at the end of the dispatch routine the driver should not hold the remove lock.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RemoveLockReleaseWrite</strong>](wdm-removelockreleasewrite.md)</p></td>
<td align="left"><p>The [<strong>RemoveLockReleaseWrite</strong>](wdm-removelockreleasewrite.md) rule verifies that calls to [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used in strict alternation. Moreover, at the end of the dispatch routine the driver should not hold the remove lock.</p></td>
</tr>
</tbody>
</table>

 

**To select the IrpTracking rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **IrpTracking**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **IrpTracking.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:IrpTracking.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20IrpTracking%20rule%20set%20%28WDM%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




