---
title: KSPROPSETID\_DirectSound3DBuffer
description: KSPROPSETID\_DirectSound3DBuffer
ms.assetid: 38ee775a-9b6c-4803-a024-fecc852d122d
keywords: ["KSPROPSETID_DirectSound3DBuffer"]
---

# KSPROPSETID\_DirectSound3DBuffer


## <span id="ddk_kspropsetid_directsound3dbuffer_ks"></span><span id="DDK_KSPROPSETID_DIRECTSOUND3DBUFFER_KS"></span>


The `KSPROPSETID_DirectSound3DBuffer` property set contains all the device-specific properties that are needed to implement the **IDirectSound3DBuffer** interface (see the Microsoft Windows SDK documentation). Using this property set, the 3D-buffer properties that are specified by the API are passed directly between DirectSound and the WDM audio driver. This property set is handled by the [**KSNODETYPE\_3D\_EFFECTS**](ksnodetype-3d-effects.md) node, which handles both the 3D-buffer and 3D-listener properties.

The property items in this set are specified by KSPROPERTY\_DIRECTSOUND3DBUFFER enumeration values.

The `KSPROPSETID_DirectSound3DBuffer` property set contains the following properties:

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_ALL**](ksproperty-directsound3dbuffer-all.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEANGLES**](ksproperty-directsound3dbuffer-coneangles.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEORIENTATION**](ksproperty-directsound3dbuffer-coneorientation.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEOUTSIDEVOLUME**](ksproperty-directsound3dbuffer-coneoutsidevolume.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_MAXDISTANCE**](ksproperty-directsound3dbuffer-maxdistance.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_MINDISTANCE**](ksproperty-directsound3dbuffer-mindistance.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_MODE**](ksproperty-directsound3dbuffer-mode.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_POSITION**](ksproperty-directsound3dbuffer-position.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_VELOCITY**](ksproperty-directsound3dbuffer-velocity.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPSETID_DirectSound3DBuffer%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




