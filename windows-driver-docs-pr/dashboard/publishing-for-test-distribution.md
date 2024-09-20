---
title: Test distribution guidance to self-host desktop drivers
description: Hardware partners can test OS upgrade scenarios by publishing a driver to Windows Update and using test distribution.
ms.topic: article
ms.date: 09/17/2024
---

# Test distribution guidance to self-host desktop drivers

Hardware partners can test OS upgrade scenarios by publishing a driver to Windows Update and using test distribution. Once published, IHVs/OEMs can configure their client systems to request these drivers by configuring a predefined registry key value. In addition to receiving drivers distributed for testing, production drivers are still offered to the same client machine. The testing registry key adds prerelease drivers to the list of production drivers offered by Windows Update. This method restricts prerelease drivers from being offered to the general public.

Client systems can participate in receiving test distributed drivers throughout the Windows upgrade process. Hardware partners can test OS upgrade scenarios using this test distribution process.

## What is test distribution, and why do I need it?

By publishing drivers for test distribution and configuring client systems to receive test distributed drivers, you enable that system to receive all prerelease drivers and firmware content that are published on Windows Update. Partners can publish drivers using Windows Update to their test audience without impacting their retail consumer audience.

## Publishing drivers with test distribution

Publishing drivers for test distribution can be done for Windows 7, Windows 8.x, and Windows 10 systems. To publish a test distribution, [create a shipping label](manage-driver-distribution-by-submission.md) as normal and select the "Test Registry Key" checkbox in the Targeting section.

:::image type="content" source="images/test-registry-key-checkbox.png" alt-text="Screenshot showing the 'test registry key' checkbox.":::

## Removing drivers published for test distribution

### How do I manually remove my driver published for test distribution?

Once a driver is published for test distribution, it can be manually expired or republished for (normal) distribution.

### How long does my driver published for test distribution last?

Drivers don't automatically expire from the test distribution workflow. After you complete testing, manually remove a driver using the procedure described in [Expire a driver from Windows Update](expire-a-driver-from-windows-update.md).

## Client PC configuration

### How do I configure my machine to receive test distribution drivers?

Configuring a system to receive test distribution updates can be performed with the following steps:

1. Open the Windows Registry Editor (regedit.exe)
1. Go to HKLM\\Software\\Microsoft\\
1. Create subkeys \\DriverFlighting\\Partner\\
1. Under the \\Partner subkey, create a string named **TargetRing** and type **Drivers** as the value
1. Make sure you have the setting as shown:

    :::image type="content" source="images/registry-editor-drivers.png" alt-text="Screenshot showing the created string under the partner subkey, within the windows registry editor.":::

1. Exit Windows Registry Editor. You don't need to restart the computer after this change.
1. Do one of the following options:
    - Run Windows Update and check for updates.
    - In Device Manager, right-click on the target device and select **Update Device Software**.
1. Verify that your test driver is offered as expected

    - If you run into issues, contact Customer Service and Support.

        :::image type="content" source="images/dashboard-help-button.png" alt-text="Screenshot showing the button to contact customer service and support.":::

### How do I stop my PC from receiving test distribution drivers?

To stop receiving test distribution drivers, remove the **TargetRing** registry data value you created in the previous section. Double-click on the **Drivers** data value to remove it, and then select **OK**. Prerelease drivers are no longer offered to your client system.

> [!NOTE]
> Your system continues to receive all production drivers from Windows Update.

1. Open the Windows Registry Editor (regedit.exe)
1. Go to HKLM\\Software\\Microsoft\\DriverFlighting\\Partner. If these keys don't exist, you're done. Otherwise, continue to the next step.
1. Under \\Partner subkey, remove the data value for **TargetRing**
1. Make sure the setting appears as shown:

    :::image type="content" source="images/registry-editor-no-drivers.png" alt-text="Screenshot showing the removed string value under the partner subkey, within the windows registry editor.":::

1. Exit Windows Registry Editor. You don't need to restart the computer after this change.
1. Do one of the following options:
    - Run Windows Update and check for updates
    - In Device Manager, right-click on the target device, and select **Update Device Software**.
