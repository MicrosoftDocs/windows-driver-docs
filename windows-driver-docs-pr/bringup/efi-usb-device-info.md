---
title: EFI\_USB\_DEVICE\_INFO
author: windows-driver-content
description: EFI\_USB\_DEVICE\_INFO
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b44f77fc-f496-488f-b53a-b54420da9360
---

# EFI\_USB\_DEVICE\_INFO


The **EFI\_USB\_DEVICE\_INFO** structure is used to define the USB function device.

## Syntax


``` syntax
typedef struct 
{
    EFI_USB_DEVICE_DESCRIPTOR           *DeviceDescriptor;
    EFI_USB_CONFIG_INFO                 **ConfigInfoTable;
} EFI_USB_DEVICE_INFO;
```

## Members


<a href="" id="devicedescriptor"></a>**DeviceDescriptor**  
A EFI\_USB\_DEVICE\_DESCRIPTOR structure that contains configuration information for the USB device.

<a href="" id="configinfotable"></a>**ConfigInfoTable**  
A EFI\_USB\_CONFIG\_INFO structure that contains information about the supported configurations.

## Remarks


The **EFI\_USB\_CONFIG\_DESCRIPTOR** and **EFI\_USB\_DEVICE\_DESCRIPTOR** structures are defined in UEFI specification 2.3. For more information, visit the [UEFI.org](http://go.microsoft.com/fwlink/p/?linkid=109526) website.

## Requirements


**Header:** User generated

 

 


--------------------


