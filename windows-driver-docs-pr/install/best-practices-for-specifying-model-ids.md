---
title: Best Practices for Specifying Model IDs
description: Best Practices for Specifying Model IDs
ms.date: 04/20/2017
---

# Best Practices for Specifying Model IDs


Model IDs are based on the business definition or stock keeping unit (SKU) of the physical device. Each model ID must be unique for all makes and models of the physical device.

The following list describes the differences between hardware IDs and model IDs for a physical device:

-   [Hardware IDs](hardware-ids.md) are specified by using one or more [**HardwareID**](/previous-versions/windows/hardware/metadata/ff546114(v=vs.85)) XML elements within the [**HardwareIDList**](/previous-versions/windows/hardware/metadata/ff546121(v=vs.85)) XML element. Each **HardwareID** value specifies a hardware function based on a bus-specific value. Hardware IDs could be used to map device drivers to device instances.

    For example, two devices with the same hardware ID share a functional interface that is used by the same driver.

-   Model IDs are specified by using one or more [**ModelID**](/previous-versions/windows/hardware/metadata/ff549295(v=vs.85)) XML elements within the [**ModelIDList**](/previous-versions/windows/hardware/metadata/ff549303(v=vs.85)) XML element. Model IDs allow the original equipment manufacturer (OEM) or independent hardware vendor (IHV) to uniquely identify the physical device independent of bus or interface technologies.

    For example, two devices with different model IDs might have the same hardware IDs for their components.

-   [Hardware IDs](hardware-ids.md) are used to map device metadata packages to device instances on a specific bus or interface.

-   Model IDs are used to map device metadata packages to physical devices, regardless of how the device is connected to the computer.

The [**ModelIDList**](/previous-versions/windows/hardware/metadata/ff549303(v=vs.85)) XML element is required only if the [**HardwareIDList**](/previous-versions/windows/hardware/metadata/ff546121(v=vs.85)) element is not specified in the [**PackageInfo**](/previous-versions/windows/hardware/metadata/ff549574(v=vs.85)) XML data. If it is specified, the **ModelIDList** element must contain one or more [**ModelID**](/previous-versions/windows/hardware/metadata/ff549295(v=vs.85)) elements to specify the unique model ID for each function that the device supports.

If the [**PackageInfo**](/previous-versions/windows/hardware/metadata/ff549574(v=vs.85)) XML data contains the [**HardwareIDList**](/previous-versions/windows/hardware/metadata/ff546121(v=vs.85)) and [**ModelIDList**](/previous-versions/windows/hardware/metadata/ff549303(v=vs.85)) elements, the operating system uses the following rules when it determines whether a device is specified by a device metadata package:

-   If the device has a model ID, the operating system does not search for a match in the **HardwareIDList** element.

-   Otherwise, the operating system searches the **HardwareIDList** element for a match of the hardware ID for the device.

If your device metadata package supports multiple device models or model IDs, you can specify a [**ModelID**](/previous-versions/windows/hardware/metadata/ff549295(v=vs.85)) element for each device model.

The following is an example of a [**ModelIDList**](/previous-versions/windows/hardware/metadata/ff549303(v=vs.85)) element that has multiple **ModelID** elements:

```cpp
<ModelIDList>
<ModelID>825AAB98-18EE-4FE2-9472-197D1D00FE31</ModelID>
<ModelID>23F64715-AC4A-4DC4-B554-C8D56E43FE8B</ModelID>
</ModelIDList>
```

For more information about the format requirements of the **ModelID** XML element, see [**ModelID**](/previous-versions/windows/hardware/metadata/ff549295(v=vs.85)).

 

