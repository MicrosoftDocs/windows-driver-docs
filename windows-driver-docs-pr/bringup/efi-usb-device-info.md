---
title: EFI_USB_DEVICE_INFO
description: EFI_USB_DEVICE_INFO
ms.date: 05/21/2020
ms.localizationpriority: medium
---

# EFI\_USB\_DEVICE\_INFO

The **EFI\_USB\_DEVICE\_INFO** structure is used to define the USB function device.

## Syntax

```cpp
typedef struct
{
    EFI_USB_DEVICE_DESCRIPTOR           *DeviceDescriptor;
    EFI_USB_CONFIG_INFO                 **ConfigInfoTable;
} EFI_USB_DEVICE_INFO;
```

## Members

### DeviceDescriptor

A EFI\_USB\_DEVICE\_DESCRIPTOR structure that contains configuration information for the USB device.

### ConfigInfoTable

A EFI\_USB\_CONFIG\_INFO structure that contains information about the supported configurations.

## Remarks

The **EFI\_USB\_CONFIG\_DESCRIPTOR** and **EFI\_USB\_DEVICE\_DESCRIPTOR** structures are defined in UEFI specification 2.3. For more information, visit the [UEFI.org](https://uefi.org/specifications) website.

## Requirements

**Header:** User generated
