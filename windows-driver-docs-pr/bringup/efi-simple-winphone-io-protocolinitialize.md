---
title: EFI_SIMPLE_WINPHONE_IO_PROTOCOL.Initialize
description: EFI_SIMPLE_WINPHONE_IO_PROTOCOL.Initialize
ms.assetid: e27ed767-7854-4b2f-8043-35c39357eee4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL.Initialize


The **Initialize** function waits for a connection from the host computer for the specified number of seconds. If a valid connection is not made, **EFI\_TIMEOUT** is returned as failure status.

## Syntax


```cpp
typedef
EFI_STATUS(EFIAPI * EFI_SIMPLE_WINPHONE_IO_INITIALIZE) 
(
  IN EFI_SIMPLE_WINPHONE_IO_PROTOCOL    *This,
  IN UINTN                              ConnectionTimeout,
  IN UINTN                              ReadWriteTimeout
  );
```

## Parameters


<a href="" id="this"></a>*This*  
A pointer to the EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL instance.

<a href="" id="connectiontimeout"></a>*ConnectionTimeout*  
Number of milliseconds to wait for connection from a host computer.

<a href="" id="readwritetimeout"></a>*ReadWriteTimeout*  
Number of milliseconds to wait for read and write operations to complete.

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
</tbody>
</table>

 

## Remarks


## Requirements


**Header:** User generated

 

 




