---
title: EFI_USBFN_MESSAGE
description: EFI_USBFN_MESSAGE
ms.assetid: 411890e1-8913-4e47-acd5-1b36b1b05f34
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USBFN\_MESSAGE


The **EFI\_USBFN\_MESSAGE** enumeration is used to indicate the event that initiated a message notification

## Syntax


```cpp
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

 

 




