---
title: Locking rule set (Storport)
description: Use these rules to verify that your driver correctly manages shared resources.
ms.assetid: FBB75F07-E689-4B7C-B053-E0B6A3772764
ms.date: 05/21/2018
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
<td align="left"><p><a href="storport-cancelspinlock.md" data-raw-source="[&lt;strong&gt;CancelSpinLock&lt;/strong&gt;](storport-cancelspinlock.md)"><strong>CancelSpinLock</strong></a></p></td>
<td align="left"><p>The <a href="storport-cancelspinlock.md" data-raw-source="[&lt;strong&gt;CancelSpinLock Rule (Storport)&lt;/strong&gt;](storport-cancelspinlock.md)"><strong>CancelSpinLock Rule (Storport)</strong></a> rule verifies that each call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548196" data-raw-source="[&lt;strong&gt;IoAcquireCancelSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548196)"><strong>IoAcquireCancelSpinLock</strong></a> is promptly followed by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff549550" data-raw-source="[&lt;strong&gt;IoReleaseCancelSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549550)"><strong>IoReleaseCancelSpinLock</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storport-queuedspinlock.md" data-raw-source="[&lt;strong&gt;QueuedSpinLock&lt;/strong&gt;](storport-queuedspinlock.md)"><strong>QueuedSpinLock</strong></a></p></td>
<td align="left"><p>The <a href="storport-queuedspinlock.md" data-raw-source="[&lt;strong&gt;QueuedSpinLock&lt;/strong&gt;](storport-queuedspinlock.md)"><strong>QueuedSpinLock</strong></a> rule verifies that in-stack queued spin locks that are acquired using <a href="https://msdn.microsoft.com/library/windows/hardware/ff551899" data-raw-source="[&lt;strong&gt;KeAcquireInStackQueuedSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551899)"><strong>KeAcquireInStackQueuedSpinLock</strong></a> are promptly released using <a href="https://msdn.microsoft.com/library/windows/hardware/ff553130" data-raw-source="[&lt;strong&gt;KeReleaseInStackQueuedSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553130)"><strong>KeReleaseInStackQueuedSpinLock</strong></a>. In addition, at the end of a dispatch or cancel routine, the driver should not hold any locks.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="storport-queuedspinlockrelease.md" data-raw-source="[&lt;strong&gt;QueuedSpinLockRelease&lt;/strong&gt;](storport-queuedspinlockrelease.md)"><strong>QueuedSpinLockRelease</strong></a></p></td>
<td align="left"><p>This rule verifies that the driver does not call <strong>KeReleaseInStackQueuedSpinLock</strong> without first acquiring the lock via <strong>KeAcquireInStackQueuedSpinLock</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storport-spinlock.md" data-raw-source="[&lt;strong&gt;SpinLock&lt;/strong&gt;](storport-spinlock.md)"><strong>SpinLock</strong></a></p></td>
<td align="left"><p>This rule verifies that a call to <strong>KeAcquireSpinLock</strong> is promptly followed by a call to <strong>KeReleaseSpinlock</strong>. If a driver calls <strong>KeAcquireSpinLockRaiseToDpc</strong> or <strong>KeAcquireSpinLock</strong> again prior to releasing the lock, it fails the rule. In addition, before exiting the dispatch or cancel routine, the driver must release the spin lock.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="storport-spinlockdpc.md" data-raw-source="[&lt;strong&gt;SpinLockDpc&lt;/strong&gt;](storport-spinlockdpc.md)"><strong>SpinLockDpc</strong></a></p></td>
<td align="left"><p>This rule verifies that a call to <strong>KeAcquireSpinLockRaiseToDpc</strong> is promptly followed by a call to <strong>KeReleaseSpinlock</strong>. If a driver calls <strong>KeAcquireSpinLock</strong> or <strong>KeAcquireSpinLockRaiseToDpc</strong> again prior to releasing the lock, it fails the rule. In addition, before exiting the dispatch or cancel routine, the driver must release the spin lock.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storport-spinlockrelease.md" data-raw-source="[&lt;strong&gt;SpinLockRelease&lt;/strong&gt;](storport-spinlockrelease.md)"><strong>SpinLockRelease</strong></a></p></td>
<td align="left"><p>This rule verifies that the driver does not attempt to release a lock via <strong>KeReleaseSpinLock</strong> without first acquiring it via <strong>KeAquireSpinlock</strong> or <strong>KeAcquireSpinLockRaiseToDpc</strong>. The rule passes when the acquired spin lock is released.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="storport-spinlocksafe.md" data-raw-source="[&lt;strong&gt;SpinLockSafe&lt;/strong&gt;](storport-spinlocksafe.md)"><strong>SpinLockSafe</strong></a></p></td>
<td align="left"><p>This rule verifies that the <strong>IoStartNextPacket</strong> and <strong>IoCompleteRequest</strong> routines are not called while holding a spin lock. The rule keeps track of the number of spin locks held at any time, and if that number is not 0 when either routine is called, the driver fails the rule.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storport-storportmsilock.md" data-raw-source="[&lt;strong&gt;StorPortMSILock&lt;/strong&gt;](storport-storportmsilock.md)"><strong>StorPortMSILock</strong></a></p></td>
<td align="left"><p>Miniport drivers are required to acquire the MSI spin lock for a message if, and only if, the <strong>InterruptSynchronizationMode</strong> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563901" data-raw-source="[&lt;strong&gt;PORT_CONFIGURATION_INFORMATION (Storport)&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563901)"><strong>PORT_CONFIGURATION_INFORMATION (Storport)</strong></a> structure is set to <strong>InterruptSynchronizePerMessage</strong>. This rule verifies that calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff567023" data-raw-source="[&lt;strong&gt;StorPortAcquireMSISpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567023)"><strong>StorPortAcquireMSISpinLock</strong></a> are only made if the synchronization mode is <strong>InterruptSynchronizePerMessage</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="storport-storportspinlock.md" data-raw-source="[&lt;strong&gt;StorPortSpinLock&lt;/strong&gt;](storport-storportspinlock.md)"><strong>StorPortSpinLock</strong></a></p></td>
<td align="left"><p>This rule verifies that locks that are acquired via <strong>StorPortAcquireSpinLock</strong> are promptly released via <strong>StorPortReleaseSpinLock</strong>. The miniport driver fails the rule if it attempts to acquire a lock that it had already acquired, or if it attempts to release a lock that it had not acquired. In addition, at the end of the dispatch or cancel routine, the driver should not hold any spin locks.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storport-storportspinlock3.md" data-raw-source="[&lt;strong&gt;StorPortSpinLock3&lt;/strong&gt;](storport-storportspinlock3.md)"><strong>StorPortSpinLock3</strong></a></p></td>
<td align="left"><p>The <a href="storport-storportspinlock3.md" data-raw-source="[&lt;strong&gt;StorPortSpinLock3&lt;/strong&gt;](storport-storportspinlock3.md)"><strong>StorPortSpinLock3</strong></a> rule verifies the lock acquisition hierarchy that is described in the documentation for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567025" data-raw-source="[&lt;strong&gt;StorPortAcquireSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567025)"><strong>StorPortAcquireSpinLock</strong></a> routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="storport-storportspinlock4.md" data-raw-source="[&lt;strong&gt;StorPortSpinLock4&lt;/strong&gt;](storport-storportspinlock4.md)"><strong>StorPortSpinLock4</strong></a></p></td>
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

 

 





