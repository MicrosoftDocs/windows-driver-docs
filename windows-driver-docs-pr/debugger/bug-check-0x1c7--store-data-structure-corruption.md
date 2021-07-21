---
title: Bug Check 0x1C7 STORE_DATA_STRUCTURE_CORRUPTION
description: The STORE_DATA_STRUCTURE_CORRUPTION bug check has a value of 0x000001C7. It indicates that the store component detected a corruption in its data structures.
keywords: ["Bug Check 0x1C7 STORE_DATA_STRUCTURE_CORRUPTION", "STORE_DATA_STRUCTURE_CORRUPTION"]
ms.date: 01/28/2019
topic_type:
- apiref
api_name:
- STORE_DATA_STRUCTURE_CORRUPTION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1C7: STORE\_DATA\_STRUCTURE\_CORRUPTION

The STORE\_DATA\_STRUCTURE\_CORRUPTION bug check has a value of 0x000001C7. It indicates that the store component detected a corruption in its data structures.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

 

## STORE\_DATA\_STRUCTURE\_CORRUPTION Parameters

|Parameter|Description|
|-------- |---------- |
|1|Corruption ID. See values below. |
|2| See values below. |
|3| See values below. |
|4| See values below. |


**Corruption ID**

```text
 0x0 : A chunk heap buffer's hash doesn't match.
    2 - Chunk heap buffer whose hash didn't match.
    3 - Expected buffer hash.
    4 - Page frame number of the corrupted page.

 0x1 : An unhandled exception occurred on the store thread and a chunk heap buffer's hash doesn't match, which is likely the source of the exception.
    2 - Chunk heap buffer whose hash didn't match.
    3 - Expected buffer hash.
    4 - Page frame number of the corrupted page.

 0x2 : Page data appears corrupt during a read and the corresponding page record's heap buffer hash doesn't match.
    2 - Chunk heap buffer whose hash didn't match containing the page record of the data being read.
    3 - Expected buffer hash.
    4 - Page frame number of the corrupted page.
 
 0x3 : Page data appears corrupt during a read and the corresponding page record has changed since the start of the read operation.
    2 - Pointer to the page location information snapped from the page record that was found when the read was initiated.
    3 - Pointer to the page record currently in the page tree for the same page key.
    4 - Reserved.
```

## ## Cause

The store component detected a corruption in its data structures.

This bugcheck can occur by memory corruption due to physical memory access. The causes for physical memory corruption include:

1.	Defective RAM hardware
2.	A driver or device incorrectly modifying physical pages via an incorrect DMA operation or associated MDL.
3.	Corruption caused by a hardware device or firmware corrupting memory, such as firmware illegally modifying physical pages across a power transition.

For more information on Windows memory manager, see [Windows Internals 7th Edition Part 1](/sysinternals/resources/windows-internals) by  Pavel Yosifovich, Mark E. Russinovich, David A. Solomon and Alex Ionescu.

## Resolution
-----

**Windows Memory Diagnostics Tool**

To investigate if this bug check is caused by defective RAM hardware, run the Windows Memory Diagnostics tool. In the control panel search box, type Memory, and then select *Diagnose your computer's memory problems*.‌ After the test is run, use Event viewer to view the results under the System log. Look for the *MemoryDiagnostics-Results* entry to view the results.

## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)

[Windows Kernel-Mode Memory Manager](../kernel/windows-kernel-mode-memory-manager.md)