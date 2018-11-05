---
title: Bug Check 0xC2 BAD_POOL_CALLER
description: The BAD_POOL_CALLER bug check has a value of 0x000000C2. This indicates that the current thread is making a bad pool request.
ms.assetid: 64803335-ab93-4c4d-9b30-2ec15a13303f
keywords: ["(Developer Content) Bug Check 0xC2 BAD_POOL_CALLER", "BAD_POOL_CALLER"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- BAD_POOL_CALLER
api_type:
- NA
ms.localizationpriority: medium
---

# (Developer Content) Bug Check 0xC2: BAD\_POOL\_CALLER


The BAD\_POOL\_CALLER bug check has a value of 0x000000C2. This indicates that the current thread is making a bad pool request.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## BAD\_POOL\_CALLER Parameters


**Parameter 1** indicates the type of violation.

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
<td align="left"><p>0</p></td>
<td align="left"><p>Pool type</p></td>
<td align="left"><p>Pool tag</p></td>
<td align="left"><p>The current thread requested a zero-byte pool allocation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x01,</p>
<p>0x02,</p>
<p>0x04</p></td>
<td align="left"><p>Pointer to pool header</p></td>
<td align="left"><p>First part of pool header contents</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The pool header has been corrupted.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x06</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Pointer to pool header</p></td>
<td align="left"><p>Pool header contents</p></td>
<td align="left"><p>The current thread attempted to free the pool, which was already freed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x07</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Pool header contents</p></td>
<td align="left"><p>Address of the block of pool being freed</p></td>
<td align="left"><p>The current thread attempted to free the pool, which was already freed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x08</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Pool type</p></td>
<td align="left"><p>Size of allocation, in bytes</p></td>
<td align="left"><p>The current thread attempted to allocate the pool at an invalid IRQL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x09</p></td>
<td align="left"><p>Current IRQL</p></td>
<td align="left"><p>Pool type</p></td>
<td align="left"><p>Address of pool</p></td>
<td align="left"><p>The current thread attempted to free the pool at an invalid IRQL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0A</p></td>
<td align="left"><p>Address of pool</p></td>
<td align="left"><p>Allocator&#39;s tag</p></td>
<td align="left"><p>Tag being used in the attempted free</p></td>
<td align="left"><p>The current thread attempted to free pool memory by using the wrong tag.</p>
<p>(The memory might belong to another component.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0B,</p>
<p>0x0C,</p>
<p>or 0x0D</p></td>
<td align="left"><p>Address of pool</p></td>
<td align="left"><p>Pool allocation&#39;s tag</p></td>
<td align="left"><p>Bad quota process pointer</p></td>
<td align="left"><p>The current thread attempted to release a quota on a corrupted pool allocation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x40</p></td>
<td align="left"><p>Starting address</p></td>
<td align="left"><p>Start of system address space</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The current thread attempted to free the kernel pool at a user-mode address.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x41</p></td>
<td align="left"><p>Starting address</p></td>
<td align="left"><p>Physical page frame</p></td>
<td align="left"><p>Highest physical page frame</p></td>
<td align="left"><p>The current thread attempted to free a non-allocated nonpaged pool address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x42</p>
<p>or 0x43</p></td>
<td align="left"><p>Address being freed</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The current thread attempted to free a virtual address that was never in any pool.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x44</p></td>
<td align="left"><p>Starting address</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The current thread attempted to free a non-allocated nonpaged pool address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x46</p></td>
<td align="left"><p>Starting address</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The current thread attempted to free an invalid pool address.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x47</p></td>
<td align="left"><p>Starting address</p></td>
<td align="left"><p>Physical page frame</p></td>
<td align="left"><p>Highest physical page frame</p></td>
<td align="left"><p>The current thread attempted to free a non-allocated nonpaged pool address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x48</p></td>
<td align="left"><p>Starting address</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The current thread attempted to free a non-allocated paged pool address.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x50</p></td>
<td align="left"><p>Starting address</p></td>
<td align="left"><p>Start offset, in pages, from beginning of paged pool</p></td>
<td align="left"><p>Size of paged pool, in bytes</p></td>
<td align="left"><p>The current thread attempted to free a non-allocated paged pool address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x60</p></td>
<td align="left"><p>Starting address</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The current thread attempted to free an invalid contiguous memory address.</p>
<p>(The caller of <strong>MmFreeContiguousMemory</strong> is passing a bad pointer.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x99</p></td>
<td align="left"><p>Address that is being freed</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The current thread attempted to free pool with an invalid address.</p>
<p>(This code can also indicate corruption in the pool header.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x9A</p></td>
<td align="left"><p>Pool type</p></td>
<td align="left"><p>Number of bytes requested</p></td>
<td align="left"><p>Pool tag</p></td>
<td align="left"><p>The current thread marked an allocation request MUST_SUCCEED.</p>
<p>(This pool type is no longer supported.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x9B</p></td>
<td align="left"><p>Pool type</p></td>
<td align="left"><p>Number of bytes requested</p></td>
<td align="left"><p>Caller&#39;s address</p></td>
<td align="left"><p>The current thread attempted to allocate a pool with a tag of 0</p>
<p>(This would be untrackable, and possibly corrupt the existing tag tables.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x9C</p></td>
<td align="left"><p>Pool type</p></td>
<td align="left"><p>Number of bytes requested</p></td>
<td align="left"><p>Caller&#39;s address</p></td>
<td align="left"><p>The current thread attempted to allocate a pool with a tag of &quot;BIG&quot;.</p>
<p>(This would be untrackable and could possibly corrupt the existing tag tables.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x9D</p></td>
<td align="left"><p>Incorrect pool tag used</p></td>
<td align="left"><p>Pool type</p></td>
<td align="left"><p>Caller&#39;s address</p></td>
<td align="left"><p>The current thread attempted to allocate a pool with a tag that does not contain any letters or digits. Using such tags makes tracking pool issues difficult.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x41286</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Start offset from the beginning of the paged pool, in pages</p></td>
<td align="left"><p>The current thread attempted to free a paged pool address in the middle of an allocation.</p></td>
</tr>
</tbody>
</table>

 

The \_POOL\_TYPE codes are enumerated in Ntddk.h. In particular, 0 indicates nonpaged pool and 1 indicates paged pool.

Cause
-----

An invalid pool request has been made by the current thread. Typically this is at a bad IRQL level or double freeing the same memory allocation, etc.

Resolution
----------

Activate Driver Verifier with memory pool options enabled, to obtain more information about these errors and to locate the faulting driver.

**Driver Verifier**

Driver Verifier is a tool that runs in real time to examine the behavior of drivers. If it see errors in the execution of driver code, it proactively creates an exception to allow that part of the driver code to be further scrutinized. The driver verifier manager is built into Windows and is available on all Windows PCs. To start the driver verifier manager, type *Verifer* at a command prompt. You can configure which drivers you would like to verify. The code that verifies drivers adds overhead as it runs, so try and verify the smallest number of drivers as possible. For more information, see [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448).

**Windows Memory Diagnostics**

In particular, for situations with memory pool corruption, run the Windows Memory Diagnostics tool, to try and isolate the physical memory as a cause. In the control panel search box, type Memory, and then click **Diagnose your computer's memory problems**.‌ After the test is run, use Event viewer to view the results under the System log. Look for the *MemoryDiagnostics-Results* entry to view the results.

 

 




