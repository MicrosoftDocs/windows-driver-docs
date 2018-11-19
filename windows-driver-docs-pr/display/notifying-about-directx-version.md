---
title: Notifying about DirectX Version
description: Notifying about DirectX Version
ms.assetid: 62c030cf-8eb6-4a94-bd15-730b9219291c
keywords:
- version numbers WDK DirectX 9.0
- notifying DirectX versions WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Notifying about DirectX Version


## <span id="ddk_notifying_about_directx_version_gg"></span><span id="DDK_NOTIFYING_ABOUT_DIRECTX_VERSION_GG"></span>


DirectX 8.0 and later drivers are always notified about the DirectX runtime version being used by an application in a D3DGDI2\_TYPE\_DXVERSION request so they can report device capabilities for the version. In addition, because an application requests operations on surfaces with various pixel formats, DirectX 9.0 and later drivers are also notified about the DirectX runtime version that the application supports in D3DGDI2\_TYPE\_GETFORMATCOUNT and D3DGDI2\_TYPE\_GETFORMAT queries so those drivers can appropriately handle the operations for the version.

For example, for version 8.0 of the DirectX runtime, a DirectX 9.0 or later driver can set the number of samples for a multiple-sampled surface using elements of the D3DMULTISAMPLE\_TYPE enumerated type regardless of whether the driver supports maskable multisampling. However, for version 9.0 of the DirectX runtime, a DirectX 9.0 or later driver must not set D3DMULTISAMPLE\_TYPE bits in the DDSCAPS3\_MULTISAMPLE\_MASK mask unless the driver supports the bits as maskable. For more information about D3DMULTISAMPLE\_TYPE, see the DirectX SDK documentation.

In a D3DGDI2\_TYPE\_GETFORMATCOUNT query, the DirectX 9.0 driver is notified of the runtime version in the **dwReserved** member of the [**DD\_GETFORMATCOUNTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551566) structure. The **dwReserved** member is set to DD\_RUNTIME\_VERSION, which is 0x00000900 for DirectX 9.0.

In a D3DGDI2\_TYPE\_GETFORMAT query, the DirectX 9.0 driver is notified of the runtime version in the **dwSize** member of the DDPIXELFORMAT structure that is specified in the **format** member of the [**DD\_GETFORMATDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551569) structure. The **dwSize** member is also set to DD\_RUNTIME\_VERSION.

 

 





