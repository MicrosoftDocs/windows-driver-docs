---
title: User Mode and Kernel Mode
description: A processor in a computer running Windows has two different modes - user mode and kernel mode.
ms.date: 12/15/2023
ms.custom: contperf-fy22q1
---

# User mode and kernel mode

A processor in a computer running Windows operates in two different modes: *user mode* and *kernel mode*. The processor switches between these modes depending on the type of code it's executing. Applications operate in user mode, while core operating system components function in kernel mode. Although many drivers operate in kernel mode, some can function in user mode.

## User mode 

When you launch an application in user mode, Windows creates a *process* for it. This process provides the application with a private [*virtual address space*](virtual-address-spaces.md) and a private *handle table*. Since each application's virtual address space is private, one application can't modify another application's data. Each application runs in isolation, ensuring that if one crashes, it doesn't affect other applications or the operating system.

The virtual address space of a user-mode application is also limited. A process running in user mode can't access virtual addresses that are reserved for the operating system. Limiting the virtual address space of a user-mode application prevents the application from modifying or damaging critical operating system data.

## Kernel mode

All code running in kernel mode shares a single [virtual address space](virtual-address-spaces.md). As a result, a kernel-mode driver isn't isolated from other drivers or the operating system. If a kernel-mode driver mistakenly writes to the wrong virtual address, it could compromise data belonging to the operating system or another driver. If a kernel-mode driver crashes, it causes the entire operating system to crash.

The following diagram illustrates the communication between user-mode and kernel-mode components.

:::image type="content" source="images/userandkernelmode01.png" alt-text="Diagram that shows the communication between user-mode and kernel-mode components in a computer system.":::

## Related articles

[Virtual address spaces](virtual-address-spaces.md)
