---
title: Reporting Support for Video Memory Vertex and Index Buffers
description: Reporting Support for Video Memory Vertex and Index Buffers
ms.assetid: fa0d7dd5-3bed-45db-a946-0761fd631a52
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , reporting capabilities
- D3DCAPS8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Support for Video Memory Vertex and Index Buffers


## <span id="ddk_reporting_support_for_video_memory_vertex_and_index_buffers_gg"></span><span id="DDK_REPORTING_SUPPORT_FOR_VIDEO_MEMORY_VERTEX_AND_INDEX_BUFFERS_GG"></span>


DirectX 8.0 has added two new Direct3D capability flags that flag to the runtime whether the driver does or does not support video memory vertex and index buffers. Before these flags were created, the runtime could not determine whether the driver provided real support for video memory vertex buffers or not. Therefore, if a DirectX 8.0 exports the execute buffer (d3d buffer) creation and destruction driver entry points it should add one or both of the capability bits D3DDEVCAPS\_HWVERTEXBUFFER and D3DDEVCAPS\_HWINDEXBUFFER to the **DevCaps** field of the D3DCAPS8 structure reported via **GetDriverInfo2** to the runtime. Set the flag D3DDEVCAPS\_HWVERTEXBUFFER if your driver supports video or nonlocal video memory vertex buffers and D3DDEVCAPS\_HWINDEXBUFFER if your driver supports video or nonlocal video memory index buffers.

The runtime masks these capability bits off before reporting capabilities to the application (they are not useful to applications only to the runtime itself). Therefore, these capabilities are not visible to the DirectX Caps Viewer application even if your driver exports them.

Correct support for these capabilities is part of Microsoft Windows Hardware Quality Labs (WHQL) testing.

 

 





