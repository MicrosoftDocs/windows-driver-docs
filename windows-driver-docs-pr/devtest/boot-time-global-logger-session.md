---
title: Boot-Time Global Logger Session
description: Boot-Time Global Logger Session
ms.assetid: f1f5bbee-48bd-4e4d-8849-9d21a4f85d44
keywords:
- boot-time tracing WDK , Global Logger trace session
- Global Logger trace session WDK
- boot-time Global Logger trace session WDK
- Global Logger trace session WDK , about Global Logger sessions
- boot-time Global Logger trace session WDK , about Global Logger sessions
- tracing WDK , during boot
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Boot-Time Global Logger Session


You can create a Global Logger trace session that traces Windows kernel events during system boot. This method combines the features of the [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md), which traces the kernel, with those of the [Global Logger trace session](global-logger-trace-session.md), which traces events that take place during system boot.

The procedure described in this section creates a Global Logger trace session, and then adds a special registry entry, **EnableKernelFlags**. The presence of the **EnableKernelFlags** entry, with a valid value, converts the Global Logger trace session to an NT Kernel Logger trace session. The valid values for **EnableKernelFlags** are taken from the values of the **EnableFlags** member of the [**EVENT\_TRACE\_PROPERTIES**](https://msdn.microsoft.com/library/windows/desktop/aa363784) structure. The procedure is described in [How to Create a Boot-Time Global Logger Session](how-to-create-a-boot-time-global-logger-session.md).

Trace providers, including drivers, can log trace messages to this type of session. The procedure for doing so is described in [Logging to the Global Logger Session](logging-to-the-global-logger-session.md).

This section includes:

[How to Create a Boot-Time Global Logger Session](how-to-create-a-boot-time-global-logger-session.md)

 

 





