---
title: EFI\_USBFN\_MESSAGE\_PAYLOAD
description: EFI\_USBFN\_MESSAGE\_PAYLOAD
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 88d32ce1-460d-4c0f-b42a-426f42e2f969
---

# EFI\_USBFN\_MESSAGE\_PAYLOAD


The **EFI\_USBFN\_MESSAGE\_PAYLOAD** union contains additional payload (device request, transfer result, or bus speed information) for the current message.

## Syntax


``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_USBFN_MESSAGE_PAYLOAD%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




