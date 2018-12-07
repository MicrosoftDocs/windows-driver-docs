---
title: EFI_USBFN_TRANSFER_RESULT
description: EFI_USBFN_TRANSFER_RESULT
ms.assetid: d101b061-2a83-4bf8-9502-ccb6e56f5cea
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USBFN\_TRANSFER\_RESULT


The **EFI\_USBFN\_TRANSFER\_RESULT** structure contains information about data transmitted to or received from the host.

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


<a href="" id="bytestransferred"></a>**BytesTransferred**  
The amount of data transferred, in bytes.

<a href="" id="transferstatus"></a>**TransferStatus**  
An enumeration of type [EFI\_USBFN\_TRANSFER\_STATUS](efi-usbfn-transfer-status.md) that indicates the status of the transfer.

<a href="" id="endpointindex"></a>**EndpointIndex**  
The index of the endpoint for which the notification occurred.

<a href="" id="direction"></a>**Direction**  
The direction of the endpoint.

<a href="" id="buffer"></a>**Buffer**  
The buffer that contains the transferred data.

## Requirements


**Header:** User generated

 

 




