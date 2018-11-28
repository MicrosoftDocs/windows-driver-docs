---
title: Buffer Handling
description: Buffer Handling
ms.assetid: 0739ff35-2915-4237-9fe0-11559eccb0bb
keywords:
- security WDK file systems , minimizing threats
- buffers WDK file systems
- paged buffers WDK file systems
- non-paged buffers WDK file systems
- bug check WDK file systems
- address validation WDK file systems
- fast I/O WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Buffer Handling


## <span id="ddk_buffer_handling_if"></span><span id="DDK_BUFFER_HANDLING_IF"></span>


Perhaps the most common error within any driver relates to buffer handling where buffers are invalid or too small. These errors can allow buffer overflows or cause system crashes, which constitute security compromises for the system.

From the perspective of a driver, buffers come in one of two varieties:

-   Paged buffers, which may or may not be resident in memory.

-   Non-paged buffers, which must be resident in memory.

Of course, an invalid address is neither paged nor nonpaged, but as the operating system begins to work toward resolving the page fault such a buffer causes, it will isolate the invalid address into one of the "standard" address ranges (paged kernel addresses, non-paged kernel addresses, or user addresses) and raise the appropriate type of error. Buffer errors are always handled either by a bug check (PAGE\_FAULT\_IN\_NONPAGED\_AREA, for example) or by an exception (STATUS\_ACCESS\_VIOLATION, for example). In the case of a bug check, the system will halt operation. In the case of an exception, the stack-based exception handlers will be invoked, and if none of them handle the exception, then a bug check will be invoked.

Regardless, any access path that may be called by an application program that causes the driver to lead to a bug check is a security violation within the driver. This allows an application to cause denial-of-service attacks to the entire system.

One of the most common problems in this area is that driver writers assume too much about the operating environment. This could include:

-   Checking that the high bit is set in the address. This does not work on x86-based computers where the system is using Four Gigabyte Tuning (4GT) by setting the /3GB option in the Boot.ini file. In that case, user-mode addresses set the high bit for the third gigabyte (GB) of the address space.

-   Using [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876) and [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879) to validate the address. While this will ensure that the address is a valid user-mode address at the time of the probe, there is nothing that requires it to remain valid after the probe operation. Thus, this technique introduces a subtle race condition that can lead to periodic irreproducible crashes. **ProbeForRead** and **ProbeForWrite** calls are necessary for a different reason: to validate whether the address is a user-mode address and that the length of the buffer is within the user address range. If the probe is omitted, users can pass in valid kernel-mode addresses, which will not be caught by a \_\_try and \_\_except block (structured exception handling) and will open up a large security hole. So **ProbeForRead** and **ProbeForWrite** calls are necessary to ensure alignment and that the user-mode address, plus the length, is within the user address range. However, a \_\_try and \_\_except block is needed to guard against access.

    Note that [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876) only validates that the address and length fall within the possible user-mode address range (slightly under 2 GB for a system without 4GT, for example), not whether the memory address is valid. In contrast, [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879) will try to access the first byte in each page of the length specified to verify that these are valid memory addresses.

-   Relying on memory manager functions ([**MmIsAddressValid**](https://msdn.microsoft.com/library/windows/hardware/ff554572), for example) to ensure that the address is valid. As with the probe functions, this introduces a race condition that can lead to irreproducible crashes.

-   Failing to use structured exception handling. The \_\_try and \_\_except functions within the compiler use operating system-level support for exception handling. Exceptions at kernel level are thrown back by calling [**ExRaiseStatus**](https://msdn.microsoft.com/library/windows/hardware/ff545529), or one of the related functions. A driver failing to use structured exception handling around any call that may raise an exception will lead to a bug check (typically KMODE\_EXCEPTION\_NOT\_HANDLED).

    Note that it is mistake to use structured exception handling around code that is not expected to raise errors. This will just mask real bugs that would otherwise be found. Putting a \_\_try and \_\_except wrapper at the top dispatch level of your routine is not the correct solution to this problem, although it is sometimes the reflex solution tried by driver writers.

-   Relying upon the contents of user memory remaining stable. For example, suppose a driver were to write a value into a user-mode memory location, and then later in the same routine refer to that memory location. A malicious application could actively modify that memory and, as a result, cause the driver to crash.

For file systems, these problems are particularly severe because they typically rely upon directly accessing user buffers (the METHOD\_NEITHER transfer method). Such drivers directly manipulate user buffers and thus must incorporate precautionary methods for buffer handling in order to avoid operating system-level crashes. Fast I/O always passes raw memory pointers, so drivers need to protect against similar problems if fast I/O is supported.

The WDK contains numerous examples of buffer validation in the FASTFAT and CDFS file system sample code, including:

-   The **FatLockUserBuffer** function in fastfat\\deviosup.c uses [**MmProbeAndLockPages**](https://msdn.microsoft.com/library/windows/hardware/ff554664) to lock down the physical pages behind the user buffer and [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559) in **FatMapUserBuffer** to create a virtual mapping for the pages that are locked down.

-   The **FatGetVolumeBitmap** function in fastfat\\fsctl.c uses [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876) and [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879) to validate user buffers in the defragmentation API.

-   The **CdCommonRead** function in cdfs\\read.c uses \_\_try and \_\_except around code to zero user buffers. Note that the sample code in **CdCommonRead** appears to use the try and except keywords. In the WDK environment, these keywords in C are defined in terms of the compiler extensions \_\_try and \_\_except. Anyone using C++ code must use the native compiler types to handle exceptions properly, as \_\_try is a C++ keyword, but not a C keyword, and will provide a form of C++ exception handling that is not valid for kernel drivers.

 

 




