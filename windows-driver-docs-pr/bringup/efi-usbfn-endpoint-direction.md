---
title: EFI_USBFN_ENDPOINT_DIRECTION
description: The EFI_USBFN_ENDPOINT_DIRECTION enumeration is used to identify direction of an USB transfer.
ms.date: 02/24/2023
ms.topic: reference
---

# EFI_USBFN_ENDPOINT_DIRECTION

The **EFI_USBFN_ENDPOINT_DIRECTION** enumeration is used to identify direction of an USB transfer.

## Syntax

```cpp
typedef enum _EFI_USBFN_ENDPOINT_DIRECTION 
{
    EfiUsbEndpointDirectionHostOut  = 0,
    EfiUsbEndpointDirectionHostIn,
    EfiUsbEndpointDirectionDeviceTx = EfiUsbEndpointDirectionHostIn,
    EfiUsbEndpointDirectionDeviceRx = EfiUsbEndpointDirectionHostOut
} EFI_USBFN_ENDPOINT_DIRECTION;
```

## Constants

**EfiUsbEndpointDirectionHostOut**  
Indicates USB OUT transfer. Direction is from host to device

**EfiUsbEndpointDirectionHostIn**  
Indicates USB IN transfer. Direction is from device to host.

**EfiUsbEndpointDirectionDeviceTx**  
Indicates USB IN transfer. Direction is from device to host.

**EfiUsbEndpointDirectionDeviceRx**  
Indicates USB OUT transfer. Direction is from host to device

## Requirements

**Header:** User generated
