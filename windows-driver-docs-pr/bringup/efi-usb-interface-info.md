---
title: EFI_USB_INTERFACE_INFO
description: EFI_USB_INTERFACE_INFO
ms.assetid: d20b78bd-8369-4f50-b161-e8ad0bb4c52f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USB\_INTERFACE\_INFO


The **EFI\_USB\_INTERFACE\_INFO** structure Used to define the supported USB interface.

## Syntax


```cpp
typedef struct 
{
    EFI_USB_INTERFACE_DESCRIPTOR        *InterfaceDescriptor;
    EFI_USB_ENDPOINT_DESCRIPTOR         **EndpointDescriptorTable;
} EFI_USB_INTERFACE_INFO;
```

## Members


<a href="" id="interfacedescriptor"></a>**InterfaceDescriptor**  
A EFI\_USB\_INTERFACE\_DESCRIPTOR structure that contains information about the USB function interface. See **Remarks**.

<a href="" id="endpointdescriptortable"></a>**EndpointDescriptorTable**  
A EFI\_USB\_ENDPOINT\_DESCRIPTOR structure that contains information about the supported endpoints. See **Remarks**.

## Remarks


The **USB\_INTERFACE\_DESCRIPTOR** and **USB\_ENDPOINT\_DESCRIPTOR** structures are defined in UEFI specification 2.3. For more information, visit the [UEFI.org](http://go.microsoft.com/fwlink/p/?linkid=109526) website.

## Requirements


**Header:** User generated

 

 




