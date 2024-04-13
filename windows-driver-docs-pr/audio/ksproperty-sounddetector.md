---
title: KSPROPERTY_SOUNDDETECTOR Enumeration
description: The KSPROPERTY\_SOUNDDETECTOR enumeration defines constants that are used to register a filter for an audio capture device that also supports a detector.
keywords: ["KSPROPERTY_SOUNDDETECTOR enumeration Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_SOUNDDETECTOR
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 03/06/2023
---

# KSPROPERTY\_SOUNDDETECTOR enumeration

The **KSPROPERTY\_SOUNDDETECTOR** enumeration defines constants that are used to register a filter for an audio capture device that also supports a detector.

## Syntax

```cpp
typedef enum  { 
  KSPROPERTY_SOUNDDETECTOR_SUPPORTEDPATTERNS  = 1,
  KSPROPERTY_SOUNDDETECTOR_PATTERNS,
  KSPROPERTY_SOUNDDETECTOR_ARMED,
  KSPROPERTY_SOUNDDETECTOR_MATCHRESULT
} KSPROPERTY_SOUNDDETECTOR;
```

## Constants

<span id="KSPROPERTY_SOUNDDETECTOR_SUPPORTEDPATTERNS"></span><span id="ksproperty_sounddetector_supportedpatterns"></span>**KSPROPERTY\_SOUNDDETECTOR\_SUPPORTEDPATTERNS**  
Specifies the ID for the [**KSPROPERTY\_SOUNDDETECTOR\_SUPPORTEDPATTERNS**](ksproperty-sounddetector-supportedpatterns.md) property.

<span id="KSPROPERTY_SOUNDDETECTOR_PATTERNS"></span><span id="ksproperty_sounddetector_patterns"></span>**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**  
Specifies the ID for the [**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](ksproperty-sounddetector-patterns.md) property.

<span id="KSPROPERTY_SOUNDDETECTOR_ARMED"></span><span id="ksproperty_sounddetector_armed"></span>**KSPROPERTY\_SOUNDDETECTOR\_ARMED**  
Specifies the ID for the [**KSPROPERTY\_SOUNDDETECTOR\_ARMED**](ksproperty-sounddetector-armed.md) property.

<span id="KSPROPERTY_SOUNDDETECTOR_MATCHRESULT"></span><span id="ksproperty_sounddetector_matchresult"></span>**KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT**  
Specifies the ID for the [**KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT**](ksproperty-sounddetector-matchresult.md) property.

## Requirements

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

## See also

[**KSPROPSETID\_SoundDetector**](kspropsetid-sounddetector.md)

[**KSPROPERTY\_SOUNDDETECTOR\_SUPPORTEDPATTERNS**](ksproperty-sounddetector-supportedpatterns.md)

[**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](ksproperty-sounddetector-patterns.md)

[**KSPROPERTY\_SOUNDDETECTOR\_ARMED**](ksproperty-sounddetector-armed.md)

[**KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT**](ksproperty-sounddetector-matchresult.md)
