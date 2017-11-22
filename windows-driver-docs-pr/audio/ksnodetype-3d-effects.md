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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSNODETYPE_3D_EFFECTS%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




