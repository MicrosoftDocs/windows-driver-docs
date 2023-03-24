---
title: EFI_USB_SUPERSPEED_CONFIG_INFO
description: The EFI_USB_SUPERSPEED_CONFIG_INFO structure defines the supported USB SuperSpeed port configuration to the USB function driver.
ms.date: 03/23/2023
ms.topic: reference
---

# EFI_USB_SUPERSPEED_CONFIG_INFO

The **EFI_USB_SUPERSPEED_CONFIG_INFO** structure defines the supported USB SuperSpeed port configuration to the USB function driver.

## Syntax

```cpp
typedef struct
{
    EFI_USB_CONFIG_DESCRIPTOR           *ConfigDescriptor;
    EFI_USB_SUPERSPEED_INTERFACE_INFO   **InterfaceInfoTable;
} EFI_USB_SUPERSPEED_CONFIG_INFO;
```

## Members

**ConfigDescriptor**
An EFI_USB_CONFIG_DESCRIPTOR structure that contains the configuration descriptor for the USB function device.

**InterfaceInfoTable**
An [EFI_USB_SUPERSPEED_INTERFACE_INFO](efi-usb-superspeed-interface-info.md) structure that describes the supported USB SuperSpeed interfaces.

## Remarks

The **EFI_USB_CONFIG_DESCRIPTOR** structure is defined in the UEFI specification version 2.3 and later. For more information, visit the [UEFI.org](https://uefi.org/specifications) website.

## Requirements

**Header:** User generated
