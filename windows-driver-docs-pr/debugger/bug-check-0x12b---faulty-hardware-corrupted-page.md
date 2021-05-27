---
title: Bug Check 0x12B FAULTY_HARDWARE_CORRUPTED_PAGE
description: The FAULTY_HARDWARE_CORRUPTED_PAGE bug check has a value of 0x0000012B. This bug check indicates that the Windows memory manager detected corruption, and the corruption could only have been caused by a component accessing memory using physical addressing. 
keywords: ["Bug Check 0x12B FAULTY_HARDWARE_CORRUPTED_PAGE", "FAULTY_HARDWARE_CORRUPTED_PAGE"]
ms.date: 01/18/2019
topic_type:
- apiref
api_name:
- FAULTY_HARDWARE_CORRUPTED_PAGE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x12B: FAULTY\_HARDWARE\_CORRUPTED\_PAGE

The FAULTY\_HARDWARE\_CORRUPTED\_PAGE bug check has a value of 0x0000012B. This bug check indicates that the Windows memory manager detected corruption, and the corruption could only have been caused by a component accessing memory using physical addressing.  

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## FAULTY\_HARDWARE\_CORRUPTED\_PAGE Parameters

There are two scenarios where the Memory Manager will raise FAULTY_HARDWARE_CORRUPTED_PAGE bug checks, with two different sets of parameters. 

If parameters 3 and 4 are both zero, the bug check indicates that Memory Manager detected a single-bit error on a page that was expected to be zeroed.

If parameters 3 and 4 are non-zero, the bug check is raised by the Compressed Store Manager due to a failure to decompress a page due to physical memory corruption.


### Memory Manager Page Not Zero Error Parameters 

This bug check indicates that a single-bit error was found in this page. This is a hardware memory error.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>Virtual address maps to the corrupted page</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Physical page number</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Zero</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Zero</p></td>
</tr>
</tbody>
</table>


### Compressed Store Manager Error Parameters 

 This bug check indicates that a store manager memory error has occurred. It may be an authentication failure, a CRC failure, or a decompression failure.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>FailStatus - Indicates the type of failure</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The CompressedSize of the page that is being read</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Source Buffer</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Target Buffer</p></td>
</tr>
</tbody>
</table>


## ## Cause

This bugcheck can only occur by memory corruption due to physical memory access. The causes for physical memory corruption include:

1. Defective RAM hardware
2. A driver or device incorrectly modifying physical pages via an incorrect DMA operation or associated MDL.
3. Corruption caused by a hardware device or firmware corrupting memory, such as firmware illegally modifying physical pages across a power transition.

NOTE:  Compressed Store Manager can detect if the corruption was caused by a single-bit error, and automatically corrects this condition without raising a bug check. This bugcheck is reported by the Compressed Store Manager if the corruption was not caused by a single bit error.

For more information on Windows memory manager and memory compression, see [Windows Internals 7th Edition Part 1](/sysinternals/resources/windows-internals) by  Pavel Yosifovich, Mark E. Russinovich, David A. Solomon and Alex Ionescu.

## Resolution
-----

**Windows Memory Diagnostics Tool**

To investigate if this bug check is caused by defective RAM hardware, run the Windows Memory Diagnostics tool. In the control panel search box, type Memory, and then select *Diagnose your computer's memory problems*.‌ After the test is run, use Event viewer to view the results under the System log. Look for the *MemoryDiagnostics-Results* entry to view the results.

## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)

[Windows Kernel-Mode Memory Manager](../kernel/windows-kernel-mode-memory-manager.md)

[Channel 9 video on memory compression](https://channel9.msdn.com/Blogs/Seth-Juarez/Memory-Compression-in-Windows-10-RTM)
