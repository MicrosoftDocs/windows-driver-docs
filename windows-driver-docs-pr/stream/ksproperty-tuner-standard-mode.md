---
title: KSPROPERTY\_TUNER\_STANDARD\_MODE
description: The KSPROPERTY\_TUNER\_STANDARD\_MODE property retrieves a BOOL value that indicates whether the driver can set the tuning device to automatically detect the tuner standard from the signal itself. This property can be implemented optionally.
ms.assetid: 9c374778-20fd-427a-864f-f57ec14add07
keywords: ["KSPROPERTY_TUNER_STANDARD_MODE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TUNER_STANDARD_MODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_TUNER\_STANDARD\_MODE


The KSPROPERTY\_TUNER\_STANDARD\_MODE property retrieves a BOOL value that indicates whether the driver can set the tuning device to automatically detect the tuner standard from the signal itself. This property can be implemented optionally.

### Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565913" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_STANDARD_MODE_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565913)"><strong>KSPROPERTY_TUNER_STANDARD_MODE_S</strong></a></p></td>
<td><p>BOOL</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a BOOL that indicates whether the tuning device can automatically detect the tuner standard from the signal itself.

Remarks
-------

For more information about how the KSPROPERTY\_TUNER\_STANDARD\_MODE property is used, see [Detecting Tuner Standards](https://msdn.microsoft.com/library/windows/hardware/ff558691).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the operating system.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## See also


[**KSPROPERTY\_TUNER\_STANDARD**](ksproperty-tuner-standard.md)

[**KSPROPERTY\_TUNER\_STANDARD\_MODE\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565913)

 

 






