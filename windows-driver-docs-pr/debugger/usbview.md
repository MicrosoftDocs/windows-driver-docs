---
title: USBView
description: USBView
ms.assetid: 88d2a93f-2e7c-493c-bb9e-487f1d1f2016
keywords: ["USBView"]
ms.author: domars
ms.date: 02/22/2017
ms.localizationpriority: medium
---

# USBView

USBView (Universal Serial Bus Viewer, USBView.exe) is a Windows graphical user interface application that enables you to browse all USB controllers and connected USB devices on your computer. USBView works on all versions of Windows.

## <span id="Where_to_get_USBView"></span><span id="where_to_get_usbview"></span><span id="WHERE_TO_GET_USBVIEW"></span>Where to get USBView

To download  and use USBView complete the following steps:

1. [Download and install the Windows SDK](https://developer.microsoft.com/windows/downloads/windows-10-sdk).

2. During the installation, select just the **Debugging Tools for Windows** box and clear all the other boxes.

3. By default on a x64 PC the SDK will install USBView to this directory.

   `C:\Program Files (x86)\Windows Kits\10\Debuggers\x64`

4. Navigate to the kits debugger directory for the processor type you are running and click on usbview.exe to start the utility.


## USBView Source Code

[USBView](https://go.microsoft.com/fwlink/p/?LinkId=618004) is also available in the [Windows driver samples](https://go.microsoft.com/fwlink/p/?LinkId=616507) repository on GitHub.

## <span id="using_usbview"></span><span id="USING_USBVIEW"></span>Using USBView


USBView can enumerate USB host controllers, USB hubs, and attached USB devices. It can also query information about the devices from the registry and through USB requests to the devices.

The main USBView window contains two panes. The left pane displays a connection-oriented tree view, enabling you to select any USB device.

The right pane displays the USB data structures that pertain to the selected USB device. These structures include Device, Configuration, Interface, and Endpoint Descriptors, as well as the current device configuration.


## Using Device Manager to Display USB Information

To use Windows Device Manager to display USB information:

1. Type the Windows Key + R and enter in `devmgmt.msc` into the pop-up box and press Enter.

2. In Device Manager, click your computer so that it is highlighted.

3. Click **Action**, and then click **Scan for hardware changes**.

4. Select **View** and then click **Hidden Devices** to display additional devices, for example those that are not currently active. 

5. Expand the *Universal Serial Bus controllers* node in Device Manager.

6. Locate the device in question, for example *USB Mass Storage Device*.

7. Right click on the device and select **Properties** to view summary device status information.

8. Click on the **Details** tab to view additional information. 

9. Use the **Property** pull down box to view desired information such as *Status* or *Problem code*.


## Windows USB Troubleshooter

If you are trying to diagnose a USB device that does not eject using the Safely Remove Hardware dialog box, you might want to try the [Windows USB Troubleshooter](https://support.microsoft.com/help/17614/automatically-diagnose-and-fix-windows-usb-problems).


 

 





