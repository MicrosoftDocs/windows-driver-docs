---
title: EFI_USBFN_TRANSFER_STATUS
description: The EFI_USBFN_TRANSFER_STATUS enumeration indicates the USB transfer status.
ms.date: 03/23/2023
ms.topic: reference
---

# EFI_USBFN_TRANSFER_STATUS

The **EFI_USBFN_TRANSFER_STATUS** enumeration indicates the USB transfer status.

## Syntax

```cpp
typedef enum _EFI_USBFN_TRANSFER_STATUS 
{
    UsbTransferStatusUnknown = 0,
    UsbTransferStatusComplete,
    UsbTransferStatusAborted,
    UsbTransferStatusActive,
    UsbTransferStatusNone
} EFI_USBFN_TRANSFER_STATUS;
```

## Constants

**UsbTransferStatusUnknown**  
Transfer status is unknown.

**UsbTransferStatusComplete**  
Transfer complete.

**UsbTransferStatusAborted**  
Transfer was aborted.

**UsbTransferStatusActive**  
Transfer is active.

**UsbTransferStatusNone**  
Transfer has no status.

## Requirements

**Header:** User generated
