---
title: EFI\_USBFN\_TRANSFER\_STATUS
author: windows-driver-content
description: EFI\_USBFN\_TRANSFER\_STATUS
ms.assetid: 60631dad-a617-4ed4-a975-5e480cf324e3
---

# EFI\_USBFN\_TRANSFER\_STATUS


This enumeration indicates the USB transfer status.

## Syntax


``` syntax
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


<a href="" id="usbtransferstatusunknown"></a>**UsbTransferStatusUnknown**  
Transfer status is unknown.

<a href="" id="usbtransferstatuscomplete"></a>**UsbTransferStatusComplete**  
Transfer complete.

<a href="" id="usbtransferstatusaborted"></a>**UsbTransferStatusAborted**  
Transfer was aborted.

<a href="" id="usbtransferstatusactive"></a>**UsbTransferStatusActive**  
Transfer is active.

<a href="" id="usbtransferstatusnone"></a>**UsbTransferStatusNone**  
Transfer has no status.

## Requirements


**Header:** User generated

 

 


--------------------


