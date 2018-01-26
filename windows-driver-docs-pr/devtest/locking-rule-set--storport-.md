---
title: Locking rule set (Storport)
description: Use these rules to verify that your driver correctly manages shared resources.
ms.assetid: FBB75F07-E689-4B7C-B053-E0B6A3772764
---

# Locking rule set (Storport)


Use these rules to verify that your driver correctly manages shared resources.

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
<td align="left"><p>[<strong>CancelSpinLock</strong>](storport-cancelspinlock.md)</p></td>
<td align="left"><p>The [<strong>CancelSpinLock Rule (Storport)</strong>](storport-cancelspinlock.md) rule verifies that each call to [<strong>IoAcquireCancelSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548196) is promptly followed by a call to [<strong>IoReleaseCancelSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549550).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>QueuedSpinLock</strong>](storport-queuedspinlock.md)</p></td>
<td align="left"><p>The [<strong>QueuedSpinLock</strong>](storport-queuedspinlock.md) rule verifies that in-stack queued spin locks that are acquired using [<strong>KeAcquireInStackQueuedSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551899) are promptly released using [<strong>KeReleaseInStackQueuedSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553130). In addition, at the end of a dispatch or cancel routine, the driver should not hold any locks.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>QueuedSpinLockRelease</strong>](storport-queuedspinlockrelease.md)</p></td>
<td align="left"><p>This rule verifies that the driver does not call <strong>KeReleaseInStackQueuedSpinLock</strong> without first acquiring the lock via <strong>KeAcquireInStackQueuedSpinLock</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SpinLock</strong>](storport-spinlock.md)</p></td>
<td align="left"><p>This rule verifies that a call to <strong>KeAcquireSpinLock</strong> is promptly followed by a call to <strong>KeReleaseSpinlock</strong>. If a driver calls <strong>KeAcquireSpinLockRaiseToDpc</strong> or <strong>KeAcquireSpinLock</strong> again prior to releasing the lock, it fails the rule. In addition, before exiting the dispatch or cancel routine, the driver must release the spin lock.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SpinLockDpc</strong>](storport-spinlockdpc.md)</p></td>
<td align="left"><p>This rule verifies that a call to <strong>KeAcquireSpinLockRaiseToDpc</strong> is promptly followed by a call to <strong>KeReleaseSpinlock</strong>. If a driver calls <strong>KeAcquireSpinLock</strong> or <strong>KeAcquireSpinLockRaiseToDpc</strong> again prior to releasing the lock, it fails the rule. In addition, before exiting the dispatch or cancel routine, the driver must release the spin lock.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SpinLockRelease</strong>](storport-spinlockrelease.md)</p></td>
<td align="left"><p>This rule verifies that the driver does not attempt to release a lock via <strong>KeReleaseSpinLock</strong> without first acquiring it via <strong>KeAquireSpinlock</strong> or <strong>KeAcquireSpinLockRaiseToDpc</strong>. The rule passes when the acquired spin lock is released.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SpinLockSafe</strong>](storport-spinlocksafe.md)</p></td>
<td align="left"><p>This rule verifies that the <strong>IoStartNextPacket</strong> and <strong>IoCompleteRequest</strong> routines are not called while holding a spin lock. The rule keeps track of the number of spin locks held at any time, and if that number is not 0 when either routine is called, the driver fails the rule.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>StorPortMSILock</strong>](storport-storportmsilock.md)</p></td>
<td align="left"><p>Miniport drivers are required to acquire the MSI spin lock for a message if, and only if, the <strong>InterruptSynchronizationMode</strong> member of the [<strong>PORT_CONFIGURATION_INFORMATION (Storport)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563901) structure is set to <strong>InterruptSynchronizePerMessage</strong>. This rule verifies that calls to [<strong>StorPortAcquireMSISpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567023) are only made if the synchronization mode is <strong>InterruptSynchronizePerMessage</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>StorPortSpinLock</strong>](storport-storportspinlock.md)</p></td>
<td align="left"><p>This rule verifies that locks that are acquired via <strong>StorPortAcquireSpinLock</strong> are promptly released via <strong>StorPortReleaseSpinLock</strong>. The miniport driver fails the rule if it attempts to acquire a lock that it had already acquired, or if it attempts to release a lock that it had not acquired. In addition, at the end of the dispatch or cancel routine, the driver should not hold any spin locks.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>StorPortSpinLock3</strong>](storport-storportspinlock3.md)</p></td>
<td align="left"><p>The [<strong>StorPortSpinLock3</strong>](storport-storportspinlock3.md) rule verifies the lock acquisition hierarchy that is described in the documentation for the [<strong>StorPortAcquireSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567025) routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>StorPortSpinLock4</strong>](storport-storportspinlock4.md)</p></td>
<td align="left"><p>This rule is the <em>release</em> counterpart of <strong>StorPortSpinLock</strong>. It is similar to the <strong>SpinLockRelease</strong> rule.</p></td>
</tr>
</tbody>
</table>

 

**To select the Locking rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **Locking**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **Locking.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:Locking.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Locking%20rule%20set%20%28Storport%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




