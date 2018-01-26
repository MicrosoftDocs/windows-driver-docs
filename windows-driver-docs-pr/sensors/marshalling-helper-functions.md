---
title: Marshalling helper functions
description: This topic provides information about the marshaling helper functions in the sensorsutils.h header file.
ms.assetid: AE5C70E4-1971-4BAF-AE7D-315A15F030DD
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Marshalling helper functions


This topic provides information about the marshaling helper functions in the *sensorsutils.h* header file.

These helper functions are used by the v2 sensor drivers, and they're used along with the sensor device driver software interface (DDSI).

If you implement your own marshaling helper functions, remember that helper functions must not be used when populating the enumeration list in the [**SENSOR\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/dn957096) structure, or when reporting updated data with the [**SensorsCxSensorDataReady**](https://msdn.microsoft.com/library/windows/hardware/dn957088) function.

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[Time stamp helper](timestamp-helper.md)</p></td>
<td><p>The time stamp helper function is used by v2 sensor drivers, and it's used with the sensor device driver software interface (DDSI).</p></td>
</tr>
<tr class="even">
<td><p>[PropVariant helpers](propvariant-helpers.md)</p></td>
<td><p>The PropVariant helper functions are used by the v2 sensor drivers for manipulating the [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) structures associated with the sensors.</p></td>
</tr>
<tr class="odd">
<td><p>[Collection list helpers](collection-list-helpers.md)</p></td>
<td><p>The collection list helper functions are used by the v2 sensor drivers, for working with [<strong>SENSOR_COLLECTION_LIST</strong>](https://msdn.microsoft.com/library/windows/hardware/dn957092) structures.</p></td>
</tr>
<tr class="even">
<td><p>[Collection list serialization helpers](collection-list-serialization-helpers.md)</p></td>
<td><p>The collection list serialization helper functions are used by the v2 sensor drivers, for performing serialization-related operations on [<strong>SENSOR_COLLECTION_LIST</strong>](https://msdn.microsoft.com/library/windows/hardware/dn957092) structures.</p></td>
</tr>
<tr class="odd">
<td><p>[Collection list legacy helpers](collection-list-legacy-helpers.md)</p></td>
<td><p>The collection list legacy helper functions are used by v2 sensor drivers for interacting with [<strong>SENSOR_COLLECTION_LIST</strong>](https://msdn.microsoft.com/library/windows/hardware/dn957092) structures.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


**Header:** Sensorsutils.h

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Marshalling%20helper%20functions%20%20RELEASE:%20%2811/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




