---
title: KSPROPSETID\_Hrtf3d
description: KSPROPSETID\_Hrtf3d
ms.assetid: 8045991b-0409-445a-bd35-d9b8644f770e
keywords: ["KSPROPSETID_Hrtf3d"]
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





