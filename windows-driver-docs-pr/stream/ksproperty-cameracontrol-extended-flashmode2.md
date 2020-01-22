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
ms.date: 09/10/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE

The **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE** property is extended to support assistant flash.

## Usage summary table


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

The capability flags are defined as follows.

```cpp
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

The descriptions for the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE** property are the same as the Windows 8.1 DDI.

## Requirements

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
