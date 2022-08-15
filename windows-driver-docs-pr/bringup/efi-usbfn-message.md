---
title: EFI_USBFN_MESSAGE
description: The EFI_USBFN_MESSAGE enumeration is used to indicate the event that initiated a message notification.
ms.date: 08/23/2021
---

# EFI_USBFN_MESSAGE

The **EFI_USBFN_MESSAGE** enumeration is used to indicate the event that initiated a message notification.

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

**EfiUsbMsgNone**  
No device info.

**EfiUsbMsgSetupPacket**  
Indicates SETUP packet is received and the returned Buffer contains an EFI_USB_DEVICE_REQUEST structure

**EfiUsbMsgEndpointStatusChangedRx**  
Indicates that some of the requested data has been received from the host. It is the responsibility of the class driver to determine if it needs to wait for any remaining data. The returned buffer contains a EFI_USBFN_TRANSFER_RESULT struct containing endpoint number, transfer status and a count of the bytes received.

**EfiUsbMsgEndpointStatusChangedTx**  
Indicates that some of the requested data has been transmitted to the host. It is the responsibility of the class driver to determine if any remaining data needs to be resent. The returned buffer contains a EFI_USBFN_TRANSFER_RESULT struct containing endpoint number, transfer status and count of bytes sent.

**EfiUsbMsgBusEventDetach**  
DETACH bus event signaled.

**EfiUsbMsgBusEventAttach**  
ATTACH bus event signaled.

**EfiUsbMsgBusEventReset**  
RESET bus event signaled.

**EfiUsbMsgBusEventSuspend**  
SUSPEND bus event signaled.

**EfiUsbMsgBusEventResume**  
RESUME bus event signaled.

**EfiUsbMsgBusEventSpeed**  
Bus speed updated, returned buffer indicated bus speed using an [EFI_USB_BUS_SPEED](efi-usb-bus-speed.md) enumeration.

## Requirements

**Header:** User generated
