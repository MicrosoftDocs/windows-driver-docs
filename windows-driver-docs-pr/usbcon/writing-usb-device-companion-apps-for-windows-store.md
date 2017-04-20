---
Description: The Windows.Devices.Usb namespace provides a way for a Windows store app to communicate with an external USB device that uses WinUSB (Winusb.sys) as the device driver.
title: Windows Store app for a USB device
author: windows-driver-content
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Windows Store app for a USB device


The [**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466) namespace provides a way for a Windows store app to communicate with an external USB device that uses WinUSB (Winusb.sys) as the device driver.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[Talking to USB devices, start to finish (Windows Store app)](talking-to-usb-devices-start-to-finish.md)</p></td>
<td><p>Use the Windows Runtime APIs, introduced in Windows 8.1, to write Windows Store apps that gives users access to their peripheral USB device. Such apps can connect to a device based on user-specified criteria, get information about the device, send data to the device and conversely get data steams from the device, and poll the device for interrupt data.</p></td>
</tr>
<tr class="even">
<td><p>[How to add USB device capabilities to the app manifest](updating-the-app-manifest-with-usb-device-capabilities.md)</p></td>
<td><p>This topic describes the device capabilities that are required for a Windows store app that uses the [<strong>Windows.Devices.Usb</strong>](https://msdn.microsoft.com/library/windows/apps/dn278466) namespace.</p></td>
</tr>
<tr class="odd">
<td><p>[How to connect to a USB device (Windows Store app)](how-to-connect-to-a-usb-device--windows-store-app-.md)</p></td>
<td><p>In Windows 8.1, you can write a Windows Store app that interacts with a USB device. The app can send control commands, get device information, and read and write data to/from bulk and interrupt endpoints. Before you can do all that, you must find the device and establish connection.</p>
<p>In this part, you will learn how to use the [<strong>DeviceWatcher</strong>](https://msdn.microsoft.com/library/windows/apps/br225446) object to find the device and then open it to start communicating from your app. You will also learn how to close the device when you are finished using it.</p></td>
</tr>
<tr class="even">
<td><p>[How to send a USB control transfer (Windows Store app)](how-to-send-a-usb-control-transfer--windows-store-app-.md)</p></td>
<td><p>An app that communicates with a USB device usually sends several control transfers requests. Those requests get information about the device and send control commands defined by the hardware vendor. In this topic you'll learn about control transfers and how to format and send them in your Windows Store app.</p></td>
</tr>
<tr class="odd">
<td><p>[How to send a USB interrupt transfer request (Windows Store app)](how-to-send-a-usb-interrupt-transfer--windows-store-app-.md)</p></td>
<td><p>A USB device can support interrupt endpoints so that it can send or receive data at regular intervals. To accomplish that, the host polls the device at regular intervals and data is transmitted each time the host polls the device. Interrupt transfers are mostly used for getting interrupt data from the device. This topic describes how a Windows Store app can get continuous interrupt data from the device.</p></td>
</tr>
<tr class="even">
<td><p>[How to send a USB bulk transfer request (Windows Store app)](how-to-send-a-usb-bulk-transfer--windows-store-app-.md)</p></td>
<td><p>In this topic, you'll learn about a USB bulk transfer and how to initiate a transfer request from your Windows Store app that communicates with a USB device.</p></td>
</tr>
<tr class="odd">
<td><p>[How to get USB descriptors (Windows Store app)](how-to-get-usb-descriptors--windows-store-app-.md)</p></td>
<td><p>One of the main tasks of interacting with a USB device is to get information about it. All USB devices provide information in the form of several data structures called descriptors. This topic describes how a Windows Store app can get descriptors from the device at the endpoint, interface, configuration, and device level.</p></td>
</tr>
<tr class="even">
<td><p>[How to select a USB interface setting (Windows Store app)](how-to-select-a-usb-interface-setting--windows-store-app-.md)</p></td>
<td><p>In this topic, you'll learn about changing a setting within a USB interface. You'll use the [<strong>UsbInterfaceSetting</strong>](https://msdn.microsoft.com/library/windows/apps/dn264278) object to get the current setting and set a setting in the interface.</p></td>
</tr>
</tbody>
</table>

 

## USB samples


-   [Custom USB device access sample](http://go.microsoft.com/fwlink/p/?linkid=309716)
-   [USB CDC Control sample](http://go.microsoft.com/fwlink/p/?linkid=309716)
-   [Firmware Update USB Device sample](http://go.microsoft.com/fwlink/p/?linkid=309716)

## What are the limitations of the namespace?


You *cannot* use [**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466) in these cases:

-   If the device driver is not Winusb.sys.
-   You want to communicate with USB isochronous endpoints of the device.
-   You want to communicate streams of a SuperSpeed bulk endpoint. For those endpoints, the USB Windows Runtime classes for bulk transfers can only send or receive data from the first stream of the endpoint.
-   You allow multiple apps to concurrently access the device.
-   Your USB device is an internal device.
    **Note**  
    The APIs are primarily designed for accessing peripheral devices. The API can also access PC internal USB devices. However access to PC internal USB devices from a Windows Store app is limited to a privileged app that is explicitly declared by the OEM for that PC.

     

-   The kernel-mode device stack has a filter driver above Winusb.sys.
    **Note**  This scenario is available to privileged apps only.

     

-   Your device has multiple USB configurations, and you want to select a configuration, other than the first. [**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466) selects the first configuration by default.

## Related topics
[**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Windows%20Store%20app%20for%20a%20USB%20device%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


