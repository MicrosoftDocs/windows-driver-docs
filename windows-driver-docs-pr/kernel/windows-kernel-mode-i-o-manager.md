---
title: Windows Kernel-Mode I/O Manager
description: Windows Kernel-Mode I/O Manager
ms.assetid: 8652f37d-0ece-4c08-9bce-499f0fedb0dd
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Windows Kernel-Mode I/O Manager


A computer consists of various devices that provide input and output (I/O) to and from the outside world. Typical devices are keyboards, mice, audio controllers, video controllers, disk drives, networking ports, and so on. Device drivers provide the software connection between the devices and the operating system. For this reason, I/O is very important to the device driver writer.

The Windows kernel-mode I/O manager manages the communication between applications and the interfaces provided by device drivers. Because devices operate at speeds that may not match the operating system, the communication between the operating system and device drivers is primarily done through I/O request packets (IRPs). These packets are similar to network packets or Windows message packets. They are passed from operating system to specific drivers and from one driver to another.

The Windows I/O system provides a layered driver model called stacks. Typically IRPs go from one driver to another in the same stack to facilitate communication. For example, a joystick driver would need to communicate to a USB hub, which in turn would need to communicate to a USB host controller, which would then need to communicate through a PCI bus to the rest of the computer hardware. The stack consists of joystick driver, USB hub, USB host controller, and the PCI bus. This communication is coordinated by having each driver in the stack send and receive IRPs.

It cannot be stressed enough that your driver must send and receive IRPs on a timely basis for the whole stack to operate efficiently. If your driver is part of a stack and does not properly receive, handle, and pass on the information, your driver may cause system crashes.

For more information about IRPs, see [Handling IRPs](handling-irps.md).

For more information about driver stacks, see [Device Objects and Device Stacks](device-objects-and-device-stacks.md).

For programming techiques related to I/O management, see [I/O Manager Programming Techniques](i-o-programming-techniques.md).

Routines that provide a direct interface to the I/O manager are usually prefixed with the letters "**Io**"; for example, **IoCreateDevice**. For a list of I/O manager routines, see [I/O Manager Routines](https://msdn.microsoft.com/library/windows/hardware/ff551797).

For lists of routines that relate to IRPS, see [IRPs](https://msdn.microsoft.com/library/windows/hardware/ff550701).

The I/O manager has two subcomponents: the Plug and Play manager and power manager. They manage the I/O functionality for the technologies of Plug and Play and power management. For more information about Plug and Play management, see [Windows Kernel-Mode Plug and Play Manager](windows-kernel-mode-plug-and-play-manager.md) and for more information about power management, see [Windows Kernel-Mode Power Manager](windows-kernel-mode-power-manager.md).

 

 




