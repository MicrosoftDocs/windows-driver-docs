---
title: Casting Ability of XR Formats
description: Casting Ability of XR Formats
ms.assetid: 18f9ce6e-df8e-4e57-b86f-338baadcb1b2
keywords:
- Direct3D version 10.1 WDK Windows 7 display , XR format casting ability
- extended format WDK Windows 7 display , XR format casting ability
- XR format casting ability WDK Windows 7 display
- casting ability WDK Windows 7 display
- casting ability WDK Windows 7 display , XR formats
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Casting Ability of XR Formats


This section applies only to Windows 7 and later operating systems.

The DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM format is a member of the DXGI\_FORMAT\_R10G10B10A2\_TYPELESS family. Therefore, an application can cast the DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM format through the API-level concept of "views" to any other member of that family. This procedure is the expected way that an application renders to a resource. Specifically, the Direct3D runtime can only scan out and copy (through the driver's [**BltDXGI**](https://msdn.microsoft.com/library/windows/hardware/ff538252) function) a resource of format XR\_BIAS. Therefore, to render to the resource, an application typically creates a view of format DXGI\_FORMAT\_R10G10B10A2\_UNORM.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Casting%20Ability%20of%20XR%20Formats%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




