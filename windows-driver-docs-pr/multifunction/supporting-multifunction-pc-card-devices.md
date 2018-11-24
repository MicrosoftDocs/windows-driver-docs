---
title: Supporting Multifunction PC Card Devices
description: Supporting Multifunction PC Card Devices
ms.assetid: 4da3b99c-0731-41b5-9f67-29c7e181342f
keywords:
- multifunction devices WDK , PC Card
- PC Card multifunction standard WDK
- resource maps WDK multifunction devices
- 16-bit PC Card multifunction devices WDK
- configuration registers WDK multifunction devices
- registers WDK multifunction devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Multifunction PC Card Devices





The PC Card multifunction standard specifies that a multifunction device has a set of configuration registers in attribute memory for each function. These registers allow the PCMCIA bus driver to, for example, enable each function independently and define a range of I/O resources that are exclusive to each function. The standard also specifies that a multifunction device contains, in attribute memory, the address of each set of configuration registers. These addresses enable the PCMCIA bus driver to program the configuration registers.

If a 16-bit PC Card device implements the PC Card multifunction standard completely and correctly, the vendor of such a device has minimal INF and driver requirements to ensure that the device is configured properly on an NT-based system. See [Supporting PC Cards That Conform to the Multifunction Standard](supporting-pc-cards-that-conform-to-the-multifunction-standard.md) for more information.

If a 16-bit PC Card device does not fully implement the PC Card multifunction standard, the vendor must provide the missing information in an INF file. There are two ways that a multifunction PC Card device might fail to implement the multifunction standard:

1.  The device implements a set of multifunction configuration registers per function but does not contain the locations of all sets of registers in its attribute memory.

2.  The device does not implement a set of multifunction configuration registers per function.

If a device has the limitations listed above, the PCMCIA bus driver can program the configuration registers if the device's INF has the necessary information in *DDInstall*.**LogConfigOverride** section(s). See the following sections for further information:

[Supporting PC Cards That Have Incomplete Configuration Register Addresses](supporting-pc-cards-that-have-incomplete-configuration-register-addres.md)

[Supporting PC Cards That Have Incomplete Configuration Registers](supporting-pc-cards-that-have-incomplete-configuration-registers.md)

Cardbus devices essentially follow the PCI multifunction rules. See [Supporting Multifunction PCI Devices](supporting-multifunction-pci-devices.md).

 

 




