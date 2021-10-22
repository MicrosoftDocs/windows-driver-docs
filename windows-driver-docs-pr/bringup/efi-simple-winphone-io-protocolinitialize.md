---
title: EFI_SIMPLE_WINPHONE_IO_PROTOCOL.Initialize
description: Waits for a connection from the host computer for the specified number of seconds.
ms.date: 08/20/2021
ms.localizationpriority: medium
---

# EFI_SIMPLE_WINPHONE_IO_PROTOCOL.Initialize

The **Initialize** function waits for a connection from the host computer for the specified number of seconds. If a valid connection is not made, **EFI_TIMEOUT** is returned as failure status.

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

*This*  
A pointer to the EFI_SIMPLE_WINPHONE_IO_PROTOCOL instance.

*ConnectionTimeout*  
Number of milliseconds to wait for connection from a host computer.

*ReadWriteTimeout*  
Number of milliseconds to wait for read and write operations to complete.

## Return values

The function returns one of the following values:

| Status code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully. |
| EFI_INVALID_PARAMETER | A parameter is invalid. |
| EFI_DEVICE_ERROR | The physical device reported an error. |
| EFI_NOT_READY | The physical device is busy or not ready to process this request. |
| EFI_TIMEOUT | Time-out occurred before establishing a connection. |

## Remarks

## Requirements

**Header:** User generated
