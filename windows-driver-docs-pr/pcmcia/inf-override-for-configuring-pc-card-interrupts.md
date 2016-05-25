---
title: INF Override for Configuring PC Card Interrupts
description: INF Override for Configuring PC Card Interrupts
MS-HAID:
- 'mcch2\_d5922a79-1e83-4f58-b4fc-9c67322cbb52.xml'
- 'PCMCIA.inf\_override\_for\_configuring\_pc\_card\_interrupts'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 90c951c4-0106-426a-b650-aeb93b893206
keywords: ["IRQ routing WDK PCMCIA bus", "PCMCIA WDK buses , IRQ routing", "PC Cards WDK PCMCIA bus", "interrupts WDK PCMCIA bus", "PCI interrupts WDK PCMCIA bus", "ISA interrupts WDK PCMCIA bus", "INF files WDK PCMCIA bus", "PcmciaExclusiveIrq"]
---

# INF Override for Configuring PC Card Interrupts


## <a href="" id="ddk-inf-override-for-configuring-pc-card-interrupts-kg"></a>


If the operating system routes an interrupt from a 16-bit PC Card that does not support sharable PCI interrupts, then the system might stop working. To prevent this from happening, you should indicate that the card does not support sharable interrupts by placing a PcmciaExclusiveIrq directive in the card's INF file.

For example, assume you have a modem whose driver contains an interrupt service routine (ISR) that was not designed to support interrupt sharing. You can direct the operating system to assign a fixed ISA interrupt to the modem by adding the following line to an AddReg section in the modem's INF file:

`HKR,,PcmciaExclusiveIrq,0x00010001,1`

Note, however, that once you put the PcmciaExclusiveIrq directive in a device's INF file, the device will not function with any controller or bridge that does not have access to ISA interrupt.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BPCMCIA\buses%5D:%20INF%20Override%20for%20Configuring%20PC%20Card%20Interrupts%20%20RELEASE:%20%285/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




