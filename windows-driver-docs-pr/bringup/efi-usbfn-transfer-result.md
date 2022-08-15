---
title: EFI_USBFN_TRANSFER_RESULT
description: The EFI_USBFN_TRANSFER_RESULT structure contains information about data transmitted to or received from the host.
ms.date: 08/23/2021
---

# EFI_USBFN_TRANSFER_RESULT

The **EFI_USBFN_TRANSFER_RESULT** structure contains information about data transmitted to or received from the host.

## Syntax

```cpp
typedef struct _EFI_USBFN_TRANSFER_RESULT 
{
    UINTN                         BytesTransferred;
    EFI_USBFN_TRANSFER_STATUS     TransferStatus;
    UINT8                         EndpointIndex;
    EFI_USBFN_ENDPOINT_DIRECTION  Direction;
    VOID                          *Buffer;
} EFI_USBFN_TRANSFER_RESULT;
```

## Members

**BytesTransferred**  
The amount of data transferred, in bytes.

**TransferStatus**  
An enumeration of type [EFI_USBFN_TRANSFER_STATUS](efi-usbfn-transfer-status.md) that indicates the status of the transfer.

**EndpointIndex**  
The index of the endpoint for which the notification occurred.

**Direction**  
The direction of the endpoint.

**Buffer**  
The buffer that contains the transferred data.

## Requirements

**Header:** User generated
