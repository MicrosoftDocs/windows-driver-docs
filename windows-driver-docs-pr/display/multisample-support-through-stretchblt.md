---
title: Multisample Support through StretchBlt
description: Multisample Support through StretchBlt
ms.assetid: c829c612-d09d-4a33-a117-e50b9ed57251
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , multisample rendering, StretchBlt
- multisample rendering WDK DirectX 8.0 , StretchBlt
- rendering multisamples WDK DirectX 8.0 , StretchBlt
- stretch blit operations WDK DirectX 8.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Multisample Support through StretchBlt


## <span id="ddk_multisample_support_through_stretchblt_gg"></span><span id="DDK_MULTISAMPLE_SUPPORT_THROUGH_STRETCHBLT_GG"></span>


Although not the recommended mechanism for supporting multisampling, the driver can implement multisampling support by rendering to a large back buffer and performing a stretch blt to resample the large back buffer to the lower resolution primary. However, if this is the mechanism by which the driver supports multisampling, the driver must set the new capability bit D3DPRASTERCAPS\_STRETCHBLTMULTISAMPLE in the **RasterCaps** member of the D3D8CAPS structure. For a description of D3DCAPS8, see the DirectX 8.0 SDK documentation.

When the driver sets the D3DPRASTERCAPS\_STRETCHBLTMULTISAMPLE bit, it indicates that it:

-   Fails requests from applications to enable and disable full-scene anti-aliasing while the same scene is being rendered. That is, it fails requests to turn on and off the **BOOL** value of the D3DRS\_MULTISAMPLEANTIALIAS device render state (D3DRENDERSTATETYPE) during the rendering of a single scene. Note that requests to change the **BOOL** value of D3DRS\_MULTISAMPLEANTIALIAS must not fail for a different scene. That is, if D3DRS\_MULTISAMPLEANTIALIAS is **TRUE** for one scene, it could be **FALSE** for another scene.

-   Is nonresponsive to requests from applications to modify samples in a multisample render target. That is, it does not respond to setting the bitmask of the D3DRS\_MULTISAMPLEMASK device render state (D3DRENDERSTATETYPE).

It is important to note that if the driver uses a stretch blt to perform a page flip in fullscreen mode, the driver should specify the supported sample counts in the **wFlipMSTypes** member of the [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274)'s **MultiSampleCaps** structure and not the **wBltMSTypes** member as a flip is being performed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Multisample%20Support%20through%20StretchBlt%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




