---
description: A Universal Serial Bus (USB) device defines its capabilities and features through configurations, interfaces, alternate settings, and endpoints.
title: Getting started with USB development
ms.date: 10/28/2022
---

# Getting started with USB development

A Universal Serial Bus (USB) device defines its capabilities and features through configurations, interfaces, alternate settings, and endpoints. This topic provides a high-level overview of those concepts. For details, see the USB specifications at [Universal Serial Bus Documents]( https://go.microsoft.com/fwlink/p/?linkid=224892).

## In this section

| Topic | Description |
|---|---|
| [USB device layout](usb-device-layout.md) | A USB device defines its capabilities and features through configurations, interfaces, alternate settings, and endpoints. This topic provides a high-level overview of those concepts. |
| [Standard USB descriptors](standard-usb-descriptors.md) | A USB device provides information about itself in data structures called _USB descriptors_. This section provides information about device, configuration, interface, and endpoint descriptors and ways to retrieve them from a USB device. |
| [USB endpoints and their pipes](usb-endpoints-and-their-pipes.md) | A USB device has endpoints that are used to for data transfers. On the host side, endpoints are represented by pipes. This topic differentiates between those two terms. |
| [USB in Windows - FAQ](usb-faq--introductory-level.yml) | This topic presents frequently asked questions for driver developers who are new to developing and integrating USB devices and drivers with Windows operating systems. |

## Common USB scenarios

**1—Get the device handle** for communication and use the retrieved handle or object to send data transfers.

| Client driver | UWP app | Windows desktop app |
|---|---|---|
| **KMDF**:</br>**[WdfUsbTargetDeviceCreateWithParameters](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters)**</br></br>**UMDF**:<br>**[IWDFUsbTargetDevice](/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbtargetdevice)** | **[UsbDevice](/uwp/api/Windows.Devices.Usb.UsbDevice)**</br></br>[How to connect to a USB device](how-to-connect-to-a-usb-device--uwp-app-.md) | **[WinUsb_Initialize](/windows/win32/api/winusb/nf-winusb-winusb_initialize)**</br></br>[Write a Windows desktop app based on the WinUSB template](how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md) |

**USB descriptor retrieval** to get information about the device's configuration(s), interface(s), setting(s), and their endpoint(s).

| Client driver | UWP app | Windows desktop app |
|---|---|---|
| **KMDF**:<br></br>**[WdfUsbTargetDeviceGetDeviceDescriptor](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicegetdevicedescriptor)**</br>**[WdfUsbTargetDeviceRetrieveConfigDescriptor](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceretrieveconfigdescriptor)**</br></br>**UMDF**:</br></br>**[IWDFUsbTargetDevice::RetrieveDescriptor](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-retrievedescriptor)**</br></br>[USB descriptors](usb-descriptors.md) | **[UsbDevice.DeviceDescriptor](/uwp/api/Windows.Devices.Usb.UsbDevice#Windows_Devices_Usb_UsbDevice_DeviceDescriptor)**</br>**[UsbConfiguration.Descriptors](/uwp/api/Windows.Devices.Usb.UsbConfiguration#Windows_Devices_Usb_UsbConfiguration_Descriptors)**</br>**[UsbInterface.Descriptors](/uwp/api/Windows.Devices.Usb.UsbInterface#Windows_Devices_Usb_UsbInterface_Descriptors)**</br>**[UsbInterfaceSetting.Descriptors](/uwp/api/Windows.Devices.Usb.UsbInterfaceSetting#Windows_Devices_Usb_UsbInterfaceSetting_Descriptors)**</br></br>[How to get USB descriptors](how-to-get-usb-descriptors--uwp-app-.md) | **[WinUsb_GetDescriptor](/windows/win32/api/winusb/nf-winusb-winusb_getdescriptor)**</br>**[WinUsb_QueryInterfaceSettings](/windows/win32/api/winusb/nf-winusb-winusb_queryinterfacesettings)**</br>**[WinUsb_QueryPipe](/windows/win32/api/winusb/nf-winusb-winusb_querypipe)**</br></br>[Query the Device for USB Descriptors](using-winusb-api-to-communicate-with-a-usb-device.md#step-2-query-the-device-for-usb-descriptors) |

**2—Configure the device** to select an active USB configuration and setting per interface.

| Client driver | UWP app | Windows desktop app |
|---|---|---|
| **KMDF:**</br>**[WdfUsbTargetDeviceSelectConfig](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceselectconfig)**</br>**[WdfUsbTargetDeviceCreateUrb](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateurb)**</br>**[USBD_SelectConfigUrbAllocateAndBuild](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_selectconfigurballocateandbuild)**</br>**[WdfUsbInterfaceSelectSetting](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfaceselectsetting)**</br></br>[How to select a configuration for a USB device](how-to-select-a-configuration-for-a-usb-device.md).</br></br>[How to select an alternate setting in a USB interface](select-a-usb-alternate-setting.md).</br></br>**UMDF:**</br>Configuration selection is not supported</br></br>**[IWDFUsbInterface::SelectSetting](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbinterface-selectsetting)** | **[UsbInterfaceSetting.SelectSettingAsync](/uwp/api/Windows.Devices.Usb.UsbInterfaceSetting#Windows_Devices_Usb_UsbInterfaceSetting_SelectSettingAsync)**</br></br>[How to select a USB interface setting](how-to-select-a-usb-interface-setting--uwp-app-.md) | **[WinUsb_SetCurrentAlternateSetting](/windows/win32/api/winusb/nf-winusb-winusb_setcurrentalternatesetting)** |

**3—Send control transfers** for configuring the device and performing vendor commands that are specific to particular device.

| Client driver | UWP app | Windows desktop app |
|---|---|---|
| **KMDF:**</br>**[WdfUsbTargetDeviceSendControlTransferSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendcontroltransfersynchronously)**</br>**[WdfUsbTargetDeviceFormatRequestForControlTransfer](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforcontroltransfer)**</br>**[USBD_SelectConfigUrbAllocateAndBuild](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_selectconfigurballocateandbuild)**</br></br>**UMDF:**</br>**[IWDFUsbTargetDevice::FormatRequestForControlTransfer](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-formatrequestforcontroltransfer)**</br></br>[How to send a USB control transfer](usb-control-transfer.md) | **[SendControlInTransferAsync](/uwp/api/Windows.Devices.Usb.UsbDevice#Windows_Devices_Usb_UsbDevice_SendControlInTransferAsync_Windows_Devices_Usb_UsbSetupPacket_)**</br>**[SendControlOutTransferAsync](/uwp/api/Windows.Devices.Usb.UsbDevice#Windows_Devices_Usb_UsbDevice_SendControlOutTransferAsync_Windows_Devices_Usb_UsbSetupPacket_)**</br></br>[How to send a USB control transfer](how-to-send-a-usb-control-transfer--uwp-app-.md) | **[WinUsb_ControlTransfer](/windows/win32/api/winusb/nf-winusb-winusb_controltransfer)**</br></br>[Send Control Transfer to the Default Endpoint](using-winusb-api-to-communicate-with-a-usb-device.md#step-3-send-control-transfer-to-the-default-endpoint) |

**4—Send bulk transfers**, typically used by mass storage devices that transfer large amount of data.

| Client driver | UWP app | Windows desktop app |
|---|---|---|
| **KMDF:**</br>**[WdfUsbTargetPipeReadSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipereadsynchronously)**</br>**[WdfUsbTargetPipeWriteSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipewritesynchronously)**</br>**[WdfUsbTargetPipeFormatRequestForRead](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeformatrequestforread)**</br>**[WdfUsbTargetPipeFormatRequestForWrite](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeformatrequestforwrite)**</br></br>[How to send USB bulk transfer requests](usb-bulk-and-interrupt-transfer.md)</br></br>[How to use the continuous reader for reading data from a USB pipe](how-to-use-the-continous-reader-for-getting-data-from-a-usb-endpoint--umdf-.md)</br></br>**UMDF:**</br>**[IUsbTargetPipeContinuousReaderCallbackReadComplete](/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iusbtargetpipecontinuousreadercallbackreadcomplete)**</br>**[IWDFUsbTargetPipe](/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbtargetpipe)**</br>**[IWDFUsbTargetPipe2](/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbtargetpipe2)** | **[UsbBulkInPipe.InputStream](/uwp/api/Windows.Devices.Usb.UsbBulkInPipe#Windows_Devices_Usb_UsbBulkInPipe_InputStream)**</br>**[UsbBulkOutPipe.OutputStream](/uwp/api/Windows.Devices.Usb.UsbBulkOutPipe#Windows_Devices_Usb_UsbBulkOutPipe_OutputStream)**</br></br>[How to send a USB bulk transfer request](how-to-send-a-usb-bulk-transfer--uwp-app-.md) | **[WinUsb_WritePipe](/windows/win32/api/winusb/nf-winusb-winusb_writepipe)**</br>**[WinUsb_ReadPipe](/windows/win32/api/winusb/nf-winusb-winusb_readpipe)**</br></br>[Issue I/O Requests](using-winusb-api-to-communicate-with-a-usb-device.md#step-4-issue-io-requests) |

**5—Send interrupt transfers**. Data is read to retrieve hardware interrupt data.

| Client driver | UWP app | Windows desktop app |
|---|---|---|
| Same as bulk transfers | **[UsbInterruptInPipe.DataReceived](/uwp/api/Windows.Devices.Usb.UsbInterruptInPipe#Windows_Devices_Usb_UsbInterruptInPipe_DataReceived)**</br>**[UsbInterruptOutPipe.OutputStream](/uwp/api/Windows.Devices.Usb.UsbInterruptOutPipe#Windows_Devices_Usb_UsbInterruptOutPipe_OutputStream)**</br></br>[How to send a USB interrupt transfer request](how-to-send-a-usb-interrupt-transfer--uwp-app-.md) | Same as bulk transfers |

**6—Send isochronous transfers**, mostly used for media streaming devices.

| Client driver | UWP app | Windows desktop app |
|---|---|---|
| **KMDF:**</br>**[WdfUsbTargetDeviceCreateIsochUrb](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateisochurb)**</br></br>[How to transfer data to USB isochronous endpoints](transfer-data-to-isochronous-endpoints.md)</br></br>**UMDF:**</br>Not supported | Not supported | **[WinUsb_RegisterIsochBuffer](/windows/win32/api/winusb/nf-winusb-winusb_registerisochbuffer)**</br>**[WinUsb_UnregisterIsochBuffer](/windows/win32/api/winusb/nf-winusb-winusb_unregisterisochbuffer)**</br>**[WinUsb_WriteIsochPipeAsap](/windows/win32/api/winusb/nf-winusb-winusb_writeisochpipeasap)**</br>**[WinUsb_ReadIsochPipeAsap](/windows/win32/api/winusb/nf-winusb-winusb_readisochpipeasap)**</br>**[WinUsb_WriteIsochPipe](/windows/win32/api/winusb/nf-winusb-winusb_writeisochpipe)**</br>**[WinUsb_ReadIsochPipe](/windows/win32/api/winusb/nf-winusb-winusb_readisochpipe)**</br>**[WinUsb_GetCurrentFrameNumber](/windows/win32/api/winusb/nf-winusb-winusb_getcurrentframenumber)**</br>**[WinUsb_GetAdjustedFrameNumber](/windows/win32/api/winusb/nf-winusb-winusb_getadjustedframenumber)**</br></br>[Sending USB isochronous transfers from a WinUSB desktop app](getting-set-up-to-use-windows-devices-usb.md) |

**7—USB selective suspend** to allow the device to enter a low power state and bring the device back to working state.

| Client driver | UWP app | Windows desktop app |
|---|---|---|
| **KMDF:**</br>**[WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_idle_settings)**</br>**[WdfDeviceAssignS0IdleSettings](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings)**</br></br>**UMDF:**</br>**[IWDFUsbTargetDevice::SetPowerPolicy](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-setpowerpolicy)**</br>**[IWDFDevice2::AssignS0IdleSettings](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice2-assigns0idlesettings)**</br>**[IWDFDevice3::AssignS0IdleSettingsEx](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice3-assigns0idlesettingsex)**</br></br>[How to send a device to selective suspend](/windows-hardware/drivers/usbcon/) | Not supported | **[WinUsb_SetPowerPolicy](/windows/win32/api/winusb/nf-winusb-winusb_setpowerpolicy)**</br></br>[WinUSB Power Management](winusb-power-management.md) |

## Related topics

- [Universal Serial Bus (USB)](../index.yml)
