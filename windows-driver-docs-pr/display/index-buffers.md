---
title: Index Buffers
description: Index Buffers
ms.assetid: 5bf7dc12-d988-4194-a81f-52c9c5356610
keywords: ["DirectX 8.0 release notes WDK Windows 2000 display , index buffers", "index buffers WDK Directx 8.0"]
---

# Index Buffers


## <span id="ddk_index_buffers_gg"></span><span id="DDK_INDEX_BUFFERS_GG"></span>


DirectX 8.0 introduces the concept of index buffers. These buffers are very similar to vertex buffers but store simple 16- or 32-bit indices into vertex data rather than the vertex data itself. Index buffers extend all the benefits of vertex buffers, for example optimal download and caching, to index data.

Index buffers are created, locked, unlocked and destroyed with the same driver entry points as those used for vertex buffers. A driver can distinguish between these buffer types using the new surface capability bit DDSCAPS2\_INDEXBUFFER. For index buffers, this flag is set in the **ddsCapsEx.dwCaps2** field of the surface's [**DD\_SURFACE\_MORE**](https://msdn.microsoft.com/library/windows/hardware/ff551737) structure. It will be clear for vertex buffers.

Unlike many other surface types, a driver does not need to set the capability DDSCAPS2\_INDEXBUFFER when reporting its capabilities to the runtime to receive driver calls for index buffer creation, destruction, and locking. A DirectX 8.0 driver that supports vertex buffers is assumed to support index buffers also. If the underlying hardware has no direct support for index buffers, then the driver should handle index buffer creation by allocating system memory for the surface.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Index%20Buffers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




