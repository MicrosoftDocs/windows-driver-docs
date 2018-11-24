---
title: Design Goals for Kernel-Mode Drivers
description: Design Goals for Kernel-Mode Drivers
ms.assetid: 2799556e-0359-4388-acf3-74d90eb86a0f
keywords: ["kernel-mode drivers WDK , design goals"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Design Goals for Kernel-Mode Drivers





Kernel-mode drivers share many of the design goals of the operating system, particularly those of the system I/O manager. Kernel-mode drivers are designed to be:

-   [Portable](portable.md) from one platform to another.

-   [Configurable](configurable.md) to various hardware and software platforms.

-   [Always preemptible and always interruptible](always-preemptible-and-always-interruptible.md).

-   [Multiprocessor-safe](multiprocessor-safe.md) on multiprocessor platforms.

-   [Object-based](object-based.md).

-   [Packet-driven I/O with reusable IRPs](packet-driven-i-o-with-reusable-irps.md).

-   Capable of [supporting asynchronous I/O](supporting-asynchronous-i-o.md).

 

 




