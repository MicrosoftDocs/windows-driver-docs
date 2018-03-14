---
title: Event Constants
description: The sensor platform defines the following constants for driver events.
ms.assetid: d9bcfda4-d731-462f-802d-99c85911a6ca
keywords: ["Event Constants Sensor Devices"]
topic_type:
- apiref
api_name:
- Event Constants
api_location:
- Sensors.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Event Constants


The sensor platform defines the following constants for driver events.

### <span id="sensor_event_types"></span><span id="SENSOR_EVENT_TYPES"></span>Sensor Event Types

The sensor platform defines the following sensor event types identifiers.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>SENSOR_EVENT_DATA_UPDATED</p></td>
<td><p>Indicates that new data is available.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_EVENT_PROPERTY_CHANGED</p></td>
<td><p>Indicates that a property value changed.</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_EVENT_STATE_CHANGED</p></td>
<td><p>Indicates a change of operational state, for example, from SENSOR_STATE_INITIALIZING to SENSOR_STATE_READY.</p></td>
</tr>
</tbody>
</table>

 

### <span id="sensor_event_propertykeys"></span><span id="SENSOR_EVENT_PROPERTYKEYS"></span>Sensor Event PROPERTYKEYs

The sensor platform defines the following **PROPERTYKEY**s to identify the parameters for sensor events.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>SENSOR_EVENT_PARAMETER_EVENT_ID</p></td>
<td><p>Indicates that the <strong>GUID</strong> value in [IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=131486) is an event type ID, such as SENSOR_EVENT_DATA_UPDATED.</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_EVENT_PARAMETER_STATE</p></td>
<td><p>Indicates that the unsigned integer value in [IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=131486) is a sensor state, such as SENSOR_STATE_READY.</p>
<div class="alert">
<strong>Note</strong>  To raise a state changed event, call [<strong>ISensorClassExtension::PostStateChange</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545523). You do not have to explicitly specify SENSOR_EVENT_PARAMETER_STATE to raise the event.
</div>
<div>
 
</div></td>
</tr>
</tbody>
</table>

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 7</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>None supported</p></td>
</tr>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows 7.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Sensors.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[About Sensor Driver Events](https://msdn.microsoft.com/library/windows/hardware/ff545385)

[Filtering data](https://msdn.microsoft.com/library/windows/hardware/hh706201)

[The Sensors Geolocation Driver Sample](https://msdn.microsoft.com/library/windows/hardware/hh768273)

[**SensorState**](https://msdn.microsoft.com/library/windows/hardware/ff545708)

 

 






