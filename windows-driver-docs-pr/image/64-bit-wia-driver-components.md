---
title: 64-bit WIA driver components
description: 64-Bit WIA driver components
ms.date: 03/21/2022
ms.custom: contperf-fy22q3
---

# 64-bit WIA driver components

A 64-bit WIA minidriver is loaded into the WIA service's process, which is a 64-bit process in 64-bit editions of the Windows operating system.

As a result, a WIA driver for x64-based versions of Windows can contain only 64-bit driver components. For example, it must contain a 64-bit minidriver, 64-bit WIA minidriver UI extensions, and potentially a 64-bit kernel-mode driver.
