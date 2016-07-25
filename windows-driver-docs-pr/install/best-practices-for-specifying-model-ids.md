---
title: Best Practices for Specifying Model IDs
description: Best Practices for Specifying Model IDs
ms.assetid: ed0cdfb4-1de8-4b4f-8bab-7c5e06cf96f6
---

# Best Practices for Specifying Model IDs


Model IDs are based on the business definition or stock keeping unit (SKU) of the physical device. Each model ID must be unique for all makes and models of the physical device.

The following list describes the differences between hardware IDs and model IDs for a physical device:

-   [Hardware IDs](hardware-ids.md) are specified by using one or more [**HardwareID**](https://msdn.microsoft.com/library/windows/hardware/ff546114) XML elements within the [**HardwareIDList**](https://msdn.microsoft.com/library/windows/hardware/ff546121) XML element. Each **HardwareID** value specifies a hardware function based on a bus-specific value. Hardware IDs could be used to map device drivers to device instances.

    For example, two devices with the same hardware ID share a functional interface that is used by the same driver.

-   Model IDs are specified by using one or more [**ModelID**](https://msdn.microsoft.com/library/windows/hardware/ff549295) XML elements within the [**ModelIDList**](https://msdn.microsoft.com/library/windows/hardware/ff549303) XML element. Model IDs allow the original equipment manufacturer (OEM) or independent hardware vendor (IHV) to uniquely identify the physical device independent of bus or interface technologies.

    For example, two devices with different model IDs might have the same hardware IDs for their components.

-   [Hardware IDs](hardware-ids.md) are used to map device metadata packages to device instances on a specific bus or interface.

-   Model IDs are used to map device metadata packages to physical devices, regardless of how the device is connected to the computer.

The [**ModelIDList**](https://msdn.microsoft.com/library/windows/hardware/ff549303) XML element is required only if the [**HardwareIDList**](https://msdn.microsoft.com/library/windows/hardware/ff546121) element is not specified in the [**PackageInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549574) XML data. If it is specified, the **ModelIDList** element must contain one or more [**ModelID**](https://msdn.microsoft.com/library/windows/hardware/ff549295) elements to specify the unique model ID for each function that the device supports.

If the [**PackageInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549574) XML data contains the [**HardwareIDList**](https://msdn.microsoft.com/library/windows/hardware/ff546121) and [**ModelIDList**](https://msdn.microsoft.com/library/windows/hardware/ff549303) elements, the operating system uses the following rules when it determines whether a device is specified by a device metadata package:

-   If the device has a model ID, the operating system does not search for a match in the **HardwareIDList** element.

-   Otherwise, the operating system searches the **HardwareIDList** element for a match of the hardware ID for the device.

If your device metadata package supports multiple device models or model IDs, you can specify a [**ModelID**](https://msdn.microsoft.com/library/windows/hardware/ff549295) element for each device model.

The following is an example of a [**ModelIDList**](https://msdn.microsoft.com/library/windows/hardware/ff549303) element that has multiple **ModelID** elements:

```
<ModelIDList>
<ModelID>825AAB98-18EE-4FE2-9472-197D1D00FE31</ModelID>
<ModelID>23F64715-AC4A-4DC4-B554-C8D56E43FE8B</ModelID>
</ModelIDList>
```

For more information about the format requirements of the **ModelID** XML element, see [**ModelID**](https://msdn.microsoft.com/library/windows/hardware/ff549295).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Best%20Practices%20for%20Specifying%20Model%20IDs%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




