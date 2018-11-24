---
title: Supporting 3D DirectSound Acceleration in WDM Audio
description: Supporting 3D DirectSound Acceleration in WDM Audio
ms.assetid: 7524c15a-e487-43b6-9101-7cdd0c5e6e0c
keywords:
- hardware acceleration WDK DirectSound , 3D mixing
- 3D mixing WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting 3D DirectSound Acceleration in WDM Audio


## <span id="supporting_3d_directsound_acceleration_in_wdm_audio"></span><span id="SUPPORTING_3D_DIRECTSOUND_ACCELERATION_IN_WDM_AUDIO"></span>


DirectSound exposes hardware-accelerated 3D mixing for WDM audio miniport drivers that meet the following requirements:

-   The pin must meet the requirements listed in [Supporting 2D DirectSound Acceleration in WDM Audio](supporting-2d-directsound-acceleration-in-wdm-audio.md).

-   The pin should include a 3D node ([**KSNODETYPE\_3D\_EFFECTS**](https://msdn.microsoft.com/library/windows/hardware/ff537148)) in its node chain. (See [DirectSound Node-Ordering Requirements](directsound-node-ordering-requirements.md).)

-   The pin must support the [KSPROPSETID\_DirectSound3DBuffer](https://msdn.microsoft.com/library/windows/hardware/ff537447) property set on the 3D node.

-   The pin must support the [KSPROPSETID\_DirectSound3DListener](https://msdn.microsoft.com/library/windows/hardware/ff537449) property set on the 3D node.

 

 




