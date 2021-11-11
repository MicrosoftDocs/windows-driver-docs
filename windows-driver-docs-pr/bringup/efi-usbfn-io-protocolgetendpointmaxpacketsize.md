---
title: EFI_USBFN_IO_PROTOCOL.GetEndpointMaxPacketSize
description: The GetEndpointMaxPacketSize function returns the maximum packet size of the specified endpoint type for the supplied bus speed.
ms.date: 08/23/2021
ms.localizationpriority: medium
---

# EFI_USBFN_IO_PROTOCOL.GetEndpointMaxPacketSize

The *GetEndpointMaxPacketSize* function returns the maximum packet size of the specified endpoint type for the supplied bus speed.

## Syntax

```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_GET_ENDPOINT_MAXPACKET_SIZE) (
  IN EFI_USBFN_IO_PROTOCOL      *This,
  IN EFI_USB_ENDPOINT_TYPE      EndpointType,
  IN EFI_USB_BUS_SPEED          BusSpeed,
  OUT UINT16                    *MaxPacketSize
  );
```

## Parameters

*This*  
A pointer to the EFI_USBFN_IO_PROTOCOL instance.

*EndpointType*  
Endpoint type as defined in the [EFI_USB_ENDPOINT_TYPE](efi-usb-endpoint-type.md). enumeration

*BusSpeed*  
An [EFI_USB_BUS_SPEED](efi-usb-bus-speed.md) enumeration value that indicates the current bus speed as known to the caller.

*MaxPacketSize*  
The maximum packet size, in bytes, of the specified endpoint type.

## Return values

This function returns the following values:

| Return code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully |
| EFI_INVALID_PARAMETER | A parameter is invalid |
| EFI_DEVICE_ERROR | The physical device reported an error. |
| EFI_NOT_READY | The physical device is busy or not ready to process this request |

## Requirements

**Header:** User generated
