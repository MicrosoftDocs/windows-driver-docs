---
title: EFI_USBFN_IO_PROTOCOL.SetEndpointStallState
description: The SetEndpointStallState function sets or clears the stall state on the specified endpoint.
ms.date: 03/23/2023
ms.topic: reference
---

# EFI_USBFN_IO_PROTOCOL.SetEndpointStallState

The *SetEndpointStallState* function sets or clears the stall state on the specified endpoint.

## Syntax

```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_SET_ENDPOINT_STALL_STATE) (
  IN EFI_USBFN_IO_PROTOCOL        *This,
  IN UINT8                        EndpointIndex,
  IN EFI_USBFN_ENDPOINT_DIRECTION Direction,
  IN BOOLEAN                      State
  );
```

## Parameters

*This*  
A pointer to the EFI_USBFN_IO_PROTOCOL instance.

*EndpointIndex*  
Indicates the endpoint that needs to be stalled.

*Direction*  
Direction of the endpoint. For more information, see [EFI_USBFN_ENDPOINT_DIRECTION](efi-usbfn-endpoint-direction.md).

*State*  
Requested stall state on the specified endpoint. Setting this parameter to **TRUE** causes the endpoint to stall. Setting it to **FALSE** clears an existing stall.

## Return values

The function returns one of the the following values:

| Return code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully. |
| EFI_INVALID_PARAMETER | A parameter is invalid. |
| EFI_DEVICE_ERROR | The physical device reported an error. |
| EFI_NOT_READY | The physical device is busy or not ready to process this request. |

## Remarks

This function fails with **EFI_INVALID_PARAMETER** if the specified direction is incorrect for the endpoint.

## Requirements

**Header:** User generated
