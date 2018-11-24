---
title: Cursors
description: Cursors
ms.assetid: 8647b0fc-b93b-489d-b2c0-b5caf98e800b
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , cursors
- cursors WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Cursors


## <span id="ddk_cursors_gg"></span><span id="DDK_CURSORS_GG"></span>


DirectX 8.0 has added an API to support high update frequency cursors without requiring API level direct access to the primary surface. For DirectX 8.0, the cursor is the standard GDI cursor if capabilities permit, or else it is emulated with DirectDraw blts. To support the DirectX cursor API, the driver has to return capability information in D3DCAPS8.

The **CursorCaps** field should be set to D3DCURSORCAPS\_MONO, D3DCURSORCAPS\_COLOR, or both, to indicate support for monochrome and color hardware cursors. The **MaxCursorEdgeSize** field should be set to the minimum of the maximum width and maximum height of the hardware cursor (or zero if no hardware cursor is supported). It is not possible to express different maximum sizes for the width and height of the cursor.

 

 





