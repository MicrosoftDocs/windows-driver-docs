---
title: Identifiers for ISAPNP Devices
description: Identifiers for ISAPNP Devices
ms.assetid: 67337bd6-3b5f-41a7-b50d-bf3587f243e8
keywords: ["device identification strings WDK , ISAPNP devices", "identification strings WDK device , ISAPNP devices", "identifiers WDK device , ISAPNP devices", "ISAPNP device identifiers WDK device installations", "hardware IDs WDK device installations"]
---

# Identifiers for ISAPNP Devices


## <a href="" id="ddk-identifiers-for-isapnp-devices-dg"></a>


Every ISAPNP card supports a readable resource data structure that describes the resources supported and those requested by the card. This structure supports the concept of multiple functions (or "logical devices") for ISA card. A separate set of "tags" or "descriptors" are associated with each function of the card. Using this tag information, the ISAPNP enumerator constructs two hardware identifiers, formatted as:

ISAPNP\\m(3)d(4)

\*m(3)n(4)

where *m(3)d(4)* together make up an EISA-style identifier for the device--three letters to identify the manufacturer and 4 hexadecimal digits to identify the particular device.

The following pair of hardware IDs might be produced by a specific function on a multifunction card:

ISAPNP\\CSC6835\_DEV0000

\*CSC0000

The first of the two hardware IDs is the device ID. If the device in question is one function of a multifunction card, the device ID takes this form:

ISAPNP\\m(3)d(4)\_DEVn(4)

where *n(4)* is the decimal index (with leading zeros) of the function.

The second of the two hardware identifiers is also a compatible ID. The ISAPNP enumerator generates one or more compatible IDs the first of which is always the second hardware ID. The first three characters, *m(3)*, that follow the "\*" in an ISAPNP-compatible ID are frequently "PNP." For example, the compatible ID for a serial port might be this:

PNP0501

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Identifiers%20for%20ISAPNP%20Devices%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




