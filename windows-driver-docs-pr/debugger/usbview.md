---
title: USBView
description: USBView
ms.assetid: 88d2a93f-2e7c-493c-bb9e-487f1d1f2016
keywords: ["USBView"]
ms.author: domars
ms.date: 02/22/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# USBView

USBView (Universal Serial Bus Viewer, USBView.exe) is a Windows graphical user interface application that enables you to browse all USB controllers and connected USB devices on your computer. USBView works on all versions of Windows.

## <span id="Where_to_get_USBView"></span><span id="where_to_get_usbview"></span><span id="WHERE_TO_GET_USBVIEW"></span>Where to get USBView

To download  and use USBView complete the following steps:

1. [Download and install the Windows SDK](https://developer.microsoft.com/windows/downloads/windows-10-sdk).

2. During the installation, select just the **Debugging Tools for Windows** box and clear all the other boxes.

3. By default on a x64 PC the SDK will install USBView to this directory.

   ```C:\Program Files (x86)\Windows Kits\10\Debuggers\x64```

4. Navigate to the kits debugger directory for the processor type you are running and click on usbview.exe to start the utility.


## USBView Source Code

[USBView](http://go.microsoft.com/fwlink/p/?LinkId=618004) is also available in the [Windows driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616507) repository on GitHub.

## <span id="using_usbview"></span><span id="USING_USBVIEW"></span>Using USBView


USBView can enumerate USB host controllers, USB hubs, and attached USB devices. It can also query information about the devices from the registry and through USB requests to the devices.

The main USBView window contains two panes. The left pane displays a connection-oriented tree view, enabling you to select any USB device.

The right pane displays the USB data structures that pertain to the selected USB device. These structures include Device, Configuration, Interface, and Endpoint Descriptors, as well as the current device configuration.


## Using Device Manager to Display USB Information

To use Windows Device Manager to display USB information:

1. Type the Windows Key + R and enter in ```devmgmt.msc``` into the pop-up box and press Enter.

2. In Device Manager, click your computer so that it is highlighted.

3. Click **Action**, and then click **Scan for hardware changes**.

4. Select **View** and then click **Hidden Devices** to display additional devices, for example those that are not currently active. 

5. Expand the *Universal Serial Bus controllers* node in Device Manager.

6. Locate the device in question, for example *USB Mass Storage Device*.

7. Right click on the device and select **Properties** to view summary device status information.

8. Click on the **Details** tab to view additional information. 

9. Use the **Property** pull down box to view desired information such as *Status* or *Problem code*.


## USB Troubleshooter

If you are trying to diagnose a USB device that does not eject using the Safely Remove Hardware dialog box, you might want to try the [Windows USB Troubleshooter](https://support.microsoft.com/help/17614/automatically-diagnose-and-fix-windows-usb-problems).


 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20USBView%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




