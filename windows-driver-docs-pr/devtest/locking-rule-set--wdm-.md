---
title: Locking rule set (WDM)
description: Use these rules to verify that your driver correctly manages shared resources.
ms.assetid: B23863BD-66F0-4E6F-B150-97FD2066F69C
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
<td align="left"><p>[<strong>CancelSpinLock</strong>](wdm-cancelspinlock.md)</p></td>
<td align="left"><p>The CancelSpinLock rule specifies that the driver calls [<strong>IoAcquireCancelSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548196) before calling [<strong>IoReleaseCancelSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549550) and that the driver calls <strong>IoReleaseCancelSpinLock</strong> before any subsequent calls to <strong>IoAcquireCancelSpinLock</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>CancelSpinlockRelease</strong>](wdm-cancelspinlockrelease.md)</p></td>
<td align="left"><p>The [<strong>CancelSpinlockRelease</strong>](wdm-cancelspinlockrelease.md) rule specifies that calls to [<strong>IoAcquireCancelSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548196) and [<strong>IoReleaseCancelSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549550) are used in strict alternation. That is, every call to <strong>IoAcquireCancelSpinLock</strong> must have a corresponding call to <strong>IoReleaseCancelSpinLock</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>CriticalRegions</strong>](wdm-criticalregions.md)</p></td>
<td align="left"><p>The [<strong>CriticalRegions</strong>](wdm-criticalregions.md) rule specifies that the driver must call [<strong>KeEnterCriticalRegion</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552021) before calling [<strong>KeLeaveCriticalRegion</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552964) and that the driver calls <strong>KeLeaveCriticalRegion</strong> before any subsequent calls to <strong>KeEnterCriticalRegion</strong>. (Nested calls are permitted.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ExclusiveResourceAccess</strong>](wdm-exclusiveresourceaccess.md)</p></td>
<td align="left"><p>The [<strong>ExclusiveResourceAccess</strong>](wdm-exclusiveresourceaccess.md) rule specifies that the driver calls [<strong>ExAcquireResourceExclusiveLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544351) before calling [<strong>ExReleaseResourceLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545597) or [<strong>ExReleaseResourceForThreadLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545585) and specifies that the driver calls <strong>ExReleaseResourceLite</strong> or <strong>ExReleaseResourceForThreadLite</strong> before any subsequent calls to <strong>ExAcquireResourceExclusiveLite</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>GuardedRegions</strong>](wdm-guardedregions.md)</p></td>
<td align="left"><p>The [<strong>GuardedRegions</strong>](wdm-guardedregions.md) rule verifies that calls to [<strong>KeEnterGuardedRegion</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552028) and [<strong>KeLeaveGuardedRegion</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552967) are used in strict alternation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>QueuedSpinLock</strong>](wdm-queuedspinlock.md)</p></td>
<td align="left"><p>The [<strong>QueuedSpinLock</strong>](wdm-queuedspinlock.md) rule specifies that the driver calls [<strong>KeAcquireInStackQueuedSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551899) before calling [<strong>KeReleaseInStackQueuedSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553130) and that the driver calls <strong>KeReleaseInStackQueuedSpinLock</strong> before any subsequent calls to <strong>KeAcquireInStackQueuedSpinLock</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>QueuedSpinLockRelease</strong>](wdm-queuedspinlockrelease.md)</p></td>
<td align="left"><p>The [<strong>QueuedSpinLockRelease</strong>](wdm-queuedspinlockrelease.md) rule specifies that calls to [<strong>KeAcquireInStackQueuedSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551899) and [<strong>KeReleaseInStackQueuedSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553130) are used in strict alternation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SpinLock</strong>](wdm-spinlock.md)</p></td>
<td align="left"><p>The [<strong>SpinLock</strong>](wdm-spinlock.md) rule specifies that, after calling [<strong>KeAcquireSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551917), the driver calls [<strong>KeReleaseSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553145) before subsequent calls to <strong>KeAcquireSpinLock</strong> or to [<strong>KeAcquireSpinLockRaiseToDpc</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551928).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SpinLockDpc</strong>](wdm-spinlockdpc.md)</p></td>
<td align="left"><p>The [<strong>SpinLockDpc</strong>](wdm-spinlockdpc.md) rule specifies that calls to [<strong>KeAcquireSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551917) or [<strong>KeAcquireSpinLockRaiseToDpc</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551928) and [<strong>KeReleaseSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553145) must be made in strict alternation. That is, after calling <strong>KeAcquireSpinLock</strong> or <strong>KeAcquireSpinLockRaiseToDpc</strong>, the driver must call <strong>KeReleaseSpinLock</strong> before subsequent calls to <strong>KeAcquireSpinLock</strong> or to <strong>KeAcquireSpinLockRaiseToDpc</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SpinlockRelease</strong>](wdm-spinlockrelease.md)</p></td>
<td align="left"><p>The [<strong>SpinlockRelease</strong>](wdm-spinlockrelease.md) rule specifies that calls to [<strong>KeReleaseSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553145) are made in strict alternation with [<strong>KeAcquireSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551917) and [<strong>KeAcquireSpinLockRaiseToDpc</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551928). That is, the driver must call <strong>KeReleaseSpinLock</strong> after calling <strong>KeAcquireSpinLock</strong> or <strong>KeAcquireSpinLockRaiseToDpc</strong> and before subsequent calls to <strong>KeAcquireSpinLock</strong> or to <strong>KeAcquireSpinLockRaiseToDpc</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SpinLockSafe</strong>](wdm-spinlocksafe.md)</p></td>
<td align="left"><p>The [<strong>SpinLockSafe</strong>](wdm-spinlocksafe.md) rule specifies that [<strong>IoStartNextPacket</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550358) and [<strong>IoCompleteRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548343) are not called while holding a spin lock.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WithinCriticalRegion</strong>](wdm-withincriticalregion.md)</p></td>
<td align="left"><p>The [<strong>WithinCriticalRegion</strong>](wdm-withincriticalregion.md) rule specifies that the driver's calls to particular synchronization functions appear only after calling [<strong>KeEnterCriticalRegion</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552021) and before calling [<strong>KeLeaveCriticalRegion</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552964).</p>
<p>The affected synchronization functions are the following:</p>
<ul>
<li><p>[<strong>ExAcquireResourceSharedLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544363)</p></li>
<li><p>[<strong>ExAcquireResourceExclusiveLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544351)</p></li>
<li><p>[<strong>ExAcquireSharedStarveExclusive</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544367)</p></li>
<li><p>[<strong>ExAcquireSharedWaitForExclusive</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544370)</p></li>
<li><p>[<strong>ExReleaseResourceLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545597)</p></li>
<li><p>[<strong>ExReleaseResourceForThreadLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545585)</p></li>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Locking%20rule%20set%20%28WDM%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




