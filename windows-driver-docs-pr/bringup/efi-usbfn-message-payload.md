---
title: EFI_USBFN_MESSAGE_PAYLOAD
description: The EFI_USBFN_MESSAGE_PAYLOAD union contains additional payload (device request, transfer result, or bus speed information) for the current message.
ms.date: 08/23/2021
ms.localizationpriority: medium
---

# EFI_USBFN_MESSAGE_PAYLOAD

The **EFI_USBFN_MESSAGE_PAYLOAD** union contains additional payload (device request, transfer result, or bus speed information) for the current message.

## Syntax

```cpp
typedef union _EFI_USBFN_MESSAGE_PAYLOAD
{
    EFI_USB_DEVICE_REQUEST      udr;
    EFI_USBFN_TRANSFER_RESULT   utr;
    EFI_USB_BUS_SPEED           ubs;
} EFI_USBFN_MESSAGE_PAYLOAD;
```

## Members

**udr**  
A **EFI_USB_DEVICE_REQUEST** structure that contains information about the device request.

**utr**  
A [**EFI_USBFN_TRANSFER_RESULT**](efi-usbfn-transfer-result.md) structure that contains information about transfer result.

**ubs**  
A [**EFI_USB_BUS_SPEED**](efi-usb-bus-speed.md) enumeration value that indicates the USB bus speed.

## Requirements

**Header:** User generated
