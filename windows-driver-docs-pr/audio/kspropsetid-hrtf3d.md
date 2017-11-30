---
title: KSPROPSETID\_Hrtf3d
description: KSPROPSETID\_Hrtf3d
ms.assetid: 8045991b-0409-445a-bd35-d9b8644f770e
keywords: ["KSPROPSETID_Hrtf3d"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPSETID\_Hrtf3d


## <span id="ddk_kspropsetid_hrtf3d_ks"></span><span id="DDK_KSPROPSETID_HRTF3D_KS"></span>


The `KSPROPSETID_Hrtf3d` property set is used to configure the 3D head-relative transfer function (HRTF) for a DirectSound buffer. This set contains optional properties of a 3D node ([**KSNODETYPE\_3D\_EFFECTS**](ksnodetype-3d-effects.md)) on a DirectSound pin instance.

Not all 3D nodes support HRTF processing. A client can send a basic-support query for an HRTF property to a 3D node to determine whether that node is capable of performing HRTF processing. A 3D node that supports the `KSPROPSETID_Hrtf3d` property set must support all three of the properties in the set.

The definition of this property set assumes that the HRTF algorithm is implemented with infinite impulse response (IIR) filters that represent the effects of an audio source at a single position.

Digital filters typically have an initial transient response. When moving a source from one position to the next, the filter coefficients change and the HRTF algorithm cross-fades the outputs from the filter at the old position to the filter at the new position. The **FilterTransientMuteLength** member of the [**KSDS3D\_HRTF\_INIT\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff537106) structure specifies the number of samples by which to delay the cross fade in order to avoid rendering the new filter's initial transient. During this time, the output comes from the old filters only. The **FilterOverlapBufferLength** member (same structure) specifies the total number of samples over which to mute and cross-fade the filter outputs.

When the source moves from the right half-plane to the left, the filters switch. This switch might cause an audible pop. The **SwapChannels** member of the [**KSDS3D\_HRTF\_PARAMS\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff537108) structure tells the HRTF algorithm to swap the outputs to reverse the location of the source to the other half-plane. The **CrossFadeOutput** member (same structure) tells the algorithm to cross-fade the output channels after a transition across azimuth angle zero. The **OutputOverlapBufferLength** member of KSDS3D\_HRTF\_INIT\_MSG specifies the number of samples over which to cross-fade when this transition occurs.

Because of symmetry, only half of the filter coefficients need to be downloaded to the HRTF algorithm when the azimuth angle is zero. The **ZeroAzimuth** member of KSDS3D\_HRTF\_PARAMS\_MSG indicates when this condition occurs.

For information about configuring HTRF processing through the DirectSound API, see the Microsoft Windows SDK documentation.

The `KSPROPSETID_Hrtf3d` property set contains the following three members:

[**KSPROPERTY\_HRTF3D\_FILTER\_FORMAT**](ksproperty-hrtf3d-filter-format.md)

[**KSPROPERTY\_HRTF3D\_INITIALIZE**](ksproperty-hrtf3d-initialize.md)

[**KSPROPERTY\_HRTF3D\_PARAMS**](ksproperty-hrtf3d-params.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPSETID_Hrtf3d%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




