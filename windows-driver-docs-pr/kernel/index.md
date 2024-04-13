---
title: Kernel-Mode Driver Architecture Design Guide
description: Kernel-Mode Driver Architecture Design Guide
ms.assetid: 21c199f3-abc3-4607-a674-eb84b6c3c25a
keywords: ["kernel-mode drivers WDK , architecture", "kernel-mode drivers WDK"]
ms.date: 03/18/2022
ms.topic: article
---

# Kernel-Mode Driver Architecture Design Guide

>[!NOTE]
>For information about programming interfaces that your driver can implement or call, see the [Kernel-Mode Driver Reference](/windows-hardware/drivers/ddi/index).

This section includes general concepts to help you understand kernel-mode programming and describes specific techniques of kernel programming. For a general overview of Windows Drivers, see [Getting Started with Windows Drivers](../develop/getting-started-with-windows-drivers.md), which provides a general overview of Windows components, lists the types of device drivers used in Windows, discusses the goals of Windows device drivers, and discusses generic sample device drivers included in the kit.

This section contains conceptual information that describes and helps you build kernel-mode drivers.

- An  **Overview** containing:
  - [An overview of Windows Components](overview-of-windows-components.md)
  - [Design Goals for Kernel-Mode Drivers](design-goals-for-kernel-mode-drivers.md)
  - A catalogue of [Sample Kernel-Mode Drivers](sample-kernel-mode-drivers.md)
  - [Kernel Driver Development Best Practices](surface-team-driver-development-best-practices.md), as compiled by the Microsoft Surface team

- **Kernel-Mode Components** describes the primary kernel-mode managers and components of the Windows operating system.

  |Component|Description|
  |----|----|
  |**Managers**||
  |[Windows Kernel-Mode Object Manager](windows-kernel-mode-object-manager.md)|Manages *objects*: files, devices, synchronization mechanisms, registry keys, and so on.|
  |[Windows Kernel-Mode Memory Manager](windows-kernel-mode-memory-manager.md)|Manages physical memory for the operating system.|
  |[Windows Kernel-Mode Process and Thread Manager](windows-kernel-mode-process-and-thread-manager.md)|Handles the execution of all threads in a process.|
  |[Windows Kernel-Mode I/O Manager](windows-kernel-mode-i-o-manager.md)|Manages the communication between applications and the interfaces provided by device drivers.|
  |[Windows Kernel-Mode Plug and Play Manager](windows-kernel-mode-plug-and-play-manager.md)|A subsystem of the I/O manager, the Plug and Play (PnP) Manager enables a PC to recognize when a device is added to the system.|
  |[Windows Kernel-Mode Power Manager](windows-kernel-mode-power-manager.md)|Manages the orderly change in power status for all devices that support power state changes.|
  |[Windows Kernel-Mode Configuration Manager](windows-kernel-mode-configuration-manager.md)|Manages the registry, such as monitoring changes in the registry or registering callbacks on specific registry data.|
  |[Windows Kernel-Mode Kernel Transaction Manager](windows-kernel-mode-kernel-transaction-manager.md)|Implements transaction processing in kernel mode.|
  |[Windows Kernel-Mode Security Reference Monitor](windows-kernel-mode-security-reference-monitor.md)|Provides routines for your driver to work with access control.|
  |**Libraries**||
  |[Windows Kernel-Mode Kernel Library](windows-kernel-mode-kernel-library.md)|Implements the core functionality that everything else in the operating system depends upon. The Microsoft Windows kernel provides basic low-level operations such as scheduling threads or routing hardware interrupts.|
  |[Windows Kernel-Mode Executive Support Library](windows-kernel-mode-executive-support-library.md)|Refers to kernel-mode components that provide a variety of services to device drivers, including: object management, memory management, process and thread management, input/output management, and configuration management.|
  |[Windows Kernel-Mode Run-Time Library](windows-kernel-mode-run-time-library.md)|A set of common utility routines needed by various kernel-mode components.|
  |[Windows Kernel-Mode Safe String Library](windows-kernel-mode-safe-string-library.md)|A safe string library to provide greater security in kernel-mode development.|
  |[Windows Kernel-Mode DMA Library](windows-kernel-mode-dma-library.md)|A direct memory access (DMA) library for device driver developers.|
  |[Windows Kernel-Mode HAL Library](windows-kernel-mode-hal-library.md)|A hardware abstraction layer (HAL) for kernel-mode driver development.|
  |[Windows Kernel-Mode CLFS Library](windows-kernel-mode-clfs-library.md)|A transactional logging system, the Common Log File System (CLFS).|
  |[Windows Kernel-Mode WMI Library](windows-kernel-mode-wmi-library.md)|A general mechanism for managing components, called Windows Management Instrumentation (WMI).|

- [**Writing WDM Drivers**](writing-wdm-drivers.md) and [Introduction to WDM](introduction-to-wdm.md) provide information needed to write drivers using the Windows Driver Model (WDM).

- [**Device Objects**](introduction-to-device-objects.md) and the other topics in **Device Objects and Device Stacks** describe how the operating system represents devices by device objects.

- [**Memory Management for Windows Drivers**](managing-memory-for-drivers.md) illustrates how kernel-mode drivers allocate memory for purposes such as storing internal data, buffering data during I/O operations, and sharing memory with other kernel-mode and user-mode components.

- **Security** From [Controlling Device Access](controlling-device-access.md) and [Privileges](privileges.md) to [SDDL for Device objects](sddl-for-device-objects.md), ensure that your drivers are as secure as possible.

- [**Handling IRPs**](handling-irps.md) describes how kernel-mode drivers handle I/O request packets (IRPs).

- **DMA** Direct Memory Access (DMA) is a critical aspect of driver development, and [the topics in this node](introduction-to-adapter-objects.md) cover DMA from A to Z.

- [**Controller Objects**](introduction-to-controller-objects.md) represent a physical device controller with attached devices.

- [**Interrupt Service Routines (ISRs)**](introduction-to-interrupt-service-routines.md) handle interrupts for drivers of a physical device that receives interrupts.

- [**Message-Signaled Interrupts**](introduction-to-message-signaled-interrupts.md) trigger an interrupt by writing a value to a particular memory address.

- [**Deferred Procedure Calls (DPC Objects)**](introduction-to-dpc-objects.md) can be queued from ISRs and are executed at a later time and at a lower IRQL than the ISR.

- [**Plug and Play (PnP)**](introduction-to-plug-and-play.md) focuses on the system software support for PnP and how drivers use that support to implement PnP.

- [**Power Management**](introduction-to-power-management.md) describes the architecture that provides a comprehensive approach to system and device power management.

- [**Windows Management Instrumentation (WMI)**](implementing-wmi.md) are extensions to your kernel-mode driver, which enable your driver to become a WMI provider. A WMI provider makes measurement and instrumentation data available to WMI consumers, such as user-mode applications.

- [**Driver Programming Techniques**](using-nt-and-zw-versions-of-the-native-system-services-routines.md) Programming drivers in the kernel mode of Windows requires techniques that sometimes differ significantly from those of ordinary user-mode programming.

- [**Bulk memory volatile accessor functions (v3)**](bulk-memory-volatile-accessor-functions-v3.md) describes prerelease bulk memory volatile accessor functions that are available starting in Windows 11 Insider Preview.
