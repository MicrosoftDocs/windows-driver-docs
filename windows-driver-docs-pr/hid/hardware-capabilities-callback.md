---
title: Hardware Capabilities Callback
description: Hardware Capabilities Callback
ms.assetid: 407505e4-c0d7-4e12-80d7-55801a66f531
keywords: ["callbacks WDK joysticks", "joysticks WDK HID , capabilities", "hardware capabilities callbacks WDK joysticks"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Hardware Capabilities Callback





```cpp
int __stdcall HWCapsRoutine( int joyid, LPJOYOEMHWCAPS pjhwc );
```

Whenever one requests the hardware capabilities of the device, HWCapsRoutine is called. In particular, VJoyD calls HWCapsRoutine before it returns from VJOYD\_Register\_Device\_Driver. So, it is important that the driver completes any initialization upon which this call relies before the device is registered. These values are generally constants. For a device that has four buttons and three axes, of which the third may return either a throttle or a rudder value, the following is appropriate:

```cpp
pjhwc->dwMaxButtons = 4;    /* This should always be the number of buttons */
pjhwc->dwMaxAxes = 4;       /* The largest axis number which may be requested */
pjhwc->dwNumAxes = 3;       /* The number of axes the device has */
```

 

 




