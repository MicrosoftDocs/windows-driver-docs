---
title: Calling a PCMCIA\_INTERFACE\_STANDARD Interface Routine
description: Calling a PCMCIA\_INTERFACE\_STANDARD Interface Routine
MS-HAID:
- 'mcch2\_051ca28a-f0dc-481e-ab30-476a555f56b8.xml'
- 'PCMCIA.calling\_a\_pcmcia\_interface\_standard\_interface\_routine'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 468d2037-a7d5-4851-9f41-d1e6c9006750
---

# Calling a PCMCIA\_INTERFACE\_STANDARD Interface Routine


## <a href="" id="ddk-calling-a-pcmcia-interface-standard-interface-routine-kg"></a>


This section describes how to call a PCMCIA\_INTERFACE\_STANDARD interface routine.

After a driver obtains an [PCMCIA\_INTERFACE\_STANDARD Interface Memory Card Routines](https://msdn.microsoft.com/library/windows/hardware/ff537607) structure from the PCMCIA bus driver, the driver can call the interface routines.

Each interface routine requires a context pointer. The driver must use the **Context** member value returned by the PCMCIA bus driver in the PCMCIA\_INTERFACE\_STANDARD structure. If the context pointer is not valid, the system behavior is not defined, and the system might halt.

The PCMCIA\_INTERFACE\_STANDARD interface routines can be called at IRQL &lt;= DISPATCH\_LEVEL. To maintain overall system performance, it is strongly recommended that a driver call these routines at IRQL &lt; DISPATCH\_LEVEL. Calling an interface routine at IRQL DISPATCH\_LEVEL can cause the caller to block system operation for a significant period of time.

 

 





