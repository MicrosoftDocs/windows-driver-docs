---
description: A Universal Serial Bus (USB) device defines its capabilities and features through configurations, interfaces, alternate settings, and endpoints.
title: Getting started with USB development
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Getting started with USB development

A Universal Serial Bus (USB) device defines its capabilities and features through configurations, interfaces, alternate settings, and endpoints. This topic provides a high-level overview of those concepts. For details, see the USB specifications at [Universal Serial Bus Documents]( https://go.microsoft.com/fwlink/p/?linkid=224892).

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
<td><p><a href="usb-faq--introductory-level.yml" data-raw-source="[USB in Windows - FAQ](usb-faq--introductory-level.yml)">USB in Windows - FAQ</a></p></td>
<td><p>This topic presents frequently asked questions for driver developers who are new to developing and integrating USB devices and drivers with Windows operating systems.</p></td>
</tr>
</tbody>
</table>

 

## Common USB scenarios


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
<td><p><strong>KMDF</strong>: <a href="/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceCreateWithParameters&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters)"><strong>WdfUsbTargetDeviceCreateWithParameters</strong></a></p>
<p><strong>UMDF</strong>: <a href="/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbtargetdevice" data-raw-source="[&lt;strong&gt;IWDFUsbTargetDevice&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbtargetdevice)"><strong>IWDFUsbTargetDevice</strong></a></p></td>
<td><p><a href="/uwp/api/Windows.Devices.Usb.UsbDevice" data-raw-source="[&lt;strong&gt;UsbDevice&lt;/strong&gt;](/uwp/api/Windows.Devices.Usb.UsbDevice)"><strong>UsbDevice</strong></a></p>
<p><a href="how-to-connect-to-a-usb-device--uwp-app-.md" data-raw-source="[How to connect to a USB device (UWP app)](how-to-connect-to-a-usb-device--uwp-app-.md)">How to connect to a USB device (UWP app)</a>.</p></td>
<td><p><a href="/windows/win32/api/winusb/nf-winusb-winusb_initialize" data-raw-source="[&lt;strong&gt;WinUsb_Initialize&lt;/strong&gt;](/windows/win32/api/winusb/nf-winusb-winusb_initialize)"><strong>WinUsb_Initialize</strong></a></p>
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
<p><a href="/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicegetdevicedescriptor" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceGetDeviceDescriptor&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicegetdevicedescriptor)"><strong>WdfUsbTargetDeviceGetDeviceDescriptor</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceretrieveconfigdescriptor" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceRetrieveConfigDescriptor&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceretrieveconfigdescriptor)"><strong>WdfUsbTargetDeviceRetrieveConfigDescriptor</strong></a></p>
<p><strong>UMDF</strong>:</p>
<p><a href="/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-retrievedescriptor" data-raw-source="[&lt;strong&gt;IWDFUsbTargetDevice::RetrieveDescriptor&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-retrievedescriptor)"><strong>IWDFUsbTargetDevice::RetrieveDescriptor</strong></a></p>
<p>See <a href="usb-descriptors.md" data-raw-source="[USB descriptors](usb-descriptors.md)">USB descriptors</a>.</p></td>
<td><p><a href="/uwp/api/Windows.Devices.Usb.UsbDevice#Windows_Devices_Usb_UsbDevice_DeviceDescriptor" data-raw-source="[&lt;strong&gt;UsbDevice.DeviceDescriptor&lt;/strong&gt;](/uwp/api/Windows.Devices.Usb.UsbDevice#Windows_Devices_Usb_UsbDevice_DeviceDescriptor)"><strong>UsbDevice.DeviceDescriptor</strong></a></p>
<p><a href="/uwp/api/Windows.Devices.Usb.UsbConfiguration#Windows_Devices_Usb_UsbConfiguration_Descriptors" data-raw-source="[&lt;strong&gt;UsbConfiguration.Descriptors&lt;/strong&gt;](/uwp/api/Windows.Devices.Usb.UsbConfiguration#Windows_Devices_Usb_UsbConfiguration_Descriptors)"><strong>UsbConfiguration.Descriptors</strong></a></p>
<p><a href="/uwp/api/Windows.Devices.Usb.UsbInterface#Windows_Devices_Usb_UsbInterface_Descriptors" data-raw-source="[&lt;strong&gt;UsbInterface.Descriptors&lt;/strong&gt;](/uwp/api/Windows.Devices.Usb.UsbInterface#Windows_Devices_Usb_UsbInterface_Descriptors)"><strong>UsbInterface.Descriptors</strong></a></p>
<p><a href="/uwp/api/Windows.Devices.Usb.UsbInterfaceSetting#Windows_Devices_Usb_UsbInterfaceSetting_Descriptors" data-raw-source="[&lt;strong&gt;UsbInterfaceSetting.Descriptors&lt;/strong&gt;](/uwp/api/Windows.Devices.Usb.UsbInterfaceSetting#Windows_Devices_Usb_UsbInterfaceSetting_Descriptors)"><strong>UsbInterfaceSetting.Descriptors</strong></a></p>
<p><a href="how-to-get-usb-descriptors--uwp-app-.md" data-raw-source="[How to get USB descriptors (UWP app)](how-to-get-usb-descriptors--uwp-app-.md)">How to get USB descriptors (UWP app)</a>.</p></td>
<td><p><a href="/windows/win32/api/winusb/nf-winusb-winusb_getdescriptor" data-raw-source="[&lt;strong&gt;WinUsb_GetDescriptor&lt;/strong&gt;](/windows/win32/api/winusb/nf-winusb-winusb_getdescriptor)"><strong>WinUsb_GetDescriptor</strong></a></p>
<p><a href="/windows/win32/api/winusb/nf-winusb-winusb_queryinterfacesettings" data-raw-source="[&lt;strong&gt;WinUsb_QueryInterfaceSettings&lt;/strong&gt;](/windows/win32/api/winusb/nf-winusb-winusb_queryinterfacesettings)"><strong>WinUsb_QueryInterfaceSettings</strong></a></p>
<p><a href="/windows/win32/api/winusb/nf-winusb-winusb_querypipe" data-raw-source="[&lt;strong&gt;WinUsb_QueryPipe&lt;/strong&gt;](/windows/win32/api/winusb/nf-winusb-winusb_querypipe)"><strong>WinUsb_QueryPipe</strong></a></p>
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
<p><a href="/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceselectconfig" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceSelectConfig&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceselectconfig)"><strong>WdfUsbTargetDeviceSelectConfig</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateurb" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceCreateUrb&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateurb)"><strong>WdfUsbTargetDeviceCreateUrb</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_selectconfigurballocateandbuild" data-raw-source="[&lt;strong&gt;USBD_SelectConfigUrbAllocateAndBuild&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_selectconfigurballocateandbuild)"><strong>USBD_SelectConfigUrbAllocateAndBuild</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfaceselectsetting" data-raw-source="[&lt;strong&gt;WdfUsbInterfaceSelectSetting&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfaceselectsetting)"><strong>WdfUsbInterfaceSelectSetting</strong></a></p>
<p>See <a href="how-to-select-a-configuration-for-a-usb-device.md" data-raw-source="[How to select a configuration for a USB device](how-to-select-a-configuration-for-a-usb-device.md)">How to select a configuration for a USB device</a>.</p>
<p>See <a href="select-a-usb-alternate-setting.md" data-raw-source="[How to select an alternate setting in a USB interface](select-a-usb-alternate-setting.md)">How to select an alternate setting in a USB interface</a>.</p>
<p><strong>UMDF:</strong></p>
<p>Configuration selection is not Supported.</p>
<p><a href="/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbinterface-selectsetting" data-raw-source="[&lt;strong&gt;IWDFUsbInterface::SelectSetting&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbinterface-selectsetting)"><strong>IWDFUsbInterface::SelectSetting</strong></a></p></td>
<td><p><a href="/uwp/api/Windows.Devices.Usb.UsbInterfaceSetting#Windows_Devices_Usb_UsbInterfaceSetting_SelectSettingAsync" data-raw-source="[&lt;strong&gt;UsbInterfaceSetting.SelectSettingAsync&lt;/strong&gt;](/uwp/api/Windows.Devices.Usb.UsbInterfaceSetting#Windows_Devices_Usb_UsbInterfaceSetting_SelectSettingAsync)"><strong>UsbInterfaceSetting.SelectSettingAsync</strong></a></p>
<p><a href="how-to-select-a-usb-interface-setting--uwp-app-.md" data-raw-source="[How to select a USB interface setting (UWP app)](how-to-select-a-usb-interface-setting--uwp-app-.md)">How to select a USB interface setting (UWP app)</a>.</p></td>
<td><a href="/windows/win32/api/winusb/nf-winusb-winusb_setcurrentalternatesetting" data-raw-source="[&lt;strong&gt;WinUsb_SetCurrentAlternateSetting&lt;/strong&gt;](/windows/win32/api/winusb/nf-winusb-winusb_setcurrentalternatesetting)"><strong>WinUsb_SetCurrentAlternateSetting</strong></a></td>
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
<p><a href="/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendcontroltransfersynchronously" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceSendControlTransferSynchronously&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendcontroltransfersynchronously)"><strong>WdfUsbTargetDeviceSendControlTransferSynchronously</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforcontroltransfer" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceFormatRequestForControlTransfer&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforcontroltransfer)"><strong>WdfUsbTargetDeviceFormatRequestForControlTransfer</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_selectconfigurballocateandbuild" data-raw-source="[&lt;strong&gt;USBD_SelectConfigUrbAllocateAndBuild&lt;/strong&gt;](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_selectconfigurballocateandbuild)"><strong>USBD_SelectConfigUrbAllocateAndBuild</strong></a></p>
<p><strong>UMDF:</strong></p>
<p><a href="/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-formatrequestforcontroltransfer" data-raw-source="[&lt;strong&gt;IWDFUsbTargetDevice::FormatRequestForControlTransfer&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-formatrequestforcontroltransfer)"><strong>IWDFUsbTargetDevice::FormatRequestForControlTransfer</strong></a></p>
<p>See <a href="usb-control-transfer.md" data-raw-source="[How to send a USB control transfer](usb-control-transfer.md)">How to send a USB control transfer</a>.</p></td>
<td><p><a href="/uwp/api/Windows.Devices.Usb.UsbDevice#Windows_Devices_Usb_UsbDevice_SendControlInTransferAsync_Windows_Devices_Usb_UsbSetupPacket_" data-raw-source="[&lt;strong&gt;SendControlInTransferAsync&lt;/strong&gt;](/uwp/api/Windows.Devices.Usb.UsbDevice#Windows_Devices_Usb_UsbDevice_SendControlInTransferAsync_Windows_Devices_Usb_UsbSetupPacket_)"><strong>SendControlInTransferAsync</strong></a></p>
<p><a href="/uwp/api/Windows.Devices.Usb.UsbDevice#Windows_Devices_Usb_UsbDevice_SendControlOutTransferAsync_Windows_Devices_Usb_UsbSetupPacket_" data-raw-source="[&lt;strong&gt;SendControlOutTransferAsync&lt;/strong&gt;](/uwp/api/Windows.Devices.Usb.UsbDevice#Windows_Devices_Usb_UsbDevice_SendControlOutTransferAsync_Windows_Devices_Usb_UsbSetupPacket_)"><strong>SendControlOutTransferAsync</strong></a></p>
<p><a href="how-to-send-a-usb-control-transfer--uwp-app-.md" data-raw-source="[How to send a USB control transfer (UWP app)](how-to-send-a-usb-control-transfer--uwp-app-.md)">How to send a USB control transfer (UWP app)</a>.</p></td>
<td><p><a href="/windows/win32/api/winusb/nf-winusb-winusb_controltransfer" data-raw-source="[&lt;strong&gt;WinUsb_ControlTransfer&lt;/strong&gt;](/windows/win32/api/winusb/nf-winusb-winusb_controltransfer)"><strong>WinUsb_ControlTransfer</strong></a></p>
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
<p><a href="/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipereadsynchronously" data-raw-source="[&lt;strong&gt;WdfUsbTargetPipeReadSynchronously&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipereadsynchronously)"><strong>WdfUsbTargetPipeReadSynchronously</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipewritesynchronously" data-raw-source="[&lt;strong&gt;WdfUsbTargetPipeWriteSynchronously&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipewritesynchronously)"><strong>WdfUsbTargetPipeWriteSynchronously</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeformatrequestforread" data-raw-source="[&lt;strong&gt;WdfUsbTargetPipeFormatRequestForRead&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeformatrequestforread)"><strong>WdfUsbTargetPipeFormatRequestForRead</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeformatrequestforwrite" data-raw-source="[&lt;strong&gt;WdfUsbTargetPipeFormatRequestForWrite&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeformatrequestforwrite)"><strong>WdfUsbTargetPipeFormatRequestForWrite</strong></a></p>
<p><a href="usb-bulk-and-interrupt-transfer.md" data-raw-source="[How to send USB bulk transfer requests](usb-bulk-and-interrupt-transfer.md)">How to send USB bulk transfer requests</a></p>
<p><a href="how-to-use-the-continous-reader-for-getting-data-from-a-usb-endpoint--umdf-.md" data-raw-source="[How to use the continuous reader for reading data from a USB pipe](how-to-use-the-continous-reader-for-getting-data-from-a-usb-endpoint--umdf-.md)">How to use the continuous reader for reading data from a USB pipe</a>.</p>
<p><strong>UMDF:</strong></p>
<p><a href="/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iusbtargetpipecontinuousreadercallbackreadcomplete" data-raw-source="[&lt;strong&gt;IUsbTargetPipeContinuousReaderCallbackReadComplete&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iusbtargetpipecontinuousreadercallbackreadcomplete)"><strong>IUsbTargetPipeContinuousReaderCallbackReadComplete</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbtargetpipe" data-raw-source="[&lt;strong&gt;IWDFUsbTargetPipe&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbtargetpipe)"><strong>IWDFUsbTargetPipe</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbtargetpipe2" data-raw-source="[&lt;strong&gt;IWDFUsbTargetPipe2&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbtargetpipe2)"><strong>IWDFUsbTargetPipe2</strong></a></p></td>
<td><p><a href="/uwp/api/Windows.Devices.Usb.UsbBulkInPipe#Windows_Devices_Usb_UsbBulkInPipe_InputStream" data-raw-source="[&lt;strong&gt;UsbBulkInPipe.InputStream&lt;/strong&gt;](/uwp/api/Windows.Devices.Usb.UsbBulkInPipe#Windows_Devices_Usb_UsbBulkInPipe_InputStream)"><strong>UsbBulkInPipe.InputStream</strong></a></p>
<p><a href="/uwp/api/Windows.Devices.Usb.UsbBulkOutPipe#Windows_Devices_Usb_UsbBulkOutPipe_OutputStream" data-raw-source="[&lt;strong&gt;UsbBulkOutPipe.OutputStream&lt;/strong&gt;](/uwp/api/Windows.Devices.Usb.UsbBulkOutPipe#Windows_Devices_Usb_UsbBulkOutPipe_OutputStream)"><strong>UsbBulkOutPipe.OutputStream</strong></a></p>
<p><a href="how-to-send-a-usb-bulk-transfer--uwp-app-.md" data-raw-source="[How to send a USB bulk transfer request (UWP app)](how-to-send-a-usb-bulk-transfer--uwp-app-.md)">How to send a USB bulk transfer request (UWP app)</a>.</p></td>
<td><p><a href="/windows/win32/api/winusb/nf-winusb-winusb_writepipe" data-raw-source="[&lt;strong&gt;WinUsb_WritePipe&lt;/strong&gt;](/windows/win32/api/winusb/nf-winusb-winusb_writepipe)"><strong>WinUsb_WritePipe</strong></a></p>
<p><a href="/windows/win32/api/winusb/nf-winusb-winusb_readpipe" data-raw-source="[&lt;strong&gt;WinUsb_ReadPipe&lt;/strong&gt;](/windows/win32/api/winusb/nf-winusb-winusb_readpipe)"><strong>WinUsb_ReadPipe</strong></a></p>
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
<td><p><a href="/uwp/api/Windows.Devices.Usb.UsbInterruptInPipe#Windows_Devices_Usb_UsbInterruptInPipe_DataReceived" data-raw-source="[&lt;strong&gt;UsbInterruptInPipe.DataReceived&lt;/strong&gt;](/uwp/api/Windows.Devices.Usb.UsbInterruptInPipe#Windows_Devices_Usb_UsbInterruptInPipe_DataReceived)"><strong>UsbInterruptInPipe.DataReceived</strong></a></p>
<p><a href="/uwp/api/Windows.Devices.Usb.UsbInterruptOutPipe#Windows_Devices_Usb_UsbInterruptOutPipe_OutputStream" data-raw-source="[&lt;strong&gt;UsbInterruptOutPipe.OutputStream&lt;/strong&gt;](/uwp/api/Windows.Devices.Usb.UsbInterruptOutPipe#Windows_Devices_Usb_UsbInterruptOutPipe_OutputStream)"><strong>UsbInterruptOutPipe.OutputStream</strong></a></p>
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
<p><a href="/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateisochurb" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceCreateIsochUrb&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateisochurb)"><strong>WdfUsbTargetDeviceCreateIsochUrb</strong></a></p>
<p>See <a href="transfer-data-to-isochronous-endpoints.md" data-raw-source="[How to transfer data to USB isochronous endpoints](transfer-data-to-isochronous-endpoints.md)">How to transfer data to USB isochronous endpoints</a>.</p>
<p><strong>UMDF:</strong> Not supported.</p></td>
<td><p>Not supported.</p></td>
<td><p><a href="/windows/win32/api/winusb/nf-winusb-winusb_registerisochbuffer" data-raw-source="[&lt;strong&gt;WinUsb_RegisterIsochBuffer&lt;/strong&gt;](/windows/win32/api/winusb/nf-winusb-winusb_registerisochbuffer)"><strong>WinUsb_RegisterIsochBuffer</strong></a></p>
<p><a href="/windows/win32/api/winusb/nf-winusb-winusb_unregisterisochbuffer" data-raw-source="[&lt;strong&gt;WinUsb_UnregisterIsochBuffer&lt;/strong&gt;](/windows/win32/api/winusb/nf-winusb-winusb_unregisterisochbuffer)"><strong>WinUsb_UnregisterIsochBuffer</strong></a></p>
<p><a href="/windows/win32/api/winusb/nf-winusb-winusb_writeisochpipeasap" data-raw-source="[&lt;strong&gt;WinUsb_WriteIsochPipeAsap&lt;/strong&gt;](/windows/win32/api/winusb/nf-winusb-winusb_writeisochpipeasap)"><strong>WinUsb_WriteIsochPipeAsap</strong></a></p>
<p><a href="/windows/win32/api/winusb/nf-winusb-winusb_readisochpipeasap" data-raw-source="[&lt;strong&gt;WinUsb_ReadIsochPipeAsap&lt;/strong&gt;](/windows/win32/api/winusb/nf-winusb-winusb_readisochpipeasap)"><strong>WinUsb_ReadIsochPipeAsap</strong></a></p>
<p><a href="/windows/win32/api/winusb/nf-winusb-winusb_writeisochpipe" data-raw-source="[&lt;strong&gt;WinUsb_WriteIsochPipe&lt;/strong&gt;](/windows/win32/api/winusb/nf-winusb-winusb_writeisochpipe)"><strong>WinUsb_WriteIsochPipe</strong></a></p>
<p><a href="/windows/win32/api/winusb/nf-winusb-winusb_readisochpipe" data-raw-source="[&lt;strong&gt;WinUsb_ReadIsochPipe&lt;/strong&gt;](/windows/win32/api/winusb/nf-winusb-winusb_readisochpipe)"><strong>WinUsb_ReadIsochPipe</strong></a></p>
<p><a href="/windows/win32/api/winusb/nf-winusb-winusb_getcurrentframenumber" data-raw-source="[&lt;strong&gt;WinUsb_GetCurrentFrameNumber&lt;/strong&gt;](/windows/win32/api/winusb/nf-winusb-winusb_getcurrentframenumber)"><strong>WinUsb_GetCurrentFrameNumber</strong></a></p>
<p><a href="/windows/win32/api/winusb/nf-winusb-winusb_getadjustedframenumber" data-raw-source="[&lt;strong&gt;WinUsb_GetAdjustedFrameNumber&lt;/strong&gt;](/windows/win32/api/winusb/nf-winusb-winusb_getadjustedframenumber)"><strong>WinUsb_GetAdjustedFrameNumber</strong></a></p>
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
<p><a href="/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_idle_settings" data-raw-source="[&lt;strong&gt;WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_idle_settings)"><strong>WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings" data-raw-source="[&lt;strong&gt;WdfDeviceAssignS0IdleSettings&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings)"><strong>WdfDeviceAssignS0IdleSettings</strong></a></p>
<p><strong>UMDF:</strong></p>
<p><a href="/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-setpowerpolicy" data-raw-source="[&lt;strong&gt;IWDFUsbTargetDevice::SetPowerPolicy&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-setpowerpolicy)"><strong>IWDFUsbTargetDevice::SetPowerPolicy</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice2-assigns0idlesettings" data-raw-source="[&lt;strong&gt;IWDFDevice2::AssignS0IdleSettings&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice2-assigns0idlesettings)"><strong>IWDFDevice2::AssignS0IdleSettings</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice3-assigns0idlesettingsex" data-raw-source="[&lt;strong&gt;IWDFDevice3::AssignS0IdleSettingsEx&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice3-assigns0idlesettingsex)"><strong>IWDFDevice3::AssignS0IdleSettingsEx</strong></a></p>
<p>See <a href="/windows-hardware/drivers/usbcon/" data-raw-source="[How to send a device to selective suspend](./index.md)">How to send a device to selective suspend</a>.</p></td>
<td><p>Not supported.</p></td>
<td><p><a href="/windows/win32/api/winusb/nf-winusb-winusb_setpowerpolicy" data-raw-source="[&lt;strong&gt;WinUsb_SetPowerPolicy&lt;/strong&gt;](/windows/win32/api/winusb/nf-winusb-winusb_setpowerpolicy)"><strong>WinUsb_SetPowerPolicy</strong></a></p>
<p>See <a href="winusb-power-management.md" data-raw-source="[WinUSB Power Management](winusb-power-management.md)">WinUSB Power Management</a>.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[Universal Serial Bus (USB)](../index.yml)