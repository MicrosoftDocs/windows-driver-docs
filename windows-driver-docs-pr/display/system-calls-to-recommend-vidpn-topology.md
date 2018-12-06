---
title: System Calls to Recommend VidPN Topology
description: System Calls to Recommend VidPN Topology
ms.assetid: cc23be93-be31-4069-960c-268a8b151063
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# System Calls to Recommend VidPN Topology


On a computer running Windows 7, the display mode manager (DMM) determines an appropriate VidPN topology to apply using VidPN history data in the CCD database. DMM no longer determines the VidPN topology based upon the last known good topology as it did in Windows Vista. Consequently, on Windows 7 DMM never calls the [**DxgkDdiRecommendVidPnTopology**](https://msdn.microsoft.com/library/windows/hardware/ff559782) function.

On Windows Vista and its service packs, DMM continues to call *DxgkDdiRecommendVidPnTopology* to request that the driver provide a recommended functional VidPN topology.

 

 





