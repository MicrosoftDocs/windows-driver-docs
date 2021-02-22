---
title: Generic Identifiers
description: Generic Identifiers
keywords:
- device identification strings WDK , generic
- identification strings WDK device , generic
- identifiers WDK device , generic
- generic device identifiers WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Generic Identifiers





Most, but not all, identifier strings are bus-specific. The Plug and Play (PnP) manager also supports a set of generic device identifiers for devices that can appear on many different buses. These identifiers are of the form:

\*PNPd(4)

where d(4) is a 4-digit, hexadecimal type identifier.

In the case of the PCMCIA bus, compatible IDs are formatted in this manner (see the following discussion of the PCMCIA bus). You can find the official list of these identifiers in [Plug and Play Vendor IDs and Device IDs](https://go.microsoft.com/fwlink/p/?linkid=49039) on the Microsoft Download Center. see [Plug and Play ID - PNPID Reqeust](./plug-and-play-id---pnpid-request.md) for more information. 

 

