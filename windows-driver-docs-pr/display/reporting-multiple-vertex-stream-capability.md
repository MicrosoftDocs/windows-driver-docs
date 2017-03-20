---
title: Reporting Multiple Vertex Stream Capability
description: Reporting Multiple Vertex Stream Capability
ms.assetid: 61441576-0e5d-4c6d-9e36-dcd8c59c8db0
keywords: ["DirectX 8.0 release notes WDK Windows 2000 display , multiple vertex streams", "multiple vertex streams WDK DirectX 8.0", "vertex multiple streams WDK DirectX 8.0"]
---

# Reporting Multiple Vertex Stream Capability


## <span id="ddk_reporting_multiple_vertex_stream_capability_gg"></span><span id="DDK_REPORTING_MULTIPLE_VERTEX_STREAM_CAPABILITY_GG"></span>


A driver reports the ability to support multiple vertex streams by setting the value of the **MaxStreams** field of the D3DCAPS8 structure. A driver that supports multiple vertex streams should specify a value greater than one. A DX8 level driver that does not support multiple vertex streams should set **MaxStreams** to one. No DX8 level driver should specify a value of zero for this field. The driver should also set the **MaxStreamStride** field to the maximum supported stride (in bytes) between vertex elements in a vertex stream.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20Multiple%20Vertex%20Stream%20Capability%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




