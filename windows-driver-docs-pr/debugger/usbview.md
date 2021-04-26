---
title: USBView in Windows
description: USBView
keywords: ["USBView"]
ms.date: 02/22/2017
ms.localizationpriority: high 
---

# USBView

Universal Serial Bus Viewer (USBView) or USBView.exe is a Windows graphical UI app that you can use to browse all USB controllers and connected USB devices on your computer. USBView works on all versions of Windows.

## <span id="Where_to_get_USBView"></span><span id="where_to_get_usbview"></span><span id="WHERE_TO_GET_USBVIEW"></span>Where to get USBView

To download  and use USBView, complete the following steps:

1. [Download and install the Windows SDK](https://developer.microsoft.com/windows/downloads/windows-10-sdk).

2. During the installation, select only the **Debugging Tools for Windows** box and clear all other boxes.

3. By default, on a x64 PC the SDK will install USBView to the following directory.

   `C:\Program Files (x86)\Windows Kits\10\Debuggers\x64`

4. Open the kits debugger directory for the processor type you're running, and then select USBView.exe to start the utility.


## USBView source code

[USBView](https://github.com/Microsoft/Windows-driver-samples/tree/master/usb/usbview) is also available in the [Windows driver samples](https://github.com/Microsoft/Windows-driver-samples) repository on GitHub.

## <span id="using_usbview"></span><span id="USING_USBVIEW"></span>Use USBView


USBView can enumerate USB host controllers, USB hubs, and attached USB devices. It can also query information about the devices from the registry and through USB requests to the devices.

The main USBView window contains two panes. The left pane displays a connection-oriented tree view that you can use to select any USB device.

The right pane displays the USB data structures that pertain to the selected USB device. These structures include Device, Configuration, Interface, and Endpoint Descriptors, as well as the current device configuration.


## Use Device Manager to display USB info

To use Device Manager to display USB info:

1. Select Windows logo key+R, enter **devmgmt.msc** into the pop-up box, and then select Enter.

2. In Device Manager, select your computer so that it's highlighted.

3. Select **Action**, and then select **Scan for hardware changes**.

4. Select **View**, and then select **Hidden Devices** to display additional devices (for example, those that are not currently active). 

5. Expand the **Universal Serial Bus controllers** node in Device Manager and select the device in question.

6. Select and hold (or right-click) to select **Properties** and view summary device status info.

7. Select the **Details** tab to view additional info. 

8. Select **Property** to view details such as **Status** or **Problem code**.


## Windows USB troubleshooter

If you're trying to diagnose a USB device that doesn't eject using the **Safely Remove Hardware** dialog box, try using the [Windows USB Troubleshooter](https://support.microsoft.com/help/17614/windows-10-troubleshoot-common-usb-problems).


 

 





