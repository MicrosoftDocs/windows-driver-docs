---
title: Notification of Stream and Vertex Buffer Binding
description: Notification of Stream and Vertex Buffer Binding
ms.assetid: 9ab9727f-053d-404b-95cc-ffd64fde7997
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , multiple vertex streams
- multiple vertex streams WDK DirectX 8.0
- vertex multiple streams WDK DirectX 8.0
- vertex buffers WDK DirectX 8.0
- stream binding to vertex buffer WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Notification of Stream and Vertex Buffer Binding


## <span id="ddk_notification_of_stream_vertex_buffer_binding_gg"></span><span id="DDK_NOTIFICATION_OF_STREAM_VERTEX_BUFFER_BINDING_GG"></span>


A driver is notified of the binding of a vertex buffer to a particular stream through a new DP2 token, D3DDP2OP\_SETSTREAMSOURCE, and its associated HAL data structure, [**D3DHAL\_DP2SETSTREAMSOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff545798).

 

 





