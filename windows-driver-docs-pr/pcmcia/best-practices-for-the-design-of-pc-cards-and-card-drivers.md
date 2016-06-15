---
title: Best Practices for the Design of PC Cards and Card Drivers
description: Best Practices for the Design of PC Cards and Card Drivers
MS-HAID:
- 'mcch2\_f331b6fa-9e96-43e5-be44-8ebfb14b3fbb.xml'
- 'PCMCIA.best\_practices\_for\_the\_design\_of\_pc\_cards\_and\_card\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c3f31757-4063-4c68-ae19-1d8af98f81bc
keywords: ["IRQ routing WDK PCMCIA bus", "PCMCIA WDK buses , IRQ routing", "PC Cards WDK PCMCIA bus", "interrupts WDK PCMCIA bus", "PCI interrupts WDK PCMCIA bus", "ISA interrupts WDK PCMCIA bus"]
---

# Best Practices for the Design of PC Cards and Card Drivers


## <a href="" id="ddk-best-practices-for-the-design-of-pc-cards-and-card-drivers-kg"></a>


Vendors and developers should observe the following cautions in order to avoid problems related with interrupt sharing:

-   Driver developers should design drivers to support sharable PCI interrupts.

-   PC Card manufacturers should manufacture CardBus cards instead of 16-bit PC Cards, because they are PCI compliant.

-   All 16-bit PC Cards should support sharable PCI interrupts.

-   All 16-bit PC Cards should support the flexible allocation of I/O resources for devices that connect to them. In particular, cards should not request specific ranges of I/O space. Instead, they should request the amount of I/O space they require and allow the system to allocate the addresses flexibly.

-   Computer manufacturers should be aware that there are devices that require ISA IRQs, and should ensure that ISA IRQs are available to CardBus controllers in the system.

-   Computer manufacturers should ensure that the BIOS code sets CardBus controllers to PCIC mode.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BPCMCIA\buses%5D:%20Best%20Practices%20for%20the%20Design%20of%20PC%20Cards%20and%20Card%20Drivers%20%20RELEASE:%20%285/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




