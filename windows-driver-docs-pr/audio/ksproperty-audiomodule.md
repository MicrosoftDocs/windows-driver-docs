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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_AUDIOMODULE%20enumeration%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





