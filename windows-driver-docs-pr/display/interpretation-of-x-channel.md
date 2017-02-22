---
title: Interpretation of X Channel
description: Interpretation of X Channel
ms.assetid: ba039e5a-78ee-43cb-b883-4675b011a29d
keywords: ["Direct3D version 10.1 WDK Windows 7 display , X channel", "extended format WDK Windows 7 display , X channel", "X channel WDK Windows 7 display"]
---

# Interpretation of X Channel


This section applies only to Windows 7 and later operating systems.

The user-mode display driver should read the X channel in all formats that include X (for example, DXGI\_FORMAT\_B8G8R8X8\_UNORM) as 1.0f when such formats are presented to filtering hardware or the blender.

The X channel must be copied unmodified when data is moved outside of the 3-D pipeline (that is, when an application calls the **ID3D10Device::CopyResource**, **ID3D10Device::CopySubresourceRegion**, or **ID3D10Device::UpdateSubResource** method). For more information about these methods, see the DirectX SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Interpretation%20of%20X%20Channel%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




