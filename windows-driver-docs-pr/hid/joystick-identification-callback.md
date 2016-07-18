---
title: Joystick Identification Callback
author: windows-driver-content
description: Joystick Identification Callback
MS-HAID:
- 'di\_c0d43617-916b-4f39-ad85-aa168e627809.xml'
- 'hid.joystick\_identification\_callback'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d5e859d2-bfe4-41ef-9d09-ebb945d299bd
keywords: ["callbacks WDK joysticks", "joysticks WDK HID , ID requests", "ID requests WDK joysticks", "identification callbacks WDK joysticks"]
---

# Joystick Identification Callback


## <a href="" id="ddk-joystick-identification-callback-di"></a>


```
int __stdcall JoyIdRoutine( int joyid, BOOL used );
```

VJoyD calls JoyIDRoutine when a user configures or de-configures a joystick as one of the 16 joysticks. If the minidriver can support the ID requested in *joyid*, JoyIdRoutine returns a nonzero value. If the minidriver cannot support the ID, the routine returns zero value.

Whenever any change is made and joyConfigChanged is called to update the driver, VJoyD cycles through all 16 devices, starting with JOYSTICKID1. It resets all devices to unused and then loops through them again to set all those that the system needs to use. During control panel operations, this process can entail a large number of calls, which creates problem in this callback usage for initialization. This is particularly true if the call is made before the system boot is complete, that is when other services are not available.

Minidrivers that service callbacks for more than one device should attempt to keep joystick identifiers tied to a single physical device, where possible, to avoid user confusion. You can implement this relatively easily during a single session, but is probably not necessary over reboots.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Joystick%20Identification%20Callback%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


