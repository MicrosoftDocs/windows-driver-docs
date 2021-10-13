---
title: EFI_USB_BUS_SPEED
description: The EFI_USB_BUS_SPEED enumeration contains values used to indicate the bus speed.
ms.date: 08/20/2021
ms.localizationpriority: medium
---

# EFI_USB_BUS_SPEED

The **EFI_USB_BUS_SPEED** enumeration contains values used to indicate the bus speed.

## Syntax

```cpp
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

**UsbBusSpeedUnknown**  
Bus speed unknown.

**UsbBusSpeedLow**  
Low speed.

**UsbBusSpeedFull**  
Full speed.

**UsbBusSpeedHigh**  
High speed.

**UsbBusSpeedSuper**  
Super speed.

## Requirements

**Header:** User generated
