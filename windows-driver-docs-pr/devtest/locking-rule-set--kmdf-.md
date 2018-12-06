---
title: Locking rule set (KMDF)
description: Use these rules to verify that your driver correctly manages shared resources.
ms.assetid: B6DD41A5-E7E5-4070-8752-68E26804A5D5
ms.date: 05/21/2018
ms.localizationpriority: medium
---

# Locking rule set (KMDF)


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
<td align="left"><p><a href="kmdf-parentobjectchecklock.md" data-raw-source="[&lt;strong&gt;ParentObjectCheckLock&lt;/strong&gt;](kmdf-parentobjectchecklock.md)"><strong>ParentObjectCheckLock</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-parentobjectchecklock.md" data-raw-source="[&lt;strong&gt;ParentObjectCheckLock&lt;/strong&gt;](kmdf-parentobjectchecklock.md)"><strong>ParentObjectCheckLock</strong></a> rule specifies that the driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551171" data-raw-source="[&lt;strong&gt;WdfWaitLockCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551171)"><strong>WdfWaitLockCreate</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff550042" data-raw-source="[&lt;strong&gt;WdfSpinLockCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550042)"><strong>WdfSpinLockCreate</strong></a> setting a parent object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-reqsendwhilespinlock.md" data-raw-source="[&lt;strong&gt;ReqSendWhileSpinlock&lt;/strong&gt;](kmdf-reqsendwhilespinlock.md)"><strong>ReqSendWhileSpinlock</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-reqsendwhilespinlock.md" data-raw-source="[&lt;strong&gt;ReqSendWhileSpinlock&lt;/strong&gt;](kmdf-reqsendwhilespinlock.md)"><strong>ReqSendWhileSpinlock</strong></a> rule specifies that no requests are sent while the driver holds a spinlock.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-spinlock.md" data-raw-source="[&lt;strong&gt;Spinlock&lt;/strong&gt;](kmdf-spinlock.md)"><strong>Spinlock</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-spinlock.md" data-raw-source="[&lt;strong&gt;Spinlock&lt;/strong&gt;](kmdf-spinlock.md)"><strong>Spinlock</strong></a> rule specifies that calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551917" data-raw-source="[&lt;strong&gt;KeAcquireSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551917)"><strong>KeAcquireSpinLock</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff551928" data-raw-source="[&lt;strong&gt;KeAcquireSpinLockRaiseToDpc&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551928)"><strong>KeAcquireSpinLockRaiseToDpc</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553145" data-raw-source="[&lt;strong&gt;KeReleaseSpinlock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553145)"><strong>KeReleaseSpinlock</strong></a> are used in strict alternation.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-spinlockdpc.md" data-raw-source="[&lt;strong&gt;SpinlockDpc&lt;/strong&gt;](kmdf-spinlockdpc.md)"><strong>SpinlockDpc</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-spinlockdpc.md" data-raw-source="[&lt;strong&gt;SpinlockDpc&lt;/strong&gt;](kmdf-spinlockdpc.md)"><strong>SpinlockDpc</strong></a> rule specifies that calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551917" data-raw-source="[&lt;strong&gt;KeAcquireSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551917)"><strong>KeAcquireSpinLock</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff551928" data-raw-source="[&lt;strong&gt;KeAcquireSpinLockRaiseToDpc&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551928)"><strong>KeAcquireSpinLockRaiseToDpc</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553145" data-raw-source="[&lt;strong&gt;KeReleaseSpinlock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553145)"><strong>KeReleaseSpinlock</strong></a> are used in strict alternation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-spinlockrelease.md" data-raw-source="[&lt;strong&gt;SpinlockRelease&lt;/strong&gt;](kmdf-spinlockrelease.md)"><strong>SpinlockRelease</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-spinlockrelease.md" data-raw-source="[&lt;strong&gt;SpinlockRelease&lt;/strong&gt;](kmdf-spinlockrelease.md)"><strong>SpinlockRelease</strong></a> rule specifies that calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551917" data-raw-source="[&lt;strong&gt;KeAcquireSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551917)"><strong>KeAcquireSpinLock</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551928" data-raw-source="[&lt;strong&gt;KeAcquireSpinLockRaiseToDpc&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551928)"><strong>KeAcquireSpinLockRaiseToDpc</strong></a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff553145" data-raw-source="[&lt;strong&gt;KeReleaseSpinLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553145)"><strong>KeReleaseSpinLock</strong></a> are used in a balanced way within a KMDF callback. At the end of any KMDF callback routine, the driver should not hold the spin lock.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-wdfinterruptlock.md" data-raw-source="[&lt;strong&gt;WdfInterruptLock&lt;/strong&gt;](kmdf-wdfinterruptlock.md)"><strong>WdfInterruptLock</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-wdfinterruptlock.md" data-raw-source="[&lt;strong&gt;WdfInterruptLock&lt;/strong&gt;](kmdf-wdfinterruptlock.md)"><strong>WdfInterruptLock</strong></a> rule specifies that calls to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547340" data-raw-source="[&lt;strong&gt;WdfInterruptAcquireLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547340)"><strong>WdfInterruptAcquireLock</strong></a> method is used in strict alternation with calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547376" data-raw-source="[&lt;strong&gt;WdfInterruptReleaseLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547376)"><strong>WdfInterruptReleaseLock</strong></a>. Moreover, at the end of any KMDF callback routine, the driver should not hold the framework spin lock object, obtained by a previous call to <strong>WdfInterruptAcquireLock</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-wdfinterruptlockrelease.md" data-raw-source="[&lt;strong&gt;WdfInterruptLockRelease&lt;/strong&gt;](kmdf-wdfinterruptlockrelease.md)"><strong>WdfInterruptLockRelease</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-wdfinterruptlockrelease.md" data-raw-source="[&lt;strong&gt;WdfInterruptLockRelease&lt;/strong&gt;](kmdf-wdfinterruptlockrelease.md)"><strong>WdfInterruptLockRelease</strong></a> rule specifies that calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547340" data-raw-source="[&lt;strong&gt;WdfInterruptAcquireLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547340)"><strong>WdfInterruptAcquireLock</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff547376" data-raw-source="[&lt;strong&gt;WdfInterruptReleaseLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547376)"><strong>WdfInterruptReleaseLock</strong></a> are used in a balanced way within a KMDF callback routine. At the end of any KMDF callback routine, the driver should not hold the framework spin lock object that was obtained by a previous call to <strong>WdfInterruptAcquireLock</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-wdfspinlock.md" data-raw-source="[&lt;strong&gt;WdfSpinlock&lt;/strong&gt;](kmdf-wdfspinlock.md)"><strong>WdfSpinlock</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-wdfspinlock.md" data-raw-source="[&lt;strong&gt;WdfSpinlock&lt;/strong&gt;](kmdf-wdfspinlock.md)"><strong>WdfSpinlock</strong></a> rule specifies that calls to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550040" data-raw-source="[&lt;strong&gt;WdfSpinLockAcquire&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550040)"><strong>WdfSpinLockAcquire</strong></a> method are used in strict alternation with <a href="kmdf-wdfspinlockrelease.md" data-raw-source="[&lt;strong&gt;WdfSpinlockRelease&lt;/strong&gt;](kmdf-wdfspinlockrelease.md)"><strong>WdfSpinlockRelease</strong></a>. At the end of any KMDF callback routine, the driver should not hold the framework spinlock object that was obtained by a previous call to <strong>WdfSpinLockAcquire</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-wdfspinlockrelease.md" data-raw-source="[&lt;strong&gt;WdfSpinlockRelease&lt;/strong&gt;](kmdf-wdfspinlockrelease.md)"><strong>WdfSpinlockRelease</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-wdfspinlockrelease.md" data-raw-source="[&lt;strong&gt;WdfSpinlockRelease&lt;/strong&gt;](kmdf-wdfspinlockrelease.md)"><strong>WdfSpinlockRelease</strong></a> rule specifies that calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff550040" data-raw-source="[&lt;strong&gt;WdfSpinLockAcquire&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550040)"><strong>WdfSpinLockAcquire</strong></a> and <strong>WdfSpinlockRelease</strong> are used in a balanced way within a KMDF event callback function. When the KMDF event callback function returns, the driver should not hold the framework spin lock object that was obtained by a previous call to <strong>WdfSpinLockAcquire</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-wdfwaitlock.md" data-raw-source="[&lt;strong&gt;WdfWaitlock&lt;/strong&gt;](kmdf-wdfwaitlock.md)"><strong>WdfWaitlock</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-wdfwaitlock.md" data-raw-source="[&lt;strong&gt;WdfWaitlock&lt;/strong&gt;](kmdf-wdfwaitlock.md)"><strong>WdfWaitlock</strong></a> rule specifies that calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551168" data-raw-source="[&lt;strong&gt;WdfWaitLockAcquire&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551168)"><strong>WdfWaitLockAcquire</strong></a> are used in strict alternation with <a href="kmdf-wdfwaitlockrelease.md" data-raw-source="[&lt;strong&gt;WdfWaitlockRelease&lt;/strong&gt;](kmdf-wdfwaitlockrelease.md)"><strong>WdfWaitlockRelease</strong></a>. When the KMDF event callback function returns, the driver should not hold the framework spin lock object that was obtained by a previous call to <strong>WdfWaitLockAcquire</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-wdfwaitlockrelease.md" data-raw-source="[&lt;strong&gt;WdfWaitlockRelease&lt;/strong&gt;](kmdf-wdfwaitlockrelease.md)"><strong>WdfWaitlockRelease</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-wdfwaitlockrelease.md" data-raw-source="[&lt;strong&gt;WdfWaitlockRelease&lt;/strong&gt;](kmdf-wdfwaitlockrelease.md)"><strong>WdfWaitlockRelease</strong></a> rule specifies that calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551168" data-raw-source="[&lt;strong&gt;WdfWaitLockAcquire&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551168)"><strong>WdfWaitLockAcquire</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff551173" data-raw-source="[&lt;strong&gt;WdfWaitLockRelease&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551173)"><strong>WdfWaitLockRelease</strong></a> are used in a balanced way within a KMDF event callback function. When the KMDF event callback function returns, the driver should not hold the framework spin lock object that was obtained by a previous call to <strong>WdfWaitLockAcquire</strong>.</p></td>
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

 

 





