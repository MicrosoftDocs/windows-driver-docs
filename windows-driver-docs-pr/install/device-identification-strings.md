---
title: Device Identification Strings
description: The Plug and Play (PnP) manager and other device installation components use device identification strings to identify devices that are installed in a computer.
ms.assetid: dae23185-63d9-4a0f-9786-c7fa66368826
keywords: ["compatible IDs WDK device installations", "device IDs WDK device installations", "device instance IDs WDK device installations", "driver nodes WDK device installations", "hardware IDs WDK device installations", "instance IDs WDK device installations", "Device setup WDK device installations , device identification strings", "device installations WDK , device identification strings", "installing devices WDK , device identification strings"]
---

# Device Identification Strings


The Plug and Play (PnP) manager and other [device installation components](https://msdn.microsoft.com/library/windows/hardware/ff541277) use device identification strings to identify devices that are installed in a computer.

## <a href="" id="ddk-device-identification-strings-dg"></a>


Windows uses the following device identification strings to locate the information (INF) file that best matches the device. These strings are reported by a device's [*enumerator*](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-enumerator):

-   [Hardware IDs](hardware-ids.md)

-   [Compatible IDs](compatible-ids.md)

Windows tries to find a match for one of the hardware IDs or compatible IDs. For more information about how Windows uses these IDs to match a device to an INF file, and how to specify IDs in an INF file, see [How Windows Selects Drivers](how-setup-selects-drivers.md).

In addition to using the preceding IDs to identify devices, the PnP manager uses the following IDs to uniquely identify instances of each device that are installed in a computer:

-   [Instance IDs](instance-ids.md)

-   [Device instance IDs](device-instance-ids.md)

Starting with Windows 7, the PnP manager uses the [Container ID](container-ids.md) device identification string to group one or more device nodes ([*devnodes*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) that were enumerated from each instance of a physical device installed in a computer:

Each enumerator customizes its device IDs, hardware IDs, and compatible IDs to uniquely identify the device that it enumerates. In addition, each enumerator has its own policy to identify hardware IDs and compatible IDs. For more information about hardware ID and compatible ID formats for most of the system buses, see [Device Identifier Formats](device-identifier-formats.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Device%20Identification%20Strings%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




