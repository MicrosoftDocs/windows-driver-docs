---
title: Windows Kernel-Mode HAL Library
description: Windows kernel-mode HAL library
ms.date: 05/01/2025
ms.topic: concept-article
---

# Windows kernel-mode HAL library

Windows runs on many different configurations of the personal computer. Each configuration requires a layer of software that interacts between the hardware and the rest of the operating system. Because this layer abstracts (hides) the low-level hardware details from drivers and the operating system, it's called the hardware abstraction layer (HAL).

Developers aren't encouraged to write their own HAL. If you need hardware access, the HAL library provides routines that can be used for that purpose. Routines that interface with the HAL directly are prefixed with the letters "**Hal**"; for a list of HAL routines, see [Hardware Abstraction Layer (HAL) Library Routines](/previous-versions/windows/hardware/drivers/ff546644(v=vs.85)).
