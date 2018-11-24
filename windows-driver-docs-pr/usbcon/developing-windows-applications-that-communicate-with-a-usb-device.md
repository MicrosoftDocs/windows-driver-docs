---
Description: This topic provides guidelines for deciding whether you should write a UWP app or a Windows desktop app to communicate with a USB device.
title: Developing Windows applications for USB devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Developing Windows applications for USB devices


**Summary**

-   Guidelines for choosing the right programming model
-   UWP app and desktop app developer experience

**Important APIs**

-   [**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466)
-   [WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md)

This topic provides guidelines for deciding whether you should write a UWP app or a Windows desktop app to communicate with a USB device.

Windows provides API sets that you can use to write apps that talk to a custom USB devices. The API performs common USB-related tasks such as, finding the device, data transfers.

"Custom device" in this context means, a device for which Microsoft does not provide an in-box class driver. Instead, you can install WinUSB (Winusb.sys) as the device driver.

## Choosing a programming model


If you install [Winusb.sys](winusb-installation.md), here are the programming model options:

-   [UWP app for a USB device](writing-usb-device-companion-apps-for-microsoft-store.md)

    Windows 8.1 provides a new namespace: [**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466). The namespace cannot be used in earlier version of Windows. Other Microsoft Store resources are here: [UWP app](https://msdn.microsoft.com/windows/apps).

-   [Windows desktop app for a USB device](windows-desktop-app-for-a-usb-device.md)

    Before Windows 8.1, apps that were communicating through [Winusb.sys](winusb-installation.md), were desktop apps written by using [WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md). In Windows 8.1, the API set has been extended. Other Windows desktop app resources are here: [Windows desktop app](https://dev.windows.com/desktop).

The strategy for choosing the best programming model depends on various factors.

-   **Will your app communicate with an internal USB device?**

    The APIs are primarily designed for accessing peripheral devices. The API can also access PC internal USB devices. However access to PC internal USB devices from a UWP app is limited to a privileged app that is explicitly declared in device metadata by the OEM for that PC.

-   **Will your app communicate with USB isochronous endpoints?**

    If your app transmits data to or from isochronous endpoints of the device, you must write a Windows desktop app. In Windows 8.1, new [WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md) have been added to the API set that allow a desktop app to send data to and receive data from isochronous endpoints.

-   **Is your app a "control panel" type of app?**

    UWP apps are per-user apps and do not have the ability to make changes outside the scope of each app. For these types of apps, you must write a Windows desktop app.

-   **Is the USB device class supported classes by UWP apps?**

    Write a UWP app if your device belongs to one these device classes.

    -   `name:cdcControl,           classId:02 * *`
    -   `name:physical, classId:05 * *`
    -   `name:personalHealthcare,   classId:0f 00 00`
    -   `name:activeSync,           classId:ef 01 01`
    -   `name:palmSync,             classId:ef 01 02`
    -   `name:deviceFirmwareUpdate, classId:fe 01 01`
    -   `name:irda,                 classId:fe 02 00     `
    -   `name:measurement,          classId:fe 03 *`
    -   `name:vendorSpecific,       classId:ff * *`

    **Note**  If your device belongs to DeviceFirmwareUpdate class, your app must be a privileged app.




If your device does not belong to one the preceding device classes, write a Windows desktop app.


## Driver requirement


| Driver requirement | UWP app                                                                                                                          | Windows desktop app                                                                                                                       |
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
<th>UWP app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Get started with these samples</td>
<td><ul>
<li><a href="http://go.microsoft.com/fwlink/p/?linkid=309716" data-raw-source="[Custom USB device access sample](http://go.microsoft.com/fwlink/p/?linkid=309716)">Custom USB device access sample</a></li>
<li><a href="http://go.microsoft.com/fwlink/p/?linkid=309716" data-raw-source="[USB CDC Control sample](http://go.microsoft.com/fwlink/p/?linkid=309716)">USB CDC Control sample</a></li>
<li><a href="http://go.microsoft.com/fwlink/p/?linkid=309716" data-raw-source="[Firmware Update USB Device sample](http://go.microsoft.com/fwlink/p/?linkid=309716)">Firmware Update USB Device sample</a></li>
</ul></td>
<td><ul>
<li>Start with the <strong>WinUsb Application</strong> template included with Microsoft Visual Studio (Ultimate or Professional)</li>
<li>Extend the template by using code examples shown in <a href="using-winusb-api-to-communicate-with-a-usb-device.md" data-raw-source="[How to Access a USB Device by Using WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md)">How to Access a USB Device by Using WinUSB Functions</a>.</li>
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
<th>UWP app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Developer environment</td>
<td><p>Microsoft Visual Studio 2013</p>
<p>Microsoft Windows Software Development Kit (SDK) for Windows 8.1</p></td>
<td><p>Use <strong>WinUSB Application</strong> template included with Visual Studio (Ultimate or Professional) and Windows Driver Kit (WDK) 8</p>
<div class="alert">
<strong>Note</strong>  For isochronous transfers, Visual Studio 2013 with Windows Driver Kit (WDK) 8.1
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
<th>UWP app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Device discovery</td>
<td>Use <a href="https://msdn.microsoft.com/library/windows/apps/br225459" data-raw-source="[&lt;strong&gt;Windows.Devices.Enumeration&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br225459)"><strong>Windows.Devices.Enumeration</strong></a> namespace to get a <a href="https://msdn.microsoft.com/library/windows/apps/dn263883" data-raw-source="[&lt;strong&gt;UsbDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn263883)"><strong>UsbDevice</strong></a>.</td>
<td>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff550855" data-raw-source="[SetupAPI](https://msdn.microsoft.com/library/windows/hardware/ff550855)">SetupAPI</a> functions and <a href="https://msdn.microsoft.com/library/windows/hardware/ff540277" data-raw-source="[&lt;strong&gt;WinUsb_Initialize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540277)"><strong>WinUsb_Initialize</strong></a> to get a WINUSB_INTERFACE_HANDLE.</td>
</tr>
<tr class="even">
<td>USB control transfer</td>
<td><p><a href="https://msdn.microsoft.com/library/windows/apps/dn278431" data-raw-source="[&lt;strong&gt;UsbSetupPacket&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn278431)"><strong>UsbSetupPacket</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/apps/dn263821" data-raw-source="[&lt;strong&gt;UsbControlRequestType&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn263821)"><strong>UsbControlRequestType</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/apps/dn264027" data-raw-source="[&lt;strong&gt;UsbDevice.SendControlInTransferAsync&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264027)"><strong>UsbDevice.SendControlInTransferAsync</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/apps/dn264044" data-raw-source="[&lt;strong&gt;UsbDevice.SendControlOutTransferAsync&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264044)"><strong>UsbDevice.SendControlOutTransferAsync</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540313" data-raw-source="[&lt;strong&gt;WINUSB_SETUP_PACKET&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540313)"><strong>WINUSB_SETUP_PACKET</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540219" data-raw-source="[&lt;strong&gt;WinUsb_ControlTransfer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540219)"><strong>WinUsb_ControlTransfer</strong></a></p></td>
</tr>
<tr class="odd">
<td>Getting USB descriptors</td>
<td><p><a href="https://msdn.microsoft.com/library/windows/apps/dn264002" data-raw-source="[&lt;strong&gt;UsbDevice.DeviceDescriptor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264002)"><strong>UsbDevice.DeviceDescriptor</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/apps/dn263802" data-raw-source="[&lt;strong&gt;UsbConfiguration.Descriptors&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn263802)"><strong>UsbConfiguration.Descriptors</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/apps/dn264289" data-raw-source="[&lt;strong&gt;UsbInterface.Descriptors&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264289)"><strong>UsbInterface.Descriptors</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/apps/dn264052" data-raw-source="[&lt;strong&gt;UsbEndpointDescriptor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264052)"><strong>UsbEndpointDescriptor</strong></a></p></td>
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff540257" data-raw-source="[&lt;strong&gt;WinUsb_GetDescriptor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540257)"><strong>WinUsb_GetDescriptor</strong></a></td>
</tr>
<tr class="even">
<td>Sending USB bulk transfer</td>
<td><p><a href="https://msdn.microsoft.com/library/windows/apps/dn297573" data-raw-source="[&lt;strong&gt;UsbBulkInPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn297573)"><strong>UsbBulkInPipe</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/apps/dn297647" data-raw-source="[&lt;strong&gt;UsbBulkOutPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn297647)"><strong>UsbBulkOutPipe</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540297" data-raw-source="[&lt;strong&gt;WinUsb_ReadPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540297)"><strong>WinUsb_ReadPipe</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540322" data-raw-source="[&lt;strong&gt;WinUsb_WritePipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540322)"><strong>WinUsb_WritePipe</strong></a></p></td>
</tr>
<tr class="odd">
<td>Sending USB interrupt transfer</td>
<td><p><a href="https://msdn.microsoft.com/library/windows/apps/dn278416" data-raw-source="[&lt;strong&gt;UsbInterruptInPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn278416)"><strong>UsbInterruptInPipe</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/apps/dn278425" data-raw-source="[&lt;strong&gt;UsbInterruptOutPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn278425)"><strong>UsbInterruptOutPipe</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540297" data-raw-source="[&lt;strong&gt;WinUsb_ReadPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540297)"><strong>WinUsb_ReadPipe</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540322" data-raw-source="[&lt;strong&gt;WinUsb_WritePipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540322)"><strong>WinUsb_WritePipe</strong></a></p></td>
</tr>
<tr class="even">
<td>Sending USB isochronous transfer</td>
<td>Not supported.</td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/dn265564" data-raw-source="[&lt;strong&gt;WinUsb_ReadIsochPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn265564)"><strong>WinUsb_ReadIsochPipe</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/dn265565" data-raw-source="[&lt;strong&gt;WinUsb_ReadIsochPipeAsap&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn265565)"><strong>WinUsb_ReadIsochPipeAsap</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/dn265568" data-raw-source="[&lt;strong&gt;WinUsb_WriteIsochPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn265568)"><strong>WinUsb_WriteIsochPipe</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/dn265569" data-raw-source="[&lt;strong&gt;WinUsb_WriteIsochPipeAsap&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn265569)"><strong>WinUsb_WriteIsochPipeAsap</strong></a></p></td>
</tr>
<tr class="odd">
<td>Closing the device</td>
<td><a href="https://msdn.microsoft.com/library/windows/apps/dn263990" data-raw-source="[&lt;strong&gt;UsbDevice.Close&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn263990)"><strong>UsbDevice.Close</strong></a></td>
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff540233" data-raw-source="[&lt;strong&gt;WinUsb_Free&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540233)"><strong>WinUsb_Free</strong></a></td>
</tr>
</tbody>
</table>



## Documentation


| Documentation     | UWP app                                                                     | Windows desktop app                                                                                           |
|-------------------|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Programming guide | [Talking to USB devices, start to finish](talking-to-usb-devices-start-to-finish.md) | [How to Access a USB Device by Using WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md) |
| API reference     | [**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466)                              | [WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md)                                     |



## Related topics
[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)  



