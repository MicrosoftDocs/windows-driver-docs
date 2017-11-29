---
title: KSPROPERTY\_AUDIOSIGNALPROCESSING enumeration
description: The KSPROPERTY\_AUDIOSIGNALPROCESSING enumeration defines a constant that is used by audio drivers in connection with audio processing modes on pins.
ms.assetid: E0552FFF-E10F-496A-9D67-0AE06AF7B877
keywords: ["KSPROPERTY_AUDIOSIGNALPROCESSING enumeration Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIOSIGNALPROCESSING
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_AUDIOSIGNALPROCESSING enumeration


The KSPROPERTY\_AUDIOSIGNALPROCESSING enumeration defines a constant that is used by audio drivers in connection with audio processing modes on pins.

Syntax
------

```ManagedCPlusPlus
typedef enum _KSPROPERTY_AUDIOSIGNALPROCESSING { 
  KSPROPERTY_AUDIOSIGNALPROCESSING_MODES
} KSPROPERTY_AUDIOSIGNALPROCESSING;
```

Constants
---------

<span id="KSPROPERTY_AUDIOSIGNALPROCESSING_MODES"></span><span id="ksproperty_audiosignalprocessing_modes"></span>**KSPROPERTY\_AUDIOSIGNALPROCESSING\_MODES**  
Specifies the ID for the [**KSPROPERTY\_AUDIOSIGNALPROCESSING\_MODES**](ksproperty-audiosignalprocessing-modes.md) property.

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
<td align="left"><p>Windows 8.1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2012 R2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY\_AUDIOSIGNALPROCESSING\_MODES**](ksproperty-audiosignalprocessing-modes.md)

[KSPROPSETID\_AudioSignalProcessing](kspropsetid-audiosignalprocessing.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_AUDIOSIGNALPROCESSING%20enumeration%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





