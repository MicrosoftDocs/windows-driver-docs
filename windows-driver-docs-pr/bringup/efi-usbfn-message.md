---
title: EFI\_USBFN\_MESSAGE
description: EFI\_USBFN\_MESSAGE
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 411890e1-8913-4e47-acd5-1b36b1b05f34
---

# EFI\_USBFN\_MESSAGE


The **EFI\_USBFN\_MESSAGE** enumeration is used to indicate the event that initiated a message notification

## Syntax


``` syntax
typedef enum _EFI_USBFN_MESSAGE
{
EfiUsbMsgNone = 0,
EfiUsbMsgSetupPacket,
EfiUsbMsgEndpointStatusChangedRx,
EfiUsbMsgEndpointStatusChangedTx
EfiUsbMsgBusEventDetach,
EfiUsbMsgBusEventAttach,
EfiUsbMsgBusEventReset,
EfiUsbMsgBusEventSuspend,
EfiUsbMsgBusEventResume,
EfiUsbMsgBusEventSpeed
} EFI_USBFN_MESSAGE;
```

## Constants


<a href="" id="efiusbmsgnone"></a>**EfiUsbMsgNone**  
No device info.

<a href="" id="efiusbmsgsetuppacket"></a>**EfiUsbMsgSetupPacket**  
Indicates SETUP packet is received and the returned Buffer contains an EFI\_USB\_DEVICE\_REQUEST structure

<a href="" id="efiusbmsgendpointstatuschangedrx"></a>**EfiUsbMsgEndpointStatusChangedRx**  
Indicates that some of the requested data has been received from the host. It is the responsibility of the class driver to determine if it needs to wait for any remaining data. The returned buffer contains a EFI\_USBFN\_TRANSFER\_RESULT struct containing endpoint number, transfer status and a count of the bytes received.

<a href="" id="efiusbmsgendpointstatuschangedtx"></a>**EfiUsbMsgEndpointStatusChangedTx**  
Indicates that some of the requested data has been transmitted to the host. It is the responsibility of the class driver to determine if any remaining data needs to be resent. The returned buffer contains a EFI\_USBFN\_TRANSFER\_RESULT struct containing endpoint number, transferstatus and count of bytes sent.

<a href="" id="efiusbmsgbuseventdetach"></a>**EfiUsbMsgBusEventDetach**  
DETACH bus event signaled.

<a href="" id="efiusbmsgbuseventattach"></a>**EfiUsbMsgBusEventAttach**  
ATTACH bus event signaled.

<a href="" id="efiusbmsgbuseventreset"></a>**EfiUsbMsgBusEventReset**  
RESET bus event signaled.

<a href="" id="efiusbmsgbuseventsuspend"></a>**EfiUsbMsgBusEventSuspend**  
SUSPEND bus event signaled.

<a href="" id="efiusbmsgbuseventresume"></a>**EfiUsbMsgBusEventResume**  
RESUME bus event signaled.

<a href="" id="efiusbmsgbuseventspeed"></a>**EfiUsbMsgBusEventSpeed**  
Bus speed updated, returned buffer indicated bus speed using an [EFI\_USB\_BUS\_SPEED](efi-usb-bus-speed.md) enumeration.

## Remarks


## Requirements


**Header:** User generated

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_USBFN_MESSAGE%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




