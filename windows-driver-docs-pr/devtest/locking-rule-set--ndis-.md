---
title: Locking Rule Set (NDIS)
description: Learn about using rules (NDIS) to verify that your driver correctly manages shared resources, and how to select the Locking rule set.
ms.date: 05/21/2018
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
<td align="left"><p><a href="ndis-spinlock.md" data-raw-source="[&lt;strong&gt;SpinLock&lt;/strong&gt;](ndis-spinlock.md)"><strong>SpinLock</strong></a></p></td>
<td align="left"><p>The <a href="ndis-spinlock.md" data-raw-source="[&lt;strong&gt;SpinLock&lt;/strong&gt;](ndis-spinlock.md)"><strong>SpinLock</strong></a> rule verifies the correct use of the NDIS spin lock interface. This rule specifies that calls to <a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisacquirespinlock" data-raw-source="[&lt;strong&gt;NdisAcquireSpinLock&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisacquirespinlock)"><strong>NdisAcquireSpinLock</strong></a> are made only when the SpinLock is in the unlocked state. This rule also verifies that the SpinLock is released before the miniport handler routine exits.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-spinlockbalanced.md" data-raw-source="[&lt;strong&gt;SpinLockBalanced&lt;/strong&gt;](ndis-spinlockbalanced.md)"><strong>SpinLockBalanced</strong></a></p></td>
<td align="left"><p>The <a href="ndis-spinlockbalanced.md" data-raw-source="[&lt;strong&gt;SpinLockBalanced&lt;/strong&gt;](ndis-spinlockbalanced.md)"><strong>SpinLockBalanced</strong></a> rule verifies that the number of calls to functions that acquire a SpinLock are equal to the number of calls to functions that release the same SpinLock.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-spinlockdpr.md" data-raw-source="[&lt;strong&gt;SpinLockDpr&lt;/strong&gt;](ndis-spinlockdpr.md)"><strong>SpinLockDpr</strong></a></p></td>
<td align="left"><p>The <a href="ndis-spinlockdpr.md" data-raw-source="[&lt;strong&gt;SpinLockDpr&lt;/strong&gt;](ndis-spinlockdpr.md)"><strong>SpinLockDpr</strong></a> rule verifies the correct use of the NDIS spin lock interface.</p>
<p>This rule specifies that calls to <a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisdpracquirespinlock" data-raw-source="[&lt;strong&gt;NdisDprAcquireSpinLock&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisdpracquirespinlock)"><strong>NdisDprAcquireSpinLock</strong></a> are made only when the spin lock is in the unlocked state. This rule also verifies that the spin lock is released before the miniport handler routine exits.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-spinlockdprrelease.md" data-raw-source="[&lt;strong&gt;SpinLockDprRelease&lt;/strong&gt;](ndis-spinlockdprrelease.md)"><strong>SpinLockDprRelease</strong></a></p></td>
<td align="left"><p>The <a href="ndis-spinlockdprrelease.md" data-raw-source="[&lt;strong&gt;SpinLockDprRelease&lt;/strong&gt;](ndis-spinlockdprrelease.md)"><strong>SpinLockDprRelease</strong></a> rule verifies that calls to <a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisacquirespinlock" data-raw-source="[&lt;strong&gt;NdisAcquireSpinLock&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisacquirespinlock)"><strong>NdisAcquireSpinLock</strong></a> or <a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisdpracquirespinlock" data-raw-source="[&lt;strong&gt;NdisDprAcquireSpinLock&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisdpracquirespinlock)"><strong>NdisDprAcquireSpinLock</strong></a> are called only when the SpinLock is the "unlocked" state. This rule also checks that before exiting the miniport handler routine the SpinLock has been release.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-spinlockrelease.md" data-raw-source="[&lt;strong&gt;SpinLockRelease&lt;/strong&gt;](ndis-spinlockrelease.md)"><strong>SpinLockRelease</strong></a></p></td>
<td align="left"><p>The SpinLockRelease rule specifies that a driver must not release a spin lock (<a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreleasespinlock" data-raw-source="[&lt;strong&gt;NdisReleaseSpinLock&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreleasespinlock)"><strong>NdisReleaseSpinLock</strong></a>) without first acquiring it.</p></td>
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

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md) and [Static Driver Verifier commands (MSBuild)](./-static-driver-verifier-commands--msbuild-.md).

