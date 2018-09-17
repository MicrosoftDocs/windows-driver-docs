---
title: Locking rule set (Storport)
description: Use these rules to verify that your driver correctly manages shared resources.
ms.assetid: FBB75F07-E689-4B7C-B053-E0B6A3772764
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
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

 

 





