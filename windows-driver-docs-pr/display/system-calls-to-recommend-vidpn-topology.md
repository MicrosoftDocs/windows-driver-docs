---
title: System Calls to Recommend VidPN Topology
description: System Calls to Recommend VidPN Topology
ms.assetid: cc23be93-be31-4069-960c-268a8b151063
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# System Calls to Recommend VidPN Topology


On a computer running Windows 7, the display mode manager (DMM) determines an appropriate VidPN topology to apply using VidPN history data in the CCD database. DMM no longer determines the VidPN topology based upon the last known good topology as it did in Windows Vista. Consequently, on Windows 7 DMM never calls the [**DxgkDdiRecommendVidPnTopology**](https://msdn.microsoft.com/library/windows/hardware/ff559782) function.

On Windows Vista and its service packs, DMM continues to call *DxgkDdiRecommendVidPnTopology* to request that the driver provide a recommended functional VidPN topology.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20System%20Calls%20to%20Recommend%20VidPN%20Topology%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




