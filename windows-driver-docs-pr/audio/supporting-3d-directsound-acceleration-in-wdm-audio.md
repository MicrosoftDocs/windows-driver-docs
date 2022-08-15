---
title: Supporting 3D DirectSound Acceleration in WDM Audio
description: Supporting 3D DirectSound Acceleration in WDM Audio
keywords:
- hardware acceleration WDK DirectSound , 3D mixing
- 3D mixing WDK audio
ms.date: 04/20/2017
---

# Supporting 3D DirectSound Acceleration in WDM Audio


## <span id="supporting_3d_directsound_acceleration_in_wdm_audio"></span><span id="SUPPORTING_3D_DIRECTSOUND_ACCELERATION_IN_WDM_AUDIO"></span>


DirectSound exposes hardware-accelerated 3D mixing for WDM audio miniport drivers that meet the following requirements:

-   The pin must meet the requirements listed in [Supporting 2D DirectSound Acceleration in WDM Audio](supporting-2d-directsound-acceleration-in-wdm-audio.md).

-   The pin should include a 3D node ([**KSNODETYPE\_3D\_EFFECTS**](./ksnodetype-3d-effects.md)) in its node chain. (See [DirectSound Node-Ordering Requirements](directsound-node-ordering-requirements.md).)

-   The pin must support the [KSPROPSETID\_DirectSound3DBuffer](./kspropsetid-directsound3dbuffer.md) property set on the 3D node.

-   The pin must support the [KSPROPSETID\_DirectSound3DListener](./kspropsetid-directsound3dlistener.md) property set on the 3D node.

 

