---
title: EFI_USBFN_IO_PROTOCOL.GetDeviceInfo
description: EFI_USBFN_IO_PROTOCOL.GetDeviceInfo
ms.date: 08/23/2021
ms.localizationpriority: medium
---

# EFI_USBFN_IO_PROTOCOL.GetDeviceInfo

The *GetDeviceInfo* function Returns device-specific information based on the supplied identifier

Specifying **EfiUsbDeviceInfoUnknown** as Id is treated as an invalid parameter.

## Syntax

```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_GET_DEVICE_INFO) (
  IN EFI_USBFN_IO_PROTOCOL      *This,
  IN EFI_USBFN_DEVICE_INFO_ID   Id,
  IN OUT UINTN                  *BufferSize,
  OUT VOID                      *Buffer OPTIONAL
  );
```

## Parameters

*This*  
A pointer to the EFI_USBFN_IO_PROTOCOL instance.

*Id*  
A [**EFI_USBFN_DEVICE_INFO_ID**](efi-usbfn-device-info-id.md) enumeration that contains the requested device ID.

*BufferSize*  
On input, the size of the Buffer in bytes. On output, the amount of data returned in Buffer in bytes.

*Buffer*  
A pointer to a buffer in which the requested information will be returned as a Unicode string.

## Return values

This function returns the following values:

| Return code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully. |
| EFI_INVALID_PARAMETER | A parameter is invalid. |
| EFI_DEVICE_ERROR | The physical device reported an error. |
| EFI_NOT_READY | The physical device is busy or not ready to process this request. |
| EFI_BUFFER_TOO_SMALL | Supplied buffer isn't large enough to hold the request string. |

## Remarks

If the supplied Buffer is too small or NULL, the method fails with **EFI_BUFFER_TOO_SMALL** and the required size is returned through **BufferSize**. All returned strings are in Unicode format.

## Requirements

**Header:** User generated
