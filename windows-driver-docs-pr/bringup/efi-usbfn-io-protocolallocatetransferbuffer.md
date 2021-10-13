---
title: EFI_USBFN_IO_PROTOCOL.AllocateTransferBuffer
description: The AllocateTransferBuffer function allocates a transfer buffer of the specified size that satisfies controller requirements.
ms.date: 08/20/2021
ms.localizationpriority: medium
---

# EFI_USBFN_IO_PROTOCOL.AllocateTransferBuffer

The **AllocateTransferBuffer** function allocates a transfer buffer of the specified size that satisfies controller requirements.

The allocated transfer buffer must be freed using a matching call to the **FreeTransferBuffer** function.

## Syntax

```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_ALLOCATE_TRANSFER_BUFFER) (
  IN EFI_USBFN_IO_PROTOCOL    *This,
  IN UINTN                    Size,
  OUT VOID                    **Buffer
  );
```

## Parameters

*This*  
A pointer to the EFI_USBFN_IO_PROTOCOL instance.

*Size*  
The number of bytes to allocate for the transfer buffer.

*Buffer*  
A pointer to a pointer to the allocated buffer if the call succeeds; undefined otherwise.

## Return values

This function returns the following values:

| Return value | Description |
| -- | -- |
| EFI_SUCCESS | The function returned successfully. |
| EFI_INVALID_PARAMETER | A parameter is invalid. |
| EFI_OUT_OF_RESOURCES | The requested transfer buffer could not be allocated. |

## Requirements

**Header:** User generated
