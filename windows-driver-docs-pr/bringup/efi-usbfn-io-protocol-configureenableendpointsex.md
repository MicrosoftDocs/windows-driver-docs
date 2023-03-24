---
title: EFI_USBFN_IO_PROTOCOL.ConfigureEnableEndpointsEx
description: Configures endpoints based on supplied list of device and configuration descriptors.
ms.date: 03/23/2023
ms.topic: reference
---

# EFI_USBFN_IO_PROTOCOL.ConfigureEnableEndpointsEx

Configures endpoints based on supplied list of device and configuration descriptors. The class driver may call this method in substitution of [EFI_USBFN_IO_PROTOCOL.ConfigureEnableEndpoints](efi-usbfn-io-protocolconfigureenableendpoints.md).

## Syntax

```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_CONFIGURE_ENABLE_ENDPOINTS_EX) (
  IN EFI_USBFN_IO_PROTOCOL           *This,
  IN EFI_USB_DEVICE_INFO             *DeviceInfo,
  IN EFI_USB_SUPERSPEED_DEVICE_INFO  *SSDeviceInfo
  );
```

## Parameters

*This*  
A pointer to the EFI_USBFN_IO_PROTOCOL instance.

*DeviceInfo*  
A pointer to an [EFI_USB_DEVICE_INFO](efi-usb-device-info.md) structure.

*SSDeviceInfo*  
A pointer to an [EFI_USB_SUPERSPEED_DEVICE_INFO](efi-usb-superspeed-device-info.md) structure.

## Return values

The function returns the following values:

| Return code | Description |
|--|--|
| EFI_UNSUPPORTED | This operation is not supported. |

## Remarks

This function is available starting in revision 0x00010002 of the **EFI_USBFN_IO_PROTOCOL**.

Assuming that the hardware has already been initialized, this function configures the endpoints using the supplied *DeviceInfo*, activates the port, and starts receiving USB events. This function accepts *DeviceInfo* and *SSDeviceInfo* objects and configures the endpoint with the information from the object that supports the highest speed allowed by the underlying hardware. The high speed and super speed *DeviceInfo* objects passed in must have the same DeviceClass in the EFI_USB_DEVICE_DESCRIPTOR. Otherwise, this function will return EFI_UNSUPPORTED.

This function must ignore the *bMaxPacketSize0* field of the Standard Device Descriptor and *wMaxPacketSize* field of Standard Endpoint Descriptor that are made available through supplied *DeviceInfo*.

## Requirements

**Header:** User generated
