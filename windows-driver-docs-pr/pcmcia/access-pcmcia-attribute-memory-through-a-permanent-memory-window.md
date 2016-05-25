---
title: Access PCMCIA Attribute Memory Through a Permanent Memory Window
description: Access PCMCIA Attribute Memory Through a Permanent Memory Window
MS-HAID:
- 'pamch1\_be9c70d2-ba3a-4920-bedd-199654ba565b.xml'
- 'PCMCIA.access\_pcmcia\_attribute\_memory\_through\_a\_permanent\_memory\_window'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 866851b9-8e39-4480-9f22-dc2a2eb80ce0
keywords: ["attribute memory WDK PCMCIA bus , permanent-assigned memory window", "permanent memory window WDK PCMCIA bus"]
---

# Access PCMCIA Attribute Memory Through a Permanent Memory Window


## <a href="" id="ddk-access-pcmcia-attribute-memory-through-a-permanent-memory-window-k"></a>


This section describes how a PC Card or CardBus card driver can use a permanent-assigned memory window to access attribute memory.

A driver should use this method to support PCMCIA devices that implement device registers in attribute memory. In such cases, a driver's ISR typically needs fast direct access to the device registers while running at IRQL DIRQL.

Drivers can use this method while running at IRQL DIRQL.

Setup and the Plug and Play manager support the [**INF DDInstall.LogConfigOverride section**](https://msdn.microsoft.com/library/windows/hardware/ff547339), which can force the Plug and Play manager to use the resources specified in a **PcCardConfig** entry. The **LogConfigOverride** section specifies a log config section that contains a **PcCardConfig** entry. Fields in the **PcCardConfig** entry specify the required memory resource, and that the memory resource is used for attribute memory.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BPCMCIA\buses%5D:%20Access%20PCMCIA%20Attribute%20Memory%20Through%20a%20Permanent%20Memory%20Window%20%20RELEASE:%20%285/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




