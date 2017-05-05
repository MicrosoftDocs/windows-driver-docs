---
title: Notifying about DirectX Version
description: Notifying about DirectX Version
ms.assetid: 62c030cf-8eb6-4a94-bd15-730b9219291c
keywords:
- version numbers WDK DirectX 9.0
- notifying DirectX versions WDK DirectX 9.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Notifying about DirectX Version


## <span id="ddk_notifying_about_directx_version_gg"></span><span id="DDK_NOTIFYING_ABOUT_DIRECTX_VERSION_GG"></span>


DirectX 8.0 and later drivers are always notified about the DirectX runtime version being used by an application in a D3DGDI2\_TYPE\_DXVERSION request so they can report device capabilities for the version. In addition, because an application requests operations on surfaces with various pixel formats, DirectX 9.0 and later drivers are also notified about the DirectX runtime version that the application supports in D3DGDI2\_TYPE\_GETFORMATCOUNT and D3DGDI2\_TYPE\_GETFORMAT queries so those drivers can appropriately handle the operations for the version.

For example, for version 8.0 of the DirectX runtime, a DirectX 9.0 or later driver can set the number of samples for a multiple-sampled surface using elements of the D3DMULTISAMPLE\_TYPE enumerated type regardless of whether the driver supports maskable multisampling. However, for version 9.0 of the DirectX runtime, a DirectX 9.0 or later driver must not set D3DMULTISAMPLE\_TYPE bits in the DDSCAPS3\_MULTISAMPLE\_MASK mask unless the driver supports the bits as maskable. For more information about D3DMULTISAMPLE\_TYPE, see the DirectX SDK documentation.

In a D3DGDI2\_TYPE\_GETFORMATCOUNT query, the DirectX 9.0 driver is notified of the runtime version in the **dwReserved** member of the [**DD\_GETFORMATCOUNTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551566) structure. The **dwReserved** member is set to DD\_RUNTIME\_VERSION, which is 0x00000900 for DirectX 9.0.

In a D3DGDI2\_TYPE\_GETFORMAT query, the DirectX 9.0 driver is notified of the runtime version in the **dwSize** member of the DDPIXELFORMAT structure that is specified in the **format** member of the [**DD\_GETFORMATDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551569) structure. The **dwSize** member is also set to DD\_RUNTIME\_VERSION.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Notifying%20about%20DirectX%20Version%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




