---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE
description: The KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE property is extended to support assistant flash.
ms.assetid: 413B3A02-498A-4C5A-8940-9A0D10D6CE81
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_FLASHMODE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_FLASHMODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE


The **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE** property is extended to support assistant flash.

## <span id="Usage_summary_table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage summary table


<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Scope</th>
<th>Control</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Version 1</p></td>
<td><p>Filter</p></td>
<td><p>Synchronous</p></td>
</tr>
</tbody>
</table>

 

The following capability flags are defined as follows.

``` syntax
#define KSCAMERA_EXTENDEDPROP_FLASH_ASSISTANT_ON               0x0000000000000080
#define KSCAMERA_EXTENDEDPROP_FLASH_ASSISTANT_AUTO             0x0000000000000100
#define KSCAMERA_EXTENDEDPROP_FLASH_ASSISTANT_OFF              0x0000000000000000
```

**KSCAMERA\_EXTENDEDPROP\_FLASH\_ASSISTANT\_ON**

This flag indicates that the AF assistant light is turned on.

**KSCAMERA\_EXTENDEDPROP\_FLASH\_ASSISTANT\_AUTO**

This flag is similar to the **ASSISTANT\_ON** flag. Instead of always turning on the AF assistant light, the camera driver will determine if the AF assistant light should be turned on based on the current lighting condition.

**KSCAMERA\_EXTENDEDPROP\_FLASH\_ASSISTANT\_OFF**

This flag indicates that AF assistant light is off.

The descriptions for the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925136) structure fields when using the **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE** property are the same as the Windows 8.1 DDI.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ksmedia.h</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_EXTENDED_FLASHMODE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




