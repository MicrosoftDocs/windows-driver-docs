---
title: EFI\_USBFN\_TRANSFER\_RESULT
author: windows-driver-content
description: EFI\_USBFN\_TRANSFER\_RESULT
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d101b061-2a83-4bf8-9502-ccb6e56f5cea
---

# EFI\_USBFN\_TRANSFER\_RESULT


The **EFI\_USBFN\_TRANSFER\_RESULT** structure contains information about data transmitted to or received from the host.

## Syntax


``` syntax
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_USBFN_TRANSFER_RESULT%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


