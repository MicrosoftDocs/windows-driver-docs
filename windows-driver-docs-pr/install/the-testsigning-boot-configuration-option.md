---
title: Loading Test Signed Code
description: Describes how to enable loading of test signed drivers using the TESTSIGNING option with BCDEdit tool.
ms.date: 04/16/2025
ms.topic: concept-article
---

# Enable loading of test-signed drivers

By default, Windows doesn't load test-signed kernel-mode drivers. To enable loading of test-signed drivers, use BCDEdit.exe to enable or disable the TESTSIGNING boot configuration option. You must have administrator rights to enable this option.

> [!NOTE]
> The kernel-mode code signing policy requires that all kernel-mode code have a digital signature to load on 64-bit versions of Windows. However, in most cases, an unsigned driver can be installed and loaded on 32-bit versions of Windows. For more information, see [Driver Signing Policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md).

## Administrator rights required

To use BCDEdit, you must be a member of the Administrators group on the system and run the command from an elevated command prompt. To open an elevated Command Prompt window, type **cmd** into the search box in the Windows taskbar, right-click **Command Prompt** in the search results, and select **Run as administrator**.

> [!WARNING]
> Administrative rights are required to use BCDEdit to modify boot configuration data. Changing some boot entry options by using **BCDEdit /set** could render your computer inoperable. As an alternative, use System Configuration utility (MSConfig.exe) to change boot settings.

## Enable or disable use of test-signed code

Run BCDEdit command lines to enable or disable the loading of test-signed code. For a change to take effect, whether enabling or disabling the option, you must restart the computer after changing the configuration.

To enable test-signed code, use the following BCDEdit command line:

```cmd
:: If this command results in "The value is protected by Secure Boot policy and cannot be modified or deleted"
:: Then reboot the PC, go into BIOS settings, and disable Secure Boot. BitLocker may also affect your ability to modify this setting.
Bcdedit.exe -set TESTSIGNING ON
```

> [!NOTE]
> Starting in Windows 10, version 1507, if you have Memory Integrity / HVCI (Hypervisor Code Integrity) enabled, you must test-sign the binary using any self-created test cert. An unsigned binary isn't supported.

To disable use of test-signed code, use the following BCDEdit command line:

```cmd
Bcdedit.exe -set TESTSIGNING OFF
```

The following figure shows the result of using the BCDEdit command line to enable test-signing.

:::image type="content" source="images/driver-signing-enable-vista-test-signing.png" alt-text="Screen shot showing the results of using the TESTSIGNING boot configuration option.":::

## Behavior of Windows when loading test-signed code is enabled

When loading test-signed code is enabled, Windows displays a watermark with the text "Test Mode" in the lower right corner of the desktop to remind users that the system has test-signing enabled. Any certificate can sign drivers that the operating system and kernel load. Certificate validation isn't required to come from a trusted root certification authority. However, each driver image file must have a digital signature.
