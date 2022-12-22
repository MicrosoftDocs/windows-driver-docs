---
title: Bug Check 0x12B FAULTY_HARDWARE_CORRUPTED_PAGE
description: Learn how the FAULTY_HARDWARE_CORRUPTED_PAGE bug check indicates the memory manager detected corruption caused by a component accessing memory using physical addressing. 
keywords: ["Bug Check 0x12B FAULTY_HARDWARE_CORRUPTED_PAGE", "FAULTY_HARDWARE_CORRUPTED_PAGE"]
ms.date: 12/15/2022
topic_type:
- apiref
api_name:
- FAULTY_HARDWARE_CORRUPTED_PAGE
api_type:
- NA
---

# Bug check 0x12B: FAULTY_HARDWARE_CORRUPTED_PAGE

The FAULTY_HARDWARE_CORRUPTED_PAGE bug check has a value of 0x0000012B. This bug check indicates that the Windows memory manager detected corruption. That corruption could only have been caused by a component accessing memory using physical addressing.  

> [!IMPORTANT]
> This topic is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## FAULTY_HARDWARE_CORRUPTED_PAGE parameters

There are two scenarios where the memory manager raises FAULTY_HARDWARE_CORRUPTED_PAGE bug checks, with two different sets of parameters.

If parameters 3 and 4 are both zero, the bug check indicates that the memory manager detected a single-bit error on a page that the memory manager expected to be zeroed.

If parameters 3 and 4 are non-zero, the bug check is raised by the Compressed Store Manager due to a failure to decompress a page due to physical memory corruption.

### Memory manager page not zero error parameters

This bug check indicates that a single-bit error was found in this page. This error is a hardware memory error.

| Parameter | Description |
|---|---|
| 1 | Virtual address maps to the corrupted page |
| 2 | Physical page number |
| 3 | Zero |
| 4 | Zero |

### Compressed Store Manager error parameters

 This bug check indicates that a store manager memory error has occurred. It might be an authentication failure, a CRC failure, or a decompression failure.

| Parameter | Description |
|---|---|
| 1 | FailStatus - Indicates the type of failure |
| 2 | The CompressedSize of the page that's being read |
| 3 | Source Buffer |
| 4 | Target Buffer |

## Cause

This bug check can only occur by memory corruption due to physical memory access. The causes for physical memory corruption include:

- Defective RAM hardware.
- A driver or device incorrectly modifying physical pages via an incorrect DMA operation or associated MDL.
- Corruption caused by a hardware device or firmware corrupting memory, such as firmware illegally modifying physical pages across a power transition.

> [!NOTE]
> Compressed Store Manager can detect if the corruption was caused by a single-bit error and automatically corrects this condition without raising a bug check. This bug check is reported by the Compressed Store Manager if the corruption wasn't caused by a single bit error.

For more information on Windows memory manager and memory compression, see [Windows Internals 7th Edition Part 1](/sysinternals/resources/windows-internals).

## Resolution
-----

To investigate if this bug check is caused by defective RAM hardware, run the Windows Memory Diagnostics tool. In the control panel search box, enter **Memory**, and then select **Diagnose your computer's memory problems**.‌ After the test is run, use the Event Viewer to view the results under the system log. Select the **MemoryDiagnostics-Results** entry to view the results.

## See also

- [Bug Check code reference](bug-check-code-reference2.md)

- [Windows kernel-mode memory manager](../kernel/windows-kernel-mode-memory-manager.md)
