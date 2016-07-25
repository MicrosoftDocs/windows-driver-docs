---
title: Best Practices for Specifying Hardware IDs
description: Best Practices for Specifying Hardware IDs
ms.assetid: 95dcf1b1-b2cd-473f-9660-a91fda20ffc2
---

# Best Practices for Specifying Hardware IDs


The [**HardwareIDList**](https://msdn.microsoft.com/library/windows/hardware/ff546121) element specifies one or more hardware identification strings for the device. Each string is specified by a [**HardwareID**](https://msdn.microsoft.com/library/windows/hardware/ff546114) XML element. The operating system first queries the device for its identification string and then loads the device metadata package that has a **HardwareID** value that matches this string.

Each **HardwareID** element value must be a [hardware ID](hardware-ids.md) that is unique to the device. You must not use the [compatible ID](compatible-ids.md) for the device, such as USB Class ID, 'HID\_DEVICE', or 'HID\_DEVICE\_SYSTEM\_KEYBOARD'.

You must ensure that each [**HardwareID**](https://msdn.microsoft.com/library/windows/hardware/ff546114) element that is specified in the metadata package has a value that accurately correlates to the [hardware ID](hardware-ids.md) that the physical device reports. For example, if a hardware ID is reused across a family of physical devices, the device metadata package that specifies that **HardwareID** element value is associated with the entire family of devices.

This section includes the following topics on best practices for specifying [hardware IDs](hardware-ids.md) for certain types of devices:

[Specifying Hardware IDs for a Bluetooth Device](specifying-hardware-ids-for-a-bluetooth-device.md)

[Specifying Hardware IDs for a Computer](specifying-hardware-ids-for-a-computer.md)

[Specifying Hardware IDs for a Multifunction Device](specifying-hardware-ids-for-a-multifunction-device.md)

For more information about the format requirements of the **HardwareID** XML element, see [**HardwareID**](https://msdn.microsoft.com/library/windows/hardware/ff546114).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Best%20Practices%20for%20Specifying%20Hardware%20IDs%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




