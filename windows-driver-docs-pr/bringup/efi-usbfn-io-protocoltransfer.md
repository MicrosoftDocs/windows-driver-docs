---
title: EFI\_USBFN\_IO\_PROTOCOL.Transfer
author: windows-driver-content
description: EFI\_USBFN\_IO\_PROTOCOL.Transfer
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 0585de75-9268-4964-8c5f-dcc3338e5287
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


``` syntax
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_USBFN_IO_PROTOCOL.Transfer%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


