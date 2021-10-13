---
title: EFI_USB_CONFIG_INFO
description: The EFI_USB_CONFIG_INFO structure is used to define the supported USB port configuration.
ms.date: 08/20/2021
ms.localizationpriority: medium
---

# EFI_USB_CONFIG_INFO

The **EFI_USB_CONFIG_INFO** structure is used to define the supported USB port configuration.

## Syntax

```cpp
typedef struct
{
    EFI_USB_CONFIG_DESCRIPTOR           *ConfigDescriptor;
    EFI_USB_INTERFACE_INFO              **InterfaceInfoTable;
} EFI_USB_CONFIG_INFO;
```

## Members

### ConfigDescriptor

An EFI_USB_CONFIG_DESCRIPTOR structure that contains configuration information for the USB function device.

### InterfaceInfoTable

An [EFI_USB_INTERFACE_INFO](efi-usb-interface-info.md) structure that contains information about the supported interfaces.

## Remarks

The structure **USB_CONFIG_DESCRIPTOR** is defined in UEFI specification 2.3. For more information, visit the [UEFI.org](https://uefi.org/specifications) website.

## Requirements

**Header:** User generated
