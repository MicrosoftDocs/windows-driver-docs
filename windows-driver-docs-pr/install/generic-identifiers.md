---
title: Generic Identifiers
description: Generic Identifiers
ms.assetid: 75dab2fc-e897-4bce-b719-98ad89817fca
keywords:
- device identification strings WDK , generic
- identification strings WDK device , generic
- identifiers WDK device , generic
- generic device identifiers WDK device installations
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Generic Identifiers


## <a href="" id="ddk-generic-identifiers-dg"></a>


Most, but not all, identifier strings are bus-specific. The Plug and Play (PnP) manager also supports a set of generic device identifiers for devices that can appear on many different buses. These identifiers are of the form:

\*PNPd(4)

where d(4) is a 4-digit, hexadecimal type identifier.

In the case of the PCMCIA bus, compatible IDs are formatted in this manner (see the following discussion of the PCMCIA bus). You can find the official list of these identifiers in [Plug and Play Vendor IDs and Device IDs](http://go.microsoft.com/fwlink/p/?linkid=49039) on the Microsoft Download Center. This information is also published in the Microsoft MSDN.

 

 





