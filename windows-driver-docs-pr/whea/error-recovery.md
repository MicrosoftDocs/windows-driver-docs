---
title: Error Recovery
description: Error Recovery
keywords:
- Windows Hardware Error Architecture WDK , error recovery
- WHEA WDK , error recovery
- hardware errors WDK WHEA , error recovery
- errors WDK WHEA , error recovery
- platform-specific hardware error driver plug-ins WDK WHEA , error recovery
- PSHED plug-ins WDK WHEA , error recovery
- error recovery WDK WHEA
ms.date: 03/03/2023
---

# Error Recovery


During the handling of a recoverable hardware error, the operating system attempts to recover from the error condition. First the operating system attempts to recover from the error condition on its own. Then the Windows kernel calls into the PSHED to give it an opportunity to perform any hardware operations that are required to recover from the error condition. If a PSHED plug-in is implemented that participates in error recovery, it is then called by the PSHED so that it can perform any additional platform-specific hardware operations that are required to fully recover from the error condition. Regardless of whether the operating system successfully recovers from the error condition on its own, the Windows kernel always calls the PSHED to ensure that the PSHED and any registered PSHED plug-in have the opportunity to update or modify the hardware state as necessary.

For more information about how to implement a PSHED plug-in that participates in error recovery, see [Participating in Error Recovery](participating-in-error-recovery.md).

 

 




