---
title: Windows Kernel-Mode HAL Library
description: Windows Kernel-Mode HAL Library
ms.date: 10/17/2018
---

# Windows Kernel-Mode HAL Library


Windows runs on many different configurations of the personal computer. Each configuration requires a layer of software that interacts between the hardware and the rest of the operating system. Because this layer abstracts (hides) the low-level hardware details from drivers and the operating system, it is called the hardware abstraction layer (HAL).

Developers are not encouraged to write their own HAL. If you need hardware access, the HAL library provides routines that can be used for that purpose. Routines that interface with the HAL directly are prefixed with the letters "**Hal**"; for a list of HAL routines, see [Hardware Abstraction Layer (HAL) Library Routines](/previous-versions/windows/hardware/drivers/ff546644(v=vs.85)).

 

