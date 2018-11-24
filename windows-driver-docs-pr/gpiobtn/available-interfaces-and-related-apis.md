---
title: Available interfaces and related APIs
description: There are three GPIO interfaces one for each device. Each interface is referenced by a GUID.
ms.assetid: 87A275B0-825A-47F1-9701-D7E91C493877
ms.localizationpriority: medium
ms.date: 10/17/2018
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

 

 




