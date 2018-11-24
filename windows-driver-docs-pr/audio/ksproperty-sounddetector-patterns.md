---
title: KSPROPERTY\_SOUNDDETECTOR\_PATTERNS
description: The KSPROPERTY\_SOUNDDETECTOR\_PATTERNS property is set by the operating system to configure the keywords to be detected.
ms.assetid: 7A6AF4F6-5F5F-4A3D-AF61-B3E4374B33AD
keywords: ["KSPROPERTY_SOUNDDETECTOR_PATTERNS Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_SOUNDDETECTOR_PATTERNS
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_SOUNDDETECTOR\_PATTERNS


The **KSPROPERTY\_SOUNDDETECTOR\_PATTERNS** property is set by the operating system to configure the keywords to be detected.

### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

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
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564262" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564262)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563441" data-raw-source="[&lt;strong&gt;KSMULTIPLE_ITEM&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563441)"><strong>KSMULTIPLE_ITEM</strong></a></p></td>
</tr>
</tbody>
</table>

 

The OS sets the keyword patterns or may set this to an empty value.

When the OS sets this property, the driver automatically disarms the detector if was previously armed.

If the driver cannot satisfy a “set” request due to insufficient resources, the driver fails the request with **STATUS\_INSUFFICIENT\_RESOURCES**.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The property value is a [**KSMULTIPLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563441) structure followed by a sequence of 64-bit aligned detection patterns. Each pattern starts with a [**SOUNDDETECTOR\_PATTERNHEADER**](https://msdn.microsoft.com/library/windows/hardware/dn957513) followed by the pattern payload.

Remarks
-------

The driver shall not complete the “set” request until:

-   The detector is disarmed and subsequent “get” requests on [**KSPROPERTY\_SOUNDDETECTOR\_ARMED**](ksproperty-sounddetector-armed.md) return false.
-   Subsequent “get” requests on [**KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT**](ksproperty-sounddetector-matchresult.md) return no data.
-   The new keyword patterns are established and the keyword detector is operating on the new patterns.

The driver may keep the request pending until the above conditions are met. Also, if the device requires measurable initialization time, the driver may keep this request pending until the device is ready and the can process the request.

The OS requires this behavior to avoid race conditions between a detected a keyword and updating keyword patterns (e.g. if a keyword was detected and the KSEVENT\_SOUNDDETECTOR generated an instant before the OS updates the keywords).

The OS waits at least 2 seconds for this request to complete.

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


[**SOUNDDETECTOR\_PATTERNHEADER**](https://msdn.microsoft.com/library/windows/hardware/dn957513)

[**SOUNDDETECTOR\_PATTERNS**](https://msdn.microsoft.com/library/windows/hardware/dn932155)

[**KSPROPERTY\_SOUNDDETECTOR\_ARMED**](ksproperty-sounddetector-armed.md)

[**KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT**](ksproperty-sounddetector-matchresult.md)

[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

[**KSMULTIPLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563441)

 

 






