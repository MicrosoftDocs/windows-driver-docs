---
title: Extensible Wave-Format Descriptors
description: Extensible Wave-Format Descriptors
keywords:
- wave-format descriptors WDK audio
- wave-format descriptors
- wave-format tags WDK audio
- wave streams WDK audio
- audio data formats WDK
- data formats WDK audio , wave-format descriptors
- formats WDK audio , wave-format descriptors
- KSDATAFORMAT structure
- WAVEFORMATEXTENSIBLE
- WAVEFORMATEX structure
- WDM audio data formats WDK
ms.date: 06/30/2020
ms.localizationpriority: medium
---

# Extensible Wave-Format Descriptors

The following figure shows the data-format descriptor for a wave audio stream.

![diagram illustrating a wave-format descriptor.](images/wavefmt.png)

As indicated in the figure, the amount of additional format information following the [**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat) structure varies depending on the data format.

Audio systems use this type of format descriptor in several ways:

- A format descriptor like the one shown in the preceding figure is passed as a call parameter to a miniport driver's **NewStream** method (for example, see [**IMiniportWaveCyclic::NewStream**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavecyclic-newstream)).

- The *ResultantFormat* parameter of the [**IMiniport::DataRangeIntersection**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiport-datarangeintersection) method points to a buffer into which the method writes a format descriptor like the one shown in the preceding figure.

- The [**KSPROPERTY\_PIN\_DATAINTERSECTION**](../stream/ksproperty-pin-dataintersection.md) get-property request retrieves a format descriptor like the one shown in the preceding figure.

- The [**KSPROPERTY\_PIN\_PROPOSEDATAFORMAT**](../stream/ksproperty-pin-proposedataformat.md) set-property request accepts a format descriptor like the one shown in the preceding figure.

- A similar format is used for the [**KsCreatePin**](/windows-hardware/drivers/ddi/ks/nf-ks-kscreatepin) function's *Connect* call parameter. This parameter points to the [**KSPIN\_CONNECT**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_connect) structure at the beginning of a buffer that also contains a format descriptor. The format descriptor, which immediately follows the KSPIN\_CONNECT structure, begins with a KSDATAFORMAT structure like the one shown in the preceding figure.

The format information that follows the KSDATAFORMAT structure should be  a [**WAVEFORMATEXTENSIBLE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-waveformatextensible) structure. WAVEFORMATEXTENSIBLE is an extended version of WAVEFORMATEX that can describe a broader range of formats than WAVEFORMATEX.

WAVEFORMAT is obsolete and is not supported by the WDM audio subsystem in any version of Microsoft Windows. PCMWAVEFORMAT structure is an extended version of WAVEFORMAT that is also obsolete.

The four wave-format structures--WAVEFORMAT, PCMWAVEFORMAT, WAVEFORMATEX, and WAVEFORMATEXTENSIBLE--all begin with the same five members, starting with **wFormatTag**. The preceding figure shows these four structures superimposed on each other to highlight the portions of the structures that are identical.

WAVEFORMATEXTENSIBLE extends WAVEFORMATEX by adding three members, beginning with **Samples**.wValidBitsPerSample. (**Samples** is a union whose other member, **wValidSamplesPerBlock**, is used instead of **wValidBitsPerSample** for some compressed formats.) The **wFormatTag** member, which immediately follows the end of the KSDATAFORMAT structure in the buffer, specifies what kind of format information follows KSDATAFORMAT.

Unlike WAVEFORMATEX, WAVEFORMATEXTENSIBLE can do the following:

1. Specify the number of bits per sample separately from the size of the sample container. For example, a 20-bit sample can be stored left-justified within a three-byte container. WAVEFORMATEX, which fails to distinguish the number of data bits per sample from the sample container size, is unable to describe such a format unambiguously.

2. Assign specific speaker locations to audio channels in multichannel streams. WAVEFORMATEX lacks this capability and can adequately support only mono and (two-channel) stereo streams.

## Legacy Use of WAVEFORMATEX

Any format that is described by WAVEFORMATEX can also be described by WAVEFORMATEXTENSIBLE. For information about converting a WAVEFORMATEX structure to WAVEFORMATEXTENSIBLE, see [Converting Between Format Tags and Subformat GUIDs](converting-between-format-tags-and-subformat-guids.md).

WAVEFORMATEX is sufficient for describing formats with sample sizes of 8 or 16 bits, but WAVEFORMATEXTENSIBLE is necessary to adequately describe formats with a sample precision of greater than 16 bits. Here are two examples:

- A stream with a sample precision of 24 bits can use a 32-bit container size for efficient processing, but can be converted to use a 24-bit container to improve storage efficiency without loss of data.

- When processing a stream with 24-bit sample data, a rendering device that provides only 20 bits of precision can use dithering to improve the fidelity of its output signal. Dithering, however, requires additional processing time, and if the original stream is accurate to only 20 bits, the additional processing is unnecessary.

In both of these examples, preserving signal quality while making the right tradeoff between processing and storage efficiency is possible only if both the sample precision and container size are known.

If a simple format can be unambiguously described by either a WAVEFORMATEX or a WAVEFORMATEXTENSIBLE structure, an audio driver has the option of selecting either structure to describe the format. However, audio drivers have typically used WAVEFORMATEX to specify mono and (two-channel) stereo PCM formats with 8-bit or 16-bit samples, and some older applications might expect all audio drivers to use WAVEFORMATEX to specify these formats.

If a driver supports an audio format that can be unambiguously specified as either a WAVEFORMATEX or a WAVEFORMATEXTENSIBLE structure, the driver should recognize the format regardless of which of the two structures a client application or component uses to specify the structure. For example, if an audio device supports a 44.1-kHz, 16-bit, stereo PCM format, the miniport driver's KSPROPERTY\_PIN\_PROPOSEDATAFORMAT property handler and its implementation of the **NewStream** method should accept that format regardless of whether the format is specified as a WAVEFORMATEX or a WAVEFORMATEXTENSIBLE structure.

To simplify the processing of format data, drivers typically use WAVEFORMATEXTENSIBLE structures to internally represent formats. This approach might require the conversion of an input WAVEFORMATEX structure to an internal WAVEFORMATEXTENSIBLE representation, or the conversion of an internal WAVEFORMATEXTENSIBLE representation to an output WAVEFORMATEX structure.

In WAVEFORMATEXTENSIBLE, **dwBitsPerSample** is the container size, and **wValidBitsPerSample** is the number of valid data bits per sample. Containers are always byte-aligned in memory, and the container size must be specified as a multiple of eight bits.
