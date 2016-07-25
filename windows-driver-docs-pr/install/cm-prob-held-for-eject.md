---
title: CM\_PROB\_HELD\_FOR\_EJECT
description: CM\_PROB\_HELD\_FOR\_EJECT
ms.assetid: 8d67ad71-276d-4dea-b3fb-61fedcfba789
keywords: ["CM_PROB_HELD_FOR_EJECT"]
---

# CM\_PROB\_HELD\_FOR\_EJECT


## <a href="" id="ddk-cm-prob-held-for-eject-dg"></a>


The device has been prepared for ejection.

### Error Code

47

### Display Message (Windows XP and later versions of Windows)

"Windows cannot use this hardware device because it has been prepared for 'safe removal', but it has not been removed from the computer. (Code 47)"

"To fix this problem, unplug this device from your computer and then plug it in again."

### Recommended Resolution (Windows XP and later versions of Windows)

Unplug the device and plug it in again. Alternatively, selecting **Restart Computer** will restart the computer and make the device available.

This error should occur only if the user invokes the hot-plug program to prepare the device for removal (which calls [**CM\_Request\_Device\_Eject**](https://msdn.microsoft.com/library/windows/hardware/ff539806)), or if the user presses a physical eject button (which calls [**IoRequestDeviceEject**](https://msdn.microsoft.com/library/windows/hardware/ff549647)). The user can prepare a device that is currently not removable, such as a CD-ROM trapped between the laptop and the docking station tray.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20CM_PROB_HELD_FOR_EJECT%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




