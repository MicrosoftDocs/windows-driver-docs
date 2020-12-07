---
title: Introduction to the Windows Hardware Error Architecture (WHEA)
description: Introduction to the Windows Hardware Error Architecture (WHEA)
keywords:
- Windows Hardware Error Architecture WDK , about Windows Hardware Error Architecture
- WHEA WDK , about Windows Hardware Error Architecture
- hardware errors WDK WHEA , about Windows Hardware Error Architecture
- errors WDK WHEA , about Windows Hardware Error Architecture
- source information WDK WHEA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to the Windows Hardware Error Architecture

The Windows Hardware Error Architecture (WHEA), introduced with Windows Vista, extends previous hardware error reporting mechanisms and brings them together as components of a coherent hardware error infrastructure. WHEA takes advantage of the additional hardware error information available in today's hardware devices and integrates much more closely with the system firmware.

As a result, WHEA provides the following benefits:

-   Allows for more extensive error data to be made available in a standard error record format for determining the root cause of hardware errors.

-   Provides mechanisms to help recover from hardware errors to avoid causing a bug check when a hardware error is nonfatal.

-   Supports user-mode error management applications and enables advanced system health monitoring through Event Tracing for Windows (ETW) events and by providing an API for error management and control.

-   Provides extensibility, so that as hardware vendors add new and better hardware error reporting mechanisms to their devices, WHEA allows the operating system to accommodate the new mechanisms.

