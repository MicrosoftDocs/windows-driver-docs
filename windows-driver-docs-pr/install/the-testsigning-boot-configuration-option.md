---
title: Loading Test Signed Code
description: Describes how to enable loading of test signed drivers using the TESTSIGNING option with BCDEdit tool
ms.date: 02/15/2021
ms.localizationpriority: medium
ms.custom: contperf-fy21q3
---

# Enable Loading of Test Signed Drivers

By default, Windows does not load test-signed kernel-mode drivers. To change this behavior and enable test-signed drivers to load, use the boot configuration data editor, BCDEdit.exe, to enable or disable TESTSIGNING, a boot configuration option. You must have Administrator rights to enable this option.

> [!Note]
> For 64-bit versions of Windows Vista and later versions of Windows, the kernel-mode code signing policy requires that all kernel-mode code have a digital signature. However, in most cases, an unsigned driver can be installed and loaded on 32-bit versions of Windows Vista and later versions of Windows. For more information, see [Driver Signing Policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md).


## Administrator rights required

To use BCDEdit, you must be a member of the Administrators group on the system and run the command from an elevated command prompt. To open an elevated Command Prompt window, type **cmd** into the search box in the Windows taskbar, select and hold (or right-click) **Command Prompt** in the search results, and then select **Run as administrator**.

> [!Warning]
> Administrative rights are required to use BCDEdit to modify boot configuration data. Changing some boot entry options by using **BCDEdit /set** could render your computer inoperable. As an alternative, use System Configuration utility (MSConfig.exe) to change boot settings.


## Enable or disable use of test-signed code

Run BCDEdit command lines to enable or disable the loading of test-signed code. For a change to take effect, whether enabling or disabling the option, you must restart the computer after changing the configuration.

To enable test-signed code, use the following BCDEdit command line:

```cmd
:: If this command results in "The value is protected by Secure Boot policy and cannot be modified or deleted"
:: Then reboot the PC, go into BIOS settings, and disable Secure Boot. BitLocker may also affect your ability to modify this setting.
Bcdedit.exe -set TESTSIGNING ON
```

To disable use of test-signed code, use the following BCDEdit command line:

```cmd
Bcdedit.exe -set TESTSIGNING OFF
```

The following figure shows the result of using the BCDEdit command line to enable test-signing.

![Screen shot of the results of using testsigning, a boot configuration option.](images/driver-signing-enable-vista-test-signing.png)


## Behavior of Windows when loading test-signed code is enabled

When loading test-signed code is enabled, Windows does the following:

-   Displays a watermark with the text "Test Mode" in all four corners of the desktop, to remind users the system has test-signing enabled.
    **Note**  Starting with Windows 7, Windows displays this watermark only in the lower right-hand corner of the desktop.

-   Displays a watermark with the text "Test Mode" in the lower-left corner of the desktop to remind users that the system has test-signing enabled.

-   The operating system loader and the kernel load drivers that are signed by any certificate. The certificate validation is not required to chain up to a trusted root certification authority. However, each driver image file must have a digital signature.
