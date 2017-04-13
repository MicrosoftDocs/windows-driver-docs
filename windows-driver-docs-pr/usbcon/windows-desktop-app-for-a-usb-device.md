---
Description: In this topic you'll learn about how an application can call WinUSB Functions to communicate with a USB device.
MS-HAID: buses.windows\_desktop\_app\_for\_a\_usb\_device
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: Windows desktop app for a USB device
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

**Note**  WinUSB functions require Windows XP or later. You can use these functions in your C/C++ application to communicate with your USB device. To write a Windows Store app that uses WinUSB APIs, see [Windows Store app for a USB device](writing-usb-device-companion-apps-for-windows-store.md).

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
<li>Install [Microsoft Visual Studio (Ultimate or Professional)]( http://go.microsoft.com/fwlink/p/?LinkId=623328).</li>
<li>Install the [Windows Driver Kit (WDK) 8.1](http://download.microsoft.com/download/E/C/E/ECE11176-1E40-46E7-A24B-D507D7F6FB65/wdk/wdksetup.exe).</li>
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
<li>OSR USB FX2 learning kit. The kit is the most suitable to study USB samples included in this documentation set. You can get the learning kit from [OSR Online](http://www.osronline.com/).</li>
<li>Microsoft USB Test Tool (MUTT) devices. MUTT hardware can be purchased from [JJG Technologies](http://jjgtechnologies.com/mutt.md). The device does not have installed firmware installed. To install firmware, download the MUTT software package from [this Web site](mutt-software-package.md) and run MUTTUtil.exe. For more information, see the documentation included with the package.</li>
</ul></td>
</tr>
<tr class="odd">
<td><p><strong>Step 3</strong>—Write a skeleton app that obtains a handle to the device.</p></td>
<td><p>You can write your first app in one of two ways:</p>
<ul>
<li><p>Write your app based on the WinUSB template included in Visual Studio. For more information, see [Write a Windows desktop app based on the WinUSB template](how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md).</p></li>
<li><p>Call [SetupAPI](https://msdn.microsoft.com/library/windows/hardware/ff550855) routines to get a handle to your device and open it by calling [<strong>WinUsb_Initialize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540277). For more information, see [How to Access a USB Device by Using WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md).</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p><strong>Step 6</strong>—Install Winusb.sys for your device.</p></td>
<td><p>Install Winusb.sys for your device.</p>
<ul>
<li>If you are using Visual Studio, install the driver package on the target computer by using Visual Studio deployment. For instructions, see [Write a Windows desktop app based on the WinUSB template](how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md).</li>
<li>Otherwise, manually install the driver in Device Manager by writing a custom INF. For more information, see [WinUSB (Winusb.sys) Installation](winusb-installation.md).</li>
</ul></td>
</tr>
<tr class="odd">
<td><p><strong>Step 4</strong>—Get information about your device and view its descriptors. For conceptual information, see [Concepts for all USB developers](usb-concepts-for-all-developers.md).</p></td>
<td><p>Get information about your device capabilities by reading the configuration descriptor, interface descriptors for each supported alternate settings, and their endpoint descriptors.</p>
<p>For information, see [Query the Device for USB Descriptors](using-winusb-api-to-communicate-with-a-usb-device.md#query).</p></td>
</tr>
<tr class="even">
<td><strong>Step 5</strong>—Send a USB control transfer from your app.</td>
<td><p>Send standard control requests and vendor commands to your device. For more information, see [Send Control Transfer to the Default Endpoint](using-winusb-api-to-communicate-with-a-usb-device.md#control).</p></td>
</tr>
<tr class="odd">
<td><p><strong>Step 6</strong>—Send bulk or interrupt transfers from your app.</p></td>
<td><p>Perform read and write operations to and from the bulk, interrupt, and isochronous endpoints supported by your device. For more information, see [Issue I/O Requests](using-winusb-api-to-communicate-with-a-usb-device.md#io).</p></td>
</tr>
<tr class="even">
<td><p><strong>Step 7</strong>—Send isochronous transfers from your app.</p></td>
<td><p>Send isochronous read and write requests, mostly used for streaming data. This feature is only available on Windows 8.1. For more information, see [Sending USB isochronous transfers from a WinUSB desktop app](getting-set-up-to-use-windows-devices-usb.md).</p></td>
</tr>
</tbody>
</table>

 

## Related topics


****
[Developing Windows applications for USB devices](developing-windows-applications-that-communicate-with-a-usb-device.md)

[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Windows%20desktop%20app%20for%20a%20USB%20device%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




