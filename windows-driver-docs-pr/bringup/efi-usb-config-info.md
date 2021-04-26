---
title: EFI_USB_CONFIG_INFO
description: EFI_USB_CONFIG_INFO
ms.date: 05/21/2020
ms.localizationpriority: medium
---

# EFI\_USB\_CONFIG\_INFO

The **EFI\_USB\_CONFIG\_INFO** structure is used to define the supported USB port configuration.

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

An EFI\_USB\_CONFIG\_DESCRIPTOR structure that contains configuration information for the USB function device.

### InterfaceInfoTable

An [EFI\_USB\_INTERFACE\_INFO](efi-usb-interface-info.md) structure that contains information about the supported interfaces.

## Remarks

The structure **USB\_CONFIG\_DESCRIPTOR** is defined in UEFI specification 2.3. For more information, visit the [UEFI.org](https://uefi.org/specifications) website.

## Requirements

**Header:** User generated
