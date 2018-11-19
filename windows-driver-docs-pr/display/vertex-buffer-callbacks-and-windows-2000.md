---
title: Vertex Buffer Callbacks and Windows 2000
description: Vertex Buffer Callbacks and Windows 2000
ms.assetid: d3b92bc9-d4f1-4079-86f1-53c04bcab443
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , vertex buffers, callbacks
- vertex buffers WDK DirectX 8.0 , callbacks and Windows 2000
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Vertex Buffer Callbacks and Windows 2000


## <span id="ddk_vertex_buffer_callbacks_and_windows_2000_gg"></span><span id="DDK_VERTEX_BUFFER_CALLBACKS_AND_WINDOWS_2000_GG"></span>


DirectX 7.0 on the initial retail release of Windows 2000 prevents a driver's execute buffer (D3D buffer) callbacks from being invoked by the runtime. This prevents the driver from being notified of vertex buffer creation requests and, hence, no video memory or nonlocal video memory buffers can be created or used in this scenario. Video memory vertex buffers are enabled in DirectX 8.0 and in the version of DirectX 7.0 that is shipped with DirectX 8.0. Furthermore, Windows 2000 Service Pack 1 (SP1) enables video memory vertex buffers and all future versions of Windows 2000 will enable video memory vertex buffers. However, there is no workaround to enable video memory vertex buffers on Windows 2000 other than to install DirectX 8.0.

 

 





