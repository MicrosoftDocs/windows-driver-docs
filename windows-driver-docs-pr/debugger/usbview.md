---
title: Universal Serial Bus Viewer in Windows
description: Universal Serial Bus Viewer is a Windows graphical UI app that you can use to browse all USB controllers and connected USB devices on your computer.
keywords: ["USBView"]
ms.date: 12/20/2023
---

# Universal Serial Bus Viewer in Windows

The Universal Serial Bus Viewer (USBView) or usbview.exe is a Windows app that you can use to browse all USB controllers and connected USB devices on your computer. USBView works on all versions of Windows.

## Where to get USBView

To download  and use USBView, complete the following steps:

1. [Download and install the Windows SDK](https://developer.microsoft.com/windows/downloads/windows-sdk/).

1. During the installation, select only the **Debugging Tools for Windows** box and clear all other boxes.

1. By default, on a x64 PC the SDK will install USBView to the following directory.

   `C:\Program Files (x86)\Windows Kits\10\Debuggers\x64`

1. Open the kits debugger directory for the processor type you're running, and then select usbview.exe to start the utility.

## USBView source code

[USBView](https://github.com/Microsoft/Windows-driver-samples/tree/main/usb/usbview) is also available in the [Windows driver samples](https://github.com/Microsoft/Windows-driver-samples) repository on GitHub.

## Use USBView

USBView is a sample application that enumerates basic information about USB host controllers, USB hubs, and attached USB devices. It also queries information about devices from the registry and through USB requests to the devices.

The main USBView window contains two panes. The left pane displays a connection-oriented tree view that you can use to select any USB device.

The right pane displays the USB data structures that pertain to the selected USB device. These structures include Device, Configuration, Interface, and Endpoint Descriptors, and the current device configuration.

As USBView is an older application, it may not display newer USB information. Other tools like Device Manager should be used as necessary. For more information on the IOCTLs that USBView uses to query information, see [USBView](https://github.com/Microsoft/Windows-driver-samples/tree/main/usb/usbview).

## Use Device Manager to display USB info

To use Device Manager to display USB info:

1. Select Windows logo key+R, enter **devmgmt.msc** into the pop-up box, and then select Enter.

1. In Device Manager, select your computer so that it's highlighted.

1. Select **Action**, and then select **Scan for hardware changes**.

1. Select **View**, and then select **Show hidden devices** to display more devices (for example, devices that aren't currently active).

1. Expand the **Universal Serial Bus controllers** node in Device Manager and select the device in question.

1. Right-click and select **Properties** to view summary device status info.

1. Select the **Details** tab to view more info.

1. Select **Property** to view details such as **Status** or **Problem code**.

## Troubleshoot common USB problems

If you're trying to diagnose a USB device, more information is available at [Troubleshoot common USB problems](https://support.microsoft.com/windows/troubleshoot-common-usb-problems-5e9a9b49-ad43-702e-083e-6107e95deb88).
