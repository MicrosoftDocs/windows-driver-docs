---
title: Using the DxApi Interface
description: Using the DxApi Interface
keywords:
- drawing kernel-mode video transport WDK DirectDraw , DxApi interface
- DirectDraw kernel-mode video transport WDK Windows 2000 display , DxApi interface
- kernel-mode video transport WDK DirectDraw , DxApi interface
- video transport kernel-mode WDK DirectDraw , DxApi interface
- DxApi interface WDK DirectDraw
- video capture WDK video transport kernel-mode
ms.date: 06/05/2024
---

# Using the DxApi Interface

As described in [Using Kernel-Mode Video Transport](using-kernel-mode-video-transport.md), a video capture driver (hardware decoder) must call the **DxApi** function to access the *DxApi* interface. As described in [VPE and Kernel-Mode Video Transport Architecture](vpe-and-kernel-mode-video-transport-architecture.md), a [video miniport driver](video-miniport-drivers-in-the-windows-2000-display-driver-model.md) implements the *DxApi* interface on Windows 2000 and later platforms. The following section describes how the DxApi interface is supported on these platforms:

[DxApi](nf-dxapi-dxapi.md)

[DxApi Miniport Driver Functions For Windows 2000 and Later](dxapi-miniport-driver-functions-for-windows-2000-and-later.md)
