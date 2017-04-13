---
title: EFI\_USB\_BUS\_SPEED
author: windows-driver-content
description: EFI\_USB\_BUS\_SPEED
ms.assetid: 2888cff6-db12-47ea-866f-de218e2b08e5
---

# EFI\_USB\_BUS\_SPEED


Is enumeration contains values used to indicate the bus speed.

## Syntax


``` syntax
typedef enum _EFI_USB_BUS_SPEED 
{
    UsbBusSpeedUnknown = 0,
    UsbBusSpeedLow,
    UsbBusSpeedFull,
    UsbBusSpeedHigh,
    UsbBusSpeedSuper,
    UsbBusSpeedMaximum = UsbBusSpeedSuper
} EFI_USB_BUS_SPEED;
```

## Constants


<a href="" id="usbbusspeedunknown"></a>**UsbBusSpeedUnknown**  
Bus speed unknown.

<a href="" id="usbbusspeedlow"></a>**UsbBusSpeedLow**  
Low speed.

<a href="" id="usbbusspeedfull"></a>**UsbBusSpeedFull**  
Full speed.

<a href="" id="usbbusspeedhigh"></a>**UsbBusSpeedHigh**  
High speed.

<a href="" id="usbbusspeedsuper"></a>**UsbBusSpeedSuper**  
Super speed.

## Requirements


**Header:** User generated

 

 


--------------------


