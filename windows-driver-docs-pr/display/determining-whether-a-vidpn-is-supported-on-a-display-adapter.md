---
title: Determining Whether a VidPN is Supported on a Display Adapter
description: Determining Whether a VidPN is Supported on a Display Adapter
ms.assetid: ebf001fb-e445-4534-8e89-60e1b06b2d6e
keywords:
- video present networks WDK display , determining if supported
- VidPN WDK display , determining if supported
- functional VidPN WDK display
- determining VidPN supported WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Determining Whether a VidPN is Supported on a Display Adapter


This topic describes how the display miniport driver determines whether a particular video present network (VidPN) is supported on a display adapter. Before reading this material, you should be familiar with the material in the following topics:

-   [Introduction to Video Present Networks](introduction-to-video-present-networks.md)

-   [VidPN Objects and Interfaces](vidpn-objects-and-interfaces.md)

A VidPN is *functional* if it satisfies the following conditions:

-   It has a topology that has at least one path. (A path is an association between a source and target.)

-   Each source and target in the topology has a pinned mode.

A VidPN is *supported on a display adapter* if one of the following conditions is true:

-   It is functional, and it can be implemented on the display adapter. That is, the video output codecs on the display adapter can be configured to support the topology and the pinned modes specified by the VidPN.

-   It has a topology with at least one path, and it can be extended to a functional VidPN that can be implemented on the display adapter. That is, it would be possible, without changing any modes that have already been pinned, to pin modes on all the video present sources and targets that don't yet have modes pinned. Furthermore, it would be possible to implement the resulting functional VidPN on the display adapter.

-   It has an empty topology. The idea is that displaying nothing is always supported on a display adapter.

Part of determining whether a VidPN is supported is determining whether the VidPN's topology is valid. In other words, can the video present sources be connected to the video present targets as specified by the topology? Note that it is not a requirement that all video present targets in the topology have connected monitors. The topology can be valid and the VidPN can be supported even if there are no connected monitors.

From time to time, the VidPN manager calls [**DxgkDdiIsSupportedVidPn**](https://msdn.microsoft.com/library/windows/hardware/ff559684) to ask the display miniport driver whether a certain VidPN is supported on a display adapter. One of the arguments passed to **DxgkDdiIsSupportedVidPn** is a handle to a VidPN object called the desired VidPN. **DxgkDdiIsSupportedVidPn** must inspect the topology of the desired VidPN and must take note of which video present sources and targets in the desired VidPN already have pinned modes. Then it must return a Boolean value that indicates whether the desired VidPN is supported (according to the definition given previously in this topic). For information about inspecting the topology, source mode sets, and target mode sets of a VidPN, see [VidPN Objects and Interfaces](vidpn-objects-and-interfaces.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Determining%20Whether%20a%20VidPN%20is%20Supported%20on%20a%20Display%20Adapter%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




