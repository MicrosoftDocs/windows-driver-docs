---
title: Generic Identifiers
description: Generic Identifiers
ms.assetid: 75dab2fc-e897-4bce-b719-98ad89817fca
keywords: ["device identification strings WDK , generic", "identification strings WDK device , generic", "identifiers WDK device , generic", "generic device identifiers WDK device installations"]
---

# Generic Identifiers


## <a href="" id="ddk-generic-identifiers-dg"></a>


Most, but not all, identifier strings are bus-specific. The Plug and Play (PnP) manager also supports a set of generic device identifiers for devices that can appear on many different buses. These identifiers are of the form:

\*PNPd(4)

where d(4) is a 4-digit, hexadecimal type identifier.

In the case of the PCMCIA bus, compatible IDs are formatted in this manner (see the following discussion of the PCMCIA bus). You can find the official list of these identifiers in [Plug and Play Vendor IDs and Device IDs](http://go.microsoft.com/fwlink/p/?linkid=49039) on the Microsoft Download Center. This information is also published in the Microsoft MSDN.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Generic%20Identifiers%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




