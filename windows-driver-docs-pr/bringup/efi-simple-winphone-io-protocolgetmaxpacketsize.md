---
title: EFI_SIMPLE_WINPHONE_IO_PROTOCOL.GetMaxPacketSize
description: EFI_SIMPLE_WINPHONE_IO_PROTOCOL.GetMaxPacketSize
ms.assetid: 8808bb5d-e00d-4b19-87ad-4a071a896e22
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL.GetMaxPacketSize


The **GetMaxPacketSize** function returns the maximum number of bytes that can be accommodated in a single read or write operation.

## Syntax


```cpp
typedef 
EFI_STATUS 
(EFIAPI * EFI_SIMPLE_WINPHONE_IO_GET_MAXPACKET_SIZE) ( 
  IN EFI_SIMPLE_WINPHONE_IO_PROTOCOL    *This, 
  OUT UINTN                             *MaxPacketSize 
  );
```

## Parameters


<a href="" id="this"></a>*This*  
A pointer to the EFI\_SIMPLE\_WINPHONE\_IO\_PROTOCOL instance.

<a href="" id="maxpacketsize"></a>*MaxPacketSize*  
The maximum supported packet size, in bytes.

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


## Requirements


**Header:** User generated

 

 




