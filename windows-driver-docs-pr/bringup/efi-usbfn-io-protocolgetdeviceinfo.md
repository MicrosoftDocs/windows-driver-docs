---
title: EFI\_USBFN\_IO\_PROTOCOL.GetDeviceInfo
description: EFI\_USBFN\_IO\_PROTOCOL.GetDeviceInfo
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b72f6ba1-7704-4661-8855-1ff88bd08e5a
---

# EFI\_USBFN\_IO\_PROTOCOL.GetDeviceInfo


The **GetDeviceInfo** function Returns device-specific information based on the supplied identifier

Specifying **EfiUsbDeviceInfoUnknown** as Id is treated as an invalid parameter.

## Syntax


``` syntax
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_USBFN_IO_PROTOCOL.GetDeviceInfo%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


