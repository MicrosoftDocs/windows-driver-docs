---
title: EFI_USBFN_IO_PROTOCOL.ConfigureEnableEndpoints
description: The ConfigureEnableEndpoints function initializes endpoints based on supplied device and configuration descriptors.
ms.date: 08/20/2021
---

# EFI_USBFN_IO_PROTOCOL.ConfigureEnableEndpoints

The **ConfigureEnableEndpoints** function initializes endpoints based on supplied device and configuration descriptors.

## Syntax

```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_CONFIGURE_ENABLE_ENDPOINTS) (
  IN EFI_USBFN_IO_PROTOCOL         *This,
  IN EFI_USB_DEVICE_INFO           *DeviceInfo
  );
```

## Parameters

*This*  
A pointer to the EFI_USBFN_IO_PROTOCOL instance.

*DeviceInfo*  
A pointer to an [EFI_USB_DEVICE_INFO](efi-usb-device-info.md) structure.

## Return values

The function returns the following values:

| Return value | Description |
| -- | -- |
| EFI_SUCCESS | The function returned successfully. |
| EFI_INVALID_PARAMETER | A parameter is invalid. |
| EFI_DEVICE_ERROR | The physical device reported an error. |
| EFI_NOT_READY | The physical device is busy or not ready to process this request. |
| EFI_OUT_OF_RESOURCES | The request could not be completed due to lack of resources. |

## Remarks

Assuming that the hardware has already been initialized, this function configures the endpoints using the supplied *DeviceInfo* , activates the port, and starts receiving USB events.

This function must ignore the *bMaxPacketSize0* field of the Standard Device Descriptor and *wMaxPacketSize* field of Standard Endpoint Descriptor that are made available through supplied *DeviceInfo*.

## Requirements

**Header:** User generated
