---
title: Casting Ability of XR Formats
description: Casting Ability of XR Formats
keywords:
- Direct3D version 10.1 WDK Windows 7 display , XR format casting ability
- extended format WDK Windows 7 display , XR format casting ability
- XR format casting ability WDK Windows 7 display
- casting ability WDK Windows 7 display
- casting ability WDK Windows 7 display , XR formats
ms.date: 04/20/2017
---

# Casting Ability of XR Formats


This section applies only to Windows 7 and later operating systems.

The DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM format is a member of the DXGI\_FORMAT\_R10G10B10A2\_TYPELESS family. Therefore, an application can cast the DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM format through the API-level concept of "views" to any other member of that family. This procedure is the expected way that an application renders to a resource. Specifically, the Direct3D runtime can only scan out and copy (through the driver's [**BltDXGI**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_base_functions) function) a resource of format XR\_BIAS. Therefore, to render to the resource, an application typically creates a view of format DXGI\_FORMAT\_R10G10B10A2\_UNORM.

 

