---
title: EFI_USBFN_IO_PROTOCOL.EventHandler
description: EFI_USBFN_IO_PROTOCOL.EventHandler
ms.assetid: d493de90-cb8c-44d1-8999-f1ceb26e5c15
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USBFN\_IO\_PROTOCOL.EventHandler


The **EventHandler** function is called repeatedly to receive updates on USB bus states, receive and transmit status changes on endpoints, and set up packet on endpoint 0.

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


<a href="" id="this"></a>*This*  
A pointer to the EFI\_USBFN\_IO\_PROTOCOL instance.

<a href="" id="message"></a>*Message*  
A [EFI\_USBFN\_MESSAGE](efi-usbfn-message.md) value that indicates the event that initiated this notification.

<a href="" id="payloadsize"></a>*PayloadSize*  
On input, the size of the memory pointed to by Payload. On output, the amount of data returned in Payload.

<a href="" id="payload"></a>*Payload*  
A pointer to the [EFI\_USBFN\_MESSAGE\_PAYLOAD](efi-usbfn-message-payload.md) instance to return additional payload for current message.

## Return values


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>EFI_SUCCESS</strong></p></td>
<td><p>The function returned successfully</p></td>
</tr>
<tr class="even">
<td><p><strong>EFI_INVALID_PARAMETER</strong></p></td>
<td><p>A parameter is invalid</p></td>
</tr>
<tr class="odd">
<td><p><strong>EFI_DEVICE_ERROR</strong></p></td>
<td><p>The physical device reported an error.</p></td>
</tr>
<tr class="even">
<td><p><strong>EFI_NOT_READY</strong></p></td>
<td><p>The physical device is busy or not ready to process this request</p></td>
</tr>
<tr class="odd">
<td><p><strong>EFI_BUFFER_TOO_SMALL</strong></p></td>
<td><p>Supplied buffer not large enough to hold the message payload.</p></td>
</tr>
</tbody>
</table>

 

## Remarks


A class driver must call EventHandler repeatedly to receive updates on the transfer status and number of bytes transferred on various endpoints. See [UEFI Sequence Diagram](uefi-sequence-diagram.md) for further information.

A few messages have associated payload that is returned in the supplied buffer. Following table describes various messages and their payload.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Message</th>
<th>Payload</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>EfiUsbMsgSetupPacket</p></td>
<td><p>EFI_USB_DEVICE_REQUEST</p></td>
<td><p>SETUP packet was received</p></td>
</tr>
<tr class="even">
<td><p>EfiUsbMsgEndpointStatusChangedRx</p></td>
<td><p><a href="efi-usbfn-transfer-result.md" data-raw-source="[EFI_USBFN_TRANSFER_RESULT](efi-usbfn-transfer-result.md)">EFI_USBFN_TRANSFER_RESULT</a></p></td>
<td><p>Some of the requested data has been transmitted to the host. It is the responsibility of the class driver to determine if any remaining data needs to be resent. The Buffer supplied to <a href="efi-usbfn-io-protocoltransfer.md" data-raw-source="[EFI_USBFN_IO_PROTOCOL.Transfer](efi-usbfn-io-protocoltransfer.md)">EFI_USBFN_IO_PROTOCOL.Transfer</a>r must be same as the Buffer field of the payload.</p></td>
</tr>
<tr class="odd">
<td><p>EfiUsbMsgEndpointStatusChangedTx</p></td>
<td><p><a href="efi-usbfn-transfer-result.md" data-raw-source="[EFI_USBFN_TRANSFER_RESULT](efi-usbfn-transfer-result.md)">EFI_USBFN_TRANSFER_RESULT</a></p></td>
<td><p>Some of the requested data has been received from the host. It is the responsibility of the class driver to determine if it needs to wait for any remaining data. The Buffer supplied to <a href="efi-usbfn-io-protocoltransfer.md" data-raw-source="[EFI_USBFN_IO_PROTOCOL.Transfer](efi-usbfn-io-protocoltransfer.md)">EFI_USBFN_IO_PROTOCOL.Transfer</a> must be same as the Buffer field of the payload.</p></td>
</tr>
<tr class="even">
<td><p>EfiUsbMsgBusEventReset</p></td>
<td><p>None</p></td>
<td><p>RESET bus event was signaled.</p></td>
</tr>
<tr class="odd">
<td><p>EfiUsbMsgBusEventDetach</p></td>
<td><p>None</p></td>
<td><p>DETACH bus event was signaled.</p></td>
</tr>
<tr class="even">
<td><p>EfiUsbMsgBusEventAttach</p></td>
<td><p>None</p></td>
<td><p>ATTACH bus event signaled.</p></td>
</tr>
<tr class="odd">
<td><p>EfiUsbMsgBusEventSuspend</p></td>
<td><p>None</p></td>
<td><p>SUSPEND bus event was signaled.</p></td>
</tr>
<tr class="even">
<td><p>EfiUsbMsgBusEventResume</p></td>
<td><p>None</p></td>
<td><p>RESUME bus event signaled.</p></td>
</tr>
<tr class="odd">
<td><p>EfiUsbMsgBusEventSpeed</p></td>
<td><p><a href="efi-usb-bus-speed.md" data-raw-source="[EFI_USB_BUS_SPEED](efi-usb-bus-speed.md)">EFI_USB_BUS_SPEED</a></p></td>
<td><p>Bus speed update signaled.</p></td>
</tr>
</tbody>
</table>

 

## Requirements


**Header:** User generated

 

 




