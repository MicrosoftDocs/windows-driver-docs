---
title: Bug Check 0xC4 DRIVER\_VERIFIER\_DETECTED\_VIOLATION
description: The DRIVER\_VERIFIER\_DETECTED\_VIOLATION bug check has a value of 0x000000C4. This is the general bug check code for fatal errors found by Driver Verifier. 
ms.assetid: 7814f827-05fc-419b-b428-4565978bbb52
keywords: ["Bug Check 0xC4 DRIVER_VERIFIER_DETECTED_VIOLATION", "DRIVER_VERIFIER_DETECTED_VIOLATION"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- DRIVER_VERIFIER_DETECTED_VIOLATION
api_type:
- NA
---

# Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION


The DRIVER\_VERIFIER\_DETECTED\_VIOLATION bug check has a value of 0x000000C4. This is the general bug check code for fatal errors found by Driver Verifier. For more information, see [Handling a Bug Check When Driver Verifier is Enabled](handling-a-bug-check-when-driver-verifier-is-enabled.md).

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](http://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## DRIVER\_VERIFIER\_DETECTED\_VIOLATION Parameters


Parameter 1 identifies the type of violation. The meaning of the remaining parameters varies with the value of Parameter 1. The parameter values are described in the following table.

**Note**  If you have trouble viewing all 5 columns in this table, try the following:
-   Expand your browser window to full size.
-   Place the cursor in the table and use the arrow keys to scroll left and right.
-   Or use the [MSDN Library version](http://msdn.microsoft.com/library/ff560187.aspx) of this page.

 

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x00</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Pool type</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver requested a zero-byte pool allocation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x01</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Pool type</p></td>
<td align="left"><p>Size of allocation, in bytes</p></td>
<td align="left"><p>The driver attempted to allocate paged memory with IRQL &gt; APC_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x02</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Pool type</p></td>
<td align="left"><p>Size of allocation, in bytes</p></td>
<td align="left"><p>The driver attempted to allocate nonpaged memory with IRQL &gt; DISPATCH_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10</p></td>
<td align="left"><p>Bad Address</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver attempted to free an address that was not returned from an allocate call.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x11</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Pool type</p></td>
<td align="left"><p>Address of pool</p></td>
<td align="left"><p>The driver attempted to free paged pool with IRQL &gt; APC_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x12</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Pool type</p></td>
<td align="left"><p>Address of pool</p></td>
<td align="left"><p>The driver attempted to free nonpaged pool with IRQL &gt; DISPATCH_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x13 or</p>
<p>0x14</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Pointer to pool header</p></td>
<td align="left"><p>Pool header contents</p></td>
<td align="left"><p>The driver attempted to free memory pool which was already freed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x16</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Pool address</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver attempted to free pool at a bad address, or the driver passed invalid parameters to a memory routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x30</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Requested IRQL</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver passed an invalid parameter to [<strong>KeRaiseIrql</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553079).</p>
<p>(The parameter was either a value lower than the current IRQL, or a value higher than HIGH_LEVEL. This may be the result of using an uninitialized parameter.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x31</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Requested IRQL</p></td>
<td align="left"><p><strong>0:</strong> New IRQL is bad</p>
<p><strong>1:</strong> New IRQL is invalid inside a DPC routine</p></td>
<td align="left"><p>The driver passed an invalid parameter to [<strong>KeLowerIrql</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552968).</p>
<p>(The parameter was either a value higher than the current IRQL, or a value higher than HIGH_LEVEL. This may be the result of using an uninitialized parameter.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x32</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Spin lock address</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver called [<strong>KeReleaseSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553145) at an IRQL other than DISPATCH_LEVEL.</p>
<p>(This may be due to a double-release of a spin lock.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x33</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Fast mutex address</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver attempted to acquire fast mutex with IRQL &gt; APC_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x34</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Fast mutex address</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver attempted to release fast mutex at an IRQL other than APC_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x35</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Spin lock address</p></td>
<td align="left"><p>Old IRQL</p></td>
<td align="left"><p>The kernel released a spin lock with IRQL not equal to DISPATCH_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x36</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Spin lock number</p></td>
<td align="left"><p>Old IRQL</p></td>
<td align="left"><p>The kernel released a queued spin lock with IRQL not equal to DISPATCH_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x37</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Thread APC disable count</p></td>
<td align="left"><p>Resource</p></td>
<td align="left"><p>The driver tried to acquire a resource, but APCs are not disabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x38</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Thread APC disable count</p></td>
<td align="left"><p>Resource</p></td>
<td align="left"><p>The driver tried to release a resource, but APCs are not disabled.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x39</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Thread APC disable count</p></td>
<td align="left"><p>Mutex</p></td>
<td align="left"><p>The driver tried to acquire a mutex &quot;unsafe&quot; with IRQL not equal to APC_LEVEL on entry.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3A</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Thread APC disable count</p></td>
<td align="left"><p>Mutex</p></td>
<td align="left"><p>The driver tried to release a mutex &quot;unsafe&quot; with IRQL not equal to APC_LEVEL on entry.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3C</p></td>
<td align="left"><p>Handle passed to routine</p></td>
<td align="left"><p>Object type</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver called [<strong>ObReferenceObjectByHandle</strong>](https://msdn.microsoft.com/library/windows/hardware/ff558679) with a bad handle.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3D</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Address of the bad resource</p></td>
<td align="left"><p>The driver passed a bad (unaligned) resource to [<strong>ExAcquireResourceExclusive</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544345).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3E</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver called [<strong>KeLeaveCriticalRegion</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552964) for a thread that is not currently in a critical region.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3F</p></td>
<td align="left"><p>Object address</p></td>
<td align="left"><p>New object reference count.</p>
<p><strong>-1:</strong> dereference case</p>
<p><strong>1:</strong> reference case</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver applied [<strong>ObReferenceObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff558678) to an object that has a reference count of zero, or the driver applied [<strong>ObDereferenceObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557724) to an object that has a reference count of zero.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x40</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Spin lock address</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver called [<strong>KeAcquireSpinLockAtDpcLevel</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551921) with IRQL &lt; DISPATCH_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x41</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Spin lock address</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver called [<strong>KeReleaseSpinLockFromDpcLevel</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553150) with IRQL &lt; DISPATCH_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x42</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Spin lock address</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver called [<strong>KeAcquireSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551917) with IRQL &gt; DISPATCH_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x51</p></td>
<td align="left"><p>Base address of allocation</p></td>
<td align="left"><p>Address of the reference beyond the allocation</p></td>
<td align="left"><p>Number of charged bytes</p></td>
<td align="left"><p>The driver attempted to free memory after having written past the end of the allocation. A bug check with this parameter occurs only when the <strong>Pool Tracking</strong> option of Driver Verifier is active.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x52</p></td>
<td align="left"><p>Base address of allocation</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Number of charged bytes</p></td>
<td align="left"><p>The driver attempted to free memory after having written past the end of the allocation. A bug check with this parameter occurs only when the <strong>Pool Tracking</strong> option of Driver Verifier is active.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x53,</p>
<p>0x54,</p>
<p>or 0x59</p></td>
<td align="left"><p>Base address of allocation</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver attempted to free memory after having written past the end of the allocation. A bug check with this parameter occurs only when the <strong>Pool Tracking</strong> option of Driver Verifier is active.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x60</p></td>
<td align="left"><p>Bytes allocated from paged pool</p></td>
<td align="left"><p>Bytes allocated from nonpaged pool</p></td>
<td align="left"><p>Total number of allocations that were not freed</p></td>
<td align="left"><p>The driver is unloading without first freeing its pool allocations. A bug check with this parameter occurs only when the <strong>Pool Tracking</strong> option of Driver Verifier is active.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x61</p></td>
<td align="left"><p>Bytes allocated from paged pool</p></td>
<td align="left"><p>Bytes allocated from nonpaged pool</p></td>
<td align="left"><p>Total number of allocations that were not freed</p></td>
<td align="left"><p>A driver thread is attempting to allocate pool memory while the driver is unloading. A bug check with this parameter occurs only when the <strong>Pool Tracking</strong> option of Driver Verifier is active.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x62</p></td>
<td align="left"><p>Name of the driver</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Total number of allocations that were not freed, including both paged and nonpaged pool</p></td>
<td align="left"><p>The driver is unloading without first freeing its pool allocations. A bug check with this parameter occurs only when the <strong>Pool Tracking</strong> option of Driver Verifier is active.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x70</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>Access mode</p></td>
<td align="left"><p>The driver called [<strong>MmProbeAndLockPages</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554664) with IRQL &gt; DISPATCH_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x71</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>Process address</p></td>
<td align="left"><p>The driver called <strong>MmProbeAndLockProcessPages</strong> with IRQL &gt; DISPATCH_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x72</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>Process address</p></td>
<td align="left"><p>The driver called <strong>MmProbeAndLockSelectedPages</strong> with IRQL &gt; DISPATCH_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x73</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>In 32-bit Windows: Low 32 bits of the physical address</p>
<p>In 64-bit Windows: the 64-bit physical address</p></td>
<td align="left"><p>Number of bytes</p></td>
<td align="left"><p>The driver called [<strong>MmMapIoSpace</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554618) with IRQL &gt; DISPATCH_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x74</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>Access mode</p></td>
<td align="left"><p>The driver called [<strong>MmMapLockedPages</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554622) in kernel mode with IRQL &gt; DISPATCH_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x75</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>Access mode</p></td>
<td align="left"><p>The driver called [<strong>MmMapLockedPages</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554622) in user mode with IRQL &gt; APC_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x76</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>Access mode</p></td>
<td align="left"><p>The driver called [<strong>MmMapLockedPagesSpecifyCache</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554629) in kernel mode with IRQL &gt; DISPATCH_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x77</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>Access mode</p></td>
<td align="left"><p>The driver called [<strong>MmMapLockedPagesSpecifyCache</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554629) in user mode with IRQL &gt; APC_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x78</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver called [<strong>MmUnlockPages</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556381) with IRQL &gt; DISPATCH_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x79</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Virtual address being unmapped</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>The driver called [<strong>MmUnmapLockedPages</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556391) in kernel mode with IRQL &gt; DISPATCH_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x7A</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Virtual address being unmapped</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>The driver called [<strong>MmUnmapLockedPages</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556391) in user mode with IRQL &gt; APC_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x7B</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Virtual address being unmapped</p></td>
<td align="left"><p>Number of bytes</p></td>
<td align="left"><p>The driver called [<strong>MmUnmapIoSpace</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556387) with IRQL &gt; APC_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x7C</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>MDL flags</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver called [<strong>MmUnlockPages</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556381), and passed an MDL whose pages were never successfully locked.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x7D</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>MDL flags</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver called [<strong>MmUnlockPages</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556381), and passed an MDL whose pages are from nonpaged pool.</p>
<p>(These should never be unlocked.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x7E</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>DISPATCH_LEVEL</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver called [<strong>MmAllocatePagesForMdl</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554482), [<strong>MmAllocatePagesForMdlEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554489), or [<strong>MmFreePagesFromMdl</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554521) with IRQL &gt; DISPATCH_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x7F</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>MDL flags</p></td>
<td align="left"><p>The driver called [<strong>BuildMdlForNonPagedPool</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554498) and passed an MDL whose pages are from paged pool.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x80</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Event address</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver called [<strong>KeSetEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553253) with IRQL &gt; DISPATCH_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x81</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>MDL flags</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver called [<strong>MmMapLockedPages</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554622).</p>
<p>(You should use [<strong>MmMapLockedPagesSpecifyCache</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554629) instead, with the <em>BugCheckOnFailure</em> parameter set to <strong>FALSE</strong>.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x82</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>MDL flags</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The driver called [<strong>MmMapLockedPagesSpecifyCache</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554629) with the <em>BugCheckOnFailure</em> parameter equal to <strong>TRUE</strong>.</p>
<p>(This parameter should be set to <strong>FALSE</strong>.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x83</p></td>
<td align="left"><p>Start of physical address range to map</p></td>
<td align="left"><p>Number of bytes to map</p></td>
<td align="left"><p>First page frame number that isn't locked down</p></td>
<td align="left"><p>The driver called [<strong>MmMapIoSpace</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554618) without having locked down the MDL pages. The physical pages represented by the physical address range being mapped must have been locked down prior to making this call.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x85</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>Number of pages to map</p></td>
<td align="left"><p>First page frame number that isn't locked down</p></td>
<td align="left"><p>The driver called [<strong>MmMapLockedPages</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554622) without having locked down the MDL pages.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x89</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>Pointer to the non-memory page in the MDL</p></td>
<td align="left"><p>The non-memory page number in the MDL</p></td>
<td align="left"><p>An MDL is not marked as &quot;I/O&quot;, but it contains non-memory page addresses.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x91</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver switched stacks using a method that is not supported by the operating system. The only supported way to extend a kernel mode stack is by using [<strong>KeExpandKernelStackAndCallout</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552030).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xA0 (Windows Server 2003 and later operating systems only)</p></td>
<td align="left"><p>Pointer to the IRP making the read or write request</p></td>
<td align="left"><p>Device object of the lower device</p></td>
<td align="left"><p>Number of the sector in which the error was detected</p></td>
<td align="left"><p>A cyclic redundancy check (CRC) error was detected on a hard disk. A bug check with this parameter occurs only when the <strong>Disk Integrity Checking</strong> option of Driver Verifier is active.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xA1 (Windows Server 2003 and later operating systems only)</p></td>
<td align="left"><p>Copy of the IRP making the read or write request. (The actual IRP has been completed.)</p></td>
<td align="left"><p>Device object of the lower device</p></td>
<td align="left"><p>Number of the sector in which the error was detected</p></td>
<td align="left"><p>A CRC error was detected on a sector (asynchronously). A bug check with this parameter occurs only when the <strong>Disk Integrity Checking</strong> option of Driver Verifier is active.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xA2 (Windows Server 2003 and later operating systems only)</p></td>
<td align="left"><p>IRP making the read or write request, or a copy of this IRP</p></td>
<td align="left"><p>Device object of the lower device</p></td>
<td align="left"><p>Number of the sector in which the error was detected</p></td>
<td align="left"><p>The CRCDISK checksum copies don't match. This could be a paging error. A bug check with this parameter occurs only when the <strong>Disk Integrity Checking</strong> option of Driver Verifier is active.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xB0 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>MDL flags</p></td>
<td align="left"><p>Incorrect MDL flags</p></td>
<td align="left"><p>The driver called [<strong>MmProbeAndLockPages</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554664) for an MDL with incorrect flags. For example, the driver passed an MDL created by [<strong>MmBuildMdlForNonPagedPool</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554498) to <strong>MmProbeAndLockPages</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xB1 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>MDL flags</p></td>
<td align="left"><p>Incorrect MDL flags</p></td>
<td align="left"><p>The driver called <strong>MmProbeAndLockProcessPages</strong> for an MDL with incorrect flags. For example, the driver passed an MDL created by [<strong>MmBuildMdlForNonPagedPool</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554498) to <strong>MmProbeAndLockProcessPages</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xB2 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>MDL flags</p></td>
<td align="left"><p>Incorrect MDL flags</p></td>
<td align="left"><p>The driver called [<strong>MmMapLockedPages</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554622) for an MDL with incorrect flags. For example, the driver passed an MDL that is already mapped to a system address or that was not locked to <strong>MmMapLockedPages</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xB3 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>MDL flags</p></td>
<td align="left"><p>Missing MDL flags (at least one was expected)</p></td>
<td align="left"><p>The driver called [<strong>MmMapLockedPages</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554622) for an MDL with incorrect flags. For example, the driver passed an MDL that is not locked to <strong>MmMapLockedPages</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xB4 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>MDL address</p></td>
<td align="left"><p>MDL flags</p></td>
<td align="left"><p>Unexpected partial MDL flag</p></td>
<td align="left"><p>The driver called [<strong>MmUnlockPages</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556381) for a partial MDL. A partial MDL is one that was created by [<strong>IoBuildPartialMdl</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548324).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xC0 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the IRP</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver called [<strong>IoCallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548336) with interrupts disabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xC1 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the driver dispatch routine</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A driver dispatch routine was returned with interrupts disabled.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xC2 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver called a Fast I/O dispatch routine after interrupts were disabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xC3 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the driver Fast I/O dispatch routine</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A driver Fast I/O dispatch routine was returned with interrupts disabled.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xC5 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the driver dispatch routine</p></td>
<td align="left"><p>The current thread's APC disable count</p></td>
<td align="left"><p>The thread's APC disable count prior to calling the driver dispatch routine</p></td>
<td align="left"><p>A driver dispatch routine has changed the thread's APC disable count.</p>
<p>The APC disable count is decremented each time a driver calls [<strong>KeEnterCriticalRegion</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552021), [<strong>FsRtlEnterFileSystem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545900), or acquires a mutex.</p>
<p>The APC disable count is incremented each time a driver calls [<strong>KeLeaveCriticalRegion</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552964), [<strong>KeReleaseMutex</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553140), or [<strong>FsRtlExitFileSystem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545908).</p>
<p>Because these calls should always be in pairs, the APC disable count should be zero whenever a thread is exited. A negative value indicates that a driver has disabled APC calls without re-enabling them. A positive value indicates that the reverse is true.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xC6 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the driver Fast I/O dispatch routine</p></td>
<td align="left"><p>Current thread's APC disable count</p></td>
<td align="left"><p>The thread's APC disable count prior to calling the Fast I/O driver dispatch routine</p></td>
<td align="left"><p>A driver Fast I/O dispatch routine has changed the thread's APC disable count.</p>
<p>The APC disable count is decremented each time a driver calls [<strong>KeEnterCriticalRegion</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552021), [<strong>FsRtlEnterFileSystem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545900), or acquires a mutex.</p>
<p>The APC disable count is incremented each time a driver calls [<strong>KeLeaveCriticalRegion</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552964), [<strong>KeReleaseMutex</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553140), or [<strong>FsRtlExitFileSystem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545908).</p>
<p>Because these calls should always be in pairs, the APC disable count should be zero whenever a thread is exited. A negative value indicates that a driver has disabled APC calls without re-enabling them. A positive value indicates that the reverse is true.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xCA (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the lookaside list</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver has attempted to re-initialize a lookaside list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xCB (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the lookaside list</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver has attempted to delete an uninitialized lookaside list.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xCC (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the lookaside list</p></td>
<td align="left"><p>Starting address of the pool allocation</p></td>
<td align="left"><p>Size of the pool allocation</p></td>
<td align="left"><p>The driver has attempted to free a pool allocation that contains an active lookaside list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xCD (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the lookaside list</p></td>
<td align="left"><p>Block size specified by the caller</p></td>
<td align="left"><p>Minimum supported block size</p></td>
<td align="left"><p>The driver has attempted to create a lookaside list with an allocation block size that is too small.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xD0 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the ERESOURCE structure</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver has attempted to re-initialize an ERESOURCE structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xD1 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the ERESOURCE structure</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver has attempted to delete an uninitialized ERESOURCE structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xD2 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the ERESOURCE structure</p></td>
<td align="left"><p>Starting address of the pool allocation</p></td>
<td align="left"><p>Size of the pool allocation</p></td>
<td align="left"><p>The driver has attempted to free a pool allocation that contains an active ERESOURCE structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xD5 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the IO_REMOVE_LOCK structure created by the checked build version of the driver</p></td>
<td align="left"><p>Current [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) tag</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The current [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) tag does not match the previous [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) tag. If the driver calling <strong>IoReleaseRemoveLock</strong> is not in a checked build, Parameter 2 is the address of the shadow IO_REMOVE_LOCK structure created by Driver Verifier on behalf of the driver. In this case, the address of the IO_REMOVE_LOCK structure used by the driver is not used at all, because Driver Verifier is replacing the lock address for all the remove lock APIs. A bug check with this parameter occurs only when the <strong>I/O Verification</strong> option of Driver Verifier is active.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xD6 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the IO_REMOVE_LOCK structure created by the checked build version of the driver</p></td>
<td align="left"><p>Tag that does not match previous [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) tag</p></td>
<td align="left"><p>Previous [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) tag</p></td>
<td align="left"><p>The current [<strong>IoReleaseRemoveLockAndWait</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549567) tag does not match the previous [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) tag. If the driver calling [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560) is not a checked build, Parameter 2 is the address of the shadow IO_REMOVE_LOCK structure created by Driver Verifier on behalf of the driver. In this case, the address of the IO_REMOVE_LOCK structure used by the driver is not used at all, because Driver Verifier is replacing the lock address for all the remove lock APIs. A bug check with this parameter occurs only when the <strong>I/O Verification</strong> option of Driver Verifier is active.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xD7 (Windows 7 operating systems and later only)</p></td>
<td align="left"><p>Address of the checked build Remove Lock structure that is used internally by Driver Verifier</p></td>
<td align="left"><p>Address of the Remove Lock structure that is specified by the driver</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A Remove Lock cannot be re-initialized, even after it calls [<strong>IoReleaseRemoveLockAndWait</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549567), because other threads might still be using that lock (by calling [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204)). The driver should allocate the Remove Lock inside its device extension, and initialize it a single time. The lock will be deleted together with the device extension.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xDA (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Starting address of the driver</p></td>
<td align="left"><p>WMI callback address inside the driver</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An attempt was made to unload a driver that has not deregistered its WMI callback function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xDB (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the device object</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An attempt was made to delete a device object that was not deregistered from WMI.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xDC (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An invalid RegHandle value was specified as a parameter of the function [<strong>EtwUnregister</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545613).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xDD (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the call to <strong>EtwRegister</strong></p></td>
<td align="left"><p>Starting address of the unloading driver</p></td>
<td align="left"><p>For Windows 8Windows 8 and later versions, this parameter is the ETW RegHandle value.</p></td>
<td align="left"><p>An attempt was made to unload a driver without calling [<strong>EtwUnregister</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545613).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xDF (Windows 7 operating systems and later only)</p></td>
<td align="left"><p>Synchronization object address</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>The synchronization object is in session address space. Synchronization objects are not allowed in session address space because they can be manipulated from another session or from system threads that have no session virtual address space.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xE0 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>User-mode address that is used as a parameter</p></td>
<td align="left"><p>Size ,in bytes, of the address range that is used as a parameter</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A call was made to an operating system kernel function that specified a user-mode address as a parameter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xE1 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the synchronization object</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A synchronization object was found to have an address that was either invalid or pageable.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xE2 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the IRP</p></td>
<td align="left"><p>User-mode address present in the IRP</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An IRP with <strong>Irp-&gt;RequestorMode</strong> set to <strong>KernelMode</strong> was found to have a user-mode address as one of its members.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xE3 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the call to the API</p></td>
<td align="left"><p>User-mode address used as a parameter in the API</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A driver has made a call to a kernel-mode <strong>Zw<em>Xxx</em></strong> routine with a user-mode address as a parameter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xE4 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the call to the API</p></td>
<td align="left"><p>Address of the malformed UNICODE_STRING structure</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A driver has made a call to a kernel-mode <strong>Zw<em>Xxx</em></strong> routine with a malformed UNICODE_STRING structure as a parameter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xE5 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A call was made to a Kernel API at the incorrect IRQL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xEA (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>The thread's APC disable count</p></td>
<td align="left"><p>Address of the pushlock</p></td>
<td align="left"><p>A driver has attempted to acquire a pushlock while APCs are enabled.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xEB (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>The thread's APC disable count</p></td>
<td align="left"><p>Address of the pushlock</p></td>
<td align="left"><p>A driver has attempted to release a pushlock while APCs are enabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xF0 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the destination buffer</p></td>
<td align="left"><p>Address of the source buffer</p></td>
<td align="left"><p>Number of bytes to copy</p></td>
<td align="left"><p>A driver called the memcpy function with overlapping source and destination buffers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xF5 (Windows Vista and later operating systems only)</p></td>
<td align="left"><p>Address of the <strong>NULL</strong> handle</p></td>
<td align="left"><p>Object type</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>A driver passed a <strong>NULL</strong> handle to [<strong>ObReferenceObjectByHandle</strong>](https://msdn.microsoft.com/library/windows/hardware/ff558679).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xF6 (Windows 7 operating systems and later)</p></td>
<td align="left"><p>Handle value being referenced</p></td>
<td align="left"><p>Address of the current process</p></td>
<td align="left"><p>Address inside the driver that performs the incorrect reference</p></td>
<td align="left"><p>A driver references a user-mode handle as kernel mode.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xF7 (Windows 7 operating systems and later)</p></td>
<td align="left"><p>Handle value specified by the caller</p></td>
<td align="left"><p>Object type specified by the caller</p></td>
<td align="left"><p>AccessMode specified by the caller</p></td>
<td align="left"><p>A driver is attempting a user-mode reference for a kernel handle in the context of the system process.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xFA (Windows 7 operating systems and later)</p></td>
<td align="left"><p>Completion routine address.</p></td>
<td align="left"><p>IRQL value before it calls the completion routine</p></td>
<td align="left"><p>Current IRQL value, after it calls the completion routine</p></td>
<td align="left"><p>The IRP completion routine returned at an IRQL that was different from the IRQL the routine was called at.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xFB (Windows 7 operating systems and later)</p></td>
<td align="left"><p>Completion routine address</p></td>
<td align="left"><p>Current thread's APC disable count</p></td>
<td align="left"><p>The thread's APC disable count before it calls the IRP completion routine</p></td>
<td align="left"><p>The thread's APC disable count was changed by the driver's IRP completion routine.</p>
<p>The APC disable count is decremented each time a driver calls [<strong>KeEnterCriticalRegion</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552021), [<strong>FsRtlEnterFileSystem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545900), or acquires a mutex.</p>
<p>The APC disable count is incremented each time a driver calls [<strong>KeLeaveCriticalRegion</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552964), [<strong>KeReleaseMutex</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553140), or [<strong>FsRtlExitFileSystem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545908).</p>
<p>Because these calls should always be in pairs, the APC disable count should be zero whenever a thread is exited. A negative value indicates that a driver has disabled APC calls without re-enabling them. A positive value indicates that the reverse is true.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x105</p>
<p>(Windows 7 operating systems and later)</p></td>
<td align="left"><p>Address of the IRP</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>The driver uses ExFreePool instead of IoFreeIrp to release the IRP.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10A</p>
<p>(Windows 7 operating systems and later)</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>The driver attempts to charge pool quota to the Idle process.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10B</p>
<p>(Windows 7 operating systems and later)</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>The driver attempts to charge pool quota from a DPC routine. This is incorrect because the current process context is undefined.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x110</p>
<p>(Windows 7 operating systems and later)</p></td>
<td align="left"><p>Address of the Interrupt Service Routine</p></td>
<td align="left"><p>Address of the extended context that was saved before it executed the ISR</p></td>
<td align="left"><p>Address of the extended context was saved after it executed the ISR</p></td>
<td align="left"><p>The interrupt service routine (ISR) for the driver has corrupted the extended thread context.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x115</p>
<p>(Windows 7 operating systems and later)</p></td>
<td align="left"><p>The address of the thread that is responsible for the shutdown, which might be deadlocked</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Driver Verifier detected that the system has taken longer than 20 minutes and shutdown is not complete.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x11A</p>
<p>(Windows 7 operating systems and later)</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>The driver calls KeEnterCriticalRegion at IRQL &gt; APC_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x11B</p>
<p>(Windows 7 operating systems and later)</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>The driver calls KeLeaveCriticalRegion at IRQL &gt; APC_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x120</p>
<p>(Windows 7 operating systems and later)</p></td>
<td align="left"><p>Address of the IRQL value</p></td>
<td align="left"><p>Address of the Object to wait on</p></td>
<td align="left"><p>Address of Timeout value</p></td>
<td align="left"><p>The thread waits at IRQL &gt; DISPATCH_LEVEL. Callers of KeWaitForSingleObject or KeWaitForMultipleObjects must run at IRQL &lt;= DISPATCH_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x121</p>
<p>(Windows 7 operating systems and later)</p></td>
<td align="left"><p>Address of the IRQL value</p></td>
<td align="left"><p>Address of the Object to wait on</p></td>
<td align="left"><p>Address of Timeout value</p></td>
<td align="left"><p>The thread waits at IRQL equals DISPATCH_LEVEL and the Timeout is <strong>NULL</strong>. Callers of KeWaitForSingleObject or KeWaitForMultipleObjects can run at IRQL &lt;= DISPATCH_LEVEL. If a <strong>NULL</strong> pointer is supplied for Timeout, the calling thread remains in a wait state until the Object is signaled.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x122</p>
<p>(Windows 7 operating systems and later)</p></td>
<td align="left"><p>Address of the IRQL value</p></td>
<td align="left"><p>Address of the Object to wait on</p></td>
<td align="left"><p>Address of the Timeout value</p></td>
<td align="left"><p>The thread waits at DISPATCH_LEVEL and Timeout value is not equal to zero (0). If the Timeout != 0, the callers of KeWaitForSingleObject or KeWaitForMultipleObjects must run at IRQL &lt;= APC_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x123</p>
<p>(Windows 7 operating systems and later)</p></td>
<td align="left"><p>Address of the Object to wait on</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>The caller of KeWaitForSingleObject or KeWaitForMultipleObjects specified the wait as <strong>UserMode</strong>, but the Object is on the kernel stack.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x130</p>
<p>(Windows 7 operating systems and later)</p></td>
<td align="left"><p>Address of work item</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>The work item is in session address space. Work items are not allowed in session address space because they can be manipulated from another session or from system threads that have no session virtual address space.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x131</p>
<p>(Windows 7 operating systems and later)</p></td>
<td align="left"><p>Address of work item</p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>The work item is in pageable memory. Work items have to be in nonpageable memory because the kernel uses them at DISPATCH_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x135</p></td>
<td align="left"><p>Address of IRP</p></td>
<td align="left"><p>Number of milliseconds allowed between the [<strong>IoCancelIrp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548338) call and the completion for this IRP</p></td>
<td align="left"></td>
<td align="left"><p>The canceled IRP did not completed in the expected time The driver took longer than expected to complete the canceled IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x13A</p></td>
<td align="left"><p>Address of the pool block being freed</p></td>
<td align="left"><p>Incorrect value</p></td>
<td align="left"><p>Address of the incorrect value</p></td>
<td align="left"><p>The driver has called [<strong>ExFreePool</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544590) and Driver Verifier detects an error in one of the internal values that is used to track pool usage.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x13B</p></td>
<td align="left"><p>Address of the pool block being freed</p></td>
<td align="left"><p>Address of the incorrect value</p></td>
<td align="left"><p>Address of a pointer to the incorrect memory page</p></td>
<td align="left"><p>The driver has called [<strong>ExFreePool</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544590) and Driver Verifier detects an error in one of the internal values that is used to track pool usage.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x13C</p></td>
<td align="left"><p>Address of the pool block being freed</p></td>
<td align="left"><p>Incorrect value</p></td>
<td align="left"><p>Address of the incorrect value</p></td>
<td align="left"><p>The driver has called [<strong>ExFreePool</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544590) and Driver Verifier detects an error in one of the internal values that is used to track pool usage.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x13D</p></td>
<td align="left"><p>Address of the pool block being freed</p></td>
<td align="left"><p>Address of the incorrect value</p></td>
<td align="left"><p>Correct value that was expected</p></td>
<td align="left"><p>The driver has called [<strong>ExFreePool</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544590) and Driver Verifier detects an error in one of the internal values that is used to track pool usage.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x13E</p></td>
<td align="left"><p>Pool block address specified by the caller</p></td>
<td align="left"><p>Pool block address tracked by Driver Verifier</p></td>
<td align="left"><p>Pointer to the pool block address that is tracked by Driver Verifier</p></td>
<td align="left"><p>The pool block address specified by the caller of [<strong>ExFreePool</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544590) is different from the address tracked by Driver Verifier.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x13F</p></td>
<td align="left"><p>Address of the pool block being freed</p></td>
<td align="left"><p>Number of bytes being freed</p></td>
<td align="left"><p>Pointer to the number of bytes tracked by Driver Verifier</p></td>
<td align="left"><p>The number of bytes of memory being freed in the call to [<strong>ExFreePool</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544590) is different from the number of bytes tracked by Driver Verifier.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1000 (Windows XP and later operating systems only)</p></td>
<td align="left"><p>Address of the resource</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p><strong>Self-deadlock:</strong> The current thread has tried to recursively acquire a resource. A bug check with this parameter occurs only when the <strong>Deadlock Detection</strong> option of Driver Verifier is active.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1001 (Windows XP and later operating systems only)</p></td>
<td align="left"><p>Address of the resource that was the final cause of the deadlock</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p><strong>Deadlock:</strong> A lock hierarchy violation has been found. A bug check with this parameter occurs only when the <strong>Deadlock Detection</strong> option of Driver Verifier is active.</p>
<p>(Use the [<strong>!deadlock</strong>](-deadlock.md) extension for further information.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1002 (Windows XP and later operating systems only)</p></td>
<td align="left"><p>Address of the resource</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p><strong>Uninitialized resource:</strong> A resource has been acquired without having been initialized first. A bug check with this parameter occurs only when the <strong>Deadlock Detection</strong> option of Driver Verifier is active.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1003 (Windows XP and later operating systems only)</p></td>
<td align="left"><p>Address of the resource that is being released deadlocked</p></td>
<td align="left"><p>Address of the resource that should have been released first</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p><strong>Unexpected release:</strong> A resource has been released in an incorrect order. A bug check with this parameter occurs only when the <strong>Deadlock Detection</strong> option of Driver Verifier is active.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1004 (Windows XP and later operating systems only)</p></td>
<td align="left"><p>Address of the resource</p></td>
<td align="left"><p>Address of the thread that acquired the resource</p></td>
<td align="left"><p>Address of the current thread</p></td>
<td align="left"><p><strong>Unexpected thread:</strong> The wrong thread releases a resource. A bug check with this parameter occurs only when the <strong>Deadlock Detection</strong> option of Driver Verifier is active.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1005 (Windows XP and later operating systems only)</p></td>
<td align="left"><p>Address of the resource</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p><strong>Multiple initialization:</strong> A resource is initialized more than one time. A bug check with this parameter occurs only when the <strong>Deadlock Detection</strong> option of Driver Verifier is active.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1007 (Windows XP and later operating systems only)</p></td>
<td align="left"><p>Address of the resource</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p><strong>Unacquired resource:</strong> A resource is released before it has been acquired. A bug check with this parameter occurs only when the <strong>Deadlock Detection</strong> option of Driver Verifier is active.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1008</p>
<p>(Windows 7 operating systems and later)</p></td>
<td align="left"><p>Lock address</p></td>
<td align="left"><p>Driver Verifier internal data</p></td>
<td align="left"><p>Driver Verifier internal data</p></td>
<td align="left"><p>The driver tried to acquire a lock by using an API that is mismatched for this lock type.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1009</p>
<p>(Windows 7 operating systems and later)</p></td>
<td align="left"><p>Lock address</p></td>
<td align="left"><p>Driver Verifier internal data</p></td>
<td align="left"><p>Driver Verifier internal data</p></td>
<td align="left"><p>The driver tried to release a lock by using an API that is mismatched for this lock type.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x100A</p>
<p>(Windows 7 operating systems and later)</p></td>
<td align="left"><p>Owner thread address</p></td>
<td align="left"><p>Driver Verifier internal data</p></td>
<td align="left"></td>
<td align="left"><p>The terminated thread owns the lock.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x100B</p>
<p>(Windows 7 operating systems and later)</p></td>
<td align="left"><p>Lock address</p></td>
<td align="left"><p>Owner thread address</p></td>
<td align="left"><p>Driver Verifier internal address</p></td>
<td align="left"><p>The deleted lock is still owned by a thread.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xA001</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>A pointer to the <em>NetBufferList</em> object</p></td>
<td align="left"><p>A pointer to the virtual switch object (if NON-NULL)</p></td>
<td align="left"><p>Reserved (unused)</p></td>
<td align="left"><p>VM Switch: The <strong>SourceHandle</strong> for the caller-supplied <em>NetBufferList</em> must be set. See the [<em>AllocateNetBufferListForwardingContext</em>](https://msdn.microsoft.com/library/windows/hardware/hh598134) routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xA002</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>A pointer to the <em>NetBufferList</em> object</p></td>
<td align="left"><p>A pointer to the virtual switch object (if NON-NULL).</p></td>
<td align="left"><p>Reserved (unused)</p></td>
<td align="left"><p>VM Switch: The caller supplied NetBufferList's forwarding detail is not zero. See the [<em>AllocateNetBufferListForwardingContext</em>](https://msdn.microsoft.com/library/windows/hardware/hh598134) routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xA003</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>A pointer to the <em>NetBufferList</em> object</p></td>
<td align="left"><p>A pointer to the virtual switch object (if NON-NULL).</p></td>
<td align="left"><p>Reserved (unused)</p></td>
<td align="left"><p>VM Switch: The caller supplied a <em>NetBufferList</em> with packet header or routing context that is NULL. See [Packet Management Guidelines for the Extensible Switch Data Path](https://msdn.microsoft.com/library/windows/hardware/hh582270).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xA004</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>ID of invalid port</p></td>
<td align="left"><p>NIC Index</p></td>
<td align="left"><p>A pointer to the virtual switch object (if NON-NULL).</p></td>
<td align="left"><p>VM Switch: The caller specified an invalid Port and NIC index combination. See [Hyper-V Extensible Switch Port and Network Adapter States](https://msdn.microsoft.com/library/windows/hardware/hh598182).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xA005</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>A pointer to the <em>NetBufferList</em> object</p></td>
<td align="left"><p>A pointer to the Destination list.</p></td>
<td align="left"><p>A pointer to the virtual switch object (if NON-NULL).</p></td>
<td align="left"><p>VM Switch: The caller supplied an invalid destination. See [<em>AddNetBufferListDestination</em>](https://msdn.microsoft.com/library/windows/hardware/hh598133) and [<em>UpdateNetBufferListDestinations</em>](https://msdn.microsoft.com/library/windows/hardware/hh598303).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xA006</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>A pointer to the <em>NetBufferList</em> object</p></td>
<td align="left"><p>A pointer to the virtual switch object (if NON-NULL).</p></td>
<td align="left"><p>Reserved (unused)</p></td>
<td align="left"><p>VM Switch: The caller supplied an invalid source NIC or Port object. See [Hyper-V Extensible Switch Port and Network Adapter States](https://msdn.microsoft.com/library/windows/hardware/hh598182).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xA007</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>A pointer to the <em>NetBufferList</em> object</p></td>
<td align="left"><p>A pointer to the virtual switch object (if NON-NULL).</p></td>
<td align="left"><p>Reserved (unused)</p></td>
<td align="left"><p>VM Switch: The caller supplied an invalid destination list. See [<em>AddNetBufferListDestination</em>](https://msdn.microsoft.com/library/windows/hardware/hh598133) and [<em>UpdateNetBufferListDestinations</em>](https://msdn.microsoft.com/library/windows/hardware/hh598303).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xA008</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Parent NIC object</p></td>
<td align="left"><p>NIC index</p></td>
<td align="left"><p>A pointer to the virtual switch object (if NON-NULL).</p></td>
<td align="left"><p>VM Switch: Attempting to reference a NIC when not allowed. See [Hyper-V Extensible Switch Port and Network Adapter States](https://msdn.microsoft.com/library/windows/hardware/hh598182).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xA009</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Port being referenced</p></td>
<td align="left"><p>A pointer to the virtual switch object (if NON-NULL)</p></td>
<td align="left"><p>Reserved (unused)</p></td>
<td align="left"><p>VM Switch: Attempt to reference a port when not allowed. See [Hyper-V Extensible Switch Port and Network Adapter States](https://msdn.microsoft.com/library/windows/hardware/hh598182).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xA00A</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>A pointer to the <em>NetBufferList</em> object</p></td>
<td align="left"><p>ContextTypeInfo object</p></td>
<td align="left"><p>Reserved (unused)</p></td>
<td align="left"><p>VM Switch: Failure context is already set. See [<em>SetNetBufferListSwitchContext</em>](https://msdn.microsoft.com/library/windows/hardware/hh846223).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xA00B</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>A pointer to the <em>NetBufferList</em> object</p></td>
<td align="left"><p>NDIS_SWITCH_REPORT_FILTERED_NBL_FLAGS_*</p></td>
<td align="left"><p>A pointer to the virtual switch object (if NON-NULL)</p></td>
<td align="left"><p>VM Switch: Invalid direction provided for dropped NetBufferList. See [<em>ReportFilteredNetBufferLists</em>](https://msdn.microsoft.com/library/windows/hardware/hh598297).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xA00C</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>A pointer to the <em>NetBufferList</em> object</p></td>
<td align="left"><p>Send Flags value</p></td>
<td align="left"><p>A pointer to the virtual switch object (if NON-NULL)</p></td>
<td align="left"><p>VM Switch: NetBufferList chain has multiple source ports when NDIS_SEND_FLAGS_SWITCH_SINGLE_SOURCE flag is set. See [Hyper-V Extensible Switch Send and Receive Flags](https://msdn.microsoft.com/library/windows/hardware/hh598186).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xA00D</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>A pointer to the <em>NetBufferList</em> object</p></td>
<td align="left"><p>A pointer to the virtual switch context</p></td>
<td align="left"><p>A pointer to the virtual switch object (if NON-NULL)</p></td>
<td align="left"><p>VM Switch: One or more NetBufferLists in chain have invalid destination when NDIS_RECEIVE_FLAGS_SWITCH_DESTINATION_GROUP flag is set. See [Hyper-V Extensible Switch Send and Receive Flags](https://msdn.microsoft.com/library/windows/hardware/hh598186).</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>0x2000</p>
<p>(Windows 7 operating systems and later)</p></td>
<td align="left"><p>The first argument passed to the [<strong>StorPortInitialize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567108) routine. This parameter is a pointer to the driver object that the operating system passed to the miniport driver in the first argument of the miniport driver's [<em>DriverEntry</em>](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine.</p></td>
<td align="left"><p>The second argument passed to the [<strong>StorPortInitialize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567108) routine. This parameter is a pointer to context information that the operating system passed to the miniport driver in the second argument of the miniport driver's [<em>DriverEntry</em>](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine.</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The Storport miniport driver passed a bad argument (a <strong>NULL</strong> pointer) to the [<strong>StorPortInitialize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567108) routine.</p>
<p></p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00020002</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlApcLte](https://msdn.microsoft.com/library/windows/hardware/ff547740). The rule specifies that the driver must call [<strong>ObGetObjectSecurity</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557738) and [<strong>ObReleaseObjectSecurity</strong>](https://msdn.microsoft.com/library/windows/hardware/ff558695) only when IRQL &lt;= APC_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00020003</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlDispatch](https://msdn.microsoft.com/library/windows/hardware/ff547743). The IrqlDispatch rule specifies that the driver must call certain routines only when IRQL = DISPATCH_LEVEL</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00020004</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlExAllocatePool](https://msdn.microsoft.com/library/windows/hardware/ff547747). The IrqlExAllocatePool rule specifies that the driver calls [<strong>ExAllocatePoolWithTag</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544520) and [<strong>ExAllocatePoolWithTagPriority</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544523) only when at IRQL&lt;=DISPATCH_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00020005</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlExApcLte1](https://msdn.microsoft.com/library/windows/hardware/ff547748). The IrqlExApcLte1 rule specifies that the driver calls ExAcquireFastMutex and ExTryToAcquireFastMutex only at IRQL &lt;= APC_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00020006</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlExApcLte2](https://msdn.microsoft.com/library/windows/hardware/ff547751). The IrqlExApcLte2 rule specifies that the driver calls certain routines only when IRQL &lt;= APC_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00020007</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlExApcLte3](https://msdn.microsoft.com/library/windows/hardware/ff547753). The IrqlExApcLte3 rule specifies that the driver must call certain executive support routines only when IRQL &lt;= APC_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00020008</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlExPassive](https://msdn.microsoft.com/library/windows/hardware/ff547756). The IrqlExPassive rule specifies that the driver must call certain executive support routines only when IRQL = PASSIVE_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00020009</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlIoApcLte](https://msdn.microsoft.com/library/windows/hardware/ff547759). The IrqlIoApcLte rule specifies that the driver must call certain I/O manager routines only when IRQL &lt;= APC_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0002000A</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlIoPassive1](https://msdn.microsoft.com/library/windows/hardware/ff547763). The IrqlIoPassive1 rule specifies that the driver must call certain I/O manager routines only when IRQL = PASSIVE_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0002000B</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlIoPassive2](https://msdn.microsoft.com/library/windows/hardware/ff547766). The IrqlIoPassive2 rule specifies that the driver must call certain I/O manager routines only when IRQL = PASSIVE_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0002000C</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlIoPassive3](https://msdn.microsoft.com/library/windows/hardware/ff547780). The IrqlIoPassive3 rule specifies that the driver must call certain I/O manager routines only when IRQL = PASSIVE_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0002000D</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlIoPassive4](https://msdn.microsoft.com/library/windows/hardware/ff547787). The IrqlIoPassive4 rule specifies that the driver must call certain I/O manager routines only when IRQL = PASSIVE_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0002000E</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlIoPassive5](https://msdn.microsoft.com/library/windows/hardware/ff547796). The IrqlIoPassive5 rule specifies that the driver must call certain I/O manager routines only when IRQL = PASSIVE_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0002000F</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlKeApcLte1](https://msdn.microsoft.com/library/windows/hardware/ff547803). The IrqlKeApcLte1 rule specifies that the driver must call certain kernel routines only when IRQL &lt;= APC_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00020010</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlKeApcLte2](https://msdn.microsoft.com/library/windows/hardware/ff547806). The IrqlKeApcLte2 rule specifies that the driver must call certain kernel routines only when IRQL &lt;= APC_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00020011</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlKeDispatchLte](https://msdn.microsoft.com/library/windows/hardware/ff547812). The IrqlKeDispatchLte rule specifies that the driver must call certain kernel routines only when IRQL &lt;= DISPATCH_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00020015</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlKeReleaseSpinLock](https://msdn.microsoft.com/library/windows/hardware/ff547830). The IrqlKeReleaseSpinLock rule specifies that the driver must call KeReleaseSpinLock only when IRQL = DISPATCH_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00020016</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlKeSetEvent](https://msdn.microsoft.com/library/windows/hardware/ff547835). The IrqlKeSetEvent rule specifies that the [<strong>KeSetEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553253) routine is only called at IRQL &lt;= DISPATCH_LEVEL when Wait is set to FALSE, and at IRQL &lt;= APC_LEVEL when Wait is set to TRUE.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00020019</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlMmApcLte](https://msdn.microsoft.com/library/windows/hardware/ff547855). The IrqlMmApcLte rule specifies that the driver must call certain memory manager routines only when IRQL &lt;= APC_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0002001A</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [<strong>IrqlMmDispatch</strong>](https://msdn.microsoft.com/library/windows/hardware/hh975186). The <strong>IrqlMmDispatch</strong> rule specifies that the driver must call [<strong>MmFreeContiguousMemory</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554503) only when IRQL = DISPATCH_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0002001B</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlObPassive](https://msdn.microsoft.com/library/windows/hardware/ff547873). The IrqlObPassive rule specifies that the driver must call [<strong>ObReferenceObjectByHandle</strong>](https://msdn.microsoft.com/library/windows/hardware/ff558679) only when IRQL = PASSIVE_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0002001C</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlPsPassive](https://msdn.microsoft.com/library/windows/hardware/ff547882). The IrqlPsPassive rule specifies that the driver must call certain process and thread manager routines only when IRQL = PASSIVE_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0002001D</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [<strong>IrqlReturn</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547886).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0002001E</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlRtlPassive](https://msdn.microsoft.com/library/windows/hardware/ff547893). The IrqlRtlPassive rule specifies that the driver must call [<strong>RtlDeleteRegistryValue</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561829) only when IRQL = PASSIVE_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0002001F</p>
<p>(Windows 8 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Optional pointer to the rule state variable(s).</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [IrqlZwPassive](https://msdn.microsoft.com/library/windows/hardware/ff547897). The IrqlZwPassive rule specifies that the driver must call [<strong>ZwClose</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566417) only when IRQL = PASSIVE_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00020022</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Reserved (unused)</p></td>
<td align="left"><p>Reserved (unused)</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [<strong>IrqlIoDispatch</strong>](https://msdn.microsoft.com/library/windows/hardware/jj157234).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00040003</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [<strong>CriticalRegions</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543603).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00040006</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [<strong>QueuedSpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551494).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00040007</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [<strong>QueuedSpinLockRelease</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551496).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00040009</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [<strong>SpinLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551861).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0004000B</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [<strong>SpinlockRelease</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552780).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0004000E</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [<strong>GuardedRegions</strong>](https://msdn.microsoft.com/library/windows/hardware/hh975150).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0004100B</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [<strong>RequestedPowerIrp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551613).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0004100F</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [<strong>IoSetCompletionExCompleteIrp</strong>](https://msdn.microsoft.com/library/windows/hardware/hh975178).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00043006</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [<strong>PnpRemove</strong>](https://msdn.microsoft.com/library/windows/hardware/dn322052).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00091001</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [<strong>NdisOidComplete</strong>](https://msdn.microsoft.com/library/windows/hardware/dn305115).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00091002</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [<strong>NdisOidDoubleComplete</strong>](https://msdn.microsoft.com/library/windows/hardware/dn305116).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0009100E</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the DDI compliance rule [<strong>NdisOidDoubleRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/dn305117).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00092003</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the NDIS/WIFI verification rule [<strong>NdisTimedOidComplete</strong>](https://msdn.microsoft.com/library/windows/hardware/dn305120).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0009200D</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the NDIS/WIFI verification rule [<strong>NdisTimedDataSend</strong>](https://msdn.microsoft.com/library/windows/hardware/dn305119).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0009200F</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the NDIS/WIFI verification rule [<strong>NdisTimedDataHang</strong>](https://msdn.microsoft.com/library/windows/hardware/dn305118).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00093004</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the NDIS/WIFI verification rule [<strong>WlanAssociation</strong>](https://msdn.microsoft.com/library/windows/hardware/dn305122).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00093005</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the NDIS/WIFI verification rule [<strong>WlanConnectionRoaming</strong>](https://msdn.microsoft.com/library/windows/hardware/dn305123).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00093006</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the NDIS/WIFI verification rule [<strong>WlanDisassociation</strong>](https://msdn.microsoft.com/library/windows/hardware/dn305124).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00094007</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the NDIS/WIFI verification rule [<strong>WlanTimedAssociation</strong>](https://msdn.microsoft.com/library/windows/hardware/dn305125).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00094008</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the NDIS/WIFI verification rule [<strong>WlanTimedConnectionRoaming</strong>](https://msdn.microsoft.com/library/windows/hardware/dn305126).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00094009</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the NDIS/WIFI verification rule [<strong>WlanTimedConnectRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/dn305127).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0009400B</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the NDIS/WIFI verification rule [<strong>WlanTimedLinkQuality</strong>](https://msdn.microsoft.com/library/windows/hardware/dn305128).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0009400C</p>
<p>(Windows 8.1 operating systems and later)</p></td>
<td align="left"><p>Pointer to the string that describes the violated rule condition.</p></td>
<td align="left"><p>Address of internal rule state (second argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>Address of supplemental states (third argument to <strong>!ruleinfo</strong>).</p></td>
<td align="left"><p>The driver violated the NDIS/WIFI verification rule [<strong>WlanTimedScan</strong>](https://msdn.microsoft.com/library/windows/hardware/dn305129).</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

See the description of each code in the Parameters section for a description of the cause. Further information can be obtained by using the [**!analyze -v**](-analyze.md) extension.

Resolution
----------

This bug check can only occur when Driver Verifier has been instructed to monitor one or more drivers. If you did not intend to use Driver Verifier, you should deactivate it. You might also consider removing the driver that caused this problem.

If you are the driver writer, use the information obtained through this bug check to fix the bugs in your code.

For full details on Driver Verifier, see the [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) section of the Windows Driver Kit (WDK).

Remarks
-------

The \_POOL\_TYPE codes are enumerated in Ntddk.h. In particular, **0** (zero) indicates nonpaged pool and **1** (one) indicates paged pool.

*(Windows 8 and later versions of Windows)* If [DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208) causes a bug check, run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) on the driver source code and specify the DDI compliance rule (identified by the parameter 1 value) that caused the bug check. Static Driver Verifier can help you locate the cause of the problem in your source code.

## <span id="see_also"></span>See also


[Handling a Bug Check When Driver Verifier is Enabled](handling-a-bug-check-when-driver-verifier-is-enabled.md)

 

 




