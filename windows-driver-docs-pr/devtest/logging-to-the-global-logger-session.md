---
title: Logging to the Global Logger Session
description: Logging to the Global Logger Session
keywords:
- tracing during boot WDK , Global Logger trace session
- boot-time tracing WDK , Global Logger trace session
- Global Logger trace session WDK , logging
- boot-time Global Logger trace session WDK , logging
- logs WDK tracing during boot
ms.date: 04/20/2017
---

# Logging to the Global Logger Session


You can trace the actions of a driver or other trace provider during system boot by configuring the driver to log to the [Global Logger trace session](global-logger-trace-session.md), a trace session that runs during system boot. The driver must be instrumented for software tracing.

Although the Global Logger trace session does not send enable notification to providers, the method described in this section adds code to the driver that lets the driver determine when it is enabled for tracing to the Global Logger session.

In Windows Vista and later versions of Windows, the preferred method of boot tracing is to use an AutoLogger a new feature specifically designed for boot tracing. For information about tracing the activity of a driver with the AutoLogger, see [Configuring and Starting an AutoLogger Session](/windows/win32/etw/configuring-and-starting-an-autologger-session).

This section includes:

[How to Log to the Global Logger Session](how-to-log-to-the-global-logger-session.md)

[Example: Global Logger Provider](example--global-logger-provider.md)

 

