---
title: Available interfaces and related APIs
author: windows-driver-content
description: There are three GPIO interfaces one for each device. Each interface is referenced by a GUID.
ms.assetid: 87A275B0-825A-47F1-9701-D7E91C493877
---

# Available interfaces and related APIs


There are three GPIO interfaces: one for each device. Each interface is referenced by a GUID.

/\* 30ebfbf8-df5f-4d4d-9fc5-a26c7fd1df4a \*/ DEFINE\_GUID(GUID\_GPIOBUTTONS\_NOTIFY\_INTERFACE, 0x30ebfbf8, 0xdf5f, 0x4d4d, 0x9f, 0xc5, 0xa2, 0x6c, 0x7f, 0xd1, 0xdf, 0x4a);

/\* 317fc439-3f77-41c8-b09e-08ad63272aa3 \*/ DEFINE\_GUID(GUID\_GPIOBUTTONS\_LAPTOPSLATE\_INTERFACE, 0x317fc439, 0x3f77, 0x41c8, 0xb0, 0x9e, 0x08, 0xad, 0x63, 0x27, 0x2a, 0xa3);

/\* a84e689b-0dce-493a-a164-acde05478fc3 \*/ DEFINE\_GUID(GUID\_GPIOBUTTONS\_DOCKMODE\_INTERFACE, 0xa84e689b, 0x0dce, 0x493a, 0xa1, 0x64, 0xac, 0xde, 0x05, 0x47, 0x8f, 0xc3);

The interfaces allow the state of the buttons or indicators to be toggled by calling WriteFile against the respective device interface.

**Note**  
To prevent potential conflicts between multiple providers, a handle to the device provides exclusive access to the device.

 

``` syntax
typedef enum {
    GPIO_BUTTON_POWER,
    GPIO_BUTTON_WINDOWS,
    GPIO_BUTTON_VOLUME_UP,
    GPIO_BUTTON_VOLUME_DOWN,
    GPIO_BUTTON_ROTATION_LOCK,
} GPIOBUTTONS_BUTTON_TYPE;
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20Available%20interfaces%20and%20related%20APIs%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


