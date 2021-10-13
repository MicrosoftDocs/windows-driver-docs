---
title: EFI_USBFN_POLICY_TYPE
description: The EFI_USBFN_POLICY_TYPE enumeration contains values used to indicate the type of endpoint.
ms.date: 08/23/2021
ms.localizationpriority: medium
---

# EFI_USBFN_POLICY_TYPE

The **EFI_USBFN_POLICY_TYPE** enumeration contains values used to indicate the type of endpoint.

## Syntax

```cpp
typedef enum _EFI_USBFN_POLICY_TYPE{
  EfiUsbPolicyUndefined = 0, 
  EfiUsbPolicyMaxTransactionSize, 
  EfiUsbPolicyZeroLengthTerminationSupport, 
  EfiUsbPolicyZeroLengthTermination
} EFI_USBFN_POLICY_TYPE;
```

## Constants

**EfiUsbPolicyUndefined**  
Invalid policy value that must never be used across a driver boundary. If used, the callee function must never return a success status code.

**EfiUsbPolicyMaxTransactionSize**  
This policy is read-only. When used with [EFI_USBFN_IO_PROTOCOL.GetEndpointPolicy](efi-usbfn-io-protocolgetendpointpolicy.md), the size of the maximum single transaction (delivery of service to an endpoint) supported by a controller is returned. It must be more than or equal to the maximum transfer size that can be retrieved by calling [EFI_USBFN_IO_PROTOCOL.GetMaxTransferSize](efi-usbfn-io-protocolgetmaxtransfersize.md).

| &nbsp; | GetEndpointPolicy | SetEndpointPolicy |
|--|--|--|
| *BufferSize* | 4 bytes, sizeof(UINT32) | Not applicable |
| Return status | EFI_STATUS | EFI_UNSUPPORTED |

**EfiUsbPolicyZeroLengthTerminationSupport**  
This policy is read-only. When used with [EFI_USBFN_IO_PROTOCOL.GetEndpointPolicy](efi-usbfn-io-protocolgetendpointpolicy.md), TRUE is returned if the USB controller hardware is capable of automatically handling zero-length packets when the transfer size is a multiple of USB maximum packet size; FALSE is returned if such a scenario is not supported by the controller hardware.

| &nbsp; | GetEndpointPolicy | SetEndpointPolicy |
|--|--|--|
| *BufferSize* | 1 byte, sizeof(BOOLEAN) | Not applicable |
| Return status | EFI_STATUS | EFI_UNSUPPORTED |

**EfiUsbPolicyZeroLengthTermination**  
When used with [EFI_USBFN_IO_PROTOCOL.GetEndpointPolicy](efi-usbfn-io-protocolgetendpointpolicy.md), TRUE is returned if the USB controller hardware is configured to automatically handle zero-length packets when the transfer size is a multiple of USB maximum packet size; FALSE is returned if the controller hardware is not configured to support such a scenario.

[EFI_USBFN_IO_PROTOCOL.SetEndpointPolicy](efi-usbfn-io-protocolsetendpointpolicy.md) can only accept this policy type if the USB controller hardware is capable of supporting automatic zero-length packet termination. When this value is set to TRUE, the controller must be configured to handle zero-length termination for the specified endpoint; a FALSE value would not configure the controller in such fashion.

Even if the controller hardware is capable of supporting automatic zero-length termination, it must not be the default configuration.

| &nbsp; | GetEndpointPolicy | SetEndpointPolicy |
|--|--|--|
| *BufferSize* | 1 byte, sizeof(BOOLEAN) | 1 byte, sizeof(BOOLEAN) |
| Return status | EFI_STATUS | EFI_STATUS |

## Requirements

**Header:** User generated
