---
title: KSPROPERTY\_SOUNDDETECTOR enumeration
description: The KSPROPERTY\_SOUNDDETECTOR enumeration defines constants that are used to register a filter for an audio capture device that also supports a detector.
ms.assetid: 6AF98B06-1531-4AC9-9E32-D812E6EA424C
keywords: ["KSPROPERTY_SOUNDDETECTOR enumeration Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_SOUNDDETECTOR
api_location:
- ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_SOUNDDETECTOR enumeration


The **KSPROPERTY\_SOUNDDETECTOR** enumeration defines constants that are used to register a filter for an audio capture device that also supports a detector.

Syntax
------

```ManagedCPlusPlus
typedef enum  { 
  KSPROPERTY_SOUNDDETECTOR_SUPPORTEDPATTERNS  = 1,
  KSPROPERTY_SOUNDDETECTOR_PATTERNS,
  KSPROPERTY_SOUNDDETECTOR_ARMED,
  KSPROPERTY_SOUNDDETECTOR_MATCHRESULT
} KSPROPERTY_SOUNDDETECTOR;
```

Constants
---------

<span id="KSPROPERTY_SOUNDDETECTOR_SUPPORTEDPATTERNS"></span><span id="ksproperty_sounddetector_supportedpatterns"></span>**KSPROPERTY\_SOUNDDETECTOR\_SUPPORTEDPATTERNS**  
Specifies the ID for the [**KSPROPERTY\_SOUNDDETECTOR\_SUPPORTEDPATTERNS**](ksproperty-sounddetector-supportedpatterns.md) property.

<span id="KSPROPERTY_SOUNDDETECTOR_PATTERNS"></span><span id="ksproperty_sounddetector_patterns"></span>**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**  
Specifies the ID for the [**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](ksproperty-sounddetector-patterns.md) property.

<span id="KSPROPERTY_SOUNDDETECTOR_ARMED"></span><span id="ksproperty_sounddetector_armed"></span>**KSPROPERTY\_SOUNDDETECTOR\_ARMED**  
Specifies the ID for the [**KSPROPERTY\_SOUNDDETECTOR\_ARMED**](ksproperty-sounddetector-armed.md) property.

<span id="KSPROPERTY_SOUNDDETECTOR_MATCHRESULT"></span><span id="ksproperty_sounddetector_matchresult"></span>**KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT**  
Specifies the ID for the [**KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT**](ksproperty-sounddetector-matchresult.md) property.

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
<td align="left"><p>Windows 10</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[KSPROPSETID\_SoundDetector](kspropsetid-sounddetector.md)

[**KSPROPERTY\_SOUNDDETECTOR\_SUPPORTEDPATTERNS**](ksproperty-sounddetector-supportedpatterns.md)

[**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](ksproperty-sounddetector-patterns.md)

[**KSPROPERTY\_SOUNDDETECTOR\_ARMED**](ksproperty-sounddetector-armed.md)

[**KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT**](ksproperty-sounddetector-matchresult.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_SOUNDDETECTOR%20enumeration%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





