---
title: Interpretation of X Channel
description: Interpretation of X Channel
ms.assetid: ba039e5a-78ee-43cb-b883-4675b011a29d
keywords:
- Direct3D version 10.1 WDK Windows 7 display , X channel
- extended format WDK Windows 7 display , X channel
- X channel WDK Windows 7 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Interpretation of X Channel


This section applies only to Windows 7 and later operating systems.

The user-mode display driver should read the X channel in all formats that include X (for example, DXGI\_FORMAT\_B8G8R8X8\_UNORM) as 1.0f when such formats are presented to filtering hardware or the blender.

The X channel must be copied unmodified when data is moved outside of the 3-D pipeline (that is, when an application calls the **ID3D10Device::CopyResource**, **ID3D10Device::CopySubresourceRegion**, or **ID3D10Device::UpdateSubResource** method). For more information about these methods, see the DirectX SDK documentation.

 

 





