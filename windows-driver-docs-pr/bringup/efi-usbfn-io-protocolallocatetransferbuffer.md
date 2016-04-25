---
title: EFI\_USBFN\_IO\_PROTOCOL.AllocateTransferBuffer
description: EFI\_USBFN\_IO\_PROTOCOL.AllocateTransferBuffer
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: dbaa4f18-97b5-4867-9e03-de19b2253722
---

# EFI\_USBFN\_IO\_PROTOCOL.AllocateTransferBuffer


The **AllocateTransferBuffer** function allocates a transfer buffer of the specified size that satisfies controller requirements.

The allocated transfer buffer must be freed using a matching call to the **FreeTransferBuffer** function.

## Syntax


``` syntax
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_ALLOCATE_TRANSFER_BUFFER) (
  IN EFI_USBFN_IO_PROTOCOL    *This,
  IN UINTN                    Size,
  OUT VOID                    **Buffer
  );
```

## Parameters


<a href="" id="this"></a>*This*  
A pointer to the EFI\_USBFN\_IO\_PROTOCOL instance.

<a href="" id="size"></a>*Size*  
The number of bytes to allocate for the transfer buffer.

<a href="" id="buffer"></a>*Buffer*  
A pointer to a pointer to the allocated buffer if the call succeeds; undefined otherwise.

## Return values


This function returns the following values:

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
<td><p><strong>EFI_OUT_OF_RESOURCES</strong></p></td>
<td><p>The requested transfer buffer could not be allocated.</p></td>
</tr>
</tbody>
</table>

 

## Remarks


## Requirements


**Header:** User generated

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_USBFN_IO_PROTOCOL.AllocateTransferBuffer%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


