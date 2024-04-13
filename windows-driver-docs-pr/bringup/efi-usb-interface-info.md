---
title: EFI_USB_INTERFACE_INFO
description: The EFI_USB_INTERFACE_INFO structure  defines the supported USB interface.
ms.date: 03/23/2023
ms.topic: reference
---

# EFI_USB_INTERFACE_INFO

The **EFI_USB_INTERFACE_INFO** structure  defines the supported USB interface.

## Syntax

```cpp
typedef struct
{
    EFI_USB_INTERFACE_DESCRIPTOR        *InterfaceDescriptor;
    EFI_USB_ENDPOINT_DESCRIPTOR         **EndpointDescriptorTable;
} EFI_USB_INTERFACE_INFO;
```

## Members

**InterfaceDescriptor**
A EFI_USB_INTERFACE_DESCRIPTOR structure that contains information about the USB function interface.

**EndpointDescriptorTable**
A EFI_USB_ENDPOINT_DESCRIPTOR structure that contains information about the supported endpoints.

## Remarks

The **USB_INTERFACE_DESCRIPTOR** and **USB_ENDPOINT_DESCRIPTOR** structures are defined in UEFI specification 2.3. For more information, visit the [UEFI.org](https://uefi.org/specifications) website.

## Requirements

**Header:** User generated
