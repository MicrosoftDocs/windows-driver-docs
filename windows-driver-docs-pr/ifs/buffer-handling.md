---
title: Buffer Handling
description: Buffer Handling
keywords:
- security WDK file systems , minimizing threats
- buffers WDK file systems
- paged buffers WDK file systems
- non-paged buffers WDK file systems
- bug check WDK file systems
- address validation WDK file systems
- fast I/O WDK file systems
ms.date: 11/04/2024
---

# Buffer Handling

One of the most common errors within any driver relates to buffer handling, where buffers are invalid or too small. These errors can allow buffer overflows or cause system crashes, which can compromise system security. This article discusses some of the common problems with buffer handling and how to avoid them. It also identifies WDK sample code that demonstrates proper buffer handling techniques.

## Buffer types and invalid addresses

From a driver's perspective, buffers come in one of two varieties:

* Paged buffers, which might or might not be resident in memory.

* Nonpaged buffers, which must be resident in memory.

An invalid memory address isn't paged nor nonpaged. As the operating system works to resolve a page fault caused by incorrect buffer handling, it takes the following steps:

* It isolates the invalid address into one of the "standard" address ranges (paged kernel addresses, nonpaged kernel addresses, or user addresses).

* It raises the appropriate type of error. The system always handles buffer errors either by a bug check such as PAGE_FAULT_IN_NONPAGED_AREA, or by an exception such as STATUS_ACCESS_VIOLATION. If the error is a bug check, the system will halt operation. In the case of an exception, the system invokes stack-based exception handlers. If none of exception handlers handle the exception, the system invokes a bug check.

Regardless, any access path that an application program can call that causes the driver to lead to a bug check is a security violation within the driver. Such a violation allows an application to cause denial-of-service attacks to the entire system.

## Common assumptions and mistakes

One of the most common problems in this area is that driver writers assume too much about the operating environment. Some common assumptions and mistakes include:

* A driver simply checking whether the high bit is set in the address. Relying on a fixed bit pattern to determine address type doesn't work on all systems or scenarios. For example, this check doesn't work on x86-based computers when the system is using [Four Gigabyte Tuning](/windows/win32/memory/4-gigabyte-tuning) (4GT). When 4GT is being used, user-mode addresses set the high bit for the third gigabyte of the address space.

* A driver solely using [**ProbeForRead**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforread) and [**ProbeForWrite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforwrite) to validate the address. These calls ensure that the address is a valid user-mode address at the time of the probe. However, there are no guarantees that this address will remain valid after the probe operation. Thus, this technique introduces a subtle race condition that can lead to periodic irreproducible crashes.

  **ProbeForRead** and **ProbeForWrite** calls are still necessary. If a driver omits the probe, users can pass in valid kernel-mode addresses that a ```__try``` and ```__except``` block (structured exception handling) won't catch and thus open up a large security hole.

  The bottom line is that both probing and structured exception handling are necessary:
  
  * Probing validates that the address is a user-mode address and that the length of the buffer is within the user address range.

  * A ```__try/__except``` block guards against access.

  Note that [**ProbeForRead**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforread) only validates that the address and length fall within the possible user-mode address range (slightly under 2 GB for a system without 4GT, for example), not whether the memory address is valid. In contrast, [**ProbeForWrite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforwrite) tries to access the first byte in each page of the length specified to verify that these bytes are valid memory addresses.

* A driver relying on memory manager functions such as [**MmIsAddressValid**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-mmisaddressvalid) to ensure that the address is valid. As described for the probe functions, this situation introduces a race condition that can lead to irreproducible crashes.

* A driver failing to use structured exception handling. The ```__try/except``` functions within the compiler use operating system-level support for exception handling. Kernel-level exceptions are thrown back to the system through a call to [**ExRaiseStatus**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exraisestatus) or one of the related functions. A driver failing to use structured exception handling around any call that might raise an exception will lead to a bug check (typically KMODE_EXCEPTION_NOT_HANDLED).

  It's a mistake to use structured exception handling around code that isn't expected to raise errors. This usage will just mask real bugs that would otherwise be found. Putting a ```__try/__except``` wrapper at the top dispatch level of your routine isn't the correct solution to this problem, although it's sometimes the reflex solution tried by driver writers.

* A driver assuming that the contents of user memory will remain stable. For example, suppose a driver wrote a value into a user-mode memory location, and then later in the same routine referred to that memory location. A malicious application could actively modify that memory after the write and, as a result, cause the driver to crash.

For file systems, these problems are severe because file systems typically rely upon directly accessing user buffers (the METHOD_NEITHER transfer method). Such drivers directly manipulate user buffers and thus must incorporate precautionary methods for buffer handling in order to avoid operating system-level crashes. Fast I/O always passes raw memory pointers, so drivers need to protect against similar problems if fast I/O is supported.

## Sample code for buffer handling

The WDK contains numerous examples of buffer validation in the [*fastfat*](https://github.com/microsoft/windows-driver-samples/tree/main/filesys/fastfat) and [*CDFS file system driver*](https://github.com/microsoft/Windows-driver-samples/blob/main/filesys/cdfs/README.md) sample code, including:

* The **FatLockUserBuffer** function in *fastfat\\deviosup.c* uses [**MmProbeAndLockPages**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmprobeandlockpages) to lock down the physical pages behind the user buffer and [**MmGetSystemAddressForMdlSafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemaddressformdlsafe) in **FatMapUserBuffer** to create a virtual mapping for the pages that are locked down.

* The **FatGetVolumeBitmap** function in *fastfat\\fsctl.c* uses [**ProbeForRead**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforread) and [**ProbeForWrite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforwrite) to validate user buffers in the defragmentation API.

* The **CdCommonRead** function in *cdfs\\read.c* uses ```__try``` and ```__except``` around code to zero user buffers. The sample code in **CdCommonRead** appears to use the ```try``` and ```except``` keywords. In the WDK environment, these keywords in C are defined in terms of the compiler extensions ```__try``` and ```__except```. Anyone using C++ code must use the native compiler types to handle exceptions properly, as ```__try``` is a C++ keyword, but not a C keyword, and will provide a form of C++ exception handling that isn't valid for kernel drivers.
