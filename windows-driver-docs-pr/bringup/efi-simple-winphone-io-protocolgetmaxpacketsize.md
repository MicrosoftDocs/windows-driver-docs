---
title: EFI_SIMPLE_WINPHONE_IO_PROTOCOL.GetMaxPacketSize
description: Returns the maximum number of bytes that can be accommodated in a single read or write operation.
ms.date: 08/20/2021
ms.localizationpriority: medium
---

# EFI_SIMPLE_WINPHONE_IO_PROTOCOL.GetMaxPacketSize

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

*This*  
A pointer to the EFI_SIMPLE_WINPHONE_IO_PROTOCOL instance.

*MaxPacketSize*  
The maximum supported packet size, in bytes.

## Return values

| Status code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully. |
| EFI_INVALID_PARAMETER | A parameter was invalid. |
| EFI_DEVICE_ERROR | The physical device reported an error. |
| EFI_NOT_READY | The physical device is busy or not ready to process this request. |

## Remarks

## Requirements

**Header:** User generated
