---
title: EFI_USBFN_IO_PROTOCOL.AbortTransfer
description: The AbortTransfer function aborts transfer on the specified endpoint.
ms.date: 02/24/2023
ms.topic: reference
---

# EFI_USBFN_IO_PROTOCOL.AbortTransfer

The **AbortTransfer** function aborts transfer on the specified endpoint.

## Syntax

```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_ABORT_TRANSFER) (
  IN EFI_USBFN_IO_PROTOCOL        *This,
  IN UINT8                        EndpointIndex,
  IN EFI_USBFN_ENDPOINT_DIRECTION Direction
  );
```

## Parameters

*This*  
A pointer to the EFI_USBFN_IO_PROTOCOL instance

*EndpointIndex*  
Indicates the endpoint on which the ongoing transfer needs to be canceled.

*Direction*  
Direction of the endpoint. For more information see [EFI_USBFN_ENDPOINT_DIRECTION](efi-usbfn-endpoint-direction.md).

## Return values

Returns one of the following status codes.

| Status code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully. |
| EFI_INVALID_PARAMETER | A parameter is invalid. |
| EFI_DEVICE_ERROR | The physical device reported an error. |
| EFI_NOT_READY | The physical device is busy or not ready to process this request. |

## Remarks

This function fails with **EFI_INVALID_PARAMETER** if the specified direction is incorrect for the endpoint.

## Requirements

**Header:** User generated
