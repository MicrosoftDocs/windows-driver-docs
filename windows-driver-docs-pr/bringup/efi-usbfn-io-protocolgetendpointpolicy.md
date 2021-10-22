---
title: EFI_USBFN_IO_PROTOCOL.GetEndpointPolicy
description: The GetEndpointPolicy function retrieves the configuration policy for the specified non-control endpoint.
ms.date: 08/23/2021
ms.localizationpriority: medium
---

# EFI_USBFN_IO_PROTOCOL.GetEndpointPolicy

The **GetEndpointPolicy** function retrieves the configuration policy for the specified non-control endpoint.

## Syntax

```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_GET_ENDPOINT_POLICY) (
  IN EFI_USBFN_IO_PROTOCOL        *This,
  IN UINT8                        EndpointIndex,
  IN EFI_USBFN_ENDPOINT_DIRECTION Direction,
  IN EFI_USBFN_POLICY_TYPE        PolicyType,
  IN OUT UINTN                    BufferSize,
  IN OUT VOID                     *Buffer
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
The policy type the user is trying to retrieve for the specified non-control endpoint. For more information, see [EFI_USBFN_POLICY_TYPE](efi-usbfn-policy-type.md).

*BufferSize*  
On input, the size of *Buffer* in bytes. On output, the amount of data returned by *Buffer* in bytes.

*Buffer*  
A pointer to a buffer to return the requested endpoint policy value. For more information about the size requirements of the policy types, see [EFI_USBFN_POLICY_TYPE](efi-usbfn-policy-type.md).

## Return values

This function returns the following values:

| Return code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully. |
| EFI_INVALID_PARAMETER | A parameter is invalid. |
| EFI_DEVICE_ERROR | The physical device reported an error. |
| EFI_UNSUPPORTED | Changing this policy value is not supported. |
| EFI_BUFFER_TOO_SMALL | The supplied buffer is not large enough to hold the requested policy value. |

## Remarks

There are no associated calling restrictions for this function. This function is available starting in revision 0x00010001 of the **EFI_USBFN_IO_PROTOCOL**.

## Requirements

**Header:** User generated
