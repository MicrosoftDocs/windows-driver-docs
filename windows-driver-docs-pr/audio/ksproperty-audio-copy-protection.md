---
title: KSPROPERTY\_AUDIO\_COPY\_PROTECTION
description: The KSPROPERTY\_AUDIO\_COPY\_PROTECTION property specifies the copy-protection status of an audio stream.
ms.assetid: 68896bd4-9ffe-4632-a3b2-441b5d04208a
keywords: ["KSPROPERTY_AUDIO_COPY_PROTECTION Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_COPY_PROTECTION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_COPY\_PROTECTION


The KSPROPERTY\_AUDIO\_COPY\_PROTECTION property specifies the copy-protection status of an audio stream.

## <span id="ddk_ksproperty_audio_copy_protection_ks"></span><span id="DDK_KSPROPERTY_AUDIO_COPY_PROTECTION_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564262" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564262)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537084" data-raw-source="[&lt;strong&gt;KSAUDIO_COPY_PROTECTION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537084)"><strong>KSAUDIO_COPY_PROTECTION</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type KSAUDIO\_COPY\_PROTECTION. The structure specifies whether a stream is copyrighted; it also specifies whether the stream is an original stream or a copy of the original stream.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_COPY\_PROTECTION property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

The KSPROPERTY\_AUDIO\_COPY\_PROTECTION property is a property of an audio device that supports a protection scheme similar to the Serial Copy Management System (SCMS). The property indicates whether a digital stream is protected by copyright and whether it is an original stream or a copy.

SCMS can provide three levels of protection of audio content:

**Level 0:** Unrestricted copying of a stream that either lacks a copyright or does not assert a copyright.

**Level 1:** Restriction of copying to first-generation streams. Users can make copies of the original copyrighted stream, but they cannot make copies of copies of the stream.

**Level 2:** No copying at all of the stream.

The KSPROPERTY\_AUDIO\_COPY\_PROTECTION property is separate from and unrelated to the implementation of [Digital Rights Management (DRM)](https://msdn.microsoft.com/library/windows/hardware/ff536260) and the Secure Audio Path (SAP) for Windows Media. For information about SAP, see the Microsoft Windows SDK documentation.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

[**KSAUDIO\_COPY\_PROTECTION**](https://msdn.microsoft.com/library/windows/hardware/ff537084)

 

 






