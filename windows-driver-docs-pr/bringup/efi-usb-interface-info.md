---
title: EFI_USB_INTERFACE_INFO
description: EFI_USB_INTERFACE_INFO
ms.date: 05/21/2020
ms.localizationpriority: medium
---

# EFI\_USB\_INTERFACE\_INFO

The **EFI\_USB\_INTERFACE\_INFO** structure Used to define the supported USB interface.

## Syntax

```cpp
typedef struct
{
    EFI_USB_INTERFACE_DESCRIPTOR        *InterfaceDescriptor;
    EFI_USB_ENDPOINT_DESCRIPTOR         **EndpointDescriptorTable;
} EFI_USB_INTERFACE_INFO;
```

## Members

### InterfaceDescriptor

A EFI\_USB\_INTERFACE\_DESCRIPTOR structure that contains information about the USB function interface.

### EndpointDescriptorTable

A EFI\_USB\_ENDPOINT\_DESCRIPTOR structure that contains information about the supported endpoints.

## Remarks

The **USB\_INTERFACE\_DESCRIPTOR** and **USB\_ENDPOINT\_DESCRIPTOR** structures are defined in UEFI specification 2.3. For more information, visit the [UEFI.org](https://uefi.org/specifications) website.

## Requirements

**Header:** User generated
