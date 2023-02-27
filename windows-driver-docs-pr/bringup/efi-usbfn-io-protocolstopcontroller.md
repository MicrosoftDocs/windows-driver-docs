---
title: EFI_USBFN_IO_PROTOCOL.StopController
description: The StopController function disables the hardware device by resetting the run/stop bit and powers off the USB controller if necessary.
ms.date: 02/24/2023
ms.topic: reference
---

# EFI_USBFN_IO_PROTOCOL.StopController

The *StopController* function disables the hardware device by resetting the run/stop bit and powers off the USB controller if necessary.

## Syntax

```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_STOP_CONTROLLER) (
  IN EFI_USBFN_IO_PROTOCOL        *This
  );
```

## Parameters

*This*  
A pointer to the EFI_USBFN_IO_PROTOCOL instance.

## Return values

The function returns one of the the following values:

| Return code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully. |
| EFI_INVALID_PARAMETER | A parameter is invalid. |
| EFI_DEVICE_ERROR | The physical device reported an error. |

## Remarks

This function is available starting in revision 0x00010001 of the **EFI_USBFN_IO_PROTOCOL**.

## Requirements

**Header:** User generated
