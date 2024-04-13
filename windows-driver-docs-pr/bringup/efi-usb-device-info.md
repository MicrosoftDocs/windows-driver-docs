---
title: EFI_USB_DEVICE_INFO
description: The EFI_USB_DEVICE_INFO structure is used to define the USB function device.
ms.date: 03/23/2023
ms.topic: reference
---

# EFI_USB_DEVICE_INFO

The **EFI_USB_DEVICE_INFO** structure is used to define the USB function device.

## Syntax

```cpp
typedef struct
{
    EFI_USB_DEVICE_DESCRIPTOR           *DeviceDescriptor;
    EFI_USB_CONFIG_INFO                 **ConfigInfoTable;
} EFI_USB_DEVICE_INFO;
```

## Members

**DeviceDescriptor**
A EFI_USB_DEVICE_DESCRIPTOR structure that contains configuration information for the USB device.

**ConfigInfoTable**
A EFI_USB_CONFIG_INFO structure that contains information about the supported configurations.

## Remarks

The **EFI_USB_CONFIG_DESCRIPTOR** and **EFI_USB_DEVICE_DESCRIPTOR** structures are defined in UEFI specification 2.3. For more information, visit the [UEFI.org](https://uefi.org/specifications) website.

## Requirements

**Header:** User generated
