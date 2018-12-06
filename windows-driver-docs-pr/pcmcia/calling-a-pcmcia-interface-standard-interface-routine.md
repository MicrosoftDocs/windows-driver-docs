---
title: Calling a PCMCIA_INTERFACE_STANDARD Interface Routine
description: Calling a PCMCIA_INTERFACE_STANDARD Interface Routine
ms.assetid: 468d2037-a7d5-4851-9f41-d1e6c9006750
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Calling a PCMCIA\_INTERFACE\_STANDARD Interface Routine





This section describes how to call a PCMCIA\_INTERFACE\_STANDARD interface routine.

After a driver obtains an [PCMCIA\_INTERFACE\_STANDARD Interface Memory Card Routines](https://msdn.microsoft.com/library/windows/hardware/ff537607) structure from the PCMCIA bus driver, the driver can call the interface routines.

Each interface routine requires a context pointer. The driver must use the **Context** member value returned by the PCMCIA bus driver in the PCMCIA\_INTERFACE\_STANDARD structure. If the context pointer is not valid, the system behavior is not defined, and the system might halt.

The PCMCIA\_INTERFACE\_STANDARD interface routines can be called at IRQL &lt;= DISPATCH\_LEVEL. To maintain overall system performance, it is strongly recommended that a driver call these routines at IRQL &lt; DISPATCH\_LEVEL. Calling an interface routine at IRQL DISPATCH\_LEVEL can cause the caller to block system operation for a significant period of time.

 

 





