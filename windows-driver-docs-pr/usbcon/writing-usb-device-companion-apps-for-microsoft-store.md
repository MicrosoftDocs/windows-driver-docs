---
Description: The Windows.Devices.Usb namespace provides APIs to communicate with an external USB device.
title: UWP app for a USB device
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UWP app for a USB device


The [**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466) namespace provides a way for a Windows app to communicate with an external USB device that uses WinUSB (Winusb.sys) as the device driver.

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
<td><p><a href="talking-to-usb-devices-start-to-finish.md" data-raw-source="[Talking to USB devices, start to finish (UWP app)](talking-to-usb-devices-start-to-finish.md)">Talking to USB devices, start to finish (UWP app)</a></p></td>
<td><p>Use the Windows Runtime APIs, introduced in Windows 8.1, to write UWP apps that gives users access to their peripheral USB device. Such apps can connect to a device based on user-specified criteria, get information about the device, send data to the device and conversely get data steams from the device, and poll the device for interrupt data.</p></td>
</tr>
<tr class="even">
<td><p><a href="updating-the-app-manifest-with-usb-device-capabilities.md" data-raw-source="[How to add USB device capabilities to the app manifest](updating-the-app-manifest-with-usb-device-capabilities.md)">How to add USB device capabilities to the app manifest</a></p></td>
<td><p>This topic describes the device capabilities that are required for a Windows app that uses the <a href="https://msdn.microsoft.com/library/windows/apps/dn278466" data-raw-source="[&lt;strong&gt;Windows.Devices.Usb&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn278466)"><strong>Windows.Devices.Usb</strong></a> namespace.</p></td>
</tr>
<tr class="odd">
<td><p><a href="how-to-connect-to-a-usb-device--uwp-app-.md" data-raw-source="[How to connect to a USB device (UWP app)](how-to-connect-to-a-usb-device--uwp-app-.md)">How to connect to a USB device (UWP app)</a></p></td>
<td><p>In Windows 8.1, you can write a UWP app that interacts with a USB device. The app can send control commands, get device information, and read and write data to/from bulk and interrupt endpoints. Before you can do all that, you must find the device and establish connection.</p>
<p>In this part, you will learn how to use the <a href="https://msdn.microsoft.com/library/windows/apps/br225446" data-raw-source="[&lt;strong&gt;DeviceWatcher&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br225446)"><strong>DeviceWatcher</strong></a> object to find the device and then open it to start communicating from your app. You will also learn how to close the device when you are finished using it.</p></td>
</tr>
<tr class="even">
<td><p><a href="how-to-send-a-usb-control-transfer--uwp-app-.md" data-raw-source="[How to send a USB control transfer (UWP app)](how-to-send-a-usb-control-transfer--uwp-app-.md)">How to send a USB control transfer (UWP app)</a></p></td>
<td><p>An app that communicates with a USB device usually sends several control transfers requests. Those requests get information about the device and send control commands defined by the hardware vendor. In this topic you&#39;ll learn about control transfers and how to format and send them in your UWP app.</p></td>
</tr>
<tr class="odd">
<td><p><a href="how-to-send-a-usb-interrupt-transfer--uwp-app-.md" data-raw-source="[How to send a USB interrupt transfer request (UWP app)](how-to-send-a-usb-interrupt-transfer--uwp-app-.md)">How to send a USB interrupt transfer request (UWP app)</a></p></td>
<td><p>A USB device can support interrupt endpoints so that it can send or receive data at regular intervals. To accomplish that, the host polls the device at regular intervals and data is transmitted each time the host polls the device. Interrupt transfers are mostly used for getting interrupt data from the device. This topic describes how a UWP app can get continuous interrupt data from the device.</p></td>
</tr>
<tr class="even">
<td><p><a href="how-to-send-a-usb-bulk-transfer--uwp-app-.md" data-raw-source="[How to send a USB bulk transfer request (UWP app)](how-to-send-a-usb-bulk-transfer--uwp-app-.md)">How to send a USB bulk transfer request (UWP app)</a></p></td>
<td><p>In this topic, you&#39;ll learn about a USB bulk transfer and how to initiate a transfer request from your UWP app that communicates with a USB device.</p></td>
</tr>
<tr class="odd">
<td><p><a href="how-to-get-usb-descriptors--uwp-app-.md" data-raw-source="[How to get USB descriptors (UWP app)](how-to-get-usb-descriptors--uwp-app-.md)">How to get USB descriptors (UWP app)</a></p></td>
<td><p>One of the main tasks of interacting with a USB device is to get information about it. All USB devices provide information in the form of several data structures called descriptors. This topic describes how a UWP app can get descriptors from the device at the endpoint, interface, configuration, and device level.</p></td>
</tr>
<tr class="even">
<td><p><a href="how-to-select-a-usb-interface-setting--uwp-app-.md" data-raw-source="[How to select a USB interface setting (UWP app)](how-to-select-a-usb-interface-setting--uwp-app-.md)">How to select a USB interface setting (UWP app)</a></p></td>
<td><p>In this topic, you&#39;ll learn about changing a setting within a USB interface. You&#39;ll use the <a href="https://msdn.microsoft.com/library/windows/apps/dn264278" data-raw-source="[&lt;strong&gt;UsbInterfaceSetting&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264278)"><strong>UsbInterfaceSetting</strong></a> object to get the current setting and set a setting in the interface.</p></td>
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
    The APIs are primarily designed for accessing peripheral devices. The API can also access PC internal USB devices. However access to PC internal USB devices from a UWP app is limited to a privileged app that is explicitly declared by the OEM for that PC.

     

-   The kernel-mode device stack has a filter driver above Winusb.sys.
    **Note**  This scenario is available to privileged apps only.

     

-   Your device has multiple USB configurations, and you want to select a configuration, other than the first. [**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466) selects the first configuration by default.

## Related topics
[**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466)  



