---
title: EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL.Write
author: windows-driver-content
description: EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL.Write
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 55475573-e904-4adc-91cf-62afe9e67927
---

# EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL.Write


The **Write** function writes data to the device.

This function will block until the requested amount of data is written to the device or it times out.

## Syntax


``` syntax
typedef
EFI_STATUS
(EFIAPI * EFI_SIMPLE_WINPHONE_IO_WRITE) (
  IN EFI_SIMPLE_WINPHONE_IO_PROTOCOL    *This,
  IN UINTN                              NumberOfBytesToWrite,
  IN OUT UINTN                          *NumberOfBytesWritten,
  IN VOID                               *Buffer
  );
```

## Parameters


<a href="" id="this"></a>*This*  
A pointer to the EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL instance

<a href="" id="numberofbytestowrite"></a>*NumberOfBytesToWrite*  
The number of bytes to be written to the device.

<a href="" id="numberofbyteswritten"></a>*NumberOfBytesWritten*  
The amount of data actually written in bytes.

<a href="" id="buffer"></a>*Buffer*  
The buffer of data to write.

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


In case of errors, the transmission will be terminated with the appropriate status code. In all cases, the number of bytes actually written to the device is returned in **NumberOfBytesWritten**.

## Requirements


**Header:** User generated

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_SIMPLE_WINPHONE_IO_PROTOCOL.Write%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


