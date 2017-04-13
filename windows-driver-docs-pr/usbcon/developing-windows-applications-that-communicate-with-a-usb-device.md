---
Description: This topic provides guidelines for deciding whether you should write a Windows Store app or a Windows desktop app to communicate with a USB device.
MS-HAID: buses.developing\_windows\_applications\_that\_communicate\_with\_a\_usb\_device
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: Developing Windows applications for USB devices
---

# Developing Windows applications for USB devices


**Summary**

-   Guidelines for choosing the right programming model
-   Windows Store app and desktop app developer experience

**Important APIs**

-   [**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466)
-   [WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md)

This topic provides guidelines for deciding whether you should write a Windows Store app or a Windows desktop app to communicate with a USB device.

Windows provides API sets that you can use to write apps that talk to a custom USB devices. The API performs common USB-related tasks such as, finding the device, data transfers.

"Custom device" in this context means, a device for which Microsoft does not provide an in-box class driver. Instead, you can install WinUSB (Winusb.sys) as the device driver.

## Choosing a programming model


If you install [Winusb.sys](winusb-installation.md), here are the programming model options:

-   [Windows Store app for a USB device](writing-usb-device-companion-apps-for-windows-store.md)

    Windows 8.1 provides a new namespace: [**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466). The namespace cannot be used in earlier version of Windows. Other Windows Store resources are here: [Windows Store app](http://msdn.microsoft.com/windows/apps).

-   [Windows desktop app for a USB device](windows-desktop-app-for-a-usb-device.md)

    Before Windows 8.1, apps that were communicating through [Winusb.sys](winusb-installation.md), were desktop apps written by using [WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md). In Windows 8.1, the API set has been extended. Other Windows desktop app resources are here: [Windows desktop app](https://dev.windows.com/desktop).

The strategy for choosing the best programming model depends on various factors.

-   **Will your app communicate with an internal USB device?**

    The APIs are primarily designed for accessing peripheral devices. The API can also access PC internal USB devices. However access to PC internal USB devices from a Windows Store app is limited to a privileged app that is explicitly declared in device metadata by the OEM for that PC.

-   **Will your app communicate with USB isochronous endpoints?**

    If your app transmits data to or from isochronous endpoints of the device, you must write a Windows desktop app. In Windows 8.1, new [WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md) have been added to the API set that allow a desktop app to send data to and receive data from isochronous endpoints.

-   **Is your app a "control panel" type of app?**

    Windows Store apps are per-user apps and do not have the ability to make changes outside the scope of each app. For these types of apps, you must write a Windows desktop app.

-   **Is the USB device class supported classes by Windows Store apps?**

    Write a Windows Store app if your device belongs to one these device classes.

    -   `name:cdcControl,           classId:02 * *`
    -   `name:physical, classId:05 * *`
    -   `name:personalHealthcare,   classId:0f 00 00`
    -   `name:activeSync,           classId:ef 01 01`
    -   `name:palmSync,             classId:ef 01 02`
    -   `name:deviceFirmwareUpdate, classId:fe 01 01`
    -   `name:irda,                 classId:fe 02 00     `
    -   `name:measurement,          classId:fe 03 *`
    -   `name:vendorSpecific,       classId:ff * *`

    **Note**  If your device belongs to DeviceFirmwareUpdate class, your app must be a privileged app.

     

    If your device does not belong to one the preceding device classes, write a Windows desktop app.

## Driver requirement


| Driver requirement | Windows Store app                                                                                                                          | Windows desktop app                                                                                                                       |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Function driver    | Microsoft-provided [Winusb.sys](winusb-installation.md) (kernel-mode driver).                                                             | Microsoft-provided [Winusb.sys](winusb-installation.md) (kernel-mode driver).                                                            |
| Filter driver      | If filter drivers are present, access is limited to privileged apps. The app is declared as privileged apps in device metadata by the OEM. | Filter driver can be present in the kernel mode device stack as long as it doesn't block access to [Winusb.sys](winusb-installation.md). |

 

## Code samples


<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Sample</th>
<th>Windows Store app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Get started with these samples</td>
<td><ul>
<li>[Custom USB device access sample](http://go.microsoft.com/fwlink/p/?linkid=309716)</li>
<li>[USB CDC Control sample](http://go.microsoft.com/fwlink/p/?linkid=309716)</li>
<li>[Firmware Update USB Device sample](http://go.microsoft.com/fwlink/p/?linkid=309716)</li>
</ul></td>
<td><ul>
<li>Start with the <strong>WinUsb Application</strong> template included with Microsoft Visual Studio (Ultimate or Professional)</li>
<li>Extend the template by using code examples shown in [How to Access a USB Device by Using WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md).</li>
</ul></td>
</tr>
</tbody>
</table>

 

## Development tools


<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Development tools</th>
<th>Windows Store app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Developer environment</td>
<td><p>Microsoft Visual Studio 2013</p>
<p>Microsoft Windows Software Development Kit (SDK) for Windows 8.1</p></td>
<td><p>Use <strong>WinUSB Application</strong> template included with Visual Studio (Ultimate or Professional) and Windows Driver Kit (WDK) 8</p>
<div class="alert">
<strong>Note</strong>  For isochronous transfers, Visual Studio 2013 with Windows Driver Kit (WDK) 8.1
</div>
<div>
 
</div></td>
</tr>
<tr class="even">
<td>Programming languages</td>
<td>C#, VB.NET, C++, JavaScript</td>
<td>C/C++</td>
</tr>
</tbody>
</table>

 

## Feature implementation


<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Key scenario</th>
<th>Windows Store app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Device discovery</td>
<td>Use [<strong>Windows.Devices.Enumeration</strong>](https://msdn.microsoft.com/library/windows/apps/br225459) namespace to get a [<strong>UsbDevice</strong>](https://msdn.microsoft.com/library/windows/apps/dn263883).</td>
<td>Use [SetupAPI](https://msdn.microsoft.com/library/windows/hardware/ff550855) functions and [<strong>WinUsb_Initialize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540277) to get a WINUSB_INTERFACE_HANDLE.</td>
</tr>
<tr class="even">
<td>USB control transfer</td>
<td><p>[<strong>UsbSetupPacket</strong>](https://msdn.microsoft.com/library/windows/apps/dn278431)</p>
<p>[<strong>UsbControlRequestType</strong>](https://msdn.microsoft.com/library/windows/apps/dn263821)</p>
<p>[<strong>UsbDevice.SendControlInTransferAsync</strong>](https://msdn.microsoft.com/library/windows/apps/dn264027)</p>
<p>[<strong>UsbDevice.SendControlOutTransferAsync</strong>](https://msdn.microsoft.com/library/windows/apps/dn264044)</p></td>
<td><p>[<strong>WINUSB_SETUP_PACKET</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540313)</p>
<p>[<strong>WinUsb_ControlTransfer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540219)</p></td>
</tr>
<tr class="odd">
<td>Getting USB descriptors</td>
<td><p>[<strong>UsbDevice.DeviceDescriptor</strong>](https://msdn.microsoft.com/library/windows/apps/dn264002)</p>
<p>[<strong>UsbConfiguration.Descriptors</strong>](https://msdn.microsoft.com/library/windows/apps/dn263802)</p>
<p>[<strong>UsbInterface.Descriptors</strong>](https://msdn.microsoft.com/library/windows/apps/dn264289)</p>
<p>[<strong>UsbEndpointDescriptor</strong>](https://msdn.microsoft.com/library/windows/apps/dn264052)</p></td>
<td>[<strong>WinUsb_GetDescriptor</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540257)</td>
</tr>
<tr class="even">
<td>Sending USB bulk transfer</td>
<td><p>[<strong>UsbBulkInPipe</strong>](https://msdn.microsoft.com/library/windows/apps/dn297573)</p>
<p>[<strong>UsbBulkOutPipe</strong>](https://msdn.microsoft.com/library/windows/apps/dn297647)</p></td>
<td><p>[<strong>WinUsb_ReadPipe</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540297)</p>
<p>[<strong>WinUsb_WritePipe</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540322)</p></td>
</tr>
<tr class="odd">
<td>Sending USB interrupt transfer</td>
<td><p>[<strong>UsbInterruptInPipe</strong>](https://msdn.microsoft.com/library/windows/apps/dn278416)</p>
<p>[<strong>UsbInterruptOutPipe</strong>](https://msdn.microsoft.com/library/windows/apps/dn278425)</p></td>
<td><p>[<strong>WinUsb_ReadPipe</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540297)</p>
<p>[<strong>WinUsb_WritePipe</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540322)</p></td>
</tr>
<tr class="even">
<td>Sending USB isochronous transfer</td>
<td>Not supported.</td>
<td><p>[<strong>WinUsb_ReadIsochPipe</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265564)</p>
<p>[<strong>WinUsb_ReadIsochPipeAsap</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265565)</p>
<p>[<strong>WinUsb_WriteIsochPipe</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265568)</p>
<p>[<strong>WinUsb_WriteIsochPipeAsap</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265569)</p></td>
</tr>
<tr class="odd">
<td>Closing the device</td>
<td>[<strong>UsbDevice.Close</strong>](https://msdn.microsoft.com/library/windows/apps/dn263990)</td>
<td>[<strong>WinUsb_Free</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540233)</td>
</tr>
</tbody>
</table>

 

## Documentation


| Documentation     | Windows Store app                                                                     | Windows desktop app                                                                                           |
|-------------------|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Programming guide | [Talking to USB devices, start to finish](talking-to-usb-devices-start-to-finish.md) | [How to Access a USB Device by Using WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md) |
| API reference     | [**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466)                              | [WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md)                                     |

 

## Related topics


[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Developing%20Windows%20applications%20for%20USB%20devices%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




