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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td align="left"><p>[<strong>KSAUDIO_COPY_PROTECTION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537084)</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_AUDIO_COPY_PROTECTION%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





