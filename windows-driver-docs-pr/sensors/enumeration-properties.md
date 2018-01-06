---
title: Enumeration properties
description: This topic describes the static sensor properties that are available from the PnP Driver Store.
ms.assetid: E4663410-375F-48B9-A9E4-6E608FA8D2FF
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Enumeration properties


This topic describes the static sensor properties that are available from the PnP Driver Store.

The following table shows static sensor properties. The Class Extension (CX) writes these properties for each sensor when [SensorsCxSensorCreate](https://msdn.microsoft.com/library/windows/hardware/dn957087) is called. Client applications can use these properties to search for sensors on the Windows device.

For more information about the data types shown in the **Type** column, see [MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

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
<td><p>A GUID that identifies the type of sensor. For more information about sensor types, see [Sensor type GUIDs](https://msdn.microsoft.com/library/windows/hardware/dn946707).</p></td>
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
<p>For more information, see the [<strong>SensorConnectionType</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545701) enumeration.</p></td>
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


[MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

[**SensorConnectionType**](https://msdn.microsoft.com/library/windows/hardware/ff545701)

[SensorsCxSensorCreate](https://msdn.microsoft.com/library/windows/hardware/dn957087)

[Sensor properties](sensor-properties2.md)

[Sensor type GUIDs](https://msdn.microsoft.com/library/windows/hardware/dn946707)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Enumeration%20properties%20%20RELEASE:%20%2811/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





