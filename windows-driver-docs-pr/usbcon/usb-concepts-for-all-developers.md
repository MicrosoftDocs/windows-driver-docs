---
Description: A Universal Serial Bus (USB) device defines its capabilities and features through configurations, interfaces, alternate settings, and endpoints.
title: Concepts for all USB developers
author: windows-driver-content
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
<td><p>[USB device layout](usb-device-layout.md)</p></td>
<td><p>A USB device defines its capabilities and features through configurations, interfaces, alternate settings, and endpoints. This topic provides a high-level overview of those concepts.</p></td>
</tr>
<tr class="even">
<td><p>[Standard USB descriptors](standard-usb-descriptors.md)</p></td>
<td><p>A USB device provides information about itself in data structures called <em>USB descriptors</em>. This section provides information about device, configuration, interface, and endpoint descriptors and ways to retrieve them from a USB device.</p></td>
</tr>
<tr class="odd">
<td><p>[USB endpoints and their pipes](usb-endpoints-and-their-pipes.md)</p></td>
<td><p>A USB device has endpoints that are used to for data transfers. On the host side, endpoints are represented by pipes. This topic differentiates between those two terms.</p></td>
</tr>
<tr class="even">
<td><p>[USB in Windows - FAQ](usb-faq--introductory-level.md)</p></td>
<td><p>This topic presents frequently asked questions for driver developers who are new to developing and integrating USB devices and drivers with Windows operating systems.</p></td>
</tr>
</tbody>
</table>

 

## <a href="" id="scenarios"></a>**Common USB scenarios**


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
<th>Windows Store app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>KMDF</strong>: [<strong>WdfUsbTargetDeviceCreateWithParameters</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439428)</p>
<p><strong>UMDF</strong>: [<strong>IWDFUsbTargetDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560362)</p></td>
<td><p>[<strong>UsbDevice</strong>](https://msdn.microsoft.com/library/windows/apps/dn263883)</p>
<p>[How to connect to a USB device (Windows Store app)](how-to-connect-to-a-usb-device--windows-store-app-.md).</p></td>
<td><p>[<strong>WinUsb_Initialize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540277)</p>
<p>See [Write a Windows desktop app based on the WinUSB template](how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md).</p></td>
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
<th>Windows Store app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>KMDF</strong>:</p>
<p>[<strong>WdfUsbTargetDeviceGetDeviceDescriptor</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550090)</p>
<p>[<strong>WdfUsbTargetDeviceRetrieveConfigDescriptor</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550098)</p>
<p><strong>UMDF</strong>:</p>
<p>[<strong>IWDFUsbTargetDevice::RetrieveDescriptor</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560374)</p>
<p>See [USB descriptors](usb-descriptors.md).</p></td>
<td><p>[<strong>UsbDevice.DeviceDescriptor</strong>](https://msdn.microsoft.com/library/windows/apps/dn264002)</p>
<p>[<strong>UsbConfiguration.Descriptors</strong>](https://msdn.microsoft.com/library/windows/apps/dn263802)</p>
<p>[<strong>UsbInterface.Descriptors</strong>](https://msdn.microsoft.com/library/windows/apps/dn264289)</p>
<p>[<strong>UsbInterfaceSetting.Descriptors</strong>](https://msdn.microsoft.com/library/windows/apps/dn264281)</p>
<p>[How to get USB descriptors (Windows Store app)](how-to-get-usb-descriptors--windows-store-app-.md).</p></td>
<td><p>[<strong>WinUsb_GetDescriptor</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540257)</p>
<p>[<strong>WinUsb_QueryInterfaceSettings</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540292)</p>
<p>[<strong>WinUsb_QueryPipe</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540293)</p>
<p>See [Query the Device for USB Descriptors](using-winusb-api-to-communicate-with-a-usb-device.md#query).</p></td>
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
<th>Windows Store app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>KMDF:</strong></p>
<p>[<strong>WdfUsbTargetDeviceSelectConfig</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550101)</p>
<p>[<strong>WdfUsbTargetDeviceCreateUrb</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439423)</p>
<p>[<strong>USBD_SelectConfigUrbAllocateAndBuild</strong>](https://msdn.microsoft.com/library/windows/hardware/hh406243)</p>
<p>[<strong>WdfUsbInterfaceSelectSetting</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550073)</p>
<p>See [How to select a configuration for a USB device](how-to-select-a-configuration-for-a-usb-device.md).</p>
<p>See [How to select an alternate setting in a USB interface](select-a-usb-alternate-setting.md).</p>
<p><strong>UMDF:</strong></p>
<p>Configuration selection is not Supported.</p>
<p>[<strong>IWDFUsbInterface::SelectSetting</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560343)</p></td>
<td><p>[<strong>UsbInterfaceSetting.SelectSettingAsync</strong>](https://msdn.microsoft.com/library/windows/apps/dn264286)</p>
<p>[How to select a USB interface setting (Windows Store app)](how-to-select-a-usb-interface-setting--windows-store-app-.md).</p></td>
<td>[<strong>WinUsb_SetCurrentAlternateSetting</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540302)</td>
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
<th>Windows Store app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>KMDF:</strong></p>
<p>[<strong>WdfUsbTargetDeviceSendControlTransferSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550104)</p>
<p>[<strong>WdfUsbTargetDeviceFormatRequestForControlTransfer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550082)</p>
<p>[<strong>USBD_SelectConfigUrbAllocateAndBuild</strong>](https://msdn.microsoft.com/library/windows/hardware/hh406243)</p>
<p><strong>UMDF:</strong></p>
<p>[<strong>IWDFUsbTargetDevice::FormatRequestForControlTransfer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560363)</p>
<p>See [How to send a USB control transfer](usb-control-transfer.md).</p></td>
<td><p>[<strong>SendControlInTransferAsync</strong>](https://msdn.microsoft.com/library/windows/apps/dn264037)</p>
<p>[<strong>SendControlOutTransferAsync</strong>](https://msdn.microsoft.com/library/windows/apps/dn264047)</p>
<p>[How to send a USB control transfer (Windows Store app)](how-to-send-a-usb-control-transfer--windows-store-app-.md).</p></td>
<td><p>[<strong>WinUsb_ControlTransfer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540219)</p>
<p>See [Send Control Transfer to the Default Endpoint](using-winusb-api-to-communicate-with-a-usb-device.md#control).</p></td>
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
<th>Windows Store app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>KMDF:</strong></p>
<p>[<strong>WdfUsbTargetPipeReadSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551155)</p>
<p>[<strong>WdfUsbTargetPipeWriteSynchronously</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551163)</p>
<p>[<strong>WdfUsbTargetPipeFormatRequestForRead</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551136)</p>
<p>[<strong>WdfUsbTargetPipeFormatRequestForWrite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551141)</p>
<p>[How to send USB bulk transfer requests](usb-bulk-and-interrupt-transfer.md)</p>
<p>[How to use the continuous reader for reading data from a USB pipe](how-to-use-the-continous-reader-for-getting-data-from-a-usb-endpoint--umdf-.md).</p>
<p><strong>UMDF:</strong></p>
<p>[<strong>IUsbTargetPipeContinuousReaderCallbackReadComplete</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556908)</p>
<p>[<strong>IWDFUsbTargetPipe</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560391)</p>
<p>[<strong>IWDFUsbTargetPipe2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560394)</p></td>
<td><p>[<strong>UsbBulkInPipe.InputStream</strong>](https://msdn.microsoft.com/library/windows/apps/dn297601)</p>
<p>[<strong>UsbBulkOutPipe.OutputStream</strong>](https://msdn.microsoft.com/library/windows/apps/dn297669)</p>
<p>[How to send a USB bulk transfer request (Windows Store app)](how-to-send-a-usb-bulk-transfer--windows-store-app-.md).</p></td>
<td><p>[<strong>WinUsb_WritePipe</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540322)</p>
<p>[<strong>WinUsb_ReadPipe</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540297)</p>
<p>See [Issue I/O Requests](using-winusb-api-to-communicate-with-a-usb-device.md#io).</p></td>
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
<th>Windows Store app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Same as bulk transfers.</p></td>
<td><p>[<strong>UsbInterruptInPipe.DataReceived</strong>](https://msdn.microsoft.com/library/windows/apps/dn278418)</p>
<p>[<strong>UsbInterruptOutPipe.OutputStream</strong>](https://msdn.microsoft.com/library/windows/apps/dn278428)</p>
<p>[How to send a USB interrupt transfer request (Windows Store app)](how-to-send-a-usb-interrupt-transfer--windows-store-app-.md).</p></td>
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
<th>Windows Store app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>KMDF:</strong></p>
<p>[<strong>WdfUsbTargetDeviceCreateIsochUrb</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439420)</p>
<p>See [How to transfer data to USB isochronous endpoints](transfer-data-to-isochronous-endpoints.md).</p>
<p><strong>UMDF:</strong> Not supported.</p></td>
<td><p>Not supported.</p></td>
<td><p>[<strong>WinUsb_RegisterIsochBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265566)</p>
<p>[<strong>WinUsb_UnregisterIsochBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265567)</p>
<p>[<strong>WinUsb_WriteIsochPipeAsap</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265569)</p>
<p>[<strong>WinUsb_ReadIsochPipeAsap</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265565)</p>
<p>[<strong>WinUsb_WriteIsochPipe</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265568)</p>
<p>[<strong>WinUsb_ReadIsochPipe</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265564)</p>
<p>[<strong>WinUsb_GetCurrentFrameNumber</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265549)</p>
<p>[<strong>WinUsb_GetAdjustedFrameNumber</strong>](https://msdn.microsoft.com/library/windows/hardware/dn265548)</p>
<p>See [Sending USB isochronous transfers from a WinUSB desktop app](getting-set-up-to-use-windows-devices-usb.md).</p></td>
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
<th>Windows Store app</th>
<th>Windows desktop app</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>KMDF:</strong></p>
<p>[<strong>WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551270)</p>
<p>[<strong>WdfDeviceAssignS0IdleSettings</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545903)</p>
<p><strong>UMDF:</strong></p>
<p>[<strong>IWDFUsbTargetDevice::SetPowerPolicy</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560385)</p>
<p>[<strong>IWDFDevice2::AssignS0IdleSettings</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556920)</p>
<p>[<strong>IWDFDevice3::AssignS0IdleSettingsEx</strong>](https://msdn.microsoft.com/library/windows/hardware/hh451202)</p>
<p>See [How to send a device to selective suspend](http://msdn.microsoft.com/windows/hardware/gg463309).</p></td>
<td><p>Not supported.</p></td>
<td><p>[<strong>WinUsb_SetPowerPolicy</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540309)</p>
<p>See [WinUSB Power Management](winusb-power-management.md).</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20%20Concepts%20for%20all%20USB%20developers%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


