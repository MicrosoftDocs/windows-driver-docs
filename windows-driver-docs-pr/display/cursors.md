---
title: Cursors
description: Cursors
ms.assetid: 8647b0fc-b93b-489d-b2c0-b5caf98e800b
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , cursors
- cursors WDK DirectX 8.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Cursors


## <span id="ddk_cursors_gg"></span><span id="DDK_CURSORS_GG"></span>


DirectX 8.0 has added an API to support high update frequency cursors without requiring API level direct access to the primary surface. For DirectX 8.0, the cursor is the standard GDI cursor if capabilities permit, or else it is emulated with DirectDraw blts. To support the DirectX cursor API, the driver has to return capability information in D3DCAPS8.

The **CursorCaps** field should be set to D3DCURSORCAPS\_MONO, D3DCURSORCAPS\_COLOR, or both, to indicate support for monochrome and color hardware cursors. The **MaxCursorEdgeSize** field should be set to the minimum of the maximum width and maximum height of the hardware cursor (or zero if no hardware cursor is supported). It is not possible to express different maximum sizes for the width and height of the cursor.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Cursors%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




