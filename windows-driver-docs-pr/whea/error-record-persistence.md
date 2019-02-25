---
title: Error Record Persistence
description: Error Record Persistence
ms.assetid: fe43f93a-59bd-4158-ad00-8fef595528cb
keywords:
- Windows Hardware Error Architecture WDK , error record persistence
- WHEA WDK , error record persistence
- errors WDK WHEA , error record persistence
- error record persistence WDK WHEA
- saving hardware error records WDK WHEA
- storing hardware error records WDK WHEA
- writing hardware error records WDK WHEA
- retrieving hardware error records WDK WHEA
- reading hardware error records WDK WHEA
- hardware errors WDK WHEA , error record persistence
- platform-specific hardware error driver plug-ins WDK WHEA , error record persistence
- PSHED plug-ins WDK WHEA , error record persistence
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Error Record Persistence


The PSHED exposes an interface to the operating system that allows the Windows kernel to save and retrieve error records to or from the system's persistent data storage. Error source control operations include the following:

-   Write an error record to the persistent data storage

-   Read an error record from the persistent data storage

-   Clear an error record from the persistent data storage

If a hardware platform does not implement hardware or firmware that is compatible with the error record persistence mechanisms that are supported by the PSHED, the platform vendor must implement a PSHED plug-in that participates in error record persistence. This PSHED plug-in interfaces with the error record persistence mechanism that is implemented by the hardware platform.

For more information about how to implement a PSHED plug-in that participates in error record persistence, see [Participating in Error Record Persistence](participating-in-error-record-persistence.md).

For more information about error record persistence, see [Error Record Persistence Mechanism](error-record-persistence-mechanism.md).

 

 




