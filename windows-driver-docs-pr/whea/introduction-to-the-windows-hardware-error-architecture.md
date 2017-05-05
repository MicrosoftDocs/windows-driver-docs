---
title: Introduction to the Windows Hardware Error Architecture
author: windows-driver-content
description: Introduction to the Windows Hardware Error Architecture
ms.assetid: 5a0bbf8c-d644-4a64-9a7e-400d5de2c8fa
keywords:
- Windows Hardware Error Architecture WDK , about Windows Hardware Error Architecture
- WHEA WDK , about Windows Hardware Error Architecture
- hardware errors WDK WHEA , about Windows Hardware Error Architecture
- errors WDK WHEA , about Windows Hardware Error Architecture
- source information WDK WHEA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Introduction%20to%20the%20Windows%20Hardware%20Error%20Architecture%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


