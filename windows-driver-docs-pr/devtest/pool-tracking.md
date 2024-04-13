---
title: Pool Tracking
description: Pool Tracking monitors the memory allocations made by the driver.
keywords:
- Memory Pool Tracking feature WDK Driver Verifier
- Pool Tracking feature WDK Driver Verifier
- memory allocations WDK Driver Verifier
- memory leaks WDK Driver Verifier
- unfreed memory allocations WDK Driver Verifier
ms.date: 04/20/2017
---

# Pool Tracking


Pool Tracking monitors the memory allocations made by the driver. At the time that the driver is unloaded, Driver Verifier ensures that all allocations made by the driver have been freed.

## <span id="ddk_memory_pool_tracking_tools"></span><span id="DDK_MEMORY_POOL_TRACKING_TOOLS"></span>


Unfreed memory allocations (also called *memory leaks*) are a common cause of lowered operating system performance. These can fragment the system pools and eventually cause system crashes.

When this option is active, Driver Verifier will issue bug check 0xC4 (with Parameter 1 equal to 0x62) if a driver unloads without freeing all its allocations.

If Driver Verifier issues this bug check with Parameter 1 equal to 0x51, 0x52, 0x53, 0x54, or 0x59, the driver has written to memory outside of its allocations. In this case, you should enable the [Special Pool](special-pool.md) feature to locate the source of the error.

See [**Bug Check 0xC4**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (DRIVER\_VERIFIER\_DETECTED\_VIOLATION) for a list of the bug check parameters.

Starting with Windows Vista, enabling the Pool Tracking option also enables the tracking of locked pages. When this option is active, Driver Verifier will issue [**Bug Check 0xCB**](../debugger/bug-check-0xcb--driver-left-locked-pages-in-process.md) (DRIVER\_LEFT\_LOCKED\_PAGES\_IN\_PROCESS) if a driver fails to release locked pages after an I/O operation.

In Windows 7 and later versions of the Windows operating system, the Pool Tracking option supports memory that was allocated by using the following kernel APIs:

-   [**IoAllocateMdl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocatemdl)

-   [**IoAllocateIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp) and the other routines that can allocate I/O request packet (IRP) data structures

-   [**RtlAnsiStringToUnicodeString**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlansistringtounicodestring) and other run-time library (RTL) string routines

-   [**IoSetCompletionRoutineEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutineex)

In Windows 7 and later versions of the Windows operating system, when Pool Tracking is activated, Driver Verifier can detect attempts to allocate kernel pool memory with *quota* in the context of the Idle process. Such attempts usually mean that the driver is allocating memory from a DPC routine. The thread or process context for DPC routines is unreliable, so trying to charge quota to that process is incorrect.

### <span id="monitoring_pool_tracking"></span><span id="MONITORING_POOL_TRACKING"></span>Monitoring Pool Tracking

Memory pool allocation statistics can be monitored separately for each driver being verified. These statistics can be displayed by Driver Verifier Manager, the Verifier.exe command line, or in a log file. See [Monitoring Individual Counters](monitoring-individual-counters.md) for details.

The kernel debugger extension **!verifier 0x3** can be used to locate outstanding memory allocations after the driver is unloaded, or to track the current allocations while the driver is running. This extension also shows the pool tag, the size of the pool, and the address of the allocator for each allocation. For information about debugger extensions, see [Windows Debugging](../debugger/index.md).

### <span id="Pool_Quota_Charges_from_DPC_Routine"></span><span id="pool_quota_charges_from_dpc_routine"></span><span id="POOL_QUOTA_CHARGES_FROM_DPC_ROUTINE"></span>Pool Quota Charges from DPC Routine

Kernel drivers can call [**ExAllocatePoolWithQuotaTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithquotatag) to allocate kernel pool memory and charge the number of bytes that are allocated to the pool quota of the current process. Drivers typically use quota for memory allocations that are directly related to a request that comes from an application.

Deferred procedure call (DPC) routines can run in the context of any process. Therefore, charging quota from a DPC routine charges a random process. Even worse, when the DPC routine runs in the context of the Idle process, this condition can result in memory corruption or system crashes.

Starting in Windows 7, Driver Verifier detects [**ExAllocatePoolWithQuotaTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithquotatag) calls from DPC routines.

### <span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating This Option

You can activate the Pool Tracking feature for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md).

-   **At the command line**

    At the command line, the Pool Tracking option is represented by **Bit 3 (0x8)**. To activate Pool Tracking, use a flag value of 0x8 or add 0x8 to the flag value. For example:

    ```
    verifier /flags 0x8 /driver MyDriver.sys
    ```

    The feature will be active after the next boot.

    On Windows Vista and later versions of Windows, you can also activate and deactivate Pool Tracking without rebooting the computer by adding the **/volatile** parameter to the command. For example:

    ```
    verifier /volatile /flags 0x8 /adddriver MyDriver.sys
    ```

    This setting is effective immediately, but is lost when you shut down or reboot the computer. For details, see [Using Volatile Settings](using-volatile-settings.md).

    The Pool Tracking feature is also included in the standard settings. For example:

    ```
    verifier /standard /driver MyDriver.sys
    ```

-   **Using Driver Verifier Manager**

    1.  Start Driver Verifier Manager. Type **Verifier** in a Command Prompt window.
    2.  Select **Create custom settings (for code developers)** and then click **Next**.
    3.  Select **Select individual settings from a full list**.
    4.  Select (check) **Pool tracking**.

    The Pool Tracking feature is also included in the standard settings. To use this feature, in Driver Verifier Manager, click **Create Standard Settings**.

 

