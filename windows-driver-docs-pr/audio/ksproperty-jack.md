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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_JACK%20enumeration%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





