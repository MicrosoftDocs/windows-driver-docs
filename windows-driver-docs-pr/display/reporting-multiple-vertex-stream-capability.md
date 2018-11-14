---
title: Reporting Multiple Vertex Stream Capability
description: Reporting Multiple Vertex Stream Capability
ms.assetid: 61441576-0e5d-4c6d-9e36-dcd8c59c8db0
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , multiple vertex streams
- multiple vertex streams WDK DirectX 8.0
- vertex multiple streams WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Multiple Vertex Stream Capability


## <span id="ddk_reporting_multiple_vertex_stream_capability_gg"></span><span id="DDK_REPORTING_MULTIPLE_VERTEX_STREAM_CAPABILITY_GG"></span>


A driver reports the ability to support multiple vertex streams by setting the value of the **MaxStreams** field of the D3DCAPS8 structure. A driver that supports multiple vertex streams should specify a value greater than one. A DX8 level driver that does not support multiple vertex streams should set **MaxStreams** to one. No DX8 level driver should specify a value of zero for this field. The driver should also set the **MaxStreamStride** field to the maximum supported stride (in bytes) between vertex elements in a vertex stream.

 

 





