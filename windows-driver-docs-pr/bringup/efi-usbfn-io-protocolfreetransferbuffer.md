---
title: EFI_USBFN_IO_PROTOCOL.FreeTransferBuffer
description: The FreeTransferBuffer function de-allocates the memory allocated for the transfer buffer by the EFI_USBFN_IO_PROTOCOL.AllocateTransferBuffer function.
ms.date: 08/20/2021
ms.localizationpriority: medium
---

# EFI_USBFN_IO_PROTOCOL.FreeTransferBuffer

The **FreeTransferBuffer** function de-allocates the memory allocated for the transfer buffer by the [EFI_USBFN_IO_PROTOCOL.AllocateTransferBuffer](efi-usbfn-io-protocolallocatetransferbuffer.md) function.

## Syntax

```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_FREE_TRANSFER_BUFFER) (
  IN EFI_USBFN_IO_PROTOCOL    *This,
  IN VOID                     *Buffer
  );
```

## Parameters

*This*  
A pointer to the EFI_USBFN_IO_PROTOCOL instance

*Buffer*  
Pointer to the transfer buffer to de-allocate.

## Return values

This function returns the following values:

| Status code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully. |
| EFI_INVALID_PARAMETER | A parameter is invalid. |

## Remarks

## Requirements

**Header:** User generated
