---
title: Notification of Stream and Vertex Buffer Binding
description: Notification of Stream and Vertex Buffer Binding
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , multiple vertex streams
- multiple vertex streams WDK DirectX 8.0
- vertex multiple streams WDK DirectX 8.0
- vertex buffers WDK DirectX 8.0
- stream binding to vertex buffer WDK DirectX 8.0
ms.date: 04/20/2017
---

# Notification of Stream and Vertex Buffer Binding


## <span id="ddk_notification_of_stream_vertex_buffer_binding_gg"></span><span id="DDK_NOTIFICATION_OF_STREAM_VERTEX_BUFFER_BINDING_GG"></span>


A driver is notified of the binding of a vertex buffer to a particular stream through a new DP2 token, D3DDP2OP\_SETSTREAMSOURCE, and its associated HAL data structure, [**D3DHAL\_DP2SETSTREAMSOURCE**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2setstreamsource).

 

