---
title: Data field properties
description: This topic describes the sensor properties that are used for data fields only.
ms.assetid: A7FA02AA-7B7B-45B4-A432-4B4ED69CB19C
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Data field properties


This topic describes the sensor properties that are used for data fields only.

The following table shows the sensor properties. Because these properties apply to any data-field, the type can vary depending on which data-field these properties are referring to, see the [Sensor data fields](sensor-data-fields.md) topic for more information.

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
<th>Property key</th>
<th>Type</th>
<th>Access (R/O, R/W)</th>
<th>Required/Optional</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PKEY_SensorDataField_Resolution</p></td>
<td><p>See the data field type.</p></td>
<td><p>R/O</p></td>
<td><p>This depends on the data fields, for a list of property keys that require this data field see the [Required data field properties](required-data-field-properties.md) topic.</p></td>
<td><p>The resolution of the data field.</p></td>
</tr>
<tr class="even">
<td><p>PKEY_SensorDataField_RangeMinimum</p></td>
<td><p>See the data field type.</p></td>
<td><p>R/O</p></td>
<td><p>This depends on the data fields, for a list of property keys that require this data field see the [Required data field properties](required-data-field-properties.md) topic.</p></td>
<td><p>The minimum value of the data field.</p></td>
</tr>
<tr class="odd">
<td><p>PKEY_SensorDataField_RangeMaximum</p></td>
<td><p>See the data field type.</p></td>
<td><p>R/O</p></td>
<td><p>This depends on the data fields, for a list of property keys that require this data field see the [Required data field properties](required-data-field-properties.md) topic.</p></td>
<td><p>The maximum value of the data field.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


**Header:** Sensorsdef.h

## <span id="related_topics"></span>Related topics


[Required data field properties](required-data-field-properties.md)

[Sensor data fields](sensor-data-fields.md)

[Sensor properties](sensor-properties2.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Data%20field%20properties%20%20RELEASE:%20%2811/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





