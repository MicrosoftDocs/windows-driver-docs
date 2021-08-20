---
title: EFI_USBFN_IO_PROTOCOL.DetectPort
description: The DetectPort function returns the type of device attached to the USB port.
ms.date: 08/20/2021
ms.localizationpriority: medium
---

# EFI_USBFN_IO_PROTOCOL.DetectPort

The **DetectPort** function returns the type of device attached to the USB port.

## Syntax

```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_DETECT_PORT) (
  IN EFI_USBFN_IO_PROTOCOL   *This,
  OUT EFI_USBFN_PORT_TYPE    *PortType
  );
```

## Parameters

*This*  
A pointer to the EFI_USBFN_IO_PROTOCOL instance.

*PortType*  
A [EFI_USBFN_PORT_TYPE](efi-usbfn-port-type.md) enumeration that indicates the USB port type.

## Return values

Returns one of the following status codes.

| Status code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully. |
| EFI_INVALID_PARAMETER | A parameter is invalid. |
| EFI_DEVICE_ERROR | The physical device reported an error. |
| EFI_NOT_READY | The physical device is busy or not ready to process this request. |

## Requirements

**Header:** User generated
