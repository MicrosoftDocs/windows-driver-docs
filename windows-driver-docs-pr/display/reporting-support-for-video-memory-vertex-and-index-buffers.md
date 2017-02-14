---
title: Reporting Support for Video Memory Vertex and Index Buffers
description: Reporting Support for Video Memory Vertex and Index Buffers
ms.assetid: fa0d7dd5-3bed-45db-a946-0761fd631a52
keywords: ["DirectX 8.0 release notes WDK Windows 2000 display , reporting capabilities", "D3DCAPS8"]
---

# Reporting Support for Video Memory Vertex and Index Buffers


## <span id="ddk_reporting_support_for_video_memory_vertex_and_index_buffers_gg"></span><span id="DDK_REPORTING_SUPPORT_FOR_VIDEO_MEMORY_VERTEX_AND_INDEX_BUFFERS_GG"></span>


DirectX 8.0 has added two new Direct3D capability flags that flag to the runtime whether the driver does or does not support video memory vertex and index buffers. Before these flags were created, the runtime could not determine whether the driver provided real support for video memory vertex buffers or not. Therefore, if a DirectX 8.0 exports the execute buffer (d3d buffer) creation and destruction driver entry points it should add one or both of the capability bits D3DDEVCAPS\_HWVERTEXBUFFER and D3DDEVCAPS\_HWINDEXBUFFER to the **DevCaps** field of the D3DCAPS8 structure reported via **GetDriverInfo2** to the runtime. Set the flag D3DDEVCAPS\_HWVERTEXBUFFER if your driver supports video or nonlocal video memory vertex buffers and D3DDEVCAPS\_HWINDEXBUFFER if your driver supports video or nonlocal video memory index buffers.

The runtime masks these capability bits off before reporting capabilities to the application (they are not useful to applications only to the runtime itself). Therefore, these capabilities are not visible to the DirectX Caps Viewer application even if your driver exports them.

Correct support for these capabilities is part of Microsoft Windows Hardware Quality Labs (WHQL) testing.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20Support%20for%20Video%20Memory%20Vertex%20and%20Index%20Buffers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




