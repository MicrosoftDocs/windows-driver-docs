---
title: Locking rule set (WDM)
description: Use these rules to verify that your driver correctly manages shared resources.
ms.assetid: B23863BD-66F0-4E6F-B150-97FD2066F69C
ms.date: 05/21/2018
ms.localizationpriority: medium
---

# Locking rule set (WDM)


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
<td align="left"><p><a href="wdm-cancelspinlock.md" data-raw-source="[&lt;strong&gt;CancelSpinLock&lt;/strong&gt;](wdm-cancelspinlock.md)"><strong>CancelSpinLock</strong></a></p></td>
<td align="left"><p>The CancelSpinLock rule specifies that the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548196" data-raw-source="[&lt;strong&gt;IoAcquireCancelSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548196)"><strong>IoAcquireCancelSpinLock</strong></a> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549550" data-raw-source="[&lt;strong&gt;IoReleaseCancelSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549550)"><strong>IoReleaseCancelSpinLock</strong></a> and that the driver calls <strong>IoReleaseCancelSpinLock</strong> before any subsequent calls to <strong>IoAcquireCancelSpinLock</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-cancelspinlockrelease.md" data-raw-source="[&lt;strong&gt;CancelSpinlockRelease&lt;/strong&gt;](wdm-cancelspinlockrelease.md)"><strong>CancelSpinlockRelease</strong></a></p></td>
<td align="left"><p>The <a href="wdm-cancelspinlockrelease.md" data-raw-source="[&lt;strong&gt;CancelSpinlockRelease&lt;/strong&gt;](wdm-cancelspinlockrelease.md)"><strong>CancelSpinlockRelease</strong></a> rule specifies that calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff548196" data-raw-source="[&lt;strong&gt;IoAcquireCancelSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548196)"><strong>IoAcquireCancelSpinLock</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff549550" data-raw-source="[&lt;strong&gt;IoReleaseCancelSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549550)"><strong>IoReleaseCancelSpinLock</strong></a> are used in strict alternation. That is, every call to <strong>IoAcquireCancelSpinLock</strong> must have a corresponding call to <strong>IoReleaseCancelSpinLock</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-criticalregions.md" data-raw-source="[&lt;strong&gt;CriticalRegions&lt;/strong&gt;](wdm-criticalregions.md)"><strong>CriticalRegions</strong></a></p></td>
<td align="left"><p>The <a href="wdm-criticalregions.md" data-raw-source="[&lt;strong&gt;CriticalRegions&lt;/strong&gt;](wdm-criticalregions.md)"><strong>CriticalRegions</strong></a> rule specifies that the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff552021" data-raw-source="[&lt;strong&gt;KeEnterCriticalRegion&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552021)"><strong>KeEnterCriticalRegion</strong></a> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff552964" data-raw-source="[&lt;strong&gt;KeLeaveCriticalRegion&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552964)"><strong>KeLeaveCriticalRegion</strong></a> and that the driver calls <strong>KeLeaveCriticalRegion</strong> before any subsequent calls to <strong>KeEnterCriticalRegion</strong>. (Nested calls are permitted.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-exclusiveresourceaccess.md" data-raw-source="[&lt;strong&gt;ExclusiveResourceAccess&lt;/strong&gt;](wdm-exclusiveresourceaccess.md)"><strong>ExclusiveResourceAccess</strong></a></p></td>
<td align="left"><p>The <a href="wdm-exclusiveresourceaccess.md" data-raw-source="[&lt;strong&gt;ExclusiveResourceAccess&lt;/strong&gt;](wdm-exclusiveresourceaccess.md)"><strong>ExclusiveResourceAccess</strong></a> rule specifies that the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff544351" data-raw-source="[&lt;strong&gt;ExAcquireResourceExclusiveLite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544351)"><strong>ExAcquireResourceExclusiveLite</strong></a> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545597" data-raw-source="[&lt;strong&gt;ExReleaseResourceLite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545597)"><strong>ExReleaseResourceLite</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff545585" data-raw-source="[&lt;strong&gt;ExReleaseResourceForThreadLite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545585)"><strong>ExReleaseResourceForThreadLite</strong></a> and specifies that the driver calls <strong>ExReleaseResourceLite</strong> or <strong>ExReleaseResourceForThreadLite</strong> before any subsequent calls to <strong>ExAcquireResourceExclusiveLite</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-guardedregions.md" data-raw-source="[&lt;strong&gt;GuardedRegions&lt;/strong&gt;](wdm-guardedregions.md)"><strong>GuardedRegions</strong></a></p></td>
<td align="left"><p>The <a href="wdm-guardedregions.md" data-raw-source="[&lt;strong&gt;GuardedRegions&lt;/strong&gt;](wdm-guardedregions.md)"><strong>GuardedRegions</strong></a> rule verifies that calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff552028" data-raw-source="[&lt;strong&gt;KeEnterGuardedRegion&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552028)"><strong>KeEnterGuardedRegion</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff552967" data-raw-source="[&lt;strong&gt;KeLeaveGuardedRegion&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552967)"><strong>KeLeaveGuardedRegion</strong></a> are used in strict alternation.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-queuedspinlock.md" data-raw-source="[&lt;strong&gt;QueuedSpinLock&lt;/strong&gt;](wdm-queuedspinlock.md)"><strong>QueuedSpinLock</strong></a></p></td>
<td align="left"><p>The <a href="wdm-queuedspinlock.md" data-raw-source="[&lt;strong&gt;QueuedSpinLock&lt;/strong&gt;](wdm-queuedspinlock.md)"><strong>QueuedSpinLock</strong></a> rule specifies that the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff551899" data-raw-source="[&lt;strong&gt;KeAcquireInStackQueuedSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551899)"><strong>KeAcquireInStackQueuedSpinLock</strong></a> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff553130" data-raw-source="[&lt;strong&gt;KeReleaseInStackQueuedSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553130)"><strong>KeReleaseInStackQueuedSpinLock</strong></a> and that the driver calls <strong>KeReleaseInStackQueuedSpinLock</strong> before any subsequent calls to <strong>KeAcquireInStackQueuedSpinLock</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-queuedspinlockrelease.md" data-raw-source="[&lt;strong&gt;QueuedSpinLockRelease&lt;/strong&gt;](wdm-queuedspinlockrelease.md)"><strong>QueuedSpinLockRelease</strong></a></p></td>
<td align="left"><p>The <a href="wdm-queuedspinlockrelease.md" data-raw-source="[&lt;strong&gt;QueuedSpinLockRelease&lt;/strong&gt;](wdm-queuedspinlockrelease.md)"><strong>QueuedSpinLockRelease</strong></a> rule specifies that calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551899" data-raw-source="[&lt;strong&gt;KeAcquireInStackQueuedSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551899)"><strong>KeAcquireInStackQueuedSpinLock</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553130" data-raw-source="[&lt;strong&gt;KeReleaseInStackQueuedSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553130)"><strong>KeReleaseInStackQueuedSpinLock</strong></a> are used in strict alternation.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-spinlock.md" data-raw-source="[&lt;strong&gt;SpinLock&lt;/strong&gt;](wdm-spinlock.md)"><strong>SpinLock</strong></a></p></td>
<td align="left"><p>The <a href="wdm-spinlock.md" data-raw-source="[&lt;strong&gt;SpinLock&lt;/strong&gt;](wdm-spinlock.md)"><strong>SpinLock</strong></a> rule specifies that, after calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff551917" data-raw-source="[&lt;strong&gt;KeAcquireSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551917)"><strong>KeAcquireSpinLock</strong></a>, the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff553145" data-raw-source="[&lt;strong&gt;KeReleaseSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553145)"><strong>KeReleaseSpinLock</strong></a> before subsequent calls to <strong>KeAcquireSpinLock</strong> or to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551928" data-raw-source="[&lt;strong&gt;KeAcquireSpinLockRaiseToDpc&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551928)"><strong>KeAcquireSpinLockRaiseToDpc</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-spinlockdpc.md" data-raw-source="[&lt;strong&gt;SpinLockDpc&lt;/strong&gt;](wdm-spinlockdpc.md)"><strong>SpinLockDpc</strong></a></p></td>
<td align="left"><p>The <a href="wdm-spinlockdpc.md" data-raw-source="[&lt;strong&gt;SpinLockDpc&lt;/strong&gt;](wdm-spinlockdpc.md)"><strong>SpinLockDpc</strong></a> rule specifies that calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551917" data-raw-source="[&lt;strong&gt;KeAcquireSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551917)"><strong>KeAcquireSpinLock</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff551928" data-raw-source="[&lt;strong&gt;KeAcquireSpinLockRaiseToDpc&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551928)"><strong>KeAcquireSpinLockRaiseToDpc</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553145" data-raw-source="[&lt;strong&gt;KeReleaseSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553145)"><strong>KeReleaseSpinLock</strong></a> must be made in strict alternation. That is, after calling <strong>KeAcquireSpinLock</strong> or <strong>KeAcquireSpinLockRaiseToDpc</strong>, the driver must call <strong>KeReleaseSpinLock</strong> before subsequent calls to <strong>KeAcquireSpinLock</strong> or to <strong>KeAcquireSpinLockRaiseToDpc</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-spinlockrelease.md" data-raw-source="[&lt;strong&gt;SpinlockRelease&lt;/strong&gt;](wdm-spinlockrelease.md)"><strong>SpinlockRelease</strong></a></p></td>
<td align="left"><p>The <a href="wdm-spinlockrelease.md" data-raw-source="[&lt;strong&gt;SpinlockRelease&lt;/strong&gt;](wdm-spinlockrelease.md)"><strong>SpinlockRelease</strong></a> rule specifies that calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff553145" data-raw-source="[&lt;strong&gt;KeReleaseSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553145)"><strong>KeReleaseSpinLock</strong></a> are made in strict alternation with <a href="https://msdn.microsoft.com/library/windows/hardware/ff551917" data-raw-source="[&lt;strong&gt;KeAcquireSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551917)"><strong>KeAcquireSpinLock</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff551928" data-raw-source="[&lt;strong&gt;KeAcquireSpinLockRaiseToDpc&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551928)"><strong>KeAcquireSpinLockRaiseToDpc</strong></a>. That is, the driver must call <strong>KeReleaseSpinLock</strong> after calling <strong>KeAcquireSpinLock</strong> or <strong>KeAcquireSpinLockRaiseToDpc</strong> and before subsequent calls to <strong>KeAcquireSpinLock</strong> or to <strong>KeAcquireSpinLockRaiseToDpc</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-spinlocksafe.md" data-raw-source="[&lt;strong&gt;SpinLockSafe&lt;/strong&gt;](wdm-spinlocksafe.md)"><strong>SpinLockSafe</strong></a></p></td>
<td align="left"><p>The <a href="wdm-spinlocksafe.md" data-raw-source="[&lt;strong&gt;SpinLockSafe&lt;/strong&gt;](wdm-spinlocksafe.md)"><strong>SpinLockSafe</strong></a> rule specifies that <a href="https://msdn.microsoft.com/library/windows/hardware/ff550358" data-raw-source="[&lt;strong&gt;IoStartNextPacket&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550358)"><strong>IoStartNextPacket</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff548343" data-raw-source="[&lt;strong&gt;IoCompleteRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548343)"><strong>IoCompleteRequest</strong></a> are not called while holding a spin lock.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-withincriticalregion.md" data-raw-source="[&lt;strong&gt;WithinCriticalRegion&lt;/strong&gt;](wdm-withincriticalregion.md)"><strong>WithinCriticalRegion</strong></a></p></td>
<td align="left"><p>The <a href="wdm-withincriticalregion.md" data-raw-source="[&lt;strong&gt;WithinCriticalRegion&lt;/strong&gt;](wdm-withincriticalregion.md)"><strong>WithinCriticalRegion</strong></a> rule specifies that the driver&#39;s calls to particular synchronization functions appear only after calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff552021" data-raw-source="[&lt;strong&gt;KeEnterCriticalRegion&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552021)"><strong>KeEnterCriticalRegion</strong></a> and before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff552964" data-raw-source="[&lt;strong&gt;KeLeaveCriticalRegion&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552964)"><strong>KeLeaveCriticalRegion</strong></a>.</p>
<p>The affected synchronization functions are the following:</p>
<ul>
<li><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff544363" data-raw-source="[&lt;strong&gt;ExAcquireResourceSharedLite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544363)"><strong>ExAcquireResourceSharedLite</strong></a></p></li>
<li><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff544351" data-raw-source="[&lt;strong&gt;ExAcquireResourceExclusiveLite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544351)"><strong>ExAcquireResourceExclusiveLite</strong></a></p></li>
<li><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff544367" data-raw-source="[&lt;strong&gt;ExAcquireSharedStarveExclusive&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544367)"><strong>ExAcquireSharedStarveExclusive</strong></a></p></li>
<li><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff544370" data-raw-source="[&lt;strong&gt;ExAcquireSharedWaitForExclusive&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544370)"><strong>ExAcquireSharedWaitForExclusive</strong></a></p></li>
<li><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff545597" data-raw-source="[&lt;strong&gt;ExReleaseResourceLite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545597)"><strong>ExReleaseResourceLite</strong></a></p></li>
<li><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff545585" data-raw-source="[&lt;strong&gt;ExReleaseResourceForThreadLite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545585)"><strong>ExReleaseResourceForThreadLite</strong></a></p></li>
</ul></td>
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

 

 





