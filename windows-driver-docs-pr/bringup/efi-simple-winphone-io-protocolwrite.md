---
title: EFI_SIMPLE_WINPHONE_IO_PROTOCOL.Write
description: EFI_SIMPLE_WINPHONE_IO_PROTOCOL.Write
ms.assetid: 55475573-e904-4adc-91cf-62afe9e67927
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL.Write


The **Write** function writes data to the device.

This function will block until the requested amount of data is written to the device or it times out.

## Syntax


```cpp
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

 

 




