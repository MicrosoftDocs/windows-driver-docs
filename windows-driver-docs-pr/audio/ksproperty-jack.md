---
title: KSPROPERTY\_JACK enumeration
description: The KSPROPERTY\_JACK enumeration defines new property IDs that are used by audio jack structures.
ms.assetid: d20a0b08-f20e-43a2-9ff5-eb0b9d1ea54e
keywords: ["KSPROPERTY_JACK enumeration Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_JACK
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_JACK enumeration


The `KSPROPERTY_JACK` enumeration defines new property IDs that are used by audio jack structures.

Syntax
------

```ManagedCPlusPlus
typedef enum  { 
  KSPROPERTY_JACK_DESCRIPTION   = 1,
  KSPROPERTY_JACK_DESCRIPTION2  = 2,
  KSPROPERTY_JACK_SINK_INFO     = 3,
  KSPROPERTY_JACK_CONTAINERID
} KSPROPERTY_JACK;
```

Constants
---------

<span id="KSPROPERTY_JACK_DESCRIPTION"></span><span id="ksproperty_jack_description"></span>**KSPROPERTY\_JACK\_DESCRIPTION**  
Specifies the ID for the [**KSPROPERTY\_JACK\_DESCRIPTION**](ksproperty-jack-description.md) property.

<span id="KSPROPERTY_JACK_DESCRIPTION2"></span><span id="ksproperty_jack_description2"></span>**KSPROPERTY\_JACK\_DESCRIPTION2**  
Specifies the ID for the [**KSPROPERTY\_JACK\_DESCRIPTION2**](ksproperty-jack-description2.md) property.

<span id="KSPROPERTY_JACK_SINK_INFO"></span><span id="ksproperty_jack_sink_info"></span>**KSPROPERTY\_JACK\_SINK\_INFO**  
Specifies the ID for the [**KSPROPERTY\_JACK\_SINK\_INFO**](ksproperty-jack-sink-info.md) property.

<span id="KSPROPERTY_JACK_CONTAINERID"></span><span id="ksproperty_jack_containerid"></span>**KSPROPERTY\_JACK\_CONTAINERID**  
Specifies the ID for the [**KSPROPERTY\_JACK\_CONTAINERID**](ksproperty-jack-containerid.md) property.

Remarks
-------

None

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows 7 and later Windows operating systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY\_JACK\_DESCRIPTION**](ksproperty-jack-description.md)

 

 






