---
title: EFI_USB_BUS_SPEED
author: windows-driver-content
description: EFI_USB_BUS_SPEED
ms.assetid: 2888cff6-db12-47ea-866f-de218e2b08e5
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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


