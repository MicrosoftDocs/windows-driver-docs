---
Description: A Universal Serial Bus (USB) device defines its capabilities and features through configurations, interfaces, alternate settings, and endpoints.
title: Concepts for all USB developers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

#  Concepts for all USB developers


A Universal Serial Bus (USB) device defines its capabilities and features through configurations, interfaces, alternate settings, and endpoints. This topic provides a high-level overview of those concepts. For details, see the USB specifications at [Universal Serial Bus Documents]( http://go.microsoft.com/fwlink/p/?linkid=224892).

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
<td><p><a href="usb-device-layout.md" data-raw-source="[USB device layout](usb-device-layout.md)">USB device layout</a></p></td>
<td><p>A USB device defines its capabilities and features through configurations, interfaces, alternate settings, and endpoints. This topic provides a high-level overview of those concepts.</p></td>
</tr>
<tr class="even">
<td><p><a href="standard-usb-descriptors.md" data-raw-source="[Standard USB descriptors](standard-usb-descriptors.md)">Standard USB descriptors</a></p></td>
<td><p>A USB device provides information about itself in data structures called <em>USB descriptors</em>. This section provides information about device, configuration, interface, and endpoint descriptors and ways to retrieve them from a USB device.</p></td>
</tr>
<tr class="odd">
<td><p><a href="usb-endpoints-and-their-pipes.md" data-raw-source="[USB endpoints and their pipes](usb-endpoints-and-their-pipes.md)">USB endpoints and their pipes</a></p></td>
<td><p>A USB device has endpoints that are used to for data transfers. On the host side, endpoints are represented by pipes. This topic differentiates between those two terms.</p></td>
</tr>
<tr class="even">
<td><p><a href="usb-faq--introductory-level.md" data-raw-source="[USB in Windows - FAQ](usb-faq--introductory-level.md)">USB in Windows - FAQ</a></p></td>
<td><p>This topic presents frequently asked questions for driver developers who are new to developing and integrating USB devices and drivers with Windows operating systems.</p></td>
</tr>
</tbody>
</table>

 

## **Common USB scenarios**


**1—Get the device handle** for communication and use the retrieved handle or object to send data transfers.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Client driver</th>
<th>UWP app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>KMDF</strong>: <a href="https://msdn.microsoft.com/library/windows/hardware/hh439428" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceCreateWithParameters&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439428)"><strong>WdfUsbTargetDeviceCreateWithParameters</strong></a></p>
<p><strong>UMDF</strong>: <a href="https://msdn.microsoft.com/library/windows/hardware/ff560362" data-raw-source="[&lt;strong&gt;IWDFUsbTargetDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560362)"><strong>IWDFUsbTargetDevice</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/apps/dn263883" data-raw-source="[&lt;strong&gt;UsbDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn263883)"><strong>UsbDevice</strong></a></p>
<p><a href="how-to-connect-to-a-usb-device--uwp-app-.md" data-raw-source="[How to connect to a USB device (UWP app)](how-to-connect-to-a-usb-device--uwp-app-.md)">How to connect to a USB device (UWP app)</a>.</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540277" data-raw-source="[&lt;strong&gt;WinUsb_Initialize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540277)"><strong>WinUsb_Initialize</strong></a></p>
<p>See <a href="how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md" data-raw-source="[Write a Windows desktop app based on the WinUSB template](how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md)">Write a Windows desktop app based on the WinUSB template</a>.</p></td>
</tr>
</tbody>
</table>

 

**USB descriptor retrieval** to get information about the device's configuration(s), interface(s), setting(s), and their endpoint(s).

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Client driver</th>
<th>UWP app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>KMDF</strong>:</p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550090" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceGetDeviceDescriptor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550090)"><strong>WdfUsbTargetDeviceGetDeviceDescriptor</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550098" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceRetrieveConfigDescriptor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550098)"><strong>WdfUsbTargetDeviceRetrieveConfigDescriptor</strong></a></p>
<p><strong>UMDF</strong>:</p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560374" data-raw-source="[&lt;strong&gt;IWDFUsbTargetDevice::RetrieveDescriptor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560374)"><strong>IWDFUsbTargetDevice::RetrieveDescriptor</strong></a></p>
<p>See <a href="usb-descriptors.md" data-raw-source="[USB descriptors](usb-descriptors.md)">USB descriptors</a>.</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/apps/dn264002" data-raw-source="[&lt;strong&gt;UsbDevice.DeviceDescriptor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264002)"><strong>UsbDevice.DeviceDescriptor</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/apps/dn263802" data-raw-source="[&lt;strong&gt;UsbConfiguration.Descriptors&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn263802)"><strong>UsbConfiguration.Descriptors</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/apps/dn264289" data-raw-source="[&lt;strong&gt;UsbInterface.Descriptors&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264289)"><strong>UsbInterface.Descriptors</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/apps/dn264281" data-raw-source="[&lt;strong&gt;UsbInterfaceSetting.Descriptors&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264281)"><strong>UsbInterfaceSetting.Descriptors</strong></a></p>
<p><a href="how-to-get-usb-descriptors--uwp-app-.md" data-raw-source="[How to get USB descriptors (UWP app)](how-to-get-usb-descriptors--uwp-app-.md)">How to get USB descriptors (UWP app)</a>.</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540257" data-raw-source="[&lt;strong&gt;WinUsb_GetDescriptor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540257)"><strong>WinUsb_GetDescriptor</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540292" data-raw-source="[&lt;strong&gt;WinUsb_QueryInterfaceSettings&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540292)"><strong>WinUsb_QueryInterfaceSettings</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540293" data-raw-source="[&lt;strong&gt;WinUsb_QueryPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540293)"><strong>WinUsb_QueryPipe</strong></a></p>
<p>See <a href="using-winusb-api-to-communicate-with-a-usb-device.md#query" data-raw-source="[Query the Device for USB Descriptors](using-winusb-api-to-communicate-with-a-usb-device.md#query)">Query the Device for USB Descriptors</a>.</p></td>
</tr>
</tbody>
</table>

 

**2—Configure the device** to select an active USB configuration and setting per interface.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Client driver</th>
<th>UWP app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>KMDF:</strong></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550101" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceSelectConfig&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550101)"><strong>WdfUsbTargetDeviceSelectConfig</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439423" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceCreateUrb&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439423)"><strong>WdfUsbTargetDeviceCreateUrb</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/hh406243" data-raw-source="[&lt;strong&gt;USBD_SelectConfigUrbAllocateAndBuild&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh406243)"><strong>USBD_SelectConfigUrbAllocateAndBuild</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550073" data-raw-source="[&lt;strong&gt;WdfUsbInterfaceSelectSetting&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550073)"><strong>WdfUsbInterfaceSelectSetting</strong></a></p>
<p>See <a href="how-to-select-a-configuration-for-a-usb-device.md" data-raw-source="[How to select a configuration for a USB device](how-to-select-a-configuration-for-a-usb-device.md)">How to select a configuration for a USB device</a>.</p>
<p>See <a href="select-a-usb-alternate-setting.md" data-raw-source="[How to select an alternate setting in a USB interface](select-a-usb-alternate-setting.md)">How to select an alternate setting in a USB interface</a>.</p>
<p><strong>UMDF:</strong></p>
<p>Configuration selection is not Supported.</p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560343" data-raw-source="[&lt;strong&gt;IWDFUsbInterface::SelectSetting&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560343)"><strong>IWDFUsbInterface::SelectSetting</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/apps/dn264286" data-raw-source="[&lt;strong&gt;UsbInterfaceSetting.SelectSettingAsync&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264286)"><strong>UsbInterfaceSetting.SelectSettingAsync</strong></a></p>
<p><a href="how-to-select-a-usb-interface-setting--uwp-app-.md" data-raw-source="[How to select a USB interface setting (UWP app)](how-to-select-a-usb-interface-setting--uwp-app-.md)">How to select a USB interface setting (UWP app)</a>.</p></td>
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff540302" data-raw-source="[&lt;strong&gt;WinUsb_SetCurrentAlternateSetting&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540302)"><strong>WinUsb_SetCurrentAlternateSetting</strong></a></td>
</tr>
</tbody>
</table>

 

**3—Send control transfers** for configuring the device and performing vendor commands that are specific to particular device.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Client driver</th>
<th>UWP app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>KMDF:</strong></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550104" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceSendControlTransferSynchronously&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550104)"><strong>WdfUsbTargetDeviceSendControlTransferSynchronously</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550082" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceFormatRequestForControlTransfer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550082)"><strong>WdfUsbTargetDeviceFormatRequestForControlTransfer</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/hh406243" data-raw-source="[&lt;strong&gt;USBD_SelectConfigUrbAllocateAndBuild&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh406243)"><strong>USBD_SelectConfigUrbAllocateAndBuild</strong></a></p>
<p><strong>UMDF:</strong></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560363" data-raw-source="[&lt;strong&gt;IWDFUsbTargetDevice::FormatRequestForControlTransfer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560363)"><strong>IWDFUsbTargetDevice::FormatRequestForControlTransfer</strong></a></p>
<p>See <a href="usb-control-transfer.md" data-raw-source="[How to send a USB control transfer](usb-control-transfer.md)">How to send a USB control transfer</a>.</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/apps/dn264037" data-raw-source="[&lt;strong&gt;SendControlInTransferAsync&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264037)"><strong>SendControlInTransferAsync</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/apps/dn264047" data-raw-source="[&lt;strong&gt;SendControlOutTransferAsync&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264047)"><strong>SendControlOutTransferAsync</strong></a></p>
<p><a href="how-to-send-a-usb-control-transfer--uwp-app-.md" data-raw-source="[How to send a USB control transfer (UWP app)](how-to-send-a-usb-control-transfer--uwp-app-.md)">How to send a USB control transfer (UWP app)</a>.</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540219" data-raw-source="[&lt;strong&gt;WinUsb_ControlTransfer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540219)"><strong>WinUsb_ControlTransfer</strong></a></p>
<p>See <a href="using-winusb-api-to-communicate-with-a-usb-device.md#control" data-raw-source="[Send Control Transfer to the Default Endpoint](using-winusb-api-to-communicate-with-a-usb-device.md#control)">Send Control Transfer to the Default Endpoint</a>.</p></td>
</tr>
</tbody>
</table>

 

**4—Send bulk transfers**, typically used by mass storage devices that transfer large amount of data.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Client driver</th>
<th>UWP app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>KMDF:</strong></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551155" data-raw-source="[&lt;strong&gt;WdfUsbTargetPipeReadSynchronously&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551155)"><strong>WdfUsbTargetPipeReadSynchronously</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551163" data-raw-source="[&lt;strong&gt;WdfUsbTargetPipeWriteSynchronously&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551163)"><strong>WdfUsbTargetPipeWriteSynchronously</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551136" data-raw-source="[&lt;strong&gt;WdfUsbTargetPipeFormatRequestForRead&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551136)"><strong>WdfUsbTargetPipeFormatRequestForRead</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551141" data-raw-source="[&lt;strong&gt;WdfUsbTargetPipeFormatRequestForWrite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551141)"><strong>WdfUsbTargetPipeFormatRequestForWrite</strong></a></p>
<p><a href="usb-bulk-and-interrupt-transfer.md" data-raw-source="[How to send USB bulk transfer requests](usb-bulk-and-interrupt-transfer.md)">How to send USB bulk transfer requests</a></p>
<p><a href="how-to-use-the-continous-reader-for-getting-data-from-a-usb-endpoint--umdf-.md" data-raw-source="[How to use the continuous reader for reading data from a USB pipe](how-to-use-the-continous-reader-for-getting-data-from-a-usb-endpoint--umdf-.md)">How to use the continuous reader for reading data from a USB pipe</a>.</p>
<p><strong>UMDF:</strong></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556908" data-raw-source="[&lt;strong&gt;IUsbTargetPipeContinuousReaderCallbackReadComplete&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556908)"><strong>IUsbTargetPipeContinuousReaderCallbackReadComplete</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560391" data-raw-source="[&lt;strong&gt;IWDFUsbTargetPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560391)"><strong>IWDFUsbTargetPipe</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560394" data-raw-source="[&lt;strong&gt;IWDFUsbTargetPipe2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560394)"><strong>IWDFUsbTargetPipe2</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/apps/dn297601" data-raw-source="[&lt;strong&gt;UsbBulkInPipe.InputStream&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn297601)"><strong>UsbBulkInPipe.InputStream</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/apps/dn297669" data-raw-source="[&lt;strong&gt;UsbBulkOutPipe.OutputStream&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn297669)"><strong>UsbBulkOutPipe.OutputStream</strong></a></p>
<p><a href="how-to-send-a-usb-bulk-transfer--uwp-app-.md" data-raw-source="[How to send a USB bulk transfer request (UWP app)](how-to-send-a-usb-bulk-transfer--uwp-app-.md)">How to send a USB bulk transfer request (UWP app)</a>.</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540322" data-raw-source="[&lt;strong&gt;WinUsb_WritePipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540322)"><strong>WinUsb_WritePipe</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540297" data-raw-source="[&lt;strong&gt;WinUsb_ReadPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540297)"><strong>WinUsb_ReadPipe</strong></a></p>
<p>See <a href="using-winusb-api-to-communicate-with-a-usb-device.md#io" data-raw-source="[Issue I/O Requests](using-winusb-api-to-communicate-with-a-usb-device.md#io)">Issue I/O Requests</a>.</p></td>
</tr>
</tbody>
</table>

 

**5—Send interrupt transfers**. Data is read to retrieve hardware interrupt data.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Client driver</th>
<th>UWP app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Same as bulk transfers.</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/apps/dn278418" data-raw-source="[&lt;strong&gt;UsbInterruptInPipe.DataReceived&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn278418)"><strong>UsbInterruptInPipe.DataReceived</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/apps/dn278428" data-raw-source="[&lt;strong&gt;UsbInterruptOutPipe.OutputStream&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn278428)"><strong>UsbInterruptOutPipe.OutputStream</strong></a></p>
<p><a href="how-to-send-a-usb-interrupt-transfer--uwp-app-.md" data-raw-source="[How to send a USB interrupt transfer request (UWP app)](how-to-send-a-usb-interrupt-transfer--uwp-app-.md)">How to send a USB interrupt transfer request (UWP app)</a>.</p></td>
<td><p>Same as bulk transfers.</p></td>
</tr>
</tbody>
</table>

 

**6—Send isochronous transfers**, mostly used for media streaming devices.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Client driver</th>
<th>UWP app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>KMDF:</strong></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/hh439420" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceCreateIsochUrb&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439420)"><strong>WdfUsbTargetDeviceCreateIsochUrb</strong></a></p>
<p>See <a href="transfer-data-to-isochronous-endpoints.md" data-raw-source="[How to transfer data to USB isochronous endpoints](transfer-data-to-isochronous-endpoints.md)">How to transfer data to USB isochronous endpoints</a>.</p>
<p><strong>UMDF:</strong> Not supported.</p></td>
<td><p>Not supported.</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/dn265566" data-raw-source="[&lt;strong&gt;WinUsb_RegisterIsochBuffer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn265566)"><strong>WinUsb_RegisterIsochBuffer</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/dn265567" data-raw-source="[&lt;strong&gt;WinUsb_UnregisterIsochBuffer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn265567)"><strong>WinUsb_UnregisterIsochBuffer</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/dn265569" data-raw-source="[&lt;strong&gt;WinUsb_WriteIsochPipeAsap&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn265569)"><strong>WinUsb_WriteIsochPipeAsap</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/dn265565" data-raw-source="[&lt;strong&gt;WinUsb_ReadIsochPipeAsap&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn265565)"><strong>WinUsb_ReadIsochPipeAsap</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/dn265568" data-raw-source="[&lt;strong&gt;WinUsb_WriteIsochPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn265568)"><strong>WinUsb_WriteIsochPipe</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/dn265564" data-raw-source="[&lt;strong&gt;WinUsb_ReadIsochPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn265564)"><strong>WinUsb_ReadIsochPipe</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/dn265549" data-raw-source="[&lt;strong&gt;WinUsb_GetCurrentFrameNumber&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn265549)"><strong>WinUsb_GetCurrentFrameNumber</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/dn265548" data-raw-source="[&lt;strong&gt;WinUsb_GetAdjustedFrameNumber&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn265548)"><strong>WinUsb_GetAdjustedFrameNumber</strong></a></p>
<p>See <a href="getting-set-up-to-use-windows-devices-usb.md" data-raw-source="[Sending USB isochronous transfers from a WinUSB desktop app](getting-set-up-to-use-windows-devices-usb.md)">Sending USB isochronous transfers from a WinUSB desktop app</a>.</p></td>
</tr>
</tbody>
</table>

 

**7—USB selective suspend** to allow the device to enter a low power state and bring the device back to working state.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Client driver</th>
<th>UWP app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>KMDF:</strong></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551270" data-raw-source="[&lt;strong&gt;WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551270)"><strong>WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff545903" data-raw-source="[&lt;strong&gt;WdfDeviceAssignS0IdleSettings&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545903)"><strong>WdfDeviceAssignS0IdleSettings</strong></a></p>
<p><strong>UMDF:</strong></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560385" data-raw-source="[&lt;strong&gt;IWDFUsbTargetDevice::SetPowerPolicy&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560385)"><strong>IWDFUsbTargetDevice::SetPowerPolicy</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556920" data-raw-source="[&lt;strong&gt;IWDFDevice2::AssignS0IdleSettings&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556920)"><strong>IWDFDevice2::AssignS0IdleSettings</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/hh451202" data-raw-source="[&lt;strong&gt;IWDFDevice3::AssignS0IdleSettingsEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451202)"><strong>IWDFDevice3::AssignS0IdleSettingsEx</strong></a></p>
<p>See <a href="https://msdn.microsoft.com/windows/hardware/gg463309" data-raw-source="[How to send a device to selective suspend](https://msdn.microsoft.com/windows/hardware/gg463309)">How to send a device to selective suspend</a>.</p></td>
<td><p>Not supported.</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff540309" data-raw-source="[&lt;strong&gt;WinUsb_SetPowerPolicy&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540309)"><strong>WinUsb_SetPowerPolicy</strong></a></p>
<p>See <a href="winusb-power-management.md" data-raw-source="[WinUSB Power Management](winusb-power-management.md)">WinUSB Power Management</a>.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)  



