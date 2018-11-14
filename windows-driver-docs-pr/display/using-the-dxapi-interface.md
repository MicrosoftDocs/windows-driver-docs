---
title: Using the DxApi Interface
description: Using the DxApi Interface
ms.assetid: 9de96d20-6cfc-42e7-821b-8256e0dd9b38
keywords:
- drawing kernel-mode video transport WDK DirectDraw , DxApi interface
- DirectDraw kernel-mode video transport WDK Windows 2000 display , DxApi interface
- kernel-mode video transport WDK DirectDraw , DxApi interface
- video transport kernel-mode WDK DirectDraw , DxApi interface
- DxApi interface WDK DirectDraw
- video capture WDK video transport kernel-mode
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the DxApi Interface


## <span id="ddk_using_the_dxapi_interface_gg"></span><span id="DDK_USING_THE_DXAPI_INTERFACE_GG"></span>


As described in [Using Kernel-Mode Video Transport](using-kernel-mode-video-transport.md), a video capture driver (hardware decoder) must call the [**DxApi**](https://msdn.microsoft.com/library/windows/hardware/ff557364) function to access the DxApi interface. As described in [VPE and Kernel-Mode Video Transport Architecture](vpe-and-kernel-mode-video-transport-architecture.md), a [video miniport driver](video-miniport-drivers-in-the-windows-2000-display-driver-model.md) implements the DxApi interface on Windows 2000 and later platforms. The following section describes how the DxApi interface is supported on these platforms:

[DxApi Miniport Driver Functions For Windows 2000 and Later](dxapi-miniport-driver-functions-for-windows-2000-and-later.md)

 

 





