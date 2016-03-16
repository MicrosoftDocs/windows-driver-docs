---
title: Handling Hardware Interrupts
description: The topics in this section describe how a Windows Driver Frameworks (WDF) driver creates framework interrupt objects to service hardware interrupts and how your driver synchronizes access to interrupt data buffers.
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 08460510-6e5f-4c02-8086-9caa9b4b4c2d
keywords: ["hardware interrupts WDK KMDF", "interrupts WDK KMDF", "framework based drivers WDK KMDF hardware interrupts", "kernel mode drivers WDK KMDF hardware interrupts", "KMDF WDK hardware interrupts", "Kernel Mode Driver Framework WDK hardware interrupts", "framework objects WDK KMDF interrupt objects", "interrupt objects WDK KMDF"]
---

# Handling Hardware Interrupts


The topics in this section describe how a Windows Driver Frameworks (WDF) driver creates framework interrupt objects to service hardware interrupts, and how your driver synchronizes access to interrupt data buffers.

## <a href="" id="ddk-handling-hardware-interrupts-df"></a>


## In this section


-   [Creating an Interrupt Object](creating-an-interrupt-object.md)
-   [Enabling and Disabling Interrupts](enabling-and-disabling-interrupts.md)
-   [Servicing an Interrupt](servicing-an-interrupt.md)
-   [Synchronizing Interrupt Code](synchronizing-interrupt-code.md)
-   [Supporting Passive-Level Interrupts](supporting-passive-level-interrupts.md)
-   [Using an Interrupt to Wake a Device](using-an-interrupt-to-wake-a-device.md)
-   [Handling Active-Both Interrupts](handling-active-both-interrupts.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Handling%20Hardware%20Interrupts%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




