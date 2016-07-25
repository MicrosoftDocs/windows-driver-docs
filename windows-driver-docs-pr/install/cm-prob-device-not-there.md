---
title: CM\_PROB\_DEVICE\_NOT\_THERE
description: CM\_PROB\_DEVICE\_NOT\_THERE
ms.assetid: 843afcc0-30ca-42f8-8c9b-3c4a56ec019d
keywords: ["CM_PROB_DEVICE_NOT_THERE"]
---

# CM\_PROB\_DEVICE\_NOT\_THERE


## <a href="" id="ddk-cm-prob-device-not-there-dg"></a>


The device does not seem to be present.

### Error Code

24

### Display Message (Windows 2000 and later versions of Windows)

"This device is not present, is not working properly, or does not have all its drivers installed. (Code 24)"

### Recommended Resolution (Windows 2000 and later versions of Windows)

The problem could be bad hardware, or a new driver might be needed. Devices stay in this state if they have been prepared for removal. This error code can be set if a driver's **DriverEntry** routine detects a device but the **DriverEntry** routine later fails.

**Note**  For Windows XP and later versions of Windows, **DriverEntry** problems have separate error codes.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20CM_PROB_DEVICE_NOT_THERE%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




