---
title: EFI_USBFN_IO_PROTOCOL.Transfer
description: EFI_USBFN_IO_PROTOCOL.Transfer
ms.assetid: 0585de75-9268-4964-8c5f-dcc3338e5287
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USBFN\_IO\_PROTOCOL.Transfer


The **Transfer** function handles transferring data to or from the host on the specified endpoint.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Direction</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>EfiUsbEndpointDirectionDeviceTx</p></td>
<td><p>Start a transmit transfer on the specified endpoint and return immediately.</p></td>
</tr>
<tr class="even">
<td><p>EfiUsbEndpointDirectionDeviceRx</p></td>
<td><p>Start a receive transfer on the specified endpoint and return immediately with available data.</p></td>
</tr>
</tbody>
</table>

 

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


<a href="" id="this"></a>*This*  
A pointer to the EFI\_USBFN\_IO\_PROTOCOL instance.

<a href="" id="endpointindex"></a>*EndpointIndex*  
Indicates the endpoint on which TX or RX transfer needs to take place.

<a href="" id="direction"></a>*Direction*  
Direction of the endpoint. For more information, see [EFI\_USBFN\_ENDPOINT\_DIRECTION](efi-usbfn-endpoint-direction.md).

<a href="" id="buffersize"></a>*BufferSize*  
If Direction is **EfiUsbEndpointDirectionDeviceRx**: On input, the size of the buffer in bytes. On output, the amount of data returned in the buffer in bytes. If Direction is **EfiUsbEndpointDirectionDeviceTx**: On input, the size of the Buffer in bytes. On output, the amount of data actually transmitted in bytes.

<a href="" id="buffer"></a>*Buffer*  
If Direction is **EfiUsbEndpointDirectionDeviceRx**:The buffer to return the received data.

If Direction is **EfiUsbEndpointDirectionDeviceTx**: The buffer that contains the data to be transmitted.

**Note**  
This buffer is allocated and freed by using the AllocateTransferBuffer and FreeTransferBuffer functions. The caller of this function must not free or reuse the buffer until an **EfiUsbMsgEndpointStatusChangedRx** or **EfiUsbMsgEndpointStatusChangedTx** message was received along with the address of the transfer buffer as part of the message payload. See [EFI\_USBFN\_IO\_PROTOCOL.EventHandler](efi-usbfn-io-protocoleventhandler.md) for more information on various messages and their payloads.

 

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
</tbody>
</table>

 

## Remarks


A class driver must call [EFI\_USBFN\_IO\_PROTOCOL.EventHandler](efi-usbfn-io-protocoleventhandler.md) repeatedly to receive updates on the transfer status and number of bytes transferred on various endpoints. Upon update on transfer status, the *Buffer* field of the [EFI\_USBFN\_TRANSFER\_RESULT](efi-usbfn-transfer-result.md) structure must be initialized with the Buffer pointer that was supplied to this method. This function fails with EFI\_INVALID\_PARAMETER return code if the specified direction is incorrect for the endpoint.

The overview of the call sequence is illustrated in [UEFI Sequence Diagram](uefi-sequence-diagram.md).

This function fails with EFI\_INVALID\_PARAMETER return code if the specified direction is incorrect for the endpoint.

## Requirements


**Header:** User generated

 

 




