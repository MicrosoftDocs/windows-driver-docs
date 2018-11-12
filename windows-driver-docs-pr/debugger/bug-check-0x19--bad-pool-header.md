---
title: Bug Check 0x19 BAD_POOL_HEADER
description: The BAD_POOL_HEADER bug check has a value of 0x00000019. This indicates that a pool header is corrupt.
ms.assetid: a3e84703-d778-426b-80e6-e143f5d8f869
keywords: ["(Developer Content) Bug Check 0x19 BAD_POOL_HEADER", "BAD_POOL_HEADER"]
ms.author: domars
ms.date: 12/07/2017
topic_type:
- apiref
api_name:
- BAD_POOL_HEADER
api_type:
- NA
ms.localizationpriority: medium
---

# (Developer Content) Bug Check 0x19: BAD\_POOL\_HEADER


The BAD\_POOL\_HEADER bug check has a value of 0x00000019. This indicates that a pool header is corrupt.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## BAD\_POOL\_HEADER Parameters


Parameter 1 indicates the type of violation. The meaning of the other parameters depends on the value of Parameter 1.

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
<td align="left"><p>0x2</p></td>
<td align="left"><p>The pool entry being checked</p></td>
<td align="left"><p>The size of the pool block</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The special pool pattern check failed.</p>
<p>(The owner has likely corrupted the pool block.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3</p></td>
<td align="left"><p>The pool entry being checked</p></td>
<td align="left"><p>The read-back <strong>flink</strong> freelist value</p></td>
<td align="left"><p>The read-back <strong>blink</strong> freelist value</p></td>
<td align="left"><p>The pool freelist is corrupt.</p>
<p>(In a healthy list, the values of Parameters 2, 3, and 4 should be identical.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x5</p></td>
<td align="left"><p>One of the pool entries</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The other pool entry</p></td>
<td align="left"><p>A pair of adjacent pool entries have headers that contradict each other. At least one of them is corrupt.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x6</p></td>
<td align="left"><p>One incorrectly-calculated entry</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The bad entry that caused the miscalculation</p></td>
<td align="left"><p>The pool block header&#39;s previous size is too large.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x7</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The bad pool entry</p></td>
<td align="left"><p>The pool block header size is corrupt.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x8</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The bad pool entry</p></td>
<td align="left"><p>The pool block header size is zero.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x9</p></td>
<td align="left"><p>One incorrectly-calculated entry</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The bad entry that caused the miscalculation</p></td>
<td align="left"><p>The pool block header size is corrupted (it is too large).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xA</p></td>
<td align="left"><p>The pool entry that should have been found</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The virtual address of the page that should have contained the pool entry</p></td>
<td align="left"><p>The pool block header size is corrupt.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xD, 0xE, 0xF, 0x23, 0x24, 0x25</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The pool header of a freed block has been modified after it was freed. This is not typically the fault of the prior owner of the freed block; instead it is usually (but not always) due to the block preceding the freed block being overrun.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x20</p></td>
<td align="left"><p>The pool entry that should have been found</p></td>
<td align="left"><p>The next pool entry</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The pool block header size is corrupt.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0X21</p></td>
<td align="left"><p>The pool pointer being freed</p></td>
<td align="left"><p>The number of bytes allocated for the pool block</p></td>
<td align="left"><p>The corrupted value found following the pool block</p></td>
<td align="left"><p>The data following the pool block being freed is corrupt. Typically this means the consumer (call stack) has overrun the block.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0X22</p></td>
<td align="left"><p>The address being freed</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>An address being freed does not have a tracking entry. This is usually because the call stack is trying to free a pointer that either has already been freed or was never allocated to begin with.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The pool is already corrupted at the time of the current request.

This may or may not be due to the caller.

Resolution
----------

The internal pool links must be walked using the kernel debugger to figure out a possible cause of the problem.

Then you can use special pool for the suspect pool tags, or use Driver Verifier "Special Pool" option on the suspect driver. The [**!analyze**](-analyze.md) extension may be of help in pinpointing the suspect driver, but this is frequently not the case with pool corrupters.

Use the steps described in [**Blue Screen Data**](blue-screen-data.md) to gather the Stop Code Parameters. Use the stop code parameters to determine the specific type of code behavior you are working to track down.

**Driver Verifier**

Driver Verifier is a tool that runs in real time to examine the behavior of drivers. If it see errors in the execution of driver code, it proactively creates an exception to allow that part of the driver code to be further scrutinized. The driver verifier manager is built into Windows and is available on all Windows PCs. To start the driver verifier manager, type *Verifer* at a command prompt. You can configure which drivers you would like to verify. The code that verifies drivers adds overhead as it runs, so try and verify the smallest number of drivers as possible. For more information, see [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448).

**Windows Memory Diagnostics**

If this Bug Check appears inconsistently, it could be related to faulty physical memory.

Run the Windows Memory Diagnostics tool, to test the memory. In the control panel search box, type Memory, and then click **Diagnose your computer's memory problems**.‌ After the test is run, use Event viewer to view the results under the System log. Look for the *MemoryDiagnostics-Results* entry to view the results.

 

 




