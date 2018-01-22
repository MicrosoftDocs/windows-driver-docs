---
title: Locking rule set (NDIS)
description: Use these rules to verify that your driver correctly manages shared resources.
ms.assetid: 1123A246-7833-4EAB-B1B8-0C71413CE86B
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Locking%20rule%20set%20%28NDIS%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




