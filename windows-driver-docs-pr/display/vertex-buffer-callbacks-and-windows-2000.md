---
title: Vertex Buffer Callbacks and Windows 2000
description: Vertex Buffer Callbacks and Windows 2000
ms.assetid: d3b92bc9-d4f1-4079-86f1-53c04bcab443
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , vertex buffers, callbacks
- vertex buffers WDK DirectX 8.0 , callbacks and Windows 2000
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Vertex Buffer Callbacks and Windows 2000


## <span id="ddk_vertex_buffer_callbacks_and_windows_2000_gg"></span><span id="DDK_VERTEX_BUFFER_CALLBACKS_AND_WINDOWS_2000_GG"></span>


DirectX 7.0 on the initial retail release of Windows 2000 prevents a driver's execute buffer (D3D buffer) callbacks from being invoked by the runtime. This prevents the driver from being notified of vertex buffer creation requests and, hence, no video memory or nonlocal video memory buffers can be created or used in this scenario. Video memory vertex buffers are enabled in DirectX 8.0 and in the version of DirectX 7.0 that is shipped with DirectX 8.0. Furthermore, Windows 2000 Service Pack 1 (SP1) enables video memory vertex buffers and all future versions of Windows 2000 will enable video memory vertex buffers. However, there is no workaround to enable video memory vertex buffers on Windows 2000 other than to install DirectX 8.0.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Vertex%20Buffer%20Callbacks%20and%20Windows%202000%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




