---
title: EFI_USBFN_IO_PROTOCOL.GetEndpointStallState
description: The GetEndpointStallState function returns the stall state on the specified endpoint.
ms.date: 02/24/2023
ms.topic: reference
---

# EFI_USBFN_IO_PROTOCOL.GetEndpointStallState

The *GetEndpointStallState* function returns the stall state on the specified endpoint.

## Syntax

```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_GET_ENDPOINT_STALL_STATE) (
  IN EFI_USBFN_IO_PROTOCOL        *This,
  IN UINT8                        EndpointIndex,
  IN EFI_USBFN_ENDPOINT_DIRECTION Direction,
  IN OUT BOOLEAN                  *State
  );
```

## Parameters

*This*  
A pointer to the EFI_USBFN_IO_PROTOCOL instance.

*EndpointIndex*  
Indicates the endpoint.

*Direction*  
Direction of the endpoint. For more information, see [EFI_USBFN_ENDPOINT_DIRECTION](efi-usbfn-endpoint-direction.md).

*State*  
Boolean; **TRUE** value indicates that the endpoint is in a stalled state, **FALSE** otherwise.

## Return values

The function returns the following values:

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
