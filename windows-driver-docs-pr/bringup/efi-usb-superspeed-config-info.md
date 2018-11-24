---
title: EFI_USB_SUPERSPEED_CONFIG_INFO
description: EFI_USB_SUPERSPEED_CONFIG_INFO
ms.assetid: 9827B0A9-AC69-43FA-922F-384E3AE140F7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USB\_SUPERSPEED\_CONFIG\_INFO


The **EFI\_USB\_SUPERSPEED\_CONFIG\_INFO** structure is used to define the supported USB SuperSpeed port configuration to the USB function driver.

## Syntax


```cpp
typedef struct
{
    EFI_USB_CONFIG_DESCRIPTOR           *ConfigDescriptor;
    EFI_USB_SUPERSPEED_INTERFACE_INFO   **InterfaceInfoTable;
} EFI_USB_SUPERSPEED_CONFIG_INFO;
```

## Members


<a href="" id="configdescriptor"></a>**ConfigDescriptor**  
An EFI\_USB\_CONFIG\_DESCRIPTOR structure that contains the configuration descriptor for the USB function device.

<a href="" id="interfaceinfotable"></a>**InterfaceInfoTable**  
An [EFI\_USB\_SUPERSPEED\_INTERFACE\_INFO](efi-usb-superspeed-interface-info.md) structure that describes the supported USB SuperSpeed interfaces.

## Remarks


The **EFI\_USB\_CONFIG\_DESCRIPTOR** structure is defined in the UEFI specification version 2.3 and later. For more information, visit the [UEFI.org](http://go.microsoft.com/fwlink/p/?linkid=109526) website.

## Requirements


**Header:** User generated

 

 




