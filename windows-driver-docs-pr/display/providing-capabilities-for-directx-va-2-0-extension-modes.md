---
title: Providing Capabilities for DirectX VA 2.0 Extension Modes
description: Providing Capabilities for DirectX VA 2.0 Extension Modes
keywords:
- DirectX Video Acceleration WDK display , extended support
- Video Acceleration WDK DirectX , extended support
- VA WDK DirectX , extended support
ms.date: 10/22/2021
---

# Providing capabilities for DirectX VA 2.0 extension modes

## How to query DXVA 2.0 extension modes

When its [**GetCaps**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_getcaps) function is called, the user-mode display driver (UMD) provides the following capabilities for DirectX VA 2.0 extension modes based on the request type specified in the **Type** member of the [**D3DDDIARG_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_getcaps) structure that its **pData** parameter points to.

## D3DDDICAPS_GETEXTENSIONGUIDCOUNT and D3DDDICAPS_GETEXTENSIONGUIDS request types

The D3D runtime first requests the number of supported GUIDs followed by a request for the list of supported GUIDs. The UMD returns the number and a list of the GUIDs that it supports for extension modes.

## D3DDDICAPS_GETEXTENSIONCAPS request type

Each extension mode that the UMD supports can have unique capabilities. The UMD returns those capabilities when the D3DDDICAPS_GETEXTENSIONCAPS request type is passed. The Direct3D runtime specifies a [**DXVADDI_QUERYEXTENSIONCAPSINPUT**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_queryextensioncapsinput) structure for the extension GUID to retrieve capabilities for in a variable that the **pInfo** member of [**D3DDDIARG_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_getcaps) points to. The UMD returns capabilities for the extension GUID in a private structure that the **pData** member of D3DDDIARG_GETCAPS points to.
