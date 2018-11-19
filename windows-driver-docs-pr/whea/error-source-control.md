---
title: Error Source Control
description: Error Source Control
ms.assetid: f73d9006-a7e7-4a0d-9654-004f53286743
keywords:
- Windows Hardware Error Architecture WDK , error source control
- WHEA WDK , error source control
- hardware errors WDK WHEA , error source control
- errors WDK WHEA , error source control
- platform-specific hardware error driver plug-ins WDK WHEA , error source control
- PSHED plug-ins WDK WHEA , error source control
- error source control WDK WHEA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Error Source Control


The PSHED exposes an interface to the operating system that allows the Windows kernel to control each of the error sources that are implemented by the hardware platform. Error source control operations include the following:

-   Enabling or disabling an error source.

-   Setting or clearing mask bits that are associated with an error source. These mask bits enable or disable specific behaviors of the error source.

-   Setting severity bits that are associated with an error source. These severity bits control the severity level at which particular hardware errors are reported to the operating system.

-   Setting threshold parameters that are associated with an error source.

The Windows kernel calls into the PSHED to configure an error source in response to an error source control request by a WHEA management application. The PSHED supports error source control operations for the standard error sources that the PSHED discovers. If a PSHED plug-in is implemented that participates in [error source discovery](error-source-discovery.md) and reports additional error sources to the operating system that the PSHED does not support, the PSHED plug-in must also participate in error source control to support the error source control operations for these additional error sources. A PSHED plug-in can also optionally participate in error source control to override the way that the PSHED controls one or more of the standard error sources.

For more information about how to implement a PSHED plug-in that participates in error source control, see [Participating in Error Source Control](participating-in-error-source-control.md).

User-mode management applications control the error sources by calling the [WHEA Management API](https://msdn.microsoft.com/library/windows/hardware/ff560556). For more information about how to implement WHEA management applications, see [WHEA Management Applications](whea-management-applications.md).

 

 




