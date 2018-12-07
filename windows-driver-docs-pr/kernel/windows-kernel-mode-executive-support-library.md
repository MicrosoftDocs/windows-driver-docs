---
title: Windows Kernel-Mode Executive Support Library
description: Windows Kernel-Mode Executive Support Library
ms.assetid: cfb8c6c0-9454-4dc6-98e8-c41cbf1c0cad
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Windows Kernel-Mode Executive Support Library


The Windows operating system uses the term *executive layer* to refer to kernel-mode components that provide a variety of services to device drivers, including:

-   Object management

-   Memory management

-   Process and thread management

-   Input/output management

-   Configuration management

Each of the above managers provides direct interfaces to their individual technologies, as do several libraries. However, routines that are grouped together as a generic interface to the Executive Library are usually prefixed with "**Ex**", for example, **ExGetCurrentResourceThread**. For a list of executive library routines, see [Executive Library Support Routines](https://msdn.microsoft.com/library/windows/hardware/ff544582).

Note that the executive layer components are part of Ntoskrnl.exe, but that drivers and the HAL are not part of the executive layer.

 

 




