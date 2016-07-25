---
title: CM\_PROB\_DUPLICATE\_DEVICE
description: CM\_PROB\_DUPLICATE\_DEVICE
ms.assetid: db0f6c98-d314-4882-ac8e-c73254f41c98
keywords: ["CM_PROB_DUPLICATE_DEVICE"]
---

# CM\_PROB\_DUPLICATE\_DEVICE


## <a href="" id="ddk-cm-prob-duplicate-device-dg"></a>


A duplicate device was detected.

### Error Code

42

### Display Message (Windows XP and later versions of Windows)

"Windows cannot load the device driver for this hardware because there is a duplicate device already running in the system. (Code 42)"

### Recommended Resolution (Windows XP and later versions of Windows)

This error is reported when one of the following occurs:

-   A device with a serial number is discovered in a new location in the computer before the operating system notices that the device is missing from the old location. This typically happens when a device is moved, either very quickly or when the computer is in a standby or hibernate state, to a different location.

    In this case, you can resolve the problem by restarting the computer.

-   A bus driver incorrectly creates two identically named children on the bus. This is caused by multiple devices on the bus that report the same serial number. This can also be caused by a bus driver that incorrectly reports the same hardware identifiers for two or more devices.

    In this case, you should contact [Microsoft support](http://support.microsoft.com/) for more assistance with this problem.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20CM_PROB_DUPLICATE_DEVICE%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




