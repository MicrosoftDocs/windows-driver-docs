---
title: KSPROPERTY\_AUDIOENGINE enumeration
description: The properties contained in the KSPROPSETID\_AudioEngine property set are defined by this enumeration and must be supported by a KSNODETYPE\_AUDIO\_ENGINE node.
ms.assetid: F20C05A3-C8A0-4061-93B9-03FD19D37C82
keywords: ["KSPROPERTY_AUDIOENGINE enumeration Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIOENGINE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIOENGINE enumeration


The properties contained in the [KSPROPSETID\_AudioEngine](kspropsetid-audioengine.md) property set are defined by this enumeration and must be supported by a [**KSNODETYPE\_AUDIO\_ENGINE**](ksnodetype-audio-engine.md) node.

Syntax
------

```ManagedCPlusPlus
typedef enum  { 
  KSPROPERTY_AUDIOENGINE_LFXENABLE               = 0,
  KSPROPERTY_AUDIOENGINE_GFXENABLE               = 1,
  KSPROPERTY_AUDIOENGINE_MIXFORMAT               = 2,
  KSPROPERTY_AUDIOENGINE_DEVICEFORMAT            = 4,
  KSPROPERTY_AUDIOENGINE_SUPPORTEDDEVICEFORMATS  = 5,
  KSPROPERTY_AUDIOENGINE_DESCRIPTOR              = 6,
  KSPROPERTY_AUDIOENGINE_BUFFER_SIZE_RANGE       = 7,
  KSPROPERTY_AUDIOENGINE_LOOPBACK_PROTECTION     = 8,
  KSPROPERTY_AUDIOENGINE_VOLUMELEVEL             = 9
} KSPROPERTY_AUDIOENGINE;
```

Constants
---------

<span id="KSPROPERTY_AUDIOENGINE_LFXENABLE"></span><span id="ksproperty_audioengine_lfxenable"></span>**KSPROPERTY\_AUDIOENGINE\_LFXENABLE**  
Specifies the ID for the [**KSPROPERTY\_AUDIOENGINE\_LFXENABLE**](ksproperty-audioengine-lfx-enable.md) property.

<span id="KSPROPERTY_AUDIOENGINE_GFXENABLE"></span><span id="ksproperty_audioengine_gfxenable"></span>**KSPROPERTY\_AUDIOENGINE\_GFXENABLE**  
Specifies the ID for the [**KSPROPERTY\_AUDIOENGINE\_GFXENABLE**](ksproperty-audioengine-gfx-enable.md) property.

<span id="KSPROPERTY_AUDIOENGINE_MIXFORMAT"></span><span id="ksproperty_audioengine_mixformat"></span>**KSPROPERTY\_AUDIOENGINE\_MIXFORMAT**  
Specifies the ID for the [**KSPROPERTY\_AUDIOENGINE\_MIXFORMAT**](ksproperty-audioengine-mixformat.md) property.

<span id="KSPROPERTY_AUDIOENGINE_DEVICEFORMAT"></span><span id="ksproperty_audioengine_deviceformat"></span>**KSPROPERTY\_AUDIOENGINE\_DEVICEFORMAT**  
Specifies the ID for the [**KSPROPERTY\_AUDIOENGINE\_DEVICEFORMAT**](ksproperty-audioengine-deviceformat.md) property.

<span id="KSPROPERTY_AUDIOENGINE_SUPPORTEDDEVICEFORMATS"></span><span id="ksproperty_audioengine_supporteddeviceformats"></span>**KSPROPERTY\_AUDIOENGINE\_SUPPORTEDDEVICEFORMATS**  
Specifies the ID for the [**KSPROPERTY\_AUDIOENGINE\_SUPPORTEDDEVICEFORMATS**](ksproperty-audioengine-supporteddeviceformats.md) property.

<span id="KSPROPERTY_AUDIOENGINE_DESCRIPTOR"></span><span id="ksproperty_audioengine_descriptor"></span>**KSPROPERTY\_AUDIOENGINE\_DESCRIPTOR**  
Specifies the ID for the [**KSPROPERTY\_AUDIOENGINE\_DESCRIPTOR**](ksproperty-audioengine-descriptor.md) property.

<span id="KSPROPERTY_AUDIOENGINE_BUFFER_SIZE_RANGE"></span><span id="ksproperty_audioengine_buffer_size_range"></span>**KSPROPERTY\_AUDIOENGINE\_BUFFER\_SIZE\_RANGE**  
Specifies the ID for the [**KSPROPERTY\_AUDIOENGINE\_BUFFER\_SIZE\_RANGE**](ksproperty-audioengine-buffer-size-limits.md) property.

<span id="KSPROPERTY_AUDIOENGINE_LOOPBACK_PROTECTION"></span><span id="ksproperty_audioengine_loopback_protection"></span>**KSPROPERTY\_AUDIOENGINE\_LOOPBACK\_PROTECTION**  
Specifies the ID for the [**KSPROPERTY\_AUDIOENGINE\_LOOPBACK\_PROTECTION**](ksproperty-audioengine-loopback-protection.md) property.

<span id="KSPROPERTY_AUDIOENGINE_VOLUMELEVEL"></span><span id="ksproperty_audioengine_volumelevel"></span>**KSPROPERTY\_AUDIOENGINE\_VOLUMELEVEL**  
Specifies the ID for the [**KSPROPERTY\_AUDIOENGINE\_VOLUMELEVEL**](ksproperty-audioengine-volumelevel.md) property.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 8</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2012</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSNODETYPE\_AUDIO\_ENGINE**](ksnodetype-audio-engine.md)

[KSPROPSETID\_AudioEngine](kspropsetid-audioengine.md)

 

 






