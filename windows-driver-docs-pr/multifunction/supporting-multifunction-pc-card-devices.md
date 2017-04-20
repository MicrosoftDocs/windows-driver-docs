---
title: Supporting Multifunction PC Card Devices
author: windows-driver-content
description: Supporting Multifunction PC Card Devices
ms.assetid: 4da3b99c-0731-41b5-9f67-29c7e181342f
keywords:
- multifunction devices WDK , PC Card
- PC Card multifunction standard WDK
- resource maps WDK multifunction devices
- 16-bit PC Card multifunction devices WDK
- configuration registers WDK multifunction devices
- registers WDK multifunction devices
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting Multifunction PC Card Devices


## <a href="" id="ddk-supporting-multifunction-pc-card-devices-dg"></a>


The PC Card multifunction standard specifies that a multifunction device has a set of configuration registers in attribute memory for each function. These registers allow the PCMCIA bus driver to, for example, enable each function independently and define a range of I/O resources that are exclusive to each function. The standard also specifies that a multifunction device contains, in attribute memory, the address of each set of configuration registers. These addresses enable the PCMCIA bus driver to program the configuration registers.

If a 16-bit PC Card device implements the PC Card multifunction standard completely and correctly, the vendor of such a device has minimal INF and driver requirements to ensure that the device is configured properly on an NT-based system. See [Supporting PC Cards That Conform to the Multifunction Standard](supporting-pc-cards-that-conform-to-the-multifunction-standard.md) for more information.

If a 16-bit PC Card device does not fully implement the PC Card multifunction standard, the vendor must provide the missing information in an INF file. There are two ways that a multifunction PC Card device might fail to implement the multifunction standard:

1.  The device implements a set of multifunction configuration registers per function but does not contain the locations of all sets of registers in its attribute memory.

2.  The device does not implement a set of multifunction configuration registers per function.

If a device has the limitations listed above, the PCMCIA bus driver can program the configuration registers if the device's INF has the necessary information in *DDInstall*.**LogConfigOverride** section(s). See the following sections for further information:

[Supporting PC Cards That Have Incomplete Configuration Register Addresses](supporting-pc-cards-that-have-incomplete-configuration-register-addres.md)

[Supporting PC Cards That Have Incomplete Configuration Registers](supporting-pc-cards-that-have-incomplete-configuration-registers.md)

Cardbus devices essentially follow the PCI multifunction rules. See [Supporting Multifunction PCI Devices](supporting-multifunction-pci-devices.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bmultifunc\multifunc%5D:%20Supporting%20Multifunction%20PC%20Card%20Devices%20%20RELEASE:%20%288/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


