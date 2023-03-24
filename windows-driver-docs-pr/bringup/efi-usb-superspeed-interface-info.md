---
title: EFI_USB_SUPERSPEED_INTERFACE_INFO
description: The EFI_USB_SUPERSPEED_INTERFACE_INFO structure defines the supported USB SuperSpeed interface to the USB function driver.
ms.date: 03/23/2023
ms.topic: reference
---

# EFI_USB_SUPERSPEED_INTERFACE_INFO

The **EFI_USB_SUPERSPEED_INTERFACE_INFO** structure defines the supported USB SuperSpeed interface to the USB function driver.

## Syntax

```cpp
typedef struct
{
    EFI_USB_INTERFACE_DESCRIPTOR            *InterfaceDescriptor;
    EFI_USB_SUPERSPEED_ENDPOINT_DESCRIPTOR  **EndpointDescriptorTable;
} EFI_USB_SUPERSPEED_INTERFACE_INFO;
```

## Members

**InterfaceDescriptor**
An EFI_USB_INTERFACE_DESCRIPTOR structure that describes the USB function interface.

**EndpointDescriptorTable**
An [EFI_USB_SUPERSPEED_ENDPOINT_DESCRIPTOR](efi-usb-superspeed-endpoint-descriptor.md) structure that describes the USB SuperSpeed endpoints.

## Remarks

The **EFI_USB_INTERFACE_DESCRIPTOR** structure is defined in the UEFI specification version 2.3 and later. For more information, visit the [UEFI.org](https://uefi.org/specifications) website.

## Requirements

**Header:** User generated
