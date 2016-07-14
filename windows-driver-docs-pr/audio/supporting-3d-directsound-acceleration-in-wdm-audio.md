---
Description: Supporting 3D DirectSound Acceleration in WDM Audio
MS-HAID: 'audio.supporting\_3d\_directsound\_acceleration\_in\_wdm\_audio'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Supporting 3D DirectSound Acceleration in WDM Audio
---

# Supporting 3D DirectSound Acceleration in WDM Audio


## <span id="supporting_3d_directsound_acceleration_in_wdm_audio"></span><span id="SUPPORTING_3D_DIRECTSOUND_ACCELERATION_IN_WDM_AUDIO"></span>


DirectSound exposes hardware-accelerated 3D mixing for WDM audio miniport drivers that meet the following requirements:

-   The pin must meet the requirements listed in [Supporting 2D DirectSound Acceleration in WDM Audio](supporting-2d-directsound-acceleration-in-wdm-audio.md).

-   The pin should include a 3D node ([**KSNODETYPE\_3D\_EFFECTS**](audio.ksnodetype_3d_effects)) in its node chain. (See [DirectSound Node-Ordering Requirements](directsound-node-ordering-requirements.md).)

-   The pin must support the [KSPROPSETID\_DirectSound3DBuffer](audio.kspropsetid_directsound3dbuffer) property set on the 3D node.

-   The pin must support the [KSPROPSETID\_DirectSound3DListener](audio.kspropsetid_directsound3dlistener) property set on the 3D node.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Supporting%203D%20DirectSound%20Acceleration%20in%20WDM%20Audio%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



