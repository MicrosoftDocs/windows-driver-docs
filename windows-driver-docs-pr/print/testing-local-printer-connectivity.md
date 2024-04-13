---
title: Testing Local Printer Connectivity
description: Testing Local Printer Connectivity
keywords:
- testing drivers WDK printer
- printer drivers WDK , testing
- local printer testing WDK
- connections WDK printer
ms.date: 01/30/2023
---

# Testing Local Printer Connectivity

[!include[Print Support Apps](../includes/print-support-apps.md)]

This section provides general guidelines for how to test the connectivity of a printer that is connected locally. You can apply these principles to any bus or port to which you connect a print device, although some principles might not apply due to the inherent nature of your bus or port.

The following information describes testing on Microsoft Windows XP. Features of other operating system versions, such as control panel applications and menu options, might differ slightly.

## Setting Up Device Testing

Before proceeding with any testing of your device, make sure you set up your debugging session as follows to catch any problems you might encounter. See [Debugging Printer Drivers and Spooler Components](debugging-printer-drivers-and-spooler-components.md) for how to properly set up your test environment.

1. Set up Application Verifier, with the default settings enabled, to monitor Spoolsv.exe. Testing on a wide variety of hardware, including 32- and 64-bit machines, is recommended.

1. Use the Driver Verifier tool to monitor any kernel-mode drivers that you are using. For printer drivers, be sure to include Win32k.sys. See [Driver Verifier](../devtest/driver-verifier.md) for information about setting up your test environment to use the tool.

1. For power management testing, before a device is attached, make sure that your test environment supports all possible system power states and that the device can enter and wake from all states successfully.

The following sections describe the common test scenarios to address when testing a port-connected device.

- [Device Installation](device-installation.md)

- [Device Functionality](testing-device-functionality.md)

- [Device Error States](device-error-states.md)

- [Power Management](power-management.md)

- [Stress Testing](stress-testing.md)
