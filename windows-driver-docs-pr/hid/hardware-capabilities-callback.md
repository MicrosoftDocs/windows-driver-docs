---
title: Hardware Capabilities Callback
author: windows-driver-content
description: Hardware Capabilities Callback
MS-HAID:
- 'di\_b1128c56-d5b3-4f38-8449-670aebfb9320.xml'
- 'hid.hardware\_capabilities\_callback'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 407505e4-c0d7-4e12-80d7-55801a66f531
keywords: ["callbacks WDK joysticks", "joysticks WDK HID , capabilities", "hardware capabilities callbacks WDK joysticks"]
---

# Hardware Capabilities Callback


## <a href="" id="ddk-hardware-capabilities-callback-di"></a>


```
int __stdcall HWCapsRoutine( int joyid, LPJOYOEMHWCAPS pjhwc );
```

Whenever one requests the hardware capabilities of the device, HWCapsRoutine is called. In particular, VJoyD calls HWCapsRoutine before it returns from VJOYD\_Register\_Device\_Driver. So, it is important that the driver completes any initialization upon which this call relies before the device is registered. These values are generally constants. For a device that has four buttons and three axes, of which the third may return either a throttle or a rudder value, the following is appropriate:

```
pjhwc->dwMaxButtons = 4;    /* This should always be the number of buttons */
pjhwc->dwMaxAxes = 4;       /* The largest axis number which may be requested */
pjhwc->dwNumAxes = 3;       /* The number of axes the device has */
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Hardware%20Capabilities%20Callback%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


