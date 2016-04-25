---
title: EFI\_USBFN\_TRANSFER\_STATUS
description: EFI\_USBFN\_TRANSFER\_STATUS
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_USBFN_TRANSFER_STATUS%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


