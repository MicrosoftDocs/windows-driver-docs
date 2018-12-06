---
title: Determining Whether a VidPN is Supported on a Display Adapter
description: Determining Whether a VidPN is Supported on a Display Adapter
ms.assetid: ebf001fb-e445-4534-8e89-60e1b06b2d6e
keywords:
- video present networks WDK display , determining if supported
- VidPN WDK display , determining if supported
- functional VidPN WDK display
- determining VidPN supported WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





