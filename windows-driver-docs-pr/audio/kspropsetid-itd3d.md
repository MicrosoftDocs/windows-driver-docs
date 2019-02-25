---
title: KSPROPSETID\_Itd3d
description: KSPROPSETID\_Itd3d
ms.assetid: 87159be4-740e-47c9-b16f-16ca4d01c793
keywords: ["KSPROPSETID_Itd3d"]
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_Itd3d


## <span id="ddk_kspropsetid_itd3d_ks"></span><span id="DDK_KSPROPSETID_ITD3D_KS"></span>


The `KSPROPSETID_Itd3d` property set is used to configure the interaural time delay (ITD) algorithm used by a 3D node ([**KSNODETYPE\_3D\_EFFECTS**](ksnodetype-3d-effects.md)).

The sound reaching a listener's left and right ears from a particular sound source is delayed by different amounts depending on the source's position. The listener can infer the direction of the sound source from the amount of differential delay. The ITD algorithm controls the differential delay to simulate a sound source at a particular location in 3D space.

The ITD algorithm provides an additional sound-positioning cue by controlling the amount by which the sound reaching each ear is muffled. High-frequency sounds can be muffled to simulate sound sources located behind the listener's head. For a sound source located near the right ear, for example, the sound reaching the left ear is more muffled than that reaching the right ear. A muffled sound is produced by combining the original signal from the sound source in some proportion with a low-pass filtered version of the same signal. Attenuating the original signal while increasing the contribution from the low-pass filtered version simulates the effect of moving the simulated sound source further behind the listener's head.

When the position of a sound source changes, the following parameters must be updated:

-   The amount of delay in the sound reaching each ear.

-   The amount by which the sound reaching each ear is muffled.

Making instantaneous changes to these parameters can cause clicks and other spurious noises. The ITD algorithm smoothes transitions in these parameters over a number of samples in order to filter out such noises.

For more information about the parameters used by the ITD algorithm, see [**KSDS3D\_ITD\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff537110).

This property set contains only a single property:

[**KSPROPERTY\_ITD3D\_PARAMS**](ksproperty-itd3d-params.md)

 

 





