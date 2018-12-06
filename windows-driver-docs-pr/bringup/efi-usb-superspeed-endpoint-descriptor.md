---
title: EFI_USB_SUPERSPEED_ENDPOINT_DESCRIPTOR
description: EFI_USB_SUPERSPEED_ENDPOINT_DESCRIPTOR
ms.assetid: 3254C0F1-85C2-472B-938A-F71645703540
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USB\_SUPERSPEED\_ENDPOINT\_DESCRIPTOR


The **EFI\_USB\_SUPERSPEED\_ENDPOINT\_DESCRIPTOR** structure is used to describe the supported USB SuperSpeed endpoints to the USB function driver.

## Syntax


```cpp
typedef struct
{
    EFI_USB_ENDPOINT_DESCRIPTOR                         *EndpointDescriptor;
    EFI_USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR    *EndpointCompanionDescriptor;
} EFI_USB_SUPERSPEED_ENDPOINT_DESCRIPTOR;
```

## Members


<a href="" id="endpointdescriptor"></a>**EndpointDescriptor**  
An EFI\_USB\_ENDPOINT\_DESCRIPTOR structure that describes the USB endpoints.

<a href="" id="endpointcompaniondescriptor"></a>**EndpointCompanionDescriptor**  
An [EFI\_USB\_SUPERSPEED\_ENDPOINT\_COMPANION\_DESCRIPTOR](efi-usb-superspeed-endpoint-companion-descriptor.md) structure that is a companion descriptor of the USB SuperSpeed endpoints.

## Remarks


The **EFI\_USB\_ENDPOINT\_DESCRIPTOR** structure is defined in the UEFI specification version 2.3 and later. For more information, visit the [UEFI.org](http://go.microsoft.com/fwlink/p/?linkid=109526) website.

## Requirements


**Header:** User generated

 

 




