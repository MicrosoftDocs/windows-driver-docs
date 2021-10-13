---
title: EFI_USBFN_IO_PROTOCOL.SetEndpointPolicy
description: The SetEndpointPolicy function sets the configuration policy for the specified non-control endpoint.
ms.date: 08/23/2021
ms.localizationpriority: medium
---

# EFI_USBFN_IO_PROTOCOL.SetEndpointPolicy

The *SetEndpointPolicy* function sets the configuration policy for the specified non-control endpoint.

## Syntax

```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_SET_ENDPOINT_POLICY) (
  IN EFI_USBFN_IO_PROTOCOL        *This,
  IN UINT8                        EndpointIndex,
  IN EFI_USBFN_ENDPOINT_DIRECTION Direction,
  IN EFI_USBFN_POLICY_TYPE        PolicyType,
  IN UINTN                        BufferSize,
  IN VOID                         *Buffer
  );
```

## Parameters

*This*  
A pointer to the EFI_USBFN_IO_PROTOCOL instance.

*EndpointIndex*  
Indicates the non-control endpoint for which the policy needs to be set.

*Direction*  
The direction of the endpoint. For more information, see [EFI_USBFN_ENDPOINT_DIRECTION](efi-usbfn-endpoint-direction.md).

*PolicyType*  
The policy type the user is trying to set for the specified non-control endpoint. For more information, see [EFI_USBFN_POLICY_TYPE](efi-usbfn-policy-type.md).

*BufferSize*  
The size of *Buffer* in bytes.

*Buffer*  
A pointer to the buffer that contains the new endpoint policy value. For more information about the size requirements of the policy types, see [EFI_USBFN_POLICY_TYPE](efi-usbfn-policy-type.md).

## Return values

The function returns one of the the following values:

| Return code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully. |
| EFI_INVALID_PARAMETER | A parameter is invalid. |
| EFI_DEVICE_ERROR | The physical device reported an error. |
| EFI_UNSUPPORTED | Changing this policy value is not supported. |

## Remarks

This function can be called only before [EFI_USBFN_IO_PROTOCOL.StartController](efi-usbfn-io-protocolstartcontroller.md) or after [EFI_USBFN_IO_PROTOCOL.StopController](efi-usbfn-io-protocolstopcontroller.md) has been called. This function is available starting in revision 0x00010001 of the **EFI_USBFN_IO_PROTOCOL**.

## Requirements

**Header:** User generated
