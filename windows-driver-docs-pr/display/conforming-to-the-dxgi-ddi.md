---
title: Conforming to the DXGI DDI
description: Conforming to the DXGI DDI
ms.assetid: 1c789f57-003e-4b29-9a81-dbf194670664
keywords:
- Direct3D version 11 WDK Windows 7 display , DXGI DDI conformance
- Direct3D version 11 WDK Windows Server 2008 R2 display , DXGI DDI conformance
- DirectX Graphics Infrastructure DDI conformance WDK Windows 7 display
- DirectX Graphics Infrastructure DDI conformance WDK Windows Server 2008 R2 display
- DXGI DDI conformance WDK Windows 7 display
- DXGI DDI conformance WDK Windows Server 2008 R2 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Conforming to the DXGI DDI


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The Direct3D version 11 DDI conforms to the [DirectX Graphics Infrastructure (DXGI) DDI's](directx-graphics-infrastructure-ddi.md) definition for resource interfaces, device enumeration, and presentation.

### <span id="presentation"></span><span id="PRESENTATION"></span>Presentation

Because Direct3D version 11 devices must support presentation from any scan-out capable format, user-mode display drivers will be required to field present operations through their display miniport drivers (kernel-mode drivers) that call for color conversion from any of the scan-out formats to any other scan-out format and also to standard GDI scan-out formats. These scan-out formats are known by the following values from the DXGI\_FORMAT enumeration:

-   DXGI\_FORMAT\_B5G6R5\_UNORM

-   DXGI\_FORMAT\_B5G5R5A1\_UNORM

-   DXGI\_FORMAT\_B8G8R8A8\_UNORM

-   DXGI\_FORMAT\_B8G8R8X8\_UNORM

There are back buffer restrictions with the Direct3D version 11 DDI. If DXGI\_USAGE\_BACKBUFFER (from the [DXGI\_USAGE](http://go.microsoft.com/fwlink/p/?linkid=122799) enumeration) is set, the following are the only other DXGI usages that are allowed:

-   DXGI\_USAGE\_SHADERINPUT, which maps to D3D11\_BIND\_SHADER\_RESOURCE

-   DXGI\_USAGE\_RENDER\_TARGET\_OUTPUT, which maps to D3D11\_BIND\_RENDER\_TARGET

Note that no CPU access flags are allowed for back buffers.

 

 





