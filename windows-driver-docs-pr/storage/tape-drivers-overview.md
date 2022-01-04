---
title: Introduction to Tape Drivers
description: Tape Drivers
keywords:
- tape drivers WDK storage
- storage tape drivers WDK
- storage drivers WDK , tape drivers
- tape drivers WDK storage , about tape drivers
- storage tape drivers WDK , about tape drivers
ms.date: 12/15/2019
---

# Introduction to Tape Drivers

NT-based operating systems provide a generic tape class driver that handles operating system-specific and device-independent tape tasks. The tape class driver is provided as a kernel-mode DLL. To support a new tape device or family of tape devices, a driver writer creates a device-specific tape miniclass driver that links dynamically to the system-supplied tape class driver.

If a tape miniclass driver calls only routines in the tape class driver, the miniclass driver can be portable across Microsoft operating systems that support Win32 applications and provide a tape class driver that uses the tape miniclass interface. A tape miniclass driver includes the header file *minitape.h*.

An existing tape miniclass driver must be modified to support one new entry point, *TapeMiniGetMediaTypes*, in order to build and run under Windows 2000 and later operating systems. No other modifications are required. The system-supplied tape class driver, together with the system-supplied storage port driver, handles Plug and Play and power management requests on behalf of a tape miniclass driver.

This section describes the support provided by the operating system-specific tape class driver and provides guidelines for writing a new tape miniclass driver.

- See [Tape Class Driver Routines](tape-class-driver-routines.md) and [Tape Miniclass Driver Routines](tape-miniclass-driver-routines.md) for details on the routines in the tape class and tape miniclass drivers.

- See [Device Configurations and Layered Drivers](../kernel/device-configurations-and-layered-drivers.md) for a description of the storage device driver layers.
