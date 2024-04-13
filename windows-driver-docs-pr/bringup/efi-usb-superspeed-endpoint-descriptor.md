---
title: EFI_USB_SUPERSPEED_ENDPOINT_DESCRIPTOR
description: The EFI_USB_SUPERSPEED_ENDPOINT_DESCRIPTOR structure is used to describe the supported USB SuperSpeed endpoints to the USB function driver.
ms.date: 03/23/2023
ms.topic: reference
---

# EFI_USB_SUPERSPEED_ENDPOINT_DESCRIPTOR

The **EFI_USB_SUPERSPEED_ENDPOINT_DESCRIPTOR** structure is used to describe the supported USB SuperSpeed endpoints to the USB function driver.

## Syntax

```cpp
typedef struct
{
    EFI_USB_ENDPOINT_DESCRIPTOR                         *EndpointDescriptor;
    EFI_USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR    *EndpointCompanionDescriptor;
} EFI_USB_SUPERSPEED_ENDPOINT_DESCRIPTOR;
```

## Members

**EndpointDescriptor**
An EFI_USB_ENDPOINT_DESCRIPTOR structure that describes the USB endpoints.

**EndpointCompanionDescriptor**
An [EFI_USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR](efi-usb-superspeed-endpoint-companion-descriptor.md) structure that is a companion descriptor of the USB SuperSpeed endpoints.

## Remarks

The **EFI_USB_ENDPOINT_DESCRIPTOR** structure is defined in the UEFI specification version 2.3 and later. For more information, visit the [UEFI.org](https://uefi.org/specifications) website.

## Requirements

**Header:** User generated
