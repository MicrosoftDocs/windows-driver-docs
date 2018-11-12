---
title: VPE and Kernel-Mode Video Transport Architecture
description: VPE and Kernel-Mode Video Transport Architecture
ms.assetid: 7264932a-7fe9-4ffe-bd25-b5cd605739fa
keywords:
- drawing kernel-mode video transport WDK DirectDraw , architecture
- DirectDraw kernel-mode video transport WDK Windows 2000 display , architecture
- kernel-mode video transport WDK DirectDraw , architecture
- video transport kernel-mode WDK DirectDraw , architecture
- video capture WDK video transport kernel-mode
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# VPE and Kernel-Mode Video Transport Architecture


## <span id="ddk_vpe_and_kernel_mode_video_transport_architecture_gg"></span><span id="DDK_VPE_AND_KERNEL_MODE_VIDEO_TRANSPORT_ARCHITECTURE_GG"></span>


This section provides some details about the Windows 2000 and later architecture for the video port extensions (VPE) and kernel-mode video transport in DirectX 5.0 and later versions. The architecture for kernel-mode video transport is based on new functions that Microsoft added as device-independent code. Kernel-mode video transport consists of a [**DxApi**](https://msdn.microsoft.com/library/windows/hardware/ff557364) function that is supplied as part of DirectDraw, the [video miniport driver](video-miniport-drivers-in-the-windows-2000-display-driver-model.md), and the COM interface methods supplied as part of DirectDraw.

### <span id="windows_2000_and_later"></span><span id="WINDOWS_2000_AND_LATER"></span>Windows 2000 and Later

In Windows 2000 and later, as shown in the following figure, the DxApi callbacks are part of the [video miniport driver](video-miniport-drivers-in-the-windows-2000-display-driver-model.md).

![diagram illustrating windows 2000 kernel-mode video transport architecture](images/ddfg011.png)

For more information about the DxApi callbacks, see [DxApi Miniport Driver Functions For Windows 2000 and Later](dxapi-miniport-driver-functions-for-windows-2000-and-later.md).

The preceding figure shows the kernel-mode video transport architecture in relation to other kernel-mode and user-mode components (the dashed line denotes the kernel transition). In this architecture, DirectShow (or another user-mode client) calls the [IDirectDrawKernel](https://msdn.microsoft.com/library/windows/hardware/ff567398) and [IDirectDrawSurfaceKernel](https://msdn.microsoft.com/library/windows/hardware/ff567409) DirectDraw COM interfaces to get handles to the DirectDraw object and surface objects.

**Note**   This architecture also supports using the PCI bus for data flow between the MPEG device and VGA device.

 

In Windows 2000 and later, the client then passes these handles to the miniport driver. These handles are specified in the calls to the kernel-mode video transport. The following figure shows a simple version of how the handles are passed in user- and kernel-mode video transport.

![diagram illustrating handle passing in windows 2000 video transport](images/ddfg012.png)

 

 





