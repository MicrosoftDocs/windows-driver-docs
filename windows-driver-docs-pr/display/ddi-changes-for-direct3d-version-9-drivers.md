---
title: DDI Changes for Direct3D Version 9 Drivers
description: DDI Changes for Direct3D Version 9 Drivers
keywords:
- Direct3D version 10.1 WDK Windows 7 display , DDI changes for Direct3D version 9 drivers
- Direct3D version 9 drivers WDK Windows 7 display
- Direct3D version 9 drivers WDK Windows 7 display , DDI changes
- XR_BIAS WDK Windows 7 display , Direct3D version 9 DDI
ms.date: 04/20/2017
---

# DDI Changes for Direct3D Version 9 Drivers


This section applies only to Windows 7 and later operating systems.

XR\_BIAS is the only new extended format ability that Windows 7 makes available to user-mode display drivers that only support the Direct3D version 9 DDI.

Such a user-mode display driver can indicate that it supports the D3DDDIFMT\_A2B10G10R10\_XR\_BIAS format value from the [**D3DDDIFORMAT**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-_d3dddiformat) enumeration. The driver indicates such support by creating an entry in the array of populated [**FORMATOP**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_formatop) structures in the **pData** member of the [**D3DDDIARG\_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_getcaps) structure that the driver returns from a call to its [**GetCaps**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_getcaps) function with the D3DDDICAPS\_GETFORMATDATA value set in the **Type** member of D3DDDIARG\_GETCAPS. This entry should indicate, in the **Operations** member of **FORMATOP**, all of the typical operations that the runtime can perform on surfaces with the D3DDDIFMT\_A2B10G10R10\_XR\_BIAS format. For example, the driver should set the FORMATOP\_\*\_RENDERTARGET bits in **Operations**. The driver must also set the FORMATOP\_DISPLAYMODE and FORMATOP\_3DACCELERATION bits in **Operations**.

If the driver returns a [**FORMATOP**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_formatop) entry for the D3DDDIFMT\_A2B10G10R10\_XR\_BIAS format, the driver can subsequently receive calls to its [**CreateResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createresource) function to create resources with the D3DDDIFMT\_A2B10G10R10\_XR\_BIAS format set in the **Format** member of the [**D3DDDIARG\_CREATERESOURCE**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddiarg_createresource) structure.

The driver only receives requests to create resources with the D3DDDIFMT\_A2B10G10R10\_XR\_BIAS format for full-screen flipping chains. The Desktop Windows Manager (DWM) handles windowed presentation of XR\_BIAS in shader code. The driver should treat D3DDDIFMT\_A2B10G10R10\_XR\_BIAS-format resources as the D3DDDIFMT\_A2B10G10R10 format in all operations except scan out, For example, the driver can treat D3DDDIFMT\_A2B10G10R10\_XR\_BIAS-format resources as the D3DDDIFMT\_A2B10G10R10 format for blending, filtering, and format-conversion operations. The only difference is how XR\_BIAS affects scan-out. For more information about scan-out, see [BGRA Scan-Out Support](bgra-scan-out-support.md).

 

