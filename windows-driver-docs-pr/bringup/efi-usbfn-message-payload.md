---
title: EFI_USBFN_MESSAGE_PAYLOAD
description: EFI_USBFN_MESSAGE_PAYLOAD
ms.assetid: 88d32ce1-460d-4c0f-b42a-426f42e2f969
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USBFN\_MESSAGE\_PAYLOAD


The **EFI\_USBFN\_MESSAGE\_PAYLOAD** union contains additional payload (device request, transfer result, or bus speed information) for the current message.

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


<a href="" id="udr"></a>**udr**  
A **EFI\_USB\_DEVICE\_REQUEST** structure that contains information about the device request.

<a href="" id="utr"></a>**utr**  
A [EFI\_USBFN\_TRANSFER\_RESULT](efi-usbfn-transfer-result.md) structure that contains information about transfer result.

<a href="" id="ubs"></a>**ubs**  
A [EFI\_USB\_BUS\_SPEED](efi-usb-bus-speed.md) enumeration value that indicates the USB bus speed.

## Requirements


**Header:** User generated

 

 




