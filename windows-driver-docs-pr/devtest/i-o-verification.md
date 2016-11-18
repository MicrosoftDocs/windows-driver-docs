---
title: I/O Verification
description: I/O Verification
ms.assetid: 41b77bba-fae8-453b-9872-911f5d5be3e6
keywords: ["I/O Verification feature WDK Driver Verifier", "Level 1 I/O Verification WDK Driver Verifier", "Level 2 I/O Verification WDK Driver Verifier"]
---

# I/O Verification


## <span id="ddk_i_o_verification_tools"></span><span id="DDK_I_O_VERIFICATION_TOOLS"></span>


Driver Verifier has two levels of I/O Verification:

-   *Level 1 I/O Verification* is always active whenever I/O Verification is selected.

-   *Level 2 I/O Verification* is always active whenever I/O Verification is selected in Windows XP and later. In Windows 2000, I/O Verification can be configured to include both levels, or just the Level 1 tests.

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

I/O Verification Level 1 failures cause bug check 0xC9 to be issued. The first parameter of this bug check indicates what violation has occurred. See [**Bug Check 0xC9**](https://msdn.microsoft.com/library/windows/hardware/ff560205) (DRIVER\_VERIFIER\_IOMANAGER\_VIOLATION) for a full parameter listing.

### <span id="level_2_i_o_verification"></span><span id="LEVEL_2_I_O_VERIFICATION"></span>Level 2 I/O Verification

I/O Verification Level 2 errors are displayed in different ways: on the blue screen, in a crash dump file, and in a kernel debugger.

On the blue screen, these errors are noted by the message **IO SYSTEM VERIFICATION ERROR** and the string **WDM DRIVER ERROR***XXX*, where *XXX* is an I/O error code.

In a crash dump file, most of these errors are noted by the message **BugCheck 0xC9 (DRIVER\_VERIFIER\_IOMANAGER\_VIOLATION)**, along with the I/O error code. In this case, the I/O error code appears as the first parameter of the bug check 0xC9. The remainder are noted by the message **Bug Check 0xC4 (DRIVER\_VERIFIER\_DETECTED\_VIOLATION)**, along with a Driver Verifier error code. In this case, the Driver Verifier error code appears as the first parameter of the bug check 0xC4.

In a kernel debugger (KD or WinDbg), these errors are noted by the message **WDM DRIVER ERROR** and a descriptive text string. When the kernel debugger is active, it is possible to ignore the Level 2 errors and resume system operation. (This is not possible with any other bug checks.)

The blue screen, the crash dump file, and the kernel debugger each display additional information as well. For a full description of most I/O Verification Level 2 error messages, see [**Bug Check 0xC9**](https://msdn.microsoft.com/library/windows/hardware/ff560205). For the remainder, see [**Bug Check 0xC4**](https://msdn.microsoft.com/library/windows/hardware/ff560187).

Starting in Window Vista, the I/O Verification option checks for the following driver errors:

-   Taking too long to complete and cancel IRPs that originated in user-mode applications.

-   Releasing a remove lock that has not yet been acquired.

-   Calling [**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560) or [**IoReleaseRemoveLockAndWait**](https://msdn.microsoft.com/library/windows/hardware/ff549567) with a tag parameter that differs from the tag parameter used in the corresponding [**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204) call.

Starting in Windows 7, the I/O Verification option checks for the following driver errors:

-   Attempts to free IRPs by calling [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590). IRPs must be freed with [**IoFreeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549113).

In addition, you can use this option to detect another common driver bug—reinitializing remove locks. Remove locks data structures should be allocated inside device extensions. This ensures that the I/O manager frees the memory that holds the IO\_REMOVE\_LOCK structure only when the device object is deleted. If the driver performs the following three steps, it is possible that after step 2, an application or driver still holds a reference to Device1:

-   Allocates the IO\_REMOVE\_LOCK structure that corresponds to Device1, but does the allocation outside of Device1’s extension.
-   Calls [**IoReleaseRemoveLockAndWait**](https://msdn.microsoft.com/library/windows/hardware/ff549567) when Device1 is being removed.
-   Calls [**IoInitializeRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549324) for the same lock to reuse it as a remove lock for Device2.

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

    In Windows 2000, you can use the **/iolevel** parameter to activate only Level 1 (the default) or both Level 1 and Level 2. In later versions of Windows, both Level 1 and Level 2 are always activated when you activate I/O Verification.

    For example, the following command activates Level 1 and Level 2 I/O verification on a computer running Windows 2000.

    ```
    verifier /flags 0x10 /iolevel 2 /driver MyDriver.sys
    ```

    On Windows Vista and later versions of Windows, you can also activate and deactivate I/O Verification without rebooting the computer by adding the **/volatile** parameter to the command. For example:

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20I/O%20Verification%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




