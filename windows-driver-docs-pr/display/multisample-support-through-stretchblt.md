---
title: Multisample Support through StretchBlt
description: Multisample Support through StretchBlt
ms.assetid: c829c612-d09d-4a33-a117-e50b9ed57251
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , multisample rendering, StretchBlt
- multisample rendering WDK DirectX 8.0 , StretchBlt
- rendering multisamples WDK DirectX 8.0 , StretchBlt
- stretch blit operations WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Multisample Support through StretchBlt


## <span id="ddk_multisample_support_through_stretchblt_gg"></span><span id="DDK_MULTISAMPLE_SUPPORT_THROUGH_STRETCHBLT_GG"></span>


Although not the recommended mechanism for supporting multisampling, the driver can implement multisampling support by rendering to a large back buffer and performing a stretch blt to resample the large back buffer to the lower resolution primary. However, if this is the mechanism by which the driver supports multisampling, the driver must set the new capability bit D3DPRASTERCAPS\_STRETCHBLTMULTISAMPLE in the **RasterCaps** member of the D3D8CAPS structure. For a description of D3DCAPS8, see the DirectX 8.0 SDK documentation.

When the driver sets the D3DPRASTERCAPS\_STRETCHBLTMULTISAMPLE bit, it indicates that it:

-   Fails requests from applications to enable and disable full-scene anti-aliasing while the same scene is being rendered. That is, it fails requests to turn on and off the **BOOL** value of the D3DRS\_MULTISAMPLEANTIALIAS device render state (D3DRENDERSTATETYPE) during the rendering of a single scene. Note that requests to change the **BOOL** value of D3DRS\_MULTISAMPLEANTIALIAS must not fail for a different scene. That is, if D3DRS\_MULTISAMPLEANTIALIAS is **TRUE** for one scene, it could be **FALSE** for another scene.

-   Is nonresponsive to requests from applications to modify samples in a multisample render target. That is, it does not respond to setting the bitmask of the D3DRS\_MULTISAMPLEMASK device render state (D3DRENDERSTATETYPE).

It is important to note that if the driver uses a stretch blt to perform a page flip in fullscreen mode, the driver should specify the supported sample counts in the **wFlipMSTypes** member of the [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274)'s **MultiSampleCaps** structure and not the **wBltMSTypes** member as a flip is being performed.

 

 





