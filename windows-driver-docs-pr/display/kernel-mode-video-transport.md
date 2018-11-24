---
title: Kernel-Mode Video Transport
description: Kernel-Mode Video Transport
ms.assetid: 3acaabc7-8d9f-441b-9170-2e5a4e0ce114
keywords:
- drawing kernel-mode video transport WDK DirectDraw , about kernel-mode video transport
- DirectDraw kernel-mode video transport WDK Windows 2000 display , about kernel-mode video transport
- kernel-mode video transport WDK DirectDraw , about kernel-mode video transport
- video transport kernel-mode WDK DirectDraw , about kernel-mode video transport
- drawing kernel-mode video transport WDK DirectDraw
- DirectDraw kernel-mode video transport WDK Windows 2000 display
- kernel-mode video transport WDK DirectDraw
- video transport kernel-mode WDK DirectDraw
- weave WDK DirectDraw
- video capture WDK video transport kernel-mode
- miniVDD WDK DirectDraw
- bus mastering WDK DirectDraw
- V-sync WDK DirectDraw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Kernel-Mode Video Transport


## <span id="ddk_kernel_mode_video_transport_gg"></span><span id="DDK_KERNEL_MODE_VIDEO_TRANSPORT_GG"></span>


This topic describes kernel-mode video transport as it exists on the Microsoft Windows 2000 and later operating systems.

Kernel-mode video transport refers to a new Microsoft DirectDraw component in ring 0 (kernel mode) that enhances video functionality. This component accesses the DxApi interface. This interface is added to the [video miniport driver](video-miniport-drivers-in-the-windows-2000-display-driver-model.md) under Windows 2000 and later operating systems.

### <span id="windows_2000_and_later"></span><span id="WINDOWS_2000_AND_LATER"></span>Windows 2000 and Later

Kernel-mode video transport refers to a Microsoft DirectDraw component that a client, such as Microsoft DirectShow, can use to enhance video functionality. A primary role of this functionality is to call the miniport driver to tell it to perform hardware video port and overlay flips when V-sync occurs. This capability can support up to ten buffers without encountering hardware limitations, as long as the hardware video port supports the V-sync interrupt request (IRQ). This capability is used automatically by the versions of DirectDraw supplied with Microsoft DirectX 5.0 and later versions when autoflipping is specified by the client and the hardware cannot autoflip.

The kernel-mode video transport also ensures enhanced capture support. Under Microsoft Windows 98/Me and Microsoft Windows 2000 and later, the WDM-based video capture driver runs in kernel mode, with direct access to the frame buffer. The capture driver can "manually" flip overlays. The Windows 2000 and later miniport video transport driver can provide V-sync notification from the hardware video port or display; it can also get field polarities, which can be useful when capturing vertical blanking interval (VBI) data.

Although the primary purpose of the kernel-mode driver is to enhance hardware video port autoflipping capabilities, it also supports video bus masters, which can write data while in kernel mode. The bus master can be notified before losing the surface because of a mode change, or because a full-screen Command Prompt instance is launched. Because the new driver support allows a bus master to be called before the changes occur, the bus master can shut off without causing a problem.

 

 





