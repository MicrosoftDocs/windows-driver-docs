---
title: Identifiers for ISAPNP Devices
description: Identifiers for ISAPNP Devices
ms.assetid: 67337bd6-3b5f-41a7-b50d-bf3587f243e8
keywords:
- device identification strings WDK , ISAPNP devices
- identification strings WDK device , ISAPNP devices
- identifiers WDK device , ISAPNP devices
- ISAPNP device identifiers WDK device installations
- hardware IDs WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Identifiers for ISAPNP Devices





Every ISAPNP card supports a readable resource data structure that describes the resources supported and those requested by the card. This structure supports the concept of multiple functions (or "logical devices") for ISA card. A separate set of "tags" or "descriptors" are associated with each function of the card. Using this tag information, the ISAPNP enumerator constructs two hardware identifiers, formatted as:

ISAPNP\\m(3)d(4)

\*m(3)n(4)

where *m(3)d(4)* together make up an EISA-style identifier for the device--three letters to identify the manufacturer and 4 hexadecimal digits to identify the particular device.

The following pair of hardware IDs might be produced by a specific function on a multifunction card:

ISAPNP\\CSC6835_DEV0000

\*CSC0000

The first of the two hardware IDs is the device ID. If the device in question is one function of a multifunction card, the device ID takes this form:

ISAPNP\\m(3)d(4)_DEVn(4)

where *n(4)* is the decimal index (with leading zeros) of the function.

The second of the two hardware identifiers is also a compatible ID. The ISAPNP enumerator generates one or more compatible IDs the first of which is always the second hardware ID. The first three characters, *m(3)*, that follow the "\*" in an ISAPNP-compatible ID are frequently "PNP." For example, the compatible ID for a serial port might be this:

PNP0501

 

 





