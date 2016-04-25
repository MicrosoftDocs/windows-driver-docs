---
title: EFI\_USB\_BUS\_SPEED
description: EFI\_USB\_BUS\_SPEED
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_USB_BUS_SPEED%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




