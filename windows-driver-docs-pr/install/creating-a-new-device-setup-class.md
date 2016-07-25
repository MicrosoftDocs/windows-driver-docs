---
title: Creating a New Device Setup Class
description: Creating a New Device Setup Class
ms.assetid: 3235d1e9-f6f7-4efe-a50c-5ea7a9956e7e
keywords: ["device setup classes WDK device installations", "setup classes WDK device installations"]
---

# Creating a New Device Setup Class


## <a href="" id="ddk-creating-a-new-device-setup-class-dg"></a>


You should only create a new device setup class if absolutely necessary. It is usually possible to assign your device to one of the [system-defined device setup classes](https://msdn.microsoft.com/library/windows/hardware/ff553419).

If your device meets both of the following criteria, you should assign it to an existing device setup class:

-   Your device's installation and configuration requirements match those of an existing class.

-   Your device's capabilities match those of an existing class.

Under the either of following circumstances, you should consider providing a device co-installer:

-   Your device has installation requirements that are not supported by an existing device type-specific INF file.

-   Installation of your device requires device property pages that are not provided by an existing class.

If your device provides capabilities that are significantly different from the capabilities that are provided by devices that belong to existing classes, it might merit a new device setup class. However, you must never create a new setup class for a device that belongs to one of the system-supplied classes. If you do, you will bypass the system-supplied class installer and your device will not be correctly integrated into the system.

If you think a new device setup class is needed, your new class should be based on new device capabilities, and not on the device's location. For example, supporting an existing device on a new bus should not require a new setup class.

Before creating a new device setup class, contact Microsoft to find out if a new system-supplied device setup class is being planned for your device type

You can create a new device setup class by using an INF file. In addition to installing support for a device, an INF file can initialize a new device setup class for the device. Such an INF file has an [**INF ClassInstall32 section**](inf-classinstall32-section.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Creating%20a%20New%20Device%20Setup%20Class%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




