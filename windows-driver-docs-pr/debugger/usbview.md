---
title: Universal Serial Bus Viewer in Windows
description: Explore the Universal Serial Bus Viewer (USBView) in Windows and browse all USB controllers and connected USB devices on your computer.
keywords: ["USBView"]
ms.date: 07/11/2025
ms.topic: how-to
---

# Universal Serial Bus Viewer in Windows

The Universal Serial Bus Viewer (USBView) or _usbview.exe_ is a Windows app that you can use to browse all USB controllers and connected USB devices on your computer. USBView works on all versions of Windows.

## Get the USBView app

To download and use USBView, complete the following steps:

1. [Download and install the Windows SDK](https://developer.microsoft.com/windows/downloads/windows-sdk/).

1. During installation, select the **Debugging Tools for Windows** option, and clear all other checkboxes.

1. Open the _Windows Kits_ debugger folder for the processor type you're running, and select _usbview.exe_ to start the utility.

   The default install location for USBView on x64 systems is _C:\Program Files (x86)\Windows Kits\10\Debuggers\x64_.

   > [!NOTE]
   > If you don't see the _usbview.exe_ file in the folder, make sure you installed Windows SDK in the correct folder. If the problem persists, reinstall the Windows SDK and be sure to select the **Debugging Tools for Windows** options during installation.

### Access USBView source code on GitHub

The [USBView application and source code](https://github.com/Microsoft/Windows-driver-samples/tree/main/usb/usbview) are available in the [Windows driver samples](https://github.com/Microsoft/Windows-driver-samples) repository on GitHub.

## Use the USBView app

USBView is a sample application that enumerates basic information about USB host controllers, USB hubs, and attached USB devices. It also queries information about devices from the registry and through USB requests to the devices.

The main USBView window contains two panes:

- The left pane displays a connection-oriented tree view that you can use to select any USB device.

- The right pane displays the USB data structures that pertain to the selected USB device. These structures include Device, Configuration, Interface, and Endpoint Descriptors, and the current device configuration.

Because USBView is an older application, it might not display newer USB information. Use other tools like Device Manager when necessary. For more information on the IOCTLs that USBView uses to query information, see [USBView](https://github.com/Microsoft/Windows-driver-samples/tree/main/usb/usbview).

## Use Device Manager to display USB information

To use Device Manager to display USB information, follow these steps:

1. Use the **Windows Key** + **R** keyboard shortcut to open the **Run** command dialog. Enter _devmgmt.msc_ and select **OK** or **Enter**.

1. In Device Manager, select your computer so the item is highlighted in the list.

1. Select **Action**, and then select **Scan for hardware changes**.

1. Select **View**, and then select **Show hidden devices** to display more devices (for example, devices that aren't currently active).

1. Expand the **Universal Serial Bus controllers** node in Device Manager and select the device.

1. Right-click and select **Properties** to view summary device status information.

1. Select the **Details** tab to view more information.

1. Select **Property** to view details, such as **Status** or **Problem code**.

## Troubleshoot common USB problems

If you're trying to diagnose a USB device, more information is available at [Fix USB-C problems in Windows](https://support.microsoft.com/windows/fix-usb-c-problems-in-windows-f4e0e529-74f5-cdae-3194-43743f30eed2).