---
title: Fully-Typed Back Buffers Casting
description: Fully-Typed Back Buffers Casting
ms.assetid: d34f95a4-e380-4bfb-9909-0938f63174be
keywords:
- Direct3D version 10.1 WDK Windows 7 display , casting fully-typed back buffers
- casting fully-typed back buffers WDK Windows 7 display
- back buffers WDK Windows 7 display
- back buffers WDK Windows 7 display , fully typed
- fully-typed back buffers WDK Windows 7 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Fully-Typed Back Buffers Casting


This section applies only to Windows 7 and later operating systems.

Consider resources that are created through a call to the driver's [**CreateResource(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540691) function with the **Format** member of the [**D3D10DDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff541697) structure set to a format of family DXGI\_FORMAT\_R8G8B8A8\_TYPELESS, DXGI\_FORMAT\_B8G8R8A8\_TYPELESS or DXGI\_FORMAT\_R10G10B10A2\_TYPELESS and with the D3D10\_DDI\_BIND\_PRESENT value set in the **BindFlags** member of **D3D10DDIARG\_CREATERESOURCE**. The Direct3D version 10.1 runtime can subsequently create views (render target or shader resource) on these resources by using any of the fully-typed members of the appropriate family (for example, DXGI\_FORMAT\_B8G8R8A8\_UNORM\_SRGB for the DXGI\_FORMAT\_B8G8R8A8\_TYPELESS family), even if the original resource is created as fully typed. If D3D10\_DDI\_BIND\_PRESENT is not set for the resource, this re-casting is not allowed, as is the case for all fully-typed resources in Direct3D version 10.

This change for Direct3D version 10.1 allows applications to re-view a DXGI\_FORMAT\_R8G8B8A8\_UNORM back buffer as DXGI\_FORMAT\_R8G8B8A8\_UNORM\_SRGB and vice versa. This change also allows applications to cast a DXGI\_FORMAT\_B8G8R8A8\_UNORM\_SRGB back buffer for DXGI\_FORMAT\_B8G8R8A8\_UNORM and to re-view DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM as DXGI\_FORMAT\_R10G10B10A2\_\* for rendering.

 

 





