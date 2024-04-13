---
title: I/O Verification
description: I/O Verification
keywords:
- I/O Verification feature WDK Driver Verifier
- Level 1 I/O Verification WDK Driver Verifier
- Level 2 I/O Verification WDK Driver Verifier
ms.date: 04/20/2017
---

# I/O Verification


## <span id="ddk_i_o_verification_tools"></span><span id="DDK_I_O_VERIFICATION_TOOLS"></span>


Driver Verifier has two levels of I/O Verification:

-   *Level 1 I/O Verification* is always active whenever I/O Verification is selected.

-   *Level 2 I/O Verification* is always active whenever I/O Verification is selected in Windows XP and later. 

**See Also:** [Enhanced I/O Verification](enhanced-i-o-verification.md) In Windows 7 and later versions of the Windows operating system, Enhanced I/O Verification is automatically activated when you select I/O Verification. It is not available or necessary to select it as a separate option.

### <span id="level_1_i_o_verification"></span><span id="LEVEL_1_I_O_VERIFICATION"></span>Level 1 I/O Verification

When Level 1 I/O Verification is enabled, all IRPs obtained through **IoAllocateIrp** are allocated from a special pool and their use is tracked.

Additionally, Driver Verifier checks for invalid I/O calls, including:

-   Attempts to free an IRP whose type is not IO\_TYPE\_IRP

-   Passes of invalid device objects to **IoCallDriver**

-   Passes of an IRP to **IoCompleteRequest** that contains invalid status or that still has a cancel routine set

-   Changes to the IRQL across a call to the driver dispatch routine

-   Attempts to free an IRP that remains associated with a thread

-   Passes of a device object to **IoInitializeTimer** that already contains an initialized timer

-   Passes of an invalid buffer to **IoBuildAsynchronousFsdRequest** or **IoBuildDeviceIoControlRequest**

-   Passes of an I/O status block to an IRP, when this I/O status block is allocated on a stack that has unwound too far

-   Passes of an event object to an IRP, when this event object is allocated on a stack that has unwound too far

Because the special IRP pool is of limited size, I/O Verification is most effective when it is only used on one driver at a time.

I/O Verification Level 1 failures cause bug check 0xC9 to be issued. The first parameter of this bug check indicates what violation has occurred. See [**Bug Check 0xC9**](../debugger/bug-check-0xc9--driver-verifier-iomanager-violation.md) (DRIVER\_VERIFIER\_IOMANAGER\_VIOLATION) for a full parameter listing.

### <span id="level_2_i_o_verification"></span><span id="LEVEL_2_I_O_VERIFICATION"></span>Level 2 I/O Verification

I/O Verification Level 2 errors are displayed in different ways: on the blue screen, in a crash dump file, and in a kernel debugger.

On the blue screen, these errors are noted by the message **IO SYSTEM VERIFICATION ERROR** and the string **WDM DRIVER ERROR***XXX*, where *XXX* is an I/O error code.

In a crash dump file, most of these errors are noted by the message **BugCheck 0xC9 (DRIVER\_VERIFIER\_IOMANAGER\_VIOLATION)**, along with the I/O error code. In this case, the I/O error code appears as the first parameter of the bug check 0xC9. The remainder are noted by the message **Bug Check 0xC4 (DRIVER\_VERIFIER\_DETECTED\_VIOLATION)**, along with a Driver Verifier error code. In this case, the Driver Verifier error code appears as the first parameter of the bug check 0xC4.

In a kernel debugger (KD or WinDbg), these errors are noted by the message **WDM DRIVER ERROR** and a descriptive text string. When the kernel debugger is active, it is possible to ignore the Level 2 errors and resume system operation. (This is not possible with any other bug checks.)

The blue screen, the crash dump file, and the kernel debugger each display additional information as well. For a full description of most I/O Verification Level 2 error messages, see [**Bug Check 0xC9**](../debugger/bug-check-0xc9--driver-verifier-iomanager-violation.md). For the remainder, see [**Bug Check 0xC4**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md).

Starting in Window Vista, the I/O Verification option checks for the following driver errors:

-   Taking too long to complete and cancel IRPs that originated in user-mode applications.

-   Releasing a remove lock that has not yet been acquired.

-   Calling [**IoReleaseRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreleaseremovelock) or [**IoReleaseRemoveLockAndWait**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreleaseremovelockandwait) with a tag parameter that differs from the tag parameter used in the corresponding [**IoAcquireRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioacquireremovelock) call.

-   Calling [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) with interrupts disabled.

-   Calling [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) at IRQL greater than DISPATCH\_LEVEL.

-   Returning from a driver dispatch routine with interrupts disabled.

-   Returning from a driver dispatch routine with a changed IRQL.

-   Returning from a driver dispatch routine with APCs disabled. In this case, the driver might have called [**KeEnterCriticalRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keentercriticalregion) more times than [**KeLeaveCriticalRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keleavecriticalregion), which is the primary cause for [**Bug Check 0x20**](../debugger/bug-check-0x20--kernel-apc-pending-during-exit.md) (KERNEL\_APC\_PENDING\_DURING\_EXIT) and [**Bug Check 0x1**](../debugger/bug-check-0x1--apc-index-mismatch.md) (APC\_INDEX\_MISMATCH).

Starting in Windows 7, the I/O Verification option checks for the following driver errors:

-   Attempts to free IRPs by calling [**ExFreePool**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exfreepool). IRPs must be freed with [**IoFreeIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iofreeirp).

In addition, you can use this option to detect another common driver bug—reinitializing remove locks. Remove locks data structures should be allocated inside device extensions. This ensures that the I/O manager frees the memory that holds the IO\_REMOVE\_LOCK structure only when the device object is deleted. If the driver performs the following three steps, it is possible that after step 2, an application or driver still holds a reference to Device1:

-   Allocates the IO\_REMOVE\_LOCK structure that corresponds to Device1, but does the allocation outside of Device1’s extension.
-   Calls [**IoReleaseRemoveLockAndWait**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreleaseremovelockandwait) when Device1 is being removed.
-   Calls [**IoInitializeRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioinitializeremovelock) for the same lock to reuse it as a remove lock for Device2.

It is possible that after step 2 an application or driver still holds a reference to Device1. The application or driver can still send requests to Device1, even though this device was removed. Therefore, it is not safe to reuse the same memory as a new remove lock until I/O manager deletes Device1. Reinitializing the same lock while another thread is trying to acquire it can result in the corruption of the lock, with unpredictable results for the driver and the entire system.

In Windows 7 and later versions of the Windows operating system, [Enhanced I/O Verification](enhanced-i-o-verification.md) is automatically activated when you select I/O Verification.

### <span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating This Option

You can activate the I/O Verification feature for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md).

-   **At the command line.**

    At the command line, the I/O Verification option is represented by **Bit 4 (0x10)**. To activate I/O Verification, use a flag value of 0x10 or add 0x10 to the flag value. For example:

    ```
    verifier /flags 0x10 /driver MyDriver.sys
    ```

    The feature will be active after the next boot.

    You can also activate and deactivate I/O Verification without rebooting the computer by adding the **/volatile** parameter to the command. For example:

    ```
    verifier /volatile /flags 0x10 /adddriver MyDriver.sys
    ```

    This setting is effective immediately, but is lost when you shut down or reboot the computer. For details, see [Using Volatile Settings](using-volatile-settings.md).

    The I/O Verification feature is also included in the standard settings. For example:

    ```
    verifier /standard /driver MyDriver.sys
    ```

-   **Using Driver Verifier Manager**

    1.  Select **Create custom settings (for code developers)** and then click **Next**.
    2.  Select **Select individual settings from a full list**.
    3.  Select (check) **I/O verification**.

    The I/O Verification feature is also included in the standard settings. To use this feature, in Driver Verifier Manager, click **Create Standard Settings**.

 

