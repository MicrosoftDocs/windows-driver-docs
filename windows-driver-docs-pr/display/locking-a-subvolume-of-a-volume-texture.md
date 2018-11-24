---
title: Locking a Subvolume of a Volume Texture
description: Locking a Subvolume of a Volume Texture
ms.assetid: fff7b9c6-5f83-4691-9e44-99e45897ae3a
keywords:
- textures WDK DirectX 8.0
- DirectX 8.0 release notes WDK Windows 2000 display , volume textures
- volume textures WDK DirectX 8.0
- subvolume locking WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Locking a Subvolume of a Volume Texture


## <span id="ddk_locking_a_subvolume_of_a_volume_texture_gg"></span><span id="DDK_LOCKING_A_SUBVOLUME_OF_A_VOLUME_TEXTURE_GG"></span>


DirectX 8.1 introduces a new feature that lets a driver lock just a subvolume of a volume texture. When a driver's [*DdLock*](https://msdn.microsoft.com/library/windows/hardware/ff549599) function is called, the driver can improve system performance by locking just a subvolume instead of the whole volume texture.

To indicate support of this feature, the driver must set the D3DDEVCAPS\_SUBVOLUMELOCK bit in the **DevCaps** member of the D3DCAPS8 structure. The driver returns a D3DCAPS8 structure in response to a **GetDriverInfo2** query as described in [Reporting DirectX 8.0 Style Direct3D Capabilities](reporting-directx-8-0-style-direct3d-capabilities.md). Support of this query is described in [Supporting GetDriverInfo2](supporting-getdriverinfo2.md).

After support of this feature is determined, the driver can receive a *DdLock* call with the DDLOCK\_HASVOLUMETEXTUREBOXRECT bit set in the **dwFlags** member of the passed DD\_LOCKDATA structure. This bit informs the driver to lock down the specified subvolume texture. The driver must then obtain the front and back coordinates of the locked subvolume from the **left** and **right** members of the RECTL structure that is specified in the **rArea** member of DD\_LOCKDATA. The driver obtains the front and back coordinates from the higher 16 bits of the **left** and **right** members respectively.

The left and right coordinates of the locked subvolume are constrained to the lower 16 bits of the **left** and **right** members. The driver uses the **top** and **bottom** members of the RECTL structure in **rArea** unchanged to specify the top and bottom coordinates of the locked subvolume. In this way, the **rArea** member effectively provides three coordinate sets to specify the locked subvolume. The RECTL structure is described in the Microsoft Windows SDK documentation.

The following code shows how to obtain the front and back coordinates:

```cpp
"real" left = rArea.left && 0xFFFF;
"real" right = rArea.right && 0xFFFF;
front = rArea.left >> 16;
back = rArea.right >> 16;
```

This feature is available on Windows Me and Windows XP and later versions. This feature is also available on Windows 2000 and Windows 98 operating system versions that have the DirectX 8.1 runtime installed on them.

 

 





