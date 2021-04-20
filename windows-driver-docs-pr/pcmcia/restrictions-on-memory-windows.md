---
title: Restrictions on Memory Windows
description: Restrictions on Memory Windows
keywords:
- PCMCIA WDK buses , memory windows
- memory windows WDK PCMCIA bus
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Restrictions on Memory Windows





This section describes the restrictions imposed by Windows 2000 and later operating systems on memory windows of PCMCIA memory cards.

The resource requirements of a PCMCIA memory card are normally specified by the bus driver when it enumerates the device at the request of the Plug and Play manager. Specific memory windows can also be specified in an [**INF DDInstall.LogConfigOverride section**](../install/inf-ddinstall-logconfigoverride-section.md) of a device driver's INF file. A maximum of two memory windows can be requested for a PCMCIA memory card.

 

