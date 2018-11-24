---
title: Force IRQL Checking
description: Force IRQL Checking
ms.assetid: cb972a72-6504-4ed7-9618-2830192fda1d
keywords:
- Force IRQL Checking feature WDK Driver Verifier
- IRQL monitoring WDK Driver Verifier
- spin locks WDK Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Force IRQL Checking


## <span id="ddk_forcing_irql_checking_tools"></span><span id="DDK_FORCING_IRQL_CHECKING_TOOLS"></span>


Although kernel-mode drivers are forbidden to access pageable memory at a high IRQL or while holding a spin lock, such an action might not be noticed if the page has not actually been trimmed from the working set and paged out to disk.

When Force IRQL Checking is enabled, Driver Verifier provides extreme pressure on the use of system memory. Whenever a driver being verified requests a spin lock, calls **KeSynchronizeExecution**, or raises the IRQL to DISPATCH\_LEVEL or higher, all of the system pageable pool, code, and data (which includes the driver's pageable code and data) are trimmed from the working set. If the driver attempts to access any of this memory, Driver Verifier issues a bug check.

Starting with Windows Vista, this option also causes Driver Verifier to detect when certain synchronization objects are included in pageable memory. These synchronization objects cannot be paged because the operating system kernel is accessing them at elevated IRQL. Driver Verifier can detect the pageable [**KTIMER**](https://msdn.microsoft.com/library/windows/hardware/ff554250), PRKMUTEX, PKSPIN\_LOCK, PRKEVENT, PKSPIN\_LOCK, PRKSEMAPHORE, PERESOURCE, and [**FAST\_MUTEX**](https://msdn.microsoft.com/library/windows/hardware/ff545715) structures.

This pressure on memory usage will not directly affect drivers that are not selected for verification. When a driver that is not selected for verification raises the IRQL, it does not trigger the trimming action. However, when a driver that is being verified raises the IRQL, Driver Verifier does trim pages that can be used by drivers that are not being verified. So errors committed by drivers that are not being verified might occasionally be caught when this option is active.

### <span id="monitoring_irql_raises_and_spin_locks"></span><span id="MONITORING_IRQL_RAISES_AND_SPIN_LOCKS"></span>Monitoring IRQL Raises and Spin Locks

The number of IRQL raises, spin locks, and calls to **KeSynchronizeExecution** made by drivers being verified can be monitored. The number of times that Driver Verifier has trimmed pageable memory from the working set can also be monitored. These statistics can be displayed by Driver Verifier Manager, the Verifier.exe command line, or in a log file. See [Monitoring Global Counters](monitoring-global-counters.md) for details.

The kernel debugger extension **!verifier** can also be used to monitor these statistics. It presents similar information to that of Driver Verifier Manager. In Windows XP and later, the **!verifier 0x8** extension will display a log of recent IRQL changes made by drivers being verified. For information about debugger extensions, see [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063).

### <span id="Calling_KeEnterCriticalRegion_or_KeLeaveCriticalRegion_at_DISPATCH_LEVEL_or_Above"></span><span id="calling_keentercriticalregion_or_keleavecriticalregion_at_dispatch_level_or_above"></span><span id="CALLING_KEENTERCRITICALREGION_OR_KELEAVECRITICALREGION_AT_DISPATCH_LEVEL_OR_ABOVE"></span>Calling KeEnterCriticalRegion or KeLeaveCriticalRegion at DISPATCH\_LEVEL or Above

[**KeEnterCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552021) and [**KeLeaveCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552964) are APIs that you can be use to synchronize the execution of a critical sequence of driver code with the delivery of ordinary kernel asynchronous procedure calls (APCs). The **KeEnterCriticalRegion** and **KeLeaveCriticalRegion** APIs cannot be called at IRQL = DISPATCH\_LEVEL or above. Calling **KeEnterCriticalRegion** or **KeLeaveCriticalRegion** at DISPATCH\_LEVEL or above can result in a system hang or memory corruption.

Starting in Windows 7, Driver Verifier detects calls to these APIs at DISPATCH\_LEVEL or above if the Force IRQL Checking option is enabled.

### <span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating This Option

You can activate the Force IRQL Checking feature for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md).

-   **At the command line**

    At the command line, the Force IRQL Checking option is represented by **Bit 1 (0x2)**. To activate Force IRQL Checking, use a flag value of 0x2 or add 0x2 to the flag value. For example:

    ```
    verifier /flags 0x2 /driver MyDriver.sys
    ```

    The feature will be active after the next boot.

    On Windows 2000 and later versions of Windows, you can also activate and deactivate Force IRQL Checking without rebooting the computer by adding the **/volatile** parameter to the command. For example:

    ```
    verifier /volatile /flags 0x2 /adddriver MyDriver.sys
    ```

    This setting is effective immediately, but is lost when you shut down or reboot the computer. For details, see [Using Volatile Settings](using-volatile-settings.md).

    The Force IRQL Checking feature is also included in the standard settings. For example:

    ```
    verifier /standard /driver MyDriver.sys
    ```

-   **Using Driver Verifier Manager**

    1.  Start Driver Verifier Manager. Type **Verifier** in a Command Prompt window.
    2.  Select **Create custom settings (for code developers)** and then click **Next**.
    3.  Select **Select individual settings from a full list**.
    4.  Select (check) **Force IRQL checking**.

    The Force IRQL Checking feature is also included in the standard settings. To use this feature, in Driver Verifier Manager, click **Create Standard Settings**.

 

 





