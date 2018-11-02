---
title: KSPROPSETID\_Audio
description: KSPROPSETID\_Audio
ms.assetid: b65620c1-0460-430d-999d-f46fe0a2702d
keywords: ["KSPROPSETID_Audio"]
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_Audio


## <span id="ddk_kspropsetid_audio_ks"></span><span id="DDK_KSPROPSETID_AUDIO_KS"></span>


The `KSPROPSETID_Audio` property set indicates the range of data and control supported by an audio stream. The miniport driver should support the KSPROPERTY\_AUDIO\_LATENCY property. All other properties in this property set are optional.

In cases where the hardware does not support a capability, the miniport driver should return an error for the get- and set-property calls so that the upper-layer driver can handle the call. For example, a miniport driver for hardware that does not support volume control should return an error for the [**KSPROPERTY\_AUDIO\_VOLUMELEVEL**](ksproperty-audio-volumelevel.md) calls, thus enabling a driver higher in the stack (such as a kernel mixer) to set the volume of a stream.

The property items in this set are specified by KSPROPERTY\_AUDIO enumeration values.

The following properties are part of the `KSPROPSETID_Audio` property set:

[**KSPROPERTY\_AUDIO\_3D\_INTERFACE**](ksproperty-audio-3d-interface.md)

[**KSPROPERTY\_AUDIO\_AGC**](ksproperty-audio-agc.md)

[**KSPROPERTY\_AUDIO\_ALGORITHM\_INSTANCE**](ksproperty-audio-algorithm-instance.md)

[**KSPROPERTY\_AUDIO\_BASS**](ksproperty-audio-bass.md)

[**KSPROPERTY\_AUDIO\_BASS\_BOOST**](ksproperty-audio-bass-boost.md)

[**KSPROPERTY\_AUDIO\_BUFFER\_DURATION**](ksproperty-audio-buffer-duration.md)

[**KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG**](ksproperty-audio-channel-config.md)

[**KSPROPERTY\_AUDIO\_CHORUS\_LEVEL**](ksproperty-audio-chorus-level.md)

[**KSPROPERTY\_AUDIO\_CHORUS\_MODULATION\_DEPTH**](ksproperty-audio-chorus-modulation-depth.md)

[**KSPROPERTY\_AUDIO\_CHORUS\_MODULATION\_RATE**](ksproperty-audio-chorus-modulation-rate.md)

[**KSPROPERTY\_AUDIO\_COPY\_PROTECTION**](ksproperty-audio-copy-protection.md)

[**KSPROPERTY\_AUDIO\_CPU\_RESOURCES**](ksproperty-audio-cpu-resources.md)

[**KSPROPERTY\_AUDIO\_DELAY**](ksproperty-audio-delay.md)

[**KSPROPERTY\_AUDIO\_DEMUX\_DEST**](ksproperty-audio-demux-dest.md)

[**KSPROPERTY\_AUDIO\_DEV\_SPECIFIC**](ksproperty-audio-dev-specific.md)

[**KSPROPERTY\_AUDIO\_DYNAMIC\_RANGE**](ksproperty-audio-dynamic-range.md)

[**KSPROPERTY\_AUDIO\_DYNAMIC\_SAMPLING\_RATE**](ksproperty-audio-dynamic-sampling-rate.md)

[**KSPROPERTY\_AUDIO\_EQ\_BANDS**](ksproperty-audio-eq-bands.md)

[**KSPROPERTY\_AUDIO\_EQ\_LEVEL**](ksproperty-audio-eq-level.md)

[**KSPROPERTY\_AUDIO\_FILTER\_STATE**](ksproperty-audio-filter-state.md)

[**KSPROPERTY\_AUDIO\_LATENCY**](ksproperty-audio-latency.md)

[**KSPROPERTY\_AUDIO\_LINEAR\_BUFFER\_POSITION**](ksproperty-audio-linear-buffer-position.md)

[**KSPROPERTY\_AUDIO\_LOUDNESS**](ksproperty-audio-loudness.md)

[**KSPROPERTY\_AUDIO\_MANUFACTURE\_GUID**](ksproperty-audio-manufacture-guid.md)

[**KSPROPERTY\_AUDIO\_MIC\_ARRAY\_GEOMETRY**](ksproperty-audio-mic-array-geometry.md)

[**KSPROPERTY\_AUDIO\_MIC\_SENSITIVITY**](ksproperty-audio-mic-sensitivity.md)

[**KSPROPERTY\_AUDIO\_MIC\_SNR**](ksproperty-audio-mic-snr.md)

[**KSPROPERTY\_AUDIO\_MID**](ksproperty-audio-mid.md)

[**KSPROPERTY\_AUDIO\_MIX\_LEVEL\_CAPS**](ksproperty-audio-mix-level-caps.md)

[**KSPROPERTY\_AUDIO\_MIX\_LEVEL\_TABLE**](ksproperty-audio-mix-level-table.md)

[**KSPROPERTY\_AUDIO\_MUTE**](ksproperty-audio-mute.md)

[**KSPROPERTY\_AUDIO\_MUX\_SOURCE**](ksproperty-audio-mux-source.md)

[**KSPROPERTY\_AUDIO\_NUM\_EQ\_BANDS**](ksproperty-audio-num-eq-bands.md)

[**KSPROPERTY\_AUDIO\_PEAKMETER**](ksproperty-audio-peakmeter.md)

[**KSPROPERTY\_AUDIO\_PEAKMETER2**](ksproperty-audio-peakmeter2.md)

[**KSPROPERTY\_AUDIO\_POSITION**](ksproperty-audio-position.md)

[**KSPROPERTY\_AUDIO\_POSITIONEX**](ksproperty-audio-positionex.md)

[**KSPROPERTY\_AUDIO\_PREFERRED\_STATUS**](ksproperty-audio-preferred-status.md)

[**KSPROPERTY\_AUDIO\_PRESENTATION\_POSITION**](ksproperty-audio-presentation-position.md)

[**KSPROPERTY\_AUDIO\_PRODUCT\_GUID**](ksproperty-audio-product-guid.md)

[**KSPROPERTY\_AUDIO\_QUALITY**](ksproperty-audio-quality.md)

[**KSPROPERTY\_AUDIO\_REVERB\_LEVEL**](ksproperty-audio-reverb-level.md)

[**KSPROPERTY\_AUDIO\_REVERB\_TIME**](ksproperty-audio-reverb-time.md)

[**KSPROPERTY\_AUDIO\_SAMPLING\_RATE**](ksproperty-audio-sampling-rate.md)

[**KSPROPERTY\_AUDIO\_STEREO\_ENHANCE**](ksproperty-audio-stereo-enhance.md)

[**KSPROPERTY\_AUDIO\_STEREO\_SPEAKER\_GEOMETRY**](ksproperty-audio-stereo-speaker-geometry.md)

[**KSPROPERTY\_AUDIO\_SURROUND\_ENCODE**](ksproperty-audio-surround-encode.md)

[**KSPROPERTY\_AUDIO\_TREBLE**](ksproperty-audio-treble.md)

[**KSPROPERTY\_AUDIO\_VOLUMELEVEL**](ksproperty-audio-volumelevel.md)

[**KSPROPERTY\_AUDIO\_VOLUMELIMIT\_ENGAGED**](ksproperty-audio-volumelimit-engaged.md)

[**KSPROPERTY\_AUDIO\_WAVERT\_CURRENT\_WRITE\_POSITION**](ksproperty-audio-wavert-current-write-position.md)

[**KSPROPERTY\_AUDIO\_WAVERT\_CURRENT\_WRITE\_LASTBUFFER\_POSITION**](ksproperty-audio-wavert-current-write-lastbuffer-position.md)

[**KSPROPERTY\_AUDIO\_WIDE\_MODE**](ksproperty-audio-wide-mode.md)

[**KSPROPERTY\_AUDIO\_WIDENESS**](ksproperty-audio-wideness.md)

 

 





