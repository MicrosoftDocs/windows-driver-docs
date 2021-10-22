---
title: EFI_USBFN_IO_PROTOCOL.Transfer
description: The Transfer function handles transferring data to or from the host on the specified endpoint.
ms.date: 08/23/2021
ms.localizationpriority: medium
---

# EFI_USBFN_IO_PROTOCOL.Transfer

The *Transfer* function handles transferring data to or from the host on the specified endpoint.

| Direction | Description |
|--|--|
| EfiUsbEndpointDirectionDeviceTx | Start a transmit transfer on the specified endpoint and return immediately. |
| EfiUsbEndpointDirectionDeviceRx | Start a receive transfer on the specified endpoint and return immediately with available data. |

## Syntax

```cpp
typedef
EFI_STATUS
(EFIAPI *EFI_USBFN_IO_TRANSFER) (
  IN EFI_USBFN_IO_PROTOCOL         *This,
  IN UINT8                         EndpointIndex,
  IN EFI_USBFN_ENDPOINT_DIRECTION  Direction,
  IN OUT UINTN                     *BufferSize,
  IN OUT VOID                      *Buffer
  );
```

## Parameters

*This*  
A pointer to the EFI_USBFN_IO_PROTOCOL instance.

*EndpointIndex*  
Indicates the endpoint on which TX or RX transfer needs to take place.

*Direction*  
Direction of the endpoint. For more information, see [EFI_USBFN_ENDPOINT_DIRECTION](efi-usbfn-endpoint-direction.md).

*BufferSize*  
If Direction is **EfiUsbEndpointDirectionDeviceRx**: On input, the size of the buffer in bytes. On output, the amount of data returned in the buffer in bytes. If Direction is **EfiUsbEndpointDirectionDeviceTx**: On input, the size of the Buffer in bytes. On output, the amount of data actually transmitted in bytes.

*Buffer*  
If Direction is **EfiUsbEndpointDirectionDeviceRx**:The buffer to return the received data. If Direction is **EfiUsbEndpointDirectionDeviceTx**: The buffer that contains the data to be transmitted.

> [!NOTE]
> This buffer is allocated and freed by using the AllocateTransferBuffer and FreeTransferBuffer functions. The caller of this function must not free or reuse the buffer until an **EfiUsbMsgEndpointStatusChangedRx** or **EfiUsbMsgEndpointStatusChangedTx** message was received along with the address of the transfer buffer as part of the message payload. See [EFI_USBFN_IO_PROTOCOL.EventHandler](efi-usbfn-io-protocoleventhandler.md) for more information on various messages and their payloads.

## Return values

The function returns one of the the following values:

| Return code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully |
| EFI_INVALID_PARAMETER | A parameter is invalid |
| EFI_DEVICE_ERROR | The physical device reported an error. |
| EFI_NOT_READY | The physical device is busy or not ready to process this request |

## Remarks

A class driver must call [EFI_USBFN_IO_PROTOCOL.EventHandler](efi-usbfn-io-protocoleventhandler.md) repeatedly to receive updates on the transfer status and number of bytes transferred on various endpoints. Upon update on transfer status, the *Buffer* field of the [EFI_USBFN_TRANSFER_RESULT](efi-usbfn-transfer-result.md) structure must be initialized with the Buffer pointer that was supplied to this method. This function fails with EFI_INVALID_PARAMETER return code if the specified direction is incorrect for the endpoint.

The overview of the call sequence is illustrated in [UEFI Sequence Diagram](uefi-sequence-diagram.md).

This function fails with EFI_INVALID_PARAMETER return code if the specified direction is incorrect for the endpoint.

## Requirements

**Header:** User generated
