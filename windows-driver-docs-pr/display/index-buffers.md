---
title: Index Buffers
description: Index Buffers
ms.assetid: 5bf7dc12-d988-4194-a81f-52c9c5356610
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , index buffers
- index buffers WDK Directx 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Index Buffers


## <span id="ddk_index_buffers_gg"></span><span id="DDK_INDEX_BUFFERS_GG"></span>


DirectX 8.0 introduces the concept of index buffers. These buffers are very similar to vertex buffers but store simple 16- or 32-bit indices into vertex data rather than the vertex data itself. Index buffers extend all the benefits of vertex buffers, for example optimal download and caching, to index data.

Index buffers are created, locked, unlocked and destroyed with the same driver entry points as those used for vertex buffers. A driver can distinguish between these buffer types using the new surface capability bit DDSCAPS2\_INDEXBUFFER. For index buffers, this flag is set in the **ddsCapsEx.dwCaps2** field of the surface's [**DD\_SURFACE\_MORE**](https://msdn.microsoft.com/library/windows/hardware/ff551737) structure. It will be clear for vertex buffers.

Unlike many other surface types, a driver does not need to set the capability DDSCAPS2\_INDEXBUFFER when reporting its capabilities to the runtime to receive driver calls for index buffer creation, destruction, and locking. A DirectX 8.0 driver that supports vertex buffers is assumed to support index buffers also. If the underlying hardware has no direct support for index buffers, then the driver should handle index buffer creation by allocating system memory for the surface.

 

 





