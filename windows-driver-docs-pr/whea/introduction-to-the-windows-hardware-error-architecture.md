---
title: Introduction to the Windows Hardware Error Architecture
description: Introduction to the Windows Hardware Error Architecture
ms.assetid: 5a0bbf8c-d644-4a64-9a7e-400d5de2c8fa
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


In versions of the Microsoft Windows operating system prior to Windows Vista, the operating system supported several unrelated mechanisms for reporting hardware errors. These mechanisms provided little support for error recovery. For uncorrected errors, the operating system simply generated a bug check and then recorded some of the available error information in the system event log after the system was restarted.

The ability to determine the root cause of hardware errors was hindered by the limited amount of error information recorded in the system event log. The operating system was not capable of preventing system crashes caused by hardware errors because there was no common error record format and little support for hardware error management applications.

The Windows Hardware Error Architecture (WHEA), introduced with Windows Vista, extends the previous hardware error reporting mechanisms and brings them together as components of a coherent hardware error infrastructure. WHEA takes advantage of the additional hardware error information available in today's hardware devices and integrates much more closely with the system firmware.

As a result, WHEA provides the following benefits:

-   Allows for more extensive error data to be made available in a standard error record format for determining the root cause of hardware errors.

-   Provides mechanisms to help recover from hardware errors to avoid causing a bug check when a hardware error is nonfatal.

-   Supports user-mode error management applications and enables advanced system health monitoring through Event Tracing for Windows (ETW) events and by providing an API for error management and control.

-   Provides extensibility, so that as hardware vendors add new and better hardware error reporting mechanisms to their devices, WHEA allows the operating system to gracefully accommodate the new mechanisms.

 

 




