---
Description: Learn about how an application can call WinUSB Functions to communicate with a USB device.
title: Windows desktop app for a USB device
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows desktop app for a USB device


In this topic you'll learn about how an application can call [WinUSB Functions](https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb) to communicate with a USB device. For such an application, [WinUSB](winusb.md) (Winusb.sys) must be installed as the device's function driver. WinUSB in the device's kernel-mode stack. This driver is included in Windows in the \\Windows\\System32\\drivers folder.

If you are using Winusb.sys as a USB device's function driver, you can call [WinUSB Functions](https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb) from an application to communicate with the device. These functions, exposed by the user-mode DLL Winusb.dll, simplify the communication process. Instead of constructing device I/O control requests to perform standard USB operations (such as configuring the device, sending control requests, and transferring data to or from the device), applications call the equivalent WinUSB function.

Winusb.dll uses the application-supplied data to construct the appropriate device I/O control request, and then sends the request to Winusb.sys for processing. To communicate with the USB stack, the WinUSB function calls the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the appropriate IOCTL that correlates to the application's request. When the request is complete, the WinUSB function passes any information returned by Winusb.sys (such as data from a read request) back to the calling process. If the call to **DeviceIoControl** is successful, it returns a nonzero value. If the call fails or is pending (not processed immediately), **DeviceIoControl** returns a zero value. In case of an error, the application can call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) for a more detailed error message.

It is simpler to use WinUSB functions to communicate with a device than it is to implement a driver. However, note the following limitations:

-   WinUSB functions allow one application at a time to communicate with the device. If you require more than one application to communicate concurrently with a device, you must implement a function driver.
-   Before Windows 8.1, WinUSB functions do not support streaming data to or from isochronous endpoints.
-   WinUSB functions do not support devices that already have kernel-mode support. Examples of such devices include modems and network adapters, which are supported by the telephony API (TAPI) and NDIS, respectively.
-   For multifunction devices, you can use the device's INF file to specify either an in-box kernel-mode driver or Winusb.sys for each USB function separately. However, you can specify only one of these options for a particular function, not both.

**Note**  WinUSB functions require Windows XP or later. You can use these functions in your C/C++ application to communicate with your USB device. To write a UWP app that uses WinUSB APIs, see [UWP app for a USB device](writing-usb-device-companion-apps-for-microsoft-store.md).

## Getting started...


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Step</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Step 1</strong>—Get the tools you need to write a Windows desktop app for devices.</p></td>
<td><ul>
<li>Install <a href="http://go.microsoft.com/fwlink/p/?LinkId=623328" data-raw-source="[Microsoft Visual Studio (Ultimate or Professional)]( http://go.microsoft.com/fwlink/p/?LinkId=623328)">Microsoft Visual Studio (Ultimate or Professional)</a>.</li>
<li>Install the <a href="http://download.microsoft.com/download/E/C/E/ECE11176-1E40-46E7-A24B-D507D7F6FB65/wdk/wdksetup.exe" data-raw-source="[Windows Driver Kit (WDK) 8.1](http://download.microsoft.com/download/E/C/E/ECE11176-1E40-46E7-A24B-D507D7F6FB65/wdk/wdksetup.exe)">Windows Driver Kit (WDK) 8.1</a>.</li>
</ul>
<div class="alert">
<strong>Note</strong>  Visual Studio must be installed before installing the WDK 8.1.
</div>
<div>
 
</div></td>
</tr>
<tr class="even">
<td><p><strong>Step 2</strong>—Obtain a test USB device and its hardware specification. Use the specification to determine the functionality of the app and the related design decisions.</p></td>
<td><p>For learning purposes, popular choices are:</p>
<ul>
<li>OSR USB FX2 learning kit. The kit is the most suitable to study USB samples included in this documentation set. You can get the learning kit from <a href="http://www.osronline.com/" data-raw-source="[OSR Online](http://www.osronline.com/)">OSR Online</a>.</li>
<li>Microsoft USB Test Tool (MUTT) devices. MUTT hardware can be purchased from <a href="http://jjgtechnologies.com/mutt.md" data-raw-source="[JJG Technologies](http://jjgtechnologies.com/mutt.md)">JJG Technologies</a>. The device does not have installed firmware installed. To install firmware, download the MUTT software package from <a href="mutt-software-package.md" data-raw-source="[this Web site](mutt-software-package.md)">this Web site</a> and run MUTTUtil.exe. For more information, see the documentation included with the package.</li>
</ul></td>
</tr>
<tr class="odd">
<td><p><strong>Step 3</strong>—Write a skeleton app that obtains a handle to the device.</p></td>
<td><p>You can write your first app in one of two ways:</p>
<ul>
<li><p>Write your app based on the WinUSB template included in Visual Studio. For more information, see <a href="how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md" data-raw-source="[Write a Windows desktop app based on the WinUSB template](how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md)">Write a Windows desktop app based on the WinUSB template</a>.</p></li>
<li><p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550855" data-raw-source="[SetupAPI](https://msdn.microsoft.com/library/windows/hardware/ff550855)">SetupAPI</a> routines to get a handle to your device and open it by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff540277" data-raw-source="[&lt;strong&gt;WinUsb_Initialize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540277)"><strong>WinUsb_Initialize</strong></a>. For more information, see <a href="using-winusb-api-to-communicate-with-a-usb-device.md" data-raw-source="[How to Access a USB Device by Using WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md)">How to Access a USB Device by Using WinUSB Functions</a>.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p><strong>Step 6</strong>—Install Winusb.sys for your device.</p></td>
<td><p>Install Winusb.sys for your device.</p>
<ul>
<li>If you are using Visual Studio, install the driver package on the target computer by using Visual Studio deployment. For instructions, see <a href="how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md" data-raw-source="[Write a Windows desktop app based on the WinUSB template](how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md)">Write a Windows desktop app based on the WinUSB template</a>.</li>
<li>Otherwise, manually install the driver in Device Manager by writing a custom INF. For more information, see <a href="winusb-installation.md" data-raw-source="[WinUSB (Winusb.sys) Installation](winusb-installation.md)">WinUSB (Winusb.sys) Installation</a>.</li>
</ul></td>
</tr>
<tr class="odd">
<td><p><strong>Step 4</strong>—Get information about your device and view its descriptors. For conceptual information, see <a href="usb-concepts-for-all-developers.md" data-raw-source="[Concepts for all USB developers](usb-concepts-for-all-developers.md)">Concepts for all USB developers</a>.</p></td>
<td><p>Get information about your device capabilities by reading the configuration descriptor, interface descriptors for each supported alternate settings, and their endpoint descriptors.</p>
<p>For information, see <a href="using-winusb-api-to-communicate-with-a-usb-device.md#query" data-raw-source="[Query the Device for USB Descriptors](using-winusb-api-to-communicate-with-a-usb-device.md#query)">Query the Device for USB Descriptors</a>.</p></td>
</tr>
<tr class="even">
<td><strong>Step 5</strong>—Send a USB control transfer from your app.</td>
<td><p>Send standard control requests and vendor commands to your device. For more information, see <a href="using-winusb-api-to-communicate-with-a-usb-device.md#control" data-raw-source="[Send Control Transfer to the Default Endpoint](using-winusb-api-to-communicate-with-a-usb-device.md#control)">Send Control Transfer to the Default Endpoint</a>.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Step 6</strong>—Send bulk or interrupt transfers from your app.</p></td>
<td><p>Perform read and write operations to and from the bulk, interrupt, and isochronous endpoints supported by your device. For more information, see <a href="using-winusb-api-to-communicate-with-a-usb-device.md#io" data-raw-source="[Issue I/O Requests](using-winusb-api-to-communicate-with-a-usb-device.md#io)">Issue I/O Requests</a>.</p></td>
</tr>
<tr class="even">
<td><p><strong>Step 7</strong>—Send isochronous transfers from your app.</p></td>
<td><p>Send isochronous read and write requests, mostly used for streaming data. This feature is only available on Windows 8.1. For more information, see <a href="getting-set-up-to-use-windows-devices-usb.md" data-raw-source="[Sending USB isochronous transfers from a WinUSB desktop app](getting-set-up-to-use-windows-devices-usb.md)">Sending USB isochronous transfers from a WinUSB desktop app</a>.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[Developing Windows applications for USB devices](developing-windows-applications-that-communicate-with-a-usb-device.md)  
[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)  



