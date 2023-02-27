---
title: EFI_USBFN_IO_PROTOCOL.EventHandler
description: The EventHandler function is called repeatedly to receive updates on USB bus states, receive and transmit status changes on endpoints, and set up packet on endpoint 0.
ms.date: 02/24/2023
ms.topic: reference
---

# EFI_USBFN_IO_PROTOCOL.EventHandler

The *EventHandler* function is called repeatedly to receive updates on USB bus states, receive and transmit status changes on endpoints, and set up packet on endpoint 0.

## Syntax

```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_EVENTHANDLER) (
  IN EFI_USBFN_IO_PROTOCOL        *This,
  OUT EFI_USBFN_MESSAGE           *Message,
  IN OUT UINTN                    *PayloadSize,
  OUT EFI_USBFN_MESSAGE_PAYLOAD   *Payload
  );
```

## Parameters

*This*  
A pointer to the EFI_USBFN_IO_PROTOCOL instance.

*Message*  
A [EFI_USBFN_MESSAGE](efi-usbfn-message.md) value that indicates the event that initiated this notification.

*PayloadSize*  
On input, the size of the memory pointed to by Payload. On output, the amount of data returned in Payload.

*Payload*  
A pointer to the [EFI_USBFN_MESSAGE_PAYLOAD](efi-usbfn-message-payload.md) instance to return additional payload for current message.

## Return values

The function returns the following values:

| Return code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully. |
| EFI_INVALID_PARAMETER | A parameter is invalid. |
| EFI_DEVICE_ERROR | The physical device reported an error. |
| EFI_NOT_READY | The physical device is busy or not ready to process this request. |
| EFI_BUFFER_TOO_SMALL | Supplied buffer not large enough to hold the message payload. |

## Remarks

A class driver must call EventHandler repeatedly to receive updates on the transfer status and number of bytes transferred on various endpoints. See [UEFI Sequence Diagram](uefi-sequence-diagram.md) for further information.

A few messages have associated payload that is returned in the supplied buffer. Following table describes various messages and their payload.

| Message | Payload | Description |
|--|--|--|
| EfiUsbMsgSetupPacket | EFI_USB_DEVICE_REQUEST | SETUP packet was received. |
| EfiUsbMsgEndpointStatusChangedRx | [EFI_USBFN_TRANSFER_RESULT](efi-usbfn-transfer-result.md) | Some of the requested data has been transmitted to the host. It is the responsibility of the class driver to determine if any remaining data needs to be resent. The Buffer supplied to [EFI_USBFN_IO_PROTOCOL.Transfer](efi-usbfn-io-protocoltransfer.md) must be same as the Buffer field of the payload. |
| EfiUsbMsgEndpointStatusChangedTx | [EFI_USBFN_TRANSFER_RESULT](efi-usbfn-transfer-result.md) | Some of the requested data has been received from the host. It is the responsibility of the class driver to determine if it needs to wait for any remaining data. The Buffer supplied to [EFI_USBFN_IO_PROTOCOL.Transfer](efi-usbfn-io-protocoltransfer.md) must be same as the Buffer field of the payload. |
| EfiUsbMsgBusEventReset | None | RESET bus event was signaled. |
| EfiUsbMsgBusEventDetach | None | DETACH bus event was signaled. |
| EfiUsbMsgBusEventAttach | None | ATTACH bus event signaled. |
| EfiUsbMsgBusEventSuspend | None | SUSPEND bus event was signaled. |
| EfiUsbMsgBusEventResume | None | RESUME bus event signaled. |
| EfiUsbMsgBusEventSpeed | [EFI_USB_BUS_SPEED](efi-usb-bus-speed.md) | Bus speed update signaled. |

## Requirements

**Header:** User generated
