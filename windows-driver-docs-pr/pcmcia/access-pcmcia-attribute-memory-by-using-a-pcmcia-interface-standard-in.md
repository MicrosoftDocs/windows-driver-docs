---
title: Access Memory by Using PCMCIA_INTERFACE_STANDARD
description: Access PCMCIA Attribute Memory by Using a PCMCIA_INTERFACE_STANDARD Interface
ms.assetid: cd73a8da-1441-4e95-a955-97235ad091ce
keywords:
- PCMCIA_INTERFACE_STANDARD
- attribute memory WDK PCMCIA bus , PCMCIA_INTERFACE_STANDARD interface
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Access PCMCIA Attribute Memory by Using a PCMCIA\_INTERFACE\_STANDARD Interface





This section describes how a driver can use a PCMCIA\_INTERFACE\_STANDARD interface to access attribute memory.

The PCMCIA interface standard is provided primarily for memory card drivers and file systems.

A driver can use the [**PCMCIA\_MODIFY\_MEMORY\_WINDOW**](https://msdn.microsoft.com/library/windows/hardware/ff537610) interface routine supported by the PCMCIA\_INTERFACE\_STANDARD interface. PCMCIA\_MODIFY\_MEMORY\_WINDOW sets the attributes of a memory window for a PCMCIA memory card. The memory window is mapped by the PCMCIA bus driver. Note that this routine does not provide a permanent window, it only modifies the current settings for an existing window. In addition, settings are not persistent over a change in the system power state.

For more information, see [PCMCIA\_INTERFACE\_STANDARD Interface for Memory Cards](https://msdn.microsoft.com/library/windows/hardware/ff537606).

 

 





