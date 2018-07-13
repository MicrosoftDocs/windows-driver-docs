---
title: Locking rule set (NDIS)
description: Use these rules to verify that your driver correctly manages shared resources.
ms.assetid: 1123A246-7833-4EAB-B1B8-0C71413CE86B
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Locking rule set (NDIS)


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
<td align="left"><p>[<strong>SpinLock</strong>](ndis-spinlock.md)</p></td>
<td align="left"><p>The [<strong>SpinLock</strong>](ndis-spinlock.md) rule verifies the correct use of the NDIS spin lock interface. This rule specifies that calls to [<strong>NdisAcquireSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560699) are made only when the SpinLock is in the unlocked state. This rule also verifies that the SpinLock is released before the miniport handler routine exits.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SpinLockBalanced</strong>](ndis-spinlockbalanced.md)</p></td>
<td align="left"><p>The [<strong>SpinLockBalanced</strong>](ndis-spinlockbalanced.md) rule verifies that the number of calls to functions that acquire a SpinLock are equal to the number of calls to functions that release the same SpinLock.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SpinLockDpr</strong>](ndis-spinlockdpr.md)</p></td>
<td align="left"><p>The [<strong>SpinLockDpr</strong>](ndis-spinlockdpr.md) rule verifies the correct use of the NDIS spin lock interface.</p>
<p>This rule specifies that calls to [<strong>NdisDprAcquireSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561749) are made only when the spin lock is in the unlocked state. This rule also verifies that the spin lock is released before the miniport handler routine exits.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SpinLockDprRelease</strong>](ndis-spinlockdprrelease.md)</p></td>
<td align="left"><p>The [<strong>SpinLockDprRelease</strong>](ndis-spinlockdprrelease.md) rule verifies that calls to [<strong>NdisAcquireSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560699) or [<strong>NdisDprAcquireSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561749) are called only when the SpinLock is the &quot;unlocked&quot; state. This rule also checks that before exiting the miniport handler routine the SpinLock has been release.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SpinLockRelease</strong>](ndis-spinlockrelease.md)</p></td>
<td align="left"><p>The SpinLockRelease rule specifies that a driver must not release a spin lock ([<strong>NdisReleaseSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564524)) without first acquiring it.</p></td>
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

 

 





