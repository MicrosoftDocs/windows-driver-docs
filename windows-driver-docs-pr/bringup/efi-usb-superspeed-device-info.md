---
title: EFI_USB_SUPERSPEED_DEVICE_INFO
description: EFI_USB_SUPERSPEED_DEVICE_INFO
ms.assetid: 7861BA16-7499-48A1-9D6A-9BB8F5AA36CE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USB\_SUPERSPEED\_DEVICE\_INFO


The **EFI\_USB\_SUPERSPEED\_DEVICE\_INFO** structure is used to define the USB SuperSpeed function device.

## Syntax


```cpp
typedef struct 
{
    EFI_USB_DEVICE_DESCRIPTOR           *DeviceDescriptor;
    EFI_USB_SUPERSPEED_CONFIG_INFO      **ConfigInfoTable;
    EFI_USB_BOS_DESCRIPTOR              *BosDescriptor
} EFI_USB_SUPERSPEED_DEVICE_INFO;
```

## Members


<a href="" id="devicedescriptor"></a>**DeviceDescriptor**  
An EFI\_USB\_DEVICE\_DESCRIPTOR structure that contains configuration information for the USB device.

<a href="" id="configinfotable"></a>**ConfigInfoTable**  
An [EFI\_USB\_SUPERSPEED\_CONFIG\_INFO](efi-usb-superspeed-config-info.md) structure that contains information about the supported USB SuperSpeed configurations.

<a href="" id="bosdescriptor"></a>**BosDescriptor**  
An [EFI\_USB\_BOS\_DESCRIPTOR](efi-usb-bos-descriptor.md) structure that contains information about the Binary Object Store to the USB function driver.

## Remarks


The **EFI\_USB\_CONFIG\_DESCRIPTOR** structure is defined in the UEFI specification version 2.3 and later. For more information, visit the [UEFI.org](http://go.microsoft.com/fwlink/p/?linkid=109526) website.

## Requirements


**Header:** User generated

 

 




