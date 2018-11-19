---
title: Enumeration properties
description: This topic describes the static sensor properties that are available from the PnP Driver Store.
ms.assetid: E4663410-375F-48B9-A9E4-6E608FA8D2FF
ms.date: 01/04/2018
ms.localizationpriority: medium
---

# Enumeration properties


This topic describes the static sensor properties that are available from the PnP Driver Store.

The following table shows static sensor properties. The Class Extension (CX) writes these properties for each sensor when [SensorsCxSensorCreate](https://msdn.microsoft.com/library/windows/hardware/dn957087) is called. Client applications can use these properties to search for sensors on the Windows device.

For more information about the data types shown in the **Type** column, see [PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Property key</th>
<th>Type</th>
<th>Required/Optional</th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>DEVPKEY_Sensor_Type</p></td>
<td><p>VT_CLSID</p></td>
<td><p>Required</p></td>
<td><p>A GUID that identifies the type of sensor. For more information about sensor types, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn946707" data-raw-source="[Sensor type GUIDs](https://msdn.microsoft.com/library/windows/hardware/dn946707)">Sensor type GUIDs</a>.</p></td>
</tr>
<tr class="even">
<td><p>DEVPKEY_Sensor_Category</p></td>
<td><p>VT_CLSID</p></td>
<td><p>Required</p></td>
<td><p>The sensor category. This is for backwards compatibility with Desktop v1 stack, where it is a requirement.</p></td>
</tr>
<tr class="odd">
<td><p>DEVPKEY_Sensor_ConnectionType</p></td>
<td><p>VT_UI4</p></td>
<td><p>Optional</p>
<p>Required for Ambient Light Sensor and Accelerometer</p></td>
<td><p>The senor connection type. Sensor connection types can be integrated, attached, or external.</p>
<p>For more information, see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545701" data-raw-source="[&lt;strong&gt;SensorConnectionType&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545701)"><strong>SensorConnectionType</strong></a> enumeration.</p></td>
</tr>
<tr class="even">
<td><p>DEVPKEY_Sensor_IsPrimary</p></td>
<td><p>VT_BOOL</p></td>
<td><p>Optional</p></td>
<td><p>An indication that this is the primary sensor. This has a default value of false, if not set.</p></td>
</tr>
<tr class="odd">
<td><p>DEVPKEY_Sensor_Name</p></td>
<td><p>VT_LPWSTR</p></td>
<td><p>Required for custom sensors.</p></td>
<td><p>The name of the sensor.</p></td>
</tr>
<tr class="even">
<td><p>DEVPKEY_Sensor_Manufacturer</p></td>
<td><p>VT_LPWSTR</p></td>
<td><p>Required</p></td>
<td><p>The manufacturer for the sensor.</p></td>
</tr>
<tr class="odd">
<td><p>DEVPKEY_Sensor_Model</p></td>
<td><p>VT_LPWSTR</p></td>
<td><p>Required</p></td>
<td><p>The model for the sensor.</p></td>
</tr>
<tr class="even">
<td><p>DEVPKEY_Sensor_PersistentUniqueId</p></td>
<td><p>VT_CLSID</p></td>
<td><p>Required</p></td>
<td><p>A GUID that identifies the sensor. This value must be unique for each sensor of the same model on a device. This requirement applies to both internally and externally connected sensors.</p></td>
</tr>
<tr class="odd">
<td><p>DEVPKEY_Sensor_VendorDefinedSubType</p></td>
<td><p>VT_CLSID</p></td>
<td><p>Required for custom sensors.</p></td>
<td><p>A GUID that identifies a sensor category subtype that was defined by a vendor.</p>
<p>For non-custom sensors, this is not required.</p></td>
</tr>
<tr class="even">
<td><p>DEVPKEY_SensorData_LightLevel_AutoBrightnessPreferred</p></td>
<td><p>VT_BOOL</p></td>
<td><p>Optional</p></td>
<td><p>The light sensor is preferred for auto-brightness.</p></td>
</tr>
<tr class="odd">
<td><p>DEVPKEY_SensorData_LightLevel_ColorCapable</p></td>
<td><p>VT_BOOL</p></td>
<td><p>Optional. Required if supporting chromaticity and light temperature.</p></td>
<td><p>The light sensor supports light temperature and/or chromaticity x/y.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

[**SensorConnectionType**](https://msdn.microsoft.com/library/windows/hardware/ff545701)

[SensorsCxSensorCreate](https://msdn.microsoft.com/library/windows/hardware/dn957087)

[Sensor properties](sensor-properties2.md)

[Sensor type GUIDs](https://msdn.microsoft.com/library/windows/hardware/dn946707)

 

 






