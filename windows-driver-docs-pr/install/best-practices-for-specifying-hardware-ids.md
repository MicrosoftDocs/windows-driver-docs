---
title: Best Practices for Specifying Hardware IDs
description: Best Practices for Specifying Hardware IDs
ms.date: 04/20/2017
---

# Best Practices for Specifying Hardware IDs


The [**HardwareIDList**](/previous-versions/windows/hardware/metadata/ff546121(v=vs.85)) element specifies one or more hardware identification strings for the device. Each string is specified by a [**HardwareID**](/previous-versions/windows/hardware/metadata/ff546114(v=vs.85)) XML element. The operating system first queries the device for its identification string and then loads the device metadata package that has a **HardwareID** value that matches this string.

Each **HardwareID** element value must be a [hardware ID](hardware-ids.md) that is unique to the device. You must not use the [compatible ID](compatible-ids.md) for the device, such as USB Class ID, 'HID_DEVICE', or 'HID_DEVICE_SYSTEM_KEYBOARD'.

You must ensure that each [**HardwareID**](/previous-versions/windows/hardware/metadata/ff546114(v=vs.85)) element that is specified in the metadata package has a value that accurately correlates to the [hardware ID](hardware-ids.md) that the physical device reports. For example, if a hardware ID is reused across a family of physical devices, the device metadata package that specifies that **HardwareID** element value is associated with the entire family of devices.

This section includes the following topics on best practices for specifying [hardware IDs](hardware-ids.md) for certain types of devices:

[Specifying Hardware IDs for a Bluetooth Device](specifying-hardware-ids-for-a-bluetooth-device.md)

[Specifying Hardware IDs for a Computer](specifying-hardware-ids-for-a-computer.md)

[Specifying Hardware IDs for a Multifunction Device](specifying-hardware-ids-for-a-multifunction-device.md)

For more information about the format requirements of the **HardwareID** XML element, see [**HardwareID**](/previous-versions/windows/hardware/metadata/ff546114(v=vs.85)).

 

