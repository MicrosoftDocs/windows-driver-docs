---
title: Accessing Hardware and Handling Interrupts
description: Accessing Hardware and Handling Interrupts
ms.assetid: 25D526CF-7C37-4D10-B099-352933F92F98
---

# Accessing Hardware and Handling Interrupts


Starting in UMDF 1.11, UMDF drivers can retrieve hardware resources that the system has assigned to the device, directly read or write to device registers that the system has assigned and mapped to memory space or I/O port space, and connect and service hardware interrupts.

## In this section


-   [Enabling Hardware Access](enabling-hardware-access.md)
-   [Finding and Mapping Hardware Resources in UMDF 1.x Drivers](finding-and-mapping-hardware-resources-in-umdf-1-x-drivers.md)
-   [Reading and Writing to Device Registers in UMDF 1.x Drivers](reading-and-writing-to-device-registers-in-umdf-1-x-drivers.md)
-   [Handling Interrupts](handling-interrupts.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Accessing%20Hardware%20and%20Handling%20Interrupts%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




