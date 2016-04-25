---
title: EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL.Read
description: EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL.Read
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9b5525a4-d98c-4328-8ebe-55ede53befca
---

# EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL.Read


The **Read** function reads data from the device.

## Syntax


``` syntax
typedef
EFI_STATUS
(EFIAPI * EFI_SIMPLE_WINPHONE_IO_READ) (
  IN EFI_SIMPLE_WINPHONE_IO_PROTOCOL    *This,
  IN UINTN                              NumberOfBytesToRead,
  IN OUT UINTN                          *NumberOfBytesRead,
  OUT VOID                              *Buffer
  );
```

## Parameters


<a href="" id="this"></a>*This*  
A pointer to the EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL instance.

<a href="" id="numberofbytestoread"></a>*NumberOfBytesToRead*  
The maximum number of bytes to be read.

<a href="" id="numberofbytesread"></a>*NumberOfBytesRead*  
The amount of data returned in the Buffer in bytes

<a href="" id="buffer"></a>*Buffer*  
The buffer to return data into.

## Return values


The function returns one of the following values:

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
<td><p><strong>EFI_TIMEOUT</strong></p></td>
<td><p>Time-out occurred before establishing a connection.</p></td>
</tr>
<tr class="even">
<td><p><strong>EFI_NO_RESPONSE</strong></p></td>
<td><p>The connection to the host is nonexistent or has been terminated.</p></td>
</tr>
</tbody>
</table>

 

## Remarks


This function will block until the requested amount of data is available or it times out.

In case of errors, no more bytes will be read, and the appropriate status code will be returned. In all cases, the number of bytes actually read is returned in **NumberOfBytesRead**.

## Requirements


**Header:** User generated

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_SIMPLE_WINPHONE_IO_PROTOCOL.Read%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




