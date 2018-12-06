---
title: KSPROPERTY\_AUDIOMODULE enumeration
description: The KSPROPERTY\_AUDIOMODULE enumeration defines constants that are used by audio drivers to communicate information about partner defined audio modules.
ms.assetid: 94873A4A-A40F-40A7-B7A2-B693A5253714
keywords: ["KSPROPERTY_AUDIOMODULE enumeration Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIOMODULE
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIOMODULE enumeration


The KSPROPERTY\_AUDIOMODULE enumeration defines constants that are used by audio drivers to communicate information about partner defined audio modules.

For more information about audio modules, see [Implementing Audio Module Discovery](https://msdn.microsoft.com/windows/hardware/drivers/audio/implementing-audio-module-communication).

Syntax
------

```ManagedCPlusPlus
typedef enum  { 
  KSPROPERTY_AUDIOMODULE_DESCRIPTORS             = 1,
  KSPROPERTY_AUDIOMODULE_COMMAND                 = 2,
  KSPROPERTY_AUDIOMODULE_NOTIFICATION_DEVICE_ID  = 3
} KSPROPERTY_AUDIOMODULE;
```

Constants
---------

<span id="KSPROPERTY_AUDIOMODULE_DESCRIPTORS__"></span><span id="ksproperty_audiomodule_descriptors__"></span>**KSPROPERTY\_AUDIOMODULE\_DESCRIPTORS**   
Specifies the ID for the [**KSPROPERTY\_AUDIOMODULE\_DESCRIPTORS**](ksproperty-audiomodule-descriptors.md) property.

<span id="KSPROPERTY_AUDIOMODULE_COMMAND"></span><span id="ksproperty_audiomodule_command"></span>**KSPROPERTY\_AUDIOMODULE\_COMMAND**  
Specifies the ID for the [**KSPROPERTY\_AUDIOMODULE\_COMMAND**](ksproperty-audiomodule-command.md) property.

<span id="KSPROPERTY_AUDIOMODULE_NOTIFICATION_DEVICE_ID"></span><span id="ksproperty_audiomodule_notification_device_id"></span>**KSPROPERTY\_AUDIOMODULE\_NOTIFICATION\_DEVICE\_ID**  
Specifies the ID for the [**KSPROPERTY\_AUDIOMODULE\_NOTIFICATION\_DEVICE\_ID**](ksproperty-audiomodule-notification-device-id.md) property.

Remarks
-------

All KS Property calls must be non-blocking because the hardware effects are part of the processing chain and should not wait.

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
<td align="left"><p>Windows 10, version 1703</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>None supported</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[KSPROPSETID\_AudioModule](kspropsetid-audiomodule.md)

 

 






