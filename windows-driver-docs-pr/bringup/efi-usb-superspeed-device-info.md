---
title: EFI_USB_SUPERSPEED_DEVICE_INFO
description: The EFI_USB_SUPERSPEED_DEVICE_INFO structure defines the USB SuperSpeed function device.
ms.date: 08/23/2021
ms.localizationpriority: medium
---

# EFI_USB_SUPERSPEED_DEVICE_INFO

The **EFI_USB_SUPERSPEED_DEVICE_INFO** structure defines the USB SuperSpeed function device.

## Syntax

```cpp
typedef struct
{
    EFI_USB_DEVICE_DESCRIPTOR           *DeviceDescriptor;
    EFI_USB_SUPERSPEED_CONFIG_INFO      **ConfigInfoTable;
    EFI_USB_BOS_DESCRIPTOR              *BosDescriptor
} EFI_USB_SUPERSPEED_DEVICE_INFO;
```

## Members

**DeviceDescriptor**
An EFI_USB_DEVICE_DESCRIPTOR structure that contains configuration information for the USB device.

**ConfigInfoTable**
An [EFI_USB_SUPERSPEED_CONFIG_INFO](efi-usb-superspeed-config-info.md) structure that contains information about the supported USB SuperSpeed configurations.

**BosDescriptor**
An [EFI_USB_BOS_DESCRIPTOR](efi-usb-bos-descriptor.md) structure that contains information about the Binary Object Store to the USB function driver.

## Remarks

The **EFI_USB_CONFIG_DESCRIPTOR** structure is defined in the UEFI specification version 2.3 and later. For more information, visit the [UEFI.org](https://uefi.org/specifications) website.

## Requirements

**Header:** User generated
