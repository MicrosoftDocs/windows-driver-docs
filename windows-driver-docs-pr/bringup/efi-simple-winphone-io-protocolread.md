---
title: EFI_SIMPLE_WINPHONE_IO_PROTOCOL.Read
description: The Read function reads data from the device.
ms.date: 02/24/2023
ms.topic: reference
---

# EFI_SIMPLE_WINPHONE_IO_PROTOCOL.Read

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

*This*  
A pointer to the EFI_SIMPLE_WINPHONE_IO_PROTOCOL instance.

*NumberOfBytesToRead*  
The maximum number of bytes to be read.

*NumberOfBytesRead*  
The amount of data returned in the Buffer in bytes.

*Buffer*  
The buffer to return data into.

## Return values

The function returns one of the following values:

| Status code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully. |
| EFI_INVALID_PARAMETER | A parameter is invalid. |
| EFI_DEVICE_ERROR | The physical device reported an error. |
| EFI_NOT_READY | The physical device is busy or not ready to process this request. |
| EFI_TIMEOUT | Time-out occurred before establishing a connection. |
| EFI_NO_RESPONSE | The connection to the host is nonexistent or has been terminated. |

## Remarks

This function will block until the requested amount of data is available or it times out.

In case of errors, no more bytes will be read, and the appropriate status code will be returned. In all cases, the number of bytes actually read is returned in **NumberOfBytesRead**.

## Requirements

**Header:** User generated
