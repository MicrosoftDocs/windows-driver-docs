---
title: No-Execute (NX) Nonpaged Pool
description: As a best practice, drivers for Windows 8 and later versions of Windows should allocate most or all of their nonpaged memory from the no-execute (NX) nonpaged pool.
ms.assetid: E5BF34F6-ABA0-4EC7-B740-CC83EF8438CF
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# No-Execute (NX) Nonpaged Pool


As a best practice, drivers for Windows 8 and later versions of Windows should allocate most or all of their nonpaged memory from the no-execute (NX) nonpaged pool. By allocating memory from NX nonpaged pool, a kernel-mode driver improves security by preventing malicious software from executing instructions in this memory.

Starting with Windows 8, kernel-mode drivers can allocate memory from a pool of NX nonpaged memory. This pool is managed by a general-purpose, kernel-mode memory allocator that operates similarly to the user-mode Win32 heap allocator. The memory in this pool is NX and nonpaged. The x86, x64, and ARM processor architectures enable memory pages to be designated as NX to prevent the execution of instructions in these pages. Typically, a kernel-mode driver uses memory allocated from nonpaged pool to store data, and does not require the ability to execute instructions in this memory.

## Support for Legacy Drivers


In Windows 7 and earlier versions of Windows, all memory allocated from the nonpaged pool is executable. To encourage porting of these drivers to use NX nonpaged pool in Windows 8 and later versions of Windows, Microsoft provides several opt-in mechanisms to enable developers to update their drivers with minimal effort. For more information, see [NX Pool Opt-In Mechanisms](nx-pool-opt-in-mechanisms.md).

For backward compatibility, driver binaries that run on Windows 7 and earlier versions of Windows, and that allocate memory from the executable nonpaged pool, will run on Windows 8 and later versions of Windows without modification. However, these drivers do not take advantage of the improved security of the NX nonpaged pool.

 

 




