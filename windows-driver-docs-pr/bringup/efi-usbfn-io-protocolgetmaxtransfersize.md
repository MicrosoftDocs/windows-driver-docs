---
title: EFI_USBFN_IO_PROTOCOL.GetMaxTransferSize
description: The GetMaxTransferSize function returns the maximum transfer size as supported by the underlying controller.
ms.date: 08/23/2021
---

# EFI_USBFN_IO_PROTOCOL.GetMaxTransferSize

The *GetMaxTransferSize* function returns the maximum transfer size as supported by the underlying controller.

## Syntax

```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_GET_MAXTRANSFER_SIZE) (
  IN EFI_USBFN_IO_PROTOCOL     *This,
  OUT UINTN                    *MaxTransferSize
  );
```

## Parameters

*This*  
A pointer to the EFI_USBFN_IO_PROTOCOL instance.

*MaxTransferSize*  
The maximum supported transfer size, in bytes.

## Return values

This function returns the following values:

| Return code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully |
| EFI_INVALID_PARAMETER | A parameter is invalid |
| EFI_DEVICE_ERROR | The physical device reported an error. |
| EFI_NOT_READY | The physical device is busy or not ready to process this request |

## Remarks

## Requirements

**Header:** User generated
