---
title: Handling Hardware Resources
description: A system's hardware resources are the I/O ports interrupt vectors direct memory access (DMA) channels and other communication paths that must be assigned to each device that is connected to the system.
ms.assetid: 30ceb7db-f11e-498c-a0c0-a63218627c6e
keywords: ["PnP WDK KMDF hardware resources", "Plug and Play WDK KMDF hardware resources", "hardware resources WDK KMDF"]
---

# Handling Hardware Resources


A system's hardware resources are the I/O ports, interrupt vectors, direct memory access (DMA) channels, and other communication paths that must be assigned to each device that is connected to the system. The topics in this section describe how Kernel-Mode Driver Framework (KMDF) drivers negotiate hardware resource requirements for a device, review the proposed resource list, and then receive the assigned resources. This section also discusses how both KMDF and User-Mode Driver Framework (UMDF) drivers access and map assigned resources.

## <a href="" id="ddk-hardware-resources-for-framework-based-drivers-df"></a>


## In this section


-   [Introduction to Hardware Resources](introduction-to-hardware-resources.md)
-   [Framework Objects for Hardware Resources](framework-objects-for-hardware-resources.md)
-   [Creating a Resource Requirements List](creating-a-resource-requirements-list.md)
-   [Modifying a Resource Requirements List](modifying-a-resource-requirements-list.md)
-   [Creating a Resource List for a Boot Configuration](creating-a-resource-list-for-a-boot-configuration.md)
-   [Modifying a Resource List](modifying-a-resource-list.md)
-   [Raw and Translated Resources](raw-and-translated-resources.md)
-   [Finding and Mapping Hardware Resources](finding-and-mapping-hardware-resources.md)
-   [Reading and Writing to Device Registers](reading-and-writing-to-device-registers.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Handling%20Hardware%20Resources%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




