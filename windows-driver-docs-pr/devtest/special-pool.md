---
title: Special Pool
description: Special Pool
ms.assetid: b1381a75-279a-42b7-b18d-43aba796424b
keywords:
- Special Pool feature WDK Driver Verifier
- memory corruption WDK Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Special Pool


## <span id="ddk_special_memory_pool_tools"></span><span id="DDK_SPECIAL_MEMORY_POOL_TOOLS"></span>


Memory corruption is a common driver problem. Driver errors can result in crashes long after the errors are made. The most common of these errors is accessing memory that has already been freed, and allocating *n* bytes and then accessing *n*+1 bytes.

To detect memory corruption, Driver Verifier can allocate driver memory from a special pool and monitor that pool for incorrect access. Special pool support is provided for kernel-mode system-supplied routines, such as [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) and also for the GDI system-supplied routines, such as [**EngAllocMem**](https://msdn.microsoft.com/library/windows/hardware/ff564176).

Two alignments of the special pool are available. The **Verify End** alignment is better at detecting access overruns, and the **Verify Start** alignment is better at detecting access underruns. (Note that the vast majority of memory corruptions are due to overruns, not underruns.)

When the Special Pool feature is active and **Verify End** has been selected, each memory allocation requested by the driver is placed on a separate page. The highest possible address that allows the allocation to fit on the page is returned, so that the memory is aligned with the end of the page. The previous portion of the page is written with special patterns. The previous page and the next page are marked inaccessible.

If the driver attempts to access memory after the end of the allocation, Driver Verifier will detect this immediately, and will issue [**Bug Check 0xCD**](https://msdn.microsoft.com/library/windows/hardware/ff560219). If the driver writes in the memory prior to the beginning of the buffer, this will (presumably) alter the patterns. When the buffer is freed, Driver Verifier will detect the alteration and issue [**Bug Check 0xC1**](https://msdn.microsoft.com/library/windows/hardware/ff560183).

If the driver reads or writes to the buffer after freeing it, Driver Verifier will issue [**Bug Check 0xCC**](https://msdn.microsoft.com/library/windows/hardware/ff560216).

When **Verify Start** is selected, the memory buffer is aligned with the beginning of the page. With this setting, underruns cause an immediate bug check and overruns cause a bug check when the memory is freed. This option is otherwise identical to the **Verify End** option.

**Verify End** is the default alignment, as overrun errors are much more common in drivers than underrun errors.

An individual memory allocation can override these settings and choose its alignment by calling [**ExAllocatePoolWithTagPriority**](https://msdn.microsoft.com/library/windows/hardware/ff544523) with the *Priority* parameter set to XxxSpecialPoolOverrun or XxxSpecialPoolUnderrun. (This routine cannot activate or deactivate the Special Pool feature, or request the special pool for a memory allocation, which would otherwise be allocated from normal pool. Only the alignment can be controlled from this routine.)

In Windows 7 and later versions of the Windows operating system, the Special Pool option supports memory that was allocated by using the following kernel APIs:

-   [**IoAllocateMdl**](https://msdn.microsoft.com/library/windows/hardware/ff548263)

-   [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257) and the other routines that can allocate I/O request packet (IRP) data structures

-   [**RtlAnsiStringToUnicodeString**](https://msdn.microsoft.com/library/windows/hardware/ff561729) and other run-time library (RTL) string routines

-   [**IoSetCompletionRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff549686)

### <span id="special_pool_by_pool_tag_or_allocation_size"></span><span id="SPECIAL_POOL_BY_POOL_TAG_OR_ALLOCATION_SIZE"></span>Special Pool by Pool Tag or Allocation Size

In addition to the Special Pool feature of Driver Verifier, which requests special pool for allocations by a specified *driver*, there are two other ways to use the special pool:

-   **Pool tag.** Request special pool for all allocations with a specified pool tag.

-   **Size.** Request special pool for all allocations within a specified size range.

To request special pool for a pool tag or size range, use Gflags, a tool included in *Debugging Tools for Windows*. For details, see [Using the Global Flags Utility](using-the-global-flags-utility.md).

You can use the Special Pool feature of Driver Verifier and the special pool features of Gflags at the same time. If you do, remember that the special pool is limited, that not all attempts to allocate from special pool succeed, and that Windows returns a success status for failed attempts to allocate from special pool that are satisfied by allocations from the regular memory pools.

### <span id="special_pool_efficiency"></span><span id="SPECIAL_POOL_EFFICIENCY"></span>Special Pool Efficiency

Not all special pool requests are fulfilled. Each allocation from the special pool uses one page of nonpageable physical memory and two pages of virtual address space. If the pool is exhausted, memory is allocated in the standard way until the special pool becomes available again. When a special pool request is filled from the standard pool, the requesting function does not return an error, since the pool request has succeeded. Thus, it is not recommended that multiple drivers be verified at the same time if the Special Pool feature is activated.

A single driver that makes many small memory requests can also deplete this pool. If this occurs, it may be preferable to assign pool tags to the driver's memory allocations and dedicate the special pool to one pool tag at a time.

The size of the special pool increases with the amount of physical memory on the system; ideally this should be at least 1 Gigabyte (GB). On x86 machines, because virtual (in addition to physical) space is consumed, do not use the [**/3GB**](https://msdn.microsoft.com/library/windows/hardware/ff556232) boot option. It is also a good idea to increase the pagefile minimum/maximum quantities by a factor of two or three.

To be sure that all of a driver's allocations are being tested, stressing the driver over long periods of time is recommended.

### <span id="monitoring_the_special_pool"></span><span id="MONITORING_THE_SPECIAL_POOL"></span>Monitoring the Special Pool

Statistics relating to pool allocations can be monitored. These can be displayed by Driver Verifier Manager, the Verifier.exe command line, or in a log file. See [Monitoring Global Counters](monitoring-global-counters.md) for details.

If the **Pool Allocations Succeeded in Special Pool** counter is equal to the **Pool Allocations Succeeded** counter, then the special pool has been sufficient to cover all memory allocations. If the former counter is lower than the latter, then the special pool has been exhausted at least once.

These counters do not track allocations whose size is one page or larger, since the special pool is not applicable to them.

If the Special Pool feature is enabled, but less than 95% of all pool allocations have been assigned from the special pool, a warning will appear in Driver Verifier Manager. In Windows 2000, this warning will appear on the **Driver Status** screen. In Windows XP and later, this warning will appear on the **Global Counters** screen. If this occurs, you should verify a shorter list of drivers, verify individual pools by pool tag, or add more physical memory to your system.

The kernel debugger extension **!verifier** can also be used to monitor special pool use. It presents similar information to that of Driver Verifier Manager. For information about debugger extensions, see [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063).

### <span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating This Option

You can activate the Special Pool feature for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md).

**Note**  To activate the Special Pool feature by pool tag or allocation size, or to set the **Verify Start** (detect underruns) and **Verify End** (detect overruns) alignments, use the [Global Flags utility](using-the-global-flags-utility.md); these alignment settings apply to all special pool allocations.

 

-   **At the command line**

    At the command line, the Special Pool option is represented by **Bit 0 (0x1)**. To activate Special Pool, use a flag value of 0x1 or add 0x1 to the flag value. For example:

    ```
    verifier /flags 0x1 /driver MyDriver.sys
    ```

    The feature will be active after the next boot.

    On Windows 2000 and later versions of Windows, you can also activate and deactivate Special Pool without rebooting the computer by adding the **/volatile** parameter to the command. For example:

    ```
    verifier /volatile /flags 0x1 /adddriver MyDriver.sys
    ```

    This setting is effective immediately, but is lost when you shut down or reboot the computer. For details, see [Using Volatile Settings](using-volatile-settings.md).

    The Special Pool feature is also included in the standard settings. For example:

    ```
    verifier /standard /driver MyDriver.sys
    ```

-   **Using Driver Verifier Manager**

    1.  Select **Create custom settings (for code developers)** and then click **Next**.
    2.  Select **Select individual settings from a full list**.
    3.  Select (check) **Special pool**.

    The Special Pool feature is also included in the standard settings. To use this feature, in Driver Verifier Manager, click **Create Standard Settings**.

 

 





