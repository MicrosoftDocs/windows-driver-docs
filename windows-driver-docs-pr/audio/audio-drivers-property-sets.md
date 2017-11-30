---
title: Audio Drivers Property Sets
description: Audio Drivers Property Sets
ms.assetid: bac74ad5-3a9b-40b1-ae49-c86558c34e94
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Audio Drivers Property Sets


## <span id="ddk_audio_drivers_property_sets_ks"></span><span id="DDK_AUDIO_DRIVERS_PROPERTY_SETS_KS"></span>


This section describes the audio-specific property sets that are available for audio drivers that use WDM kernel-streaming services in Microsoft Windows 2000 and later, and in Windows Millennium Edition (Me) and Windows 98.

The reference page for each property contains a table with the following column headings.

| Get | Set | Target | Property descriptor type | Property value type |
|-----|-----|--------|--------------------------|---------------------|

 

These headings have the following meanings:

-   **Get**

    Does the target KS object support the KSPROPERTY\_TYPE\_GET property request? (Specify yes or no.)

-   **Set**

    Does the target KS object support the KSPROPERTY\_TYPE\_SET property request? (Specify yes or no.)

-   **Target**

    The target for the request is the KS object that the property request is sent to. The target for an audio property is either a filter or a pin. (The property request specifies the target object by its kernel handle.)

-   **Property Descriptor Type**

    The property descriptor specifies the property and the operation to perform on that property. The descriptor always begins with a [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262) structure, but some types of descriptor contain additional information. For example, the [**KSNODEPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537143) structure is a property descriptor that begins with a KSPROPERTY structure but also includes a node ID.

-   **Property Value Type**

    A property typically has a value, and the type of this value depends on the property. For example, a property that can be in one of only two states--on or off--typically has a BOOL value. A property that can assume integer values from 0 to 0xFFFFFFFF might have a ULONG value. More complex properties might have values that are arrays or structures.

The preceding property descriptor and property value are the property-specific versions of the instance-specification and operation-data buffers that are discussed in [KS Properties, Events, and Methods](https://msdn.microsoft.com/library/windows/hardware/ff567673).

A property request uses one of the following flags to specify the operation that is to be performed on the property:

-   KSPROPERTY\_TYPE\_BASICSUPPORT

-   KSPROPERTY\_TYPE\_GET

-   KSPROPERTY\_TYPE\_SET

All filter and pin objects support the basic-support operation on their properties. Whether they support the get and set operations depends on the property. A property that represents an inherent capability of the filter or pin object is likely to require only a get operation. A property that represents a configurable setting might require only a set operation, although a get operation might also be useful for reading the current setting. For more information about using the get, set, and basic-support operations with audio properties, see [Audio Endpoints, Properties and Events](https://msdn.microsoft.com/library/windows/hardware/ff536199).

The following property sets are defined for audio drivers:

[KSPROPSETID\_AC3](kspropsetid-ac3.md)

[KSPROPSETID\_Acoustic\_Echo\_Cancel](kspropsetid-acoustic-echo-cancel.md)

[KSPROPSETID\_Audio](kspropsetid-audio.md)

[KSPROPSETID\_AudioEngine](kspropsetid-audioengine.md)

[KSPROPSETID\_AudioGfx](kspropsetid-audiogfx.md)

[KSPROPSETID\_DirectSound3DBuffer](kspropsetid-directsound3dbuffer.md)

[KSPROPSETID\_DirectSound3DListener](kspropsetid-directsound3dlistener.md)

[KSPROPSETID\_DrmAudioStream](kspropsetid-drmaudiostream.md)

[KSPROPSETID\_FMRXTopology](kspropsetid-fmrxtopology.md)

[KSPROPSETID\_Hrtf3d](kspropsetid-hrtf3d.md)

[KSPROPSETID\_Itd3d](kspropsetid-itd3d.md)

[KSPROPSETID\_Jack](kspropsetid-jack.md)

[KSPROPSETID\_RTAudio](kspropsetid-rtaudio.md)

[KSPROPSETID\_SoundDetector](kspropsetid-sounddetector.md)

[KSPROPSETID\_Synth](kspropsetid-synth.md)

[KSPROPSETID\_SynthClock](kspropsetid-synthclock.md)

[KSPROPSETID\_Synth\_Dls](kspropsetid-synth-dls.md)

[KSPROPSETID\_Sysaudio](kspropsetid-sysaudio.md)

[KSPROPSETID\_Sysaudio\_Pin](kspropsetid-sysaudio-pin.md)

[KSPROPSETID\_TelephonyControl](kspropsetid-telephonycontrol.md)

[KSPROPSETID\_TelephonyTopology](kspropsetid-telephonytopology.md)

[KSPROPSETID\_TopologyNode](kspropsetid-topologynode.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Audio%20Drivers%20Property%20Sets%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




