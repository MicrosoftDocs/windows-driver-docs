---
title: EFI_SIMPLE_WINPHONE_IO_PROTOCOL.Read
description: EFI_SIMPLE_WINPHONE_IO_PROTOCOL.Read
ms.assetid: 9b5525a4-d98c-4328-8ebe-55ede53befca
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL.Read


The **Read** function reads data from the device.

## Syntax


```cpp
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

 

 




