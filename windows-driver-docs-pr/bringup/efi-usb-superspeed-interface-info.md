---
title: EFI_USB_SUPERSPEED_INTERFACE_INFO
description: EFI_USB_SUPERSPEED_INTERFACE_INFO
ms.assetid: 1B0C04D0-5254-4B9A-A94D-4FF1CEAD4627
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USB\_SUPERSPEED\_INTERFACE\_INFO


The **EFI\_USB\_SUPERSPEED\_INTERFACE\_INFO** structure is used to define the supported USB SuperSpeed interface to the USB function driver.

## Syntax


```cpp
typedef struct
{
    EFI_USB_INTERFACE_DESCRIPTOR            *InterfaceDescriptor;
    EFI_USB_SUPERSPEED_ENDPOINT_DESCRIPTOR  **EndpointDescriptorTable; 
} EFI_USB_SUPERSPEED_INTERFACE_INFO;
```

## Members


<a href="" id="interfacedescriptor"></a>**InterfaceDescriptor**  
An EFI\_USB\_INTERFACE\_DESCRIPTOR structure that describes the USB function interface.

<a href="" id="endpointdescriptortable"></a>**EndpointDescriptorTable**  
An [EFI\_USB\_SUPERSPEED\_ENDPOINT\_DESCRIPTOR](efi-usb-superspeed-endpoint-descriptor.md) structure that describes the USB SuperSpeed endpoints.

## Remarks


The **EFI\_USB\_INTERFACE\_DESCRIPTOR** structure is defined in the UEFI specification version 2.3 and later. For more information, visit the [UEFI.org](http://go.microsoft.com/fwlink/p/?linkid=109526) website.

## Requirements


**Header:** User generated

 

 




