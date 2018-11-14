---
title: Enhanced I/O Verification
description: Enhanced I/O Verification
ms.assetid: ce8a0b22-fa27-45e5-b013-b3accf604ed4
keywords:
- Enhanced I/O Verification feature WDK Driver Verifier
- I/O Verification feature WDK Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enhanced I/O Verification


This feature is only available in Windows XP and later versions of the Windows operating system.

In Windows 7 and later versions of the Windows operating system, Enhanced I/O Verification is automatically activated when you select I/O Verification. It is not available or necessary to select it as a separate option.

When Enhanced I/O Verification is activated, Driver Verifier monitors the calls of several I/O Manager routines and performs stress testing of PnP IRPs, power IRPs and WMI IRPs.

In Windows Vista and Windows XP, Enhanced I/O Verification is activated independently of [I/O Verification](i-o-verification.md), but selecting both options provides for a more complete test of I/O interface methods in a driver.

### <span id="features_of_enhanced_i_o_verification"></span><span id="FEATURES_OF_ENHANCED_I_O_VERIFICATION"></span>Features of Enhanced I/O Verification

Driver Verifier adds the following checks when you activate Enhanced I/O Verification.

-   Monitors all IRPs to ensure that the driver returns STATUS\_PENDING if and only if it has called [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422).

-   Monitors the use of [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083) to verify that the driver is not deleting the same device more that once and to detect inappropriate detaching and deleting of device objects.

-   Verifies that the driver correctly unwinds all [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355) calls.

New stresses and tests include:

-   Scrambling the order of enumerated devices, to ensure that Plug and Play (PnP) drivers don't make assumptions about the device start order.

-   Adjusting the status of PnP and Power IRPs when they complete, to catch drivers that return an incorrect status from their dispatch routines.

-   Sending fake Power IRPs to test for driver code path bugs.

-   Sending fake WMI IRPs to test for driver code path bugs.

-   Inserting a fake filter into every WDM stack.

### <span id="displaying_enhanced_i_o_verification_errors"></span><span id="DISPLAYING_ENHANCED_I_O_VERIFICATION_ERRORS"></span>Displaying Enhanced I/O Verification Errors

Driver errors caught by Enhanced I/O Verification are displayed in the same manner as those caught by [Level 2 I/O Verification](i-o-verification.md).

On the blue screen, these errors are noted by the message **IO SYSTEM VERIFICATION ERROR** and the string **WDM DRIVER ERROR** *XXX*, where *XXX* is an I/O error code.

In a crash dump file, these errors are noted by the message **BugCheck 0xC9 (DRIVER\_VERIFIER\_IOMANAGER\_VIOLATION)**, along with the I/O error code. In this case, the I/O error code appears as the first parameter of the bug check 0xC9.

In a kernel debugger (KD or WinDbg), these errors are noted by the message **WDM DRIVER ERROR** and a descriptive text string. When the kernel debugger is active, it is possible to ignore the Level 2 errors and resume system operation. (This is not possible with any other bug checks.)

The blue screen, the crash dump file, and the kernel debugger each display additional information as well. For a full description of all I/O Verification Level 2 error messages, see [**Bug Check 0xC9**](https://msdn.microsoft.com/library/windows/hardware/ff560205).

### <span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating This Option

You can activate the Enhanced I/O Verification feature for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md).

**Note**  In Windows 7 and later versions of the Windows operating system, Enhanced I/O Verification is automatically activated when you select [I/O Verification](i-o-verification.md). It is not available or necessary to select it as a separate option.

 

-   **At the command line**

    At the command line, the Enhanced I/O Verification option is represented by **Bit 6 (0x40)**. To activate Enhanced I/O Verification, use a flag value of 0x40 or add 0x40 to the flag value. For example:

    ```
    verifier /flags 0x40 /driver MyDriver.sys
    ```

    The feature will be active after the next boot.

    On Windows Vista and later versions of Windows, you can also activate and deactivate Enhanced I/O Verification without rebooting the computer by adding the **/volatile** parameter to the command. For example:

    ```
    verifier /volatile /flags 0x40 /adddriver MyDriver.sys
    ```

    This setting is effective immediately, but is lost when you shut down or reboot the computer. For details, see [Using Volatile Settings](using-volatile-settings.md).

-   **Using Driver Verifier Manager**

    1.  Start Driver Verifier Manager. Type **Verifier** in a Command Prompt window.
    2.  Select **Create custom settings (for code developers)** and then click **Next**.
    3.  Select **Select individual settings from a full list**.
    4.  Select (check) **Enhanced I/O verification**.

    The DMA Verification feature is also included in the standard settings. To use this feature, in Driver Verifier Manager, click **Create Standard Settings**.

 

 





