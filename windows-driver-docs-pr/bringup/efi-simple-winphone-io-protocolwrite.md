---
title: EFI_SIMPLE_WINPHONE_IO_PROTOCOL.Write
description: The Write function writes data to the device.
ms.date: 08/20/2021
ms.localizationpriority: medium
---

# EFI_SIMPLE_WINPHONE_IO_PROTOCOL.Write

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

*This*  
A pointer to the EFI_SIMPLE_WINPHONE_IO_PROTOCOL instance

*NumberOfBytesToWrite*  
The number of bytes to be written to the device.

*NumberOfBytesWritten*  
The amount of data actually written in bytes.

*Buffer*  
The buffer of data to write.

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

In case of errors, the transmission will be terminated with the appropriate status code. In all cases, the number of bytes actually written to the device is returned in **NumberOfBytesWritten**.

## Requirements

**Header:** User generated
