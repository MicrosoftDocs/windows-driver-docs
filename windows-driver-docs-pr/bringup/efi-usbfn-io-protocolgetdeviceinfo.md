---
title: EFI_USBFN_IO_PROTOCOL.GetDeviceInfo
description: EFI_USBFN_IO_PROTOCOL.GetDeviceInfo
ms.assetid: b72f6ba1-7704-4661-8855-1ff88bd08e5a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USBFN\_IO\_PROTOCOL.GetDeviceInfo


The **GetDeviceInfo** function Returns device-specific information based on the supplied identifier

Specifying **EfiUsbDeviceInfoUnknown** as Id is treated as an invalid parameter.

## Syntax


```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_GET_DEVICE_INFO) (
  IN EFI_USBFN_IO_PROTOCOL      *This,
  IN EFI_USBFN_DEVICE_INFO_ID   Id,
  IN OUT UINTN                  *BufferSize,
  OUT VOID                      *Buffer OPTIONAL
  );
```

## Parameters


<a href="" id="this"></a>*This*  
A pointer to the EFI\_USBFN\_IO\_PROTOCOL instance.

<a href="" id="id"></a>*Id*  
A [EFI\_USBFN\_DEVICE\_INFO\_ID](efi-usbfn-device-info-id.md) enumeration that contains the requested device ID.

<a href="" id="buffersize"></a>*BufferSize*  
On input, the size of the Buffer in bytes. On output, the amount of data returned in Buffer in bytes.

<a href="" id="buffer"></a>*Buffer*  
A pointer to a buffer in which the requested information will be returned as a Unicode string.

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
<td><p>Supplied buffer isn’t large enough to hold the request string.</p></td>
</tr>
</tbody>
</table>

 

## Remarks


If the supplied Buffer is too small or NULL, the method fails with **EFI\_BUFFER\_TOO\_SMALL** and the required size is returned through **BufferSize**. All returned strings are in Unicode format.

## Requirements


**Header:** User generated

 

 




