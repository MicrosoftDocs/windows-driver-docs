---
title: Supporting 3D DirectSound Acceleration in WDM Audio
description: Supporting 3D DirectSound Acceleration in WDM Audio
ms.assetid: 7524c15a-e487-43b6-9101-7cdd0c5e6e0c
keywords:
- hardware acceleration WDK DirectSound , 3D mixing
- 3D mixing WDK audio
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting 3D DirectSound Acceleration in WDM Audio


## <span id="supporting_3d_directsound_acceleration_in_wdm_audio"></span><span id="SUPPORTING_3D_DIRECTSOUND_ACCELERATION_IN_WDM_AUDIO"></span>


DirectSound exposes hardware-accelerated 3D mixing for WDM audio miniport drivers that meet the following requirements:

-   The pin must meet the requirements listed in [Supporting 2D DirectSound Acceleration in WDM Audio](supporting-2d-directsound-acceleration-in-wdm-audio.md).

-   The pin should include a 3D node ([**KSNODETYPE\_3D\_EFFECTS**](https://msdn.microsoft.com/library/windows/hardware/ff537148)) in its node chain. (See [DirectSound Node-Ordering Requirements](directsound-node-ordering-requirements.md).)

-   The pin must support the [KSPROPSETID\_DirectSound3DBuffer](https://msdn.microsoft.com/library/windows/hardware/ff537447) property set on the 3D node.

-   The pin must support the [KSPROPSETID\_DirectSound3DListener](https://msdn.microsoft.com/library/windows/hardware/ff537449) property set on the 3D node.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Supporting%203D%20DirectSound%20Acceleration%20in%20WDM%20Audio%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


