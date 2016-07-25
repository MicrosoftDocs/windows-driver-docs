---
title: CM\_PROB\_FAILED\_ADD
description: CM\_PROB\_FAILED\_ADD
ms.assetid: 3004f9fa-4afb-47a9-8aa1-95086eb4f38d
keywords: ["CM_PROB_FAILED_ADD"]
---

# CM\_PROB\_FAILED\_ADD


## <a href="" id="ddk-cm-prob-failed-add-dg"></a>


A driver's attempt to add a device failed.

### Error Code

31

### Display Message (Windows 2000 and later versions of Windows)

"This device is not working properly because Windows cannot load the drivers required for this device. (Code 31)"

### Recommended Resolution (Windows 2000 and later versions of Windows)

Update the device driver.

Starting with Windows XP, this problem can only occur if the driver's [AddDevice routine](https://msdn.microsoft.com/library/windows/hardware/ff566398) fails.

For Windows 2000, this problem can occur in any of the following cases:

-   The service key is corrupted.

-   The driver's image could not be loaded from the disk.

-   The driver's [DriverEntry routine](https://msdn.microsoft.com/library/windows/hardware/ff566402) failed.

-   The driver could not unload because of a leaked reference.

-   The driver is a legacy driver that did not create device objects.

-   The driver's *AddDevice* routine failed.

To update a device driver, follow these steps:

1.  [Open Device Manager](using-device-manager.md).

2.  Right-click the icon that represents the device in the Device Manager window.

3.  On the menu that appears, click **Update Driver** to start the Hardware Update wizard.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20CM_PROB_FAILED_ADD%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




