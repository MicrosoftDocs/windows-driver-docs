---
title: KSNODETYPE\_3D\_EFFECTS
description: KSNODETYPE\_3D\_EFFECTS
ms.assetid: 8b19423b-c1ad-4b59-bdae-a53bb99469ea
keywords: ["KSNODETYPE_3D_EFFECTS Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_3D_EFFECTS
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSNODETYPE\_3D\_EFFECTS


## <span id="ddk_ksnodetype_3d_effects_ks"></span><span id="DDK_KSNODETYPE_3D_EFFECTS_KS"></span>


The KSNODETYPE\_3D\_EFFECTS node represents a 3D-effects processor for the device-specific 3D HAL (hardware acceleration layer) that underlies the **IDirectSound3DBuffer** and **IDirectSound3DListener** APIs (described in the Microsoft Windows SDK documentation). The 3D node has one input stream with either one or two channels and one output stream with *n* channels. It positions the individual channels of the input stream within the 3D-sound field of the output stream.

The input stream to the 3D node typically contains a single channel. In DirectSound 8.0 and later, only mono PCM buffers can be created with 3D effects. Earlier versions of DirectSound, however, support 3D nodes with both mono and stereo input streams, and drivers should support both in order to ensure compatibility with older applications.

The KSNODETYPE\_3D\_EFFECTS node is used to control the DirectSound speaker configuration through the following optional properties:

[**KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG**](ksproperty-audio-channel-config.md)

[**KSPROPERTY\_AUDIO\_STEREO\_SPEAKER\_GEOMETRY**](ksproperty-audio-stereo-speaker-geometry.md)

For more information, see [DirectSound Speaker-Configuration Settings](https://msdn.microsoft.com/library/windows/hardware/ff536332).

In addition, DirectSound requires that a KSNODETYPE\_3D\_EFFECTS node support the following 3D-listener and 3D-buffer properties:

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_ALL**](ksproperty-directsound3dbuffer-all.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_POSITION**](ksproperty-directsound3dbuffer-position.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_VELOCITY**](ksproperty-directsound3dbuffer-velocity.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEANGLES**](ksproperty-directsound3dbuffer-coneangles.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEORIENTATION**](ksproperty-directsound3dbuffer-coneorientation.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEOUTSIDEVOLUME**](ksproperty-directsound3dbuffer-coneoutsidevolume.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_MINDISTANCE**](ksproperty-directsound3dbuffer-mindistance.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_MAXDISTANCE**](ksproperty-directsound3dbuffer-maxdistance.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_MODE**](ksproperty-directsound3dbuffer-mode.md)

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_ALL**](ksproperty-directsound3dlistener-all.md)

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_POSITION**](ksproperty-directsound3dlistener-position.md)

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_VELOCITY**](ksproperty-directsound3dlistener-velocity.md)

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_ORIENTATION**](ksproperty-directsound3dlistener-orientation.md)

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_DISTANCEFACTOR**](ksproperty-directsound3dlistener-distancefactor.md)

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_ROLLOFFFACTOR**](ksproperty-directsound3dlistener-rollofffactor.md)

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_DOPPLERFACTOR**](ksproperty-directsound3dlistener-dopplerfactor.md)

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_BATCH**](ksproperty-directsound3dlistener-batch.md)

A KSNODETYPE\_3D\_EFFECTS node might implement a head-relative transfer function (HRTF), in which case it should support the following optional properties:

[**KSPROPERTY\_HRTF3D\_FILTER\_FORMAT**](ksproperty-hrtf3d-filter-format.md)

[**KSPROPERTY\_HRTF3D\_INITIALIZE**](ksproperty-hrtf3d-initialize.md)

[**KSPROPERTY\_HRTF3D\_PARAMS**](ksproperty-hrtf3d-params.md)

A KSNODETYPE\_3D\_EFFECTS node might implement an interaural time delay (ITD) algorithm, in which case it should support the following optional property:

[**KSPROPERTY\_ITD3D\_PARAMS**](ksproperty-itd3d-params.md)

 

 





