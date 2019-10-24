---
title: Writing a location sensor driver for Windows 8.1
description: Writing a location sensor driver for Windows 8.1
ms.assetid: 18852282-6529-4934-a448-b699e01987de
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing a location sensor driver for Windows 8.1

This section provides specific guidance for writing drivers for devices that provide location data. In addition to the information that is contained in this section, location driver authors must also understand and apply the information that is provided in [Writing a Sensor Device Driver](https://docs.microsoft.com/windows-hardware/drivers/sensors/writing-a-sensor-device-driver).

The Sensor and Location Platform provides the Windows Location API to enable software developers to add location features to their programs easily. If you are writing a driver for a location sensor, you must understand how to make the driver compatible with the Location API and follow the guidelines in [Location Driver Guidelines for Power and Performance](location-driver-guidelines-for-power-and-performance.md).

## Windows Hardware Certification Program requirements

The Windows Hardware Certification Program enables hardware manufacturers to receive certification that their devices meet the required standards for working with Windows. The certification program describes the requirements for location sensors and other types of sensors. You should make your location sensor driver comply with all the certification program requirements. These requirements include the following:

-   Location sensors must support the required set of data and sensor properties.

-   Location sensors must support the required data fields for at least one built-in data report type.

Generally, the recommendations in this WDK documentation match the Certification Program requirements. However, you must review the official Certification Program documentation when you create sensor drivers that you intend to submit for approval. For more information about the Windows Hardware Certification Program, see the [Windows Hardware Developer Central](https://developer.microsoft.com/en-us/windows/hardware) website.

## Location API requirements

You create drivers for location sensors by using the same driver model and class extension as for any other category of sensor. At a minimum, to work as a location sensor, the driver must:

-   Identify the location sensor as belonging to the Location category.

-   Set the sensor type to one of the location sensor types.

-   Identify the location report data fields the sensor provides.

-   Support the required properties.

-   Provide data, when it is requested.

-   Manage state transitions.

-   Raise data-updated and state-changed events.

The rest of this section describes these minimum requirements

## Identifying the category

When it is called through [**ISensorDriver::OnGetProperties**](https://docs.microsoft.com/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetproperties), set the **WPD\_FUNCTIONAL\_OBJECT\_CATEGORY** property value to **SENSOR\_CATEGORY\_LOCATION**. The following code example shows how to set this constant through a pointer to [IPortableDeviceValues](https://go.microsoft.com/fwlink/p/?linkid=131486) named pValues.

```cpp
hr = pValues->SetGuidValue(WPD_FUNCTIONAL_OBJECT_CATEGORY, SENSOR_CATEGORY_LOCATION);
```

## Setting the location sensor type

When it is called through [**ISensorDriver::OnGetProperties**](https://docs.microsoft.com/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetproperties), set the **SENSOR\_PROPERTY\_TYPE** property value to the correct value. The following code example shows how to set the sensor type by using the **SENSOR\_TYPE\_LOCATION\_GPS** constant through a pointer to [IPortableDeviceValues](https://go.microsoft.com/fwlink/p/?linkid=131486) named pValues.

```cpp
hr = pValues->SetGuidValue(SENSOR_PROPERTY_TYPE, SENSOR_TYPE_LOCATION_GPS);
```

## Identifying the supported data fields

The Location API defines two kinds of location reports. These are objects that organize location data. LatLong reports contain latitude, longitude, and altitude data fields, together with data fields that contain error range information. Civic address reports contain street address data fields, such as city and postal code. Your location driver must support the required data fields for at least one of these two data report types.

To support a LatLong report, the following data fields are required:

-   SENSOR\_DATA\_TYPE\_LATITUDE\_DEGREES
-   SENSOR\_DATA\_TYPE\_LONGITUDE\_DEGREES
-   SENSOR\_DATA\_TYPE\_ERROR\_RADIUS\_METERS

To support a civic address report, at least one of the following data fields is required:

-   SENSOR\_DATA\_TYPE\_COUNTRY\_REGION

(To view the complete set of platform-defined location data fields, see [**SENSOR\_CATEGORY\_LOCATION**](https://docs.microsoft.com/windows-hardware/drivers/sensors/sensor-category-loc) in the [Windows Sensor Reference](https://docs.microsoft.com/windows-hardware/drivers/ddi/index) section.)

When they are called through [**ISensorDriver::OnGetSupportedDataFields**](https://docs.microsoft.com/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetsupporteddatafields), add the supported data field property key constants to the [IPortableDeviceKeyCollection](https://go.microsoft.com/fwlink/p/?linkid=131484) that you return through the *ppSupportedDataFields* parameter. The following code example shows how to add the postal code data field to [IPortableDeviceKeyCollection](https://go.microsoft.com/fwlink/p/?linkid=131484) through a variable named pKeyCollection.

```cpp
pKeyCollection->Add(SENSOR_DATA_TYPE_POSTALCODE);
```

## Support the required properties

Like other sensor drivers, location drivers provide information about the sensor itself through a set of properties. The Windows Hardware Certification Program specifies the minimum required set of properties that a location sensor must support. For more information about sensor properties, their meanings, and which properties are required for sensor drivers, see [**Sensor Properties**](https://docs.microsoft.com/windows-hardware/drivers/sensors/sensor-properties). The following list contains the required properties:

-   WPD\_FUNCTIONAL\_OBJECT\_CATEGORY

-   SENSOR\_PROPERTY\_TYPE

-   SENSOR\_PROPERTY\_STATE

-   SENSOR\_PROPERTY\_PERSISTENT\_UNIQUE\_ID

-   SENSOR\_PROPERTY\_MANUFACTURER

-   SENSOR\_PROPERTY\_MODEL

-   SENSOR\_PROPERTY\_SERIAL\_NUMBER

-   SENSOR\_PROPERTY\_FRIENDLY\_NAME

-   SENSOR\_PROPERTY\_MIN\_REPORT\_INTERVAL

-   SENSOR\_PROPERTY\_CURRENT\_REPORT\_INTERVAL

-   SENSOR\_PROPERTY\_LOCATION\_DESIRED\_ACCURACY

## Providing data

Location drivers provide data through the same mechanisms as other sensor drivers. That is, the sensor class extension calls the driver through [**ISensorDriver::OnGetDataFields**](https://docs.microsoft.com/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetdatafields) and the driver returns the values through the *ppDataValues* parameter.

The following requirements apply to providing data from a location sensor:

-   Provide data both through synchronous requests and by [raising events](https://docs.microsoft.com/windows-hardware/drivers/sensors/raising-events).

-   Maintain a copy of your most recent data report. If new data is not available when you request it, return the cached report. Do not update the time stamp.

-   Do not provide values for SENSOR\_DATA\_TYPE\_LATITUDE\_DEGREES and SENSOR\_DATA\_TYPE\_LONGITUDE\_DEGREES that fall outside the range of real-world latitudes and longitudes.

-   Do not report a value for SENSOR\_DATA\_TYPE\_ERROR\_RADIUS\_METERS that is zero or less.

-   Set the value for SENSOR\_DATA\_TYPE\_COUNTRY\_REGION to a valid ISO 3166 1-alpha-2 country code.

-   If your driver supports both latitude/longitude and civic address reports, the location data in these reports should correspond to the same physical location.

The following table describes the [sensor data fields](https://docs.microsoft.com/windows-hardware/drivers/sensors/sensor-categories--types--and-data-fields) that correspond to Location API data report fields. Use these data field constants when you provide data reports for a location.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Sensor constant</th>
<th>Location API method and property</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>SENSOR_DATA_TYPE_ADDRESS1</strong></p></td>
<td><p><a href="https://go.microsoft.com/fwlink/p/?linkid=157816" data-raw-source="[ICivicAddressReport::GetAddressLine1](https://go.microsoft.com/fwlink/p/?linkid=157816)">ICivicAddressReport::GetAddressLine1</a></p>
<p><a href="https://go.microsoft.com/fwlink/p/?linkid=157817" data-raw-source="[LocationDisp.DispCivicAddressReport.AddressLine1](https://go.microsoft.com/fwlink/p/?linkid=157817)">LocationDisp.DispCivicAddressReport.AddressLine1</a></p></td>
</tr>
<tr class="even">
<td><p><strong>SENSOR_DATA_TYPE_ADDRESS2</strong></p></td>
<td><p><a href="https://go.microsoft.com/fwlink/p/?linkid=157818" data-raw-source="[ICivicAddressReport::GetAddressLine2](https://go.microsoft.com/fwlink/p/?linkid=157818)">ICivicAddressReport::GetAddressLine2</a></p>
<p><a href="https://go.microsoft.com/fwlink/p/?linkid=157820" data-raw-source="[LocationDisp.DispCivicAddressReport.AddressLine2](https://go.microsoft.com/fwlink/p/?linkid=157820)">LocationDisp.DispCivicAddressReport.AddressLine2</a></p></td>
</tr>
<tr class="odd">
<td><p><strong>SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_ERROR_METERS</strong></p></td>
<td><p><a href="https://go.microsoft.com/fwlink/p/?linkid=157823" data-raw-source="[ILatLongReport::GetAltitudeError](https://go.microsoft.com/fwlink/p/?linkid=157823)">ILatLongReport::GetAltitudeError</a></p>
<p><a href="https://go.microsoft.com/fwlink/p/?linkid=157824" data-raw-source="[LocationDisp.DispLatLongReport.AltitudeError](https://go.microsoft.com/fwlink/p/?linkid=157824)">LocationDisp.DispLatLongReport.AltitudeError</a></p></td>
</tr>
<tr class="even">
<td><p><strong>SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_METERS</strong></p></td>
<td><p><a href="https://go.microsoft.com/fwlink/p/?linkid=157825" data-raw-source="[ILatLongReport::GetAltitude](https://go.microsoft.com/fwlink/p/?linkid=157825)">ILatLongReport::GetAltitude</a></p>
<p><a href="https://go.microsoft.com/fwlink/p/?linkid=157827" data-raw-source="[LocationDisp.DispLatLongReport.Altitude](https://go.microsoft.com/fwlink/p/?linkid=157827)">LocationDisp.DispLatLongReport.Altitude</a></p></td>
</tr>
<tr class="odd">
<td><p><strong>SENSOR_DATA_TYPE_CITY</strong></p></td>
<td><p><a href="https://go.microsoft.com/fwlink/p/?linkid=157828" data-raw-source="[ICivicAddressReport::GetCity](https://go.microsoft.com/fwlink/p/?linkid=157828)">ICivicAddressReport::GetCity</a></p>
<p><a href="https://go.microsoft.com/fwlink/p/?linkid=157830" data-raw-source="[LocationDisp.DispCivicAddressReport.City](https://go.microsoft.com/fwlink/p/?linkid=157830)">LocationDisp.DispCivicAddressReport.City</a></p>
<p><a href="https://docs.microsoft.com/uwp/api/Windows.Devices.Geolocation.CivicAddress#Windows_Devices_Geolocation_CivicAddress_City" data-raw-source="[Windows.Devices. Geolocation.CivicAddress](https://docs.microsoft.com/uwp/api/Windows.Devices.Geolocation.CivicAddress#Windows_Devices_Geolocation_CivicAddress_City)">Windows.Devices. Geolocation.CivicAddress</a></p></td>
</tr>
<tr class="even">
<td><p><strong>SENSOR_DATA_TYPE_COUNTRY_REGION</strong></p></td>
<td><p><a href="https://go.microsoft.com/fwlink/p/?linkid=157831" data-raw-source="[ICivicAddressReport::GetCountryRegion](https://go.microsoft.com/fwlink/p/?linkid=157831)">ICivicAddressReport::GetCountryRegion</a></p>
<p><a href="https://go.microsoft.com/fwlink/p/?linkid=157832" data-raw-source="[LocationDisp.DispCivicAddressReport.CountryRegion](https://go.microsoft.com/fwlink/p/?linkid=157832)">LocationDisp.DispCivicAddressReport.CountryRegion</a></p></td>
</tr>
<tr class="odd">
<td><p><strong>SENSOR_DATA_TYPE_ERROR_RADIUS_METERS</strong></p></td>
<td><p><a href="https://go.microsoft.com/fwlink/p/?linkid=157834" data-raw-source="[ILatLongReport::GetErrorRadius](https://go.microsoft.com/fwlink/p/?linkid=157834)">ILatLongReport::GetErrorRadius</a></p>
<p><a href="https://go.microsoft.com/fwlink/p/?linkid=157835" data-raw-source="[LocationDisp.DispLatLongReport.ErrorRadius](https://go.microsoft.com/fwlink/p/?linkid=157835)">LocationDisp.DispLatLongReport.ErrorRadius</a></p></td>
</tr>
<tr class="even">
<td><p><strong>SENSOR_DATA_TYPE_LATITUDE_DEGREES</strong></p></td>
<td><p><a href="https://go.microsoft.com/fwlink/p/?linkid=157836" data-raw-source="[ILatLongReport::GetLatitude](https://go.microsoft.com/fwlink/p/?linkid=157836)">ILatLongReport::GetLatitude</a></p>
<p><a href="https://go.microsoft.com/fwlink/p/?linkid=157839" data-raw-source="[LocationDisp.DispLatLongReport.Latitude](https://go.microsoft.com/fwlink/p/?linkid=157839)">LocationDisp.DispLatLongReport.Latitude</a></p></td>
</tr>
<tr class="odd">
<td><p><strong>SENSOR_DATA_TYPE_LONGITUDE_DEGREES</strong></p></td>
<td><p><a href="https://go.microsoft.com/fwlink/p/?linkid=157840" data-raw-source="[ILatLongReport::GetLongitude](https://go.microsoft.com/fwlink/p/?linkid=157840)">ILatLongReport::GetLongitude</a></p>
<p><a href="https://go.microsoft.com/fwlink/p/?linkid=157841" data-raw-source="[LocationDisp.DispLatLongReport.Longitude](https://go.microsoft.com/fwlink/p/?linkid=157841)">LocationDisp.DispLatLongReport.Longitude</a></p></td>
</tr>
<tr class="even">
<td><p><strong>SENSOR_DATA_TYPE_POSTALCODE</strong></p></td>
<td><p><a href="https://go.microsoft.com/fwlink/p/?linkid=157842" data-raw-source="[ICivicAddressReport::GetPostalCode](https://go.microsoft.com/fwlink/p/?linkid=157842)">ICivicAddressReport::GetPostalCode</a></p>
<p><a href="https://go.microsoft.com/fwlink/p/?linkid=157844" data-raw-source="[LocationDisp.DispCivicAddressReport.PostalCode](https://go.microsoft.com/fwlink/p/?linkid=157844)">LocationDisp.DispCivicAddressReport.PostalCode</a></p></td>
</tr>
<tr class="odd">
<td><p><strong>SENSOR_DATA_TYPE_STATE_PROVINCE</strong></p></td>
<td><p><a href="https://go.microsoft.com/fwlink/p/?linkid=157846" data-raw-source="[ICivicAddressReport::GetStateProvince](https://go.microsoft.com/fwlink/p/?linkid=157846)">ICivicAddressReport::GetStateProvince</a></p>
<p><a href="https://go.microsoft.com/fwlink/p/?linkid=157847" data-raw-source="[LocationDisp.DispCivicAddressReport.StateProvince](https://go.microsoft.com/fwlink/p/?linkid=157847)">LocationDisp.DispCivicAddressReport.StateProvince</a></p></td>
</tr>
</tbody>
</table>

## Managing state transitions

At any time, a sensor driver can be in one of a number of states. Sensor states are defined by the [**SensorState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/sensorsclassextension/ne-sensorsclassextension-__midl___midl_itf_windowssensorclassextension_0000_0000_0001) enumeration. To work correctly with the Location API, location sensors must follow these rules for handling state transitions.

-   Always start in the SENSOR\_STATE\_INITIALIZING state, but do not raise a state-changed event at startup.

-   The driver should transition from SENSOR\_STATE\_INITIALIZING to SENSOR\_STATE\_READY when data is available.
-   The driver should transition back to SENSOR\_STATE\_INITIALIZING when the driver does not have current data to report. The driver should decide when that transition occurs. If you have lost a signal, but still have a means to provide valid data, stay in the SENSOR\_STATE\_READY state.
-   Always raise events in the correct order. First, establish that data is available. Then, raise a state-changed event. Finally, raise the data-updated event.

-   Always raise a state-changed event when the driver's state changes.

-   The Location API does not use data from sensors that are in the following states: SENSOR\_STATE\_NO\_DATA, SENSOR\_STATE\_NOT\_AVAILABLE, SENSOR\_STATE\_ERROR.

The various sensor states for location sensor drivers are described in the following table..

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
<th>Location API state</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>SENSOR_STATE_READY</p></td>
<td><p>Sensor driver can provide new location reports that have complete and accurate data.</p>
<p>For example, a Wi-Fi or cellular provider is connected and working, or a GPS sensor has a fix.</p>
<p>A GPS driver that has used data from a triangulation sensor to determine location has this state.</p></td>
<td><p>REPORT_RUNNING</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_STATE_INITIALIZING</p></td>
<td><p>Sensor driver is trying to acquire a fix. The sensor driver should leave this state to transition to SENSOR_STATE_READY, after a fix is locked and tracking.</p>
<p>For example, a Wi-Fi provider is looking for an Internet connection, a cellular provider is looking for radios, or a GPS sensor is acquiring a fix.</p>
<p>GPS sensors should re-enter this state when they try to reacquire a fix.</p></td>
<td><p>REPORT_INITIALIZING</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_STATE_NO_DATA</p></td>
<td><p>The location provider is available, but is unable to provide location data.</p>
<p>For example, a Wi-Fi provider has access to the Internet, but the database has no location data.</p></td>
<td><p>REPORT_ERROR</p></td>
</tr>
<tr class="even">
<td><p>SENSOR_STATE_NOT_AVAILABLE</p></td>
<td><p>The functionality that the location provider uses to acquire data is disabled.</p>
<p>A GPS sensor could be in this state if the radio is turned off.</p></td>
<td><p>REPORT_ERROR</p></td>
</tr>
<tr class="odd">
<td><p>SENSOR_STATE_ERROR</p></td>
<td><p>The sensor has encountered a major error. The sensor can recover from this state, but the time frame for recovery is not known.</p></td>
<td><p>REPORT_ERROR</p></td>
</tr>
</tbody>
</table>

 

The following diagram shows how state transitions may occur in a location sensor.![state transitions](images/gps-state-transitions.png)

## Raising data-updated and state-changed events

The Location API, requires location sensors, such as GPS sensors, to raise events that provide data and state-change information. For more information about raising sensor events, see [About Sensor Driver Events](https://docs.microsoft.com/windows-hardware/drivers/sensors/about-sensor-driver-events).

When raising these events, location drivers must follow these rules:

-   Raise state change events by calling the sensor class extension's [**ISensorClassExtension::PostStateChange**](https://docs.microsoft.com/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensorclassextension-poststatechange) method. Do not call [**PostEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensorclassextension-postevent) to raise state change events.

-   Raise data-updated events by calling [**PostEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensorclassextension-postevent).
-   Raise a data-updated event only if the data is up to date and accurate.

-   Do not raise a data-updated event twice. This means that you should not raise a data-updated event by using cached data. You can provide cached data in response to a synchronous request for data.

-   Always include all the required data fields when you send a latitude/longitude report through an event.

-   Always raise a data-updated event when the sensor accuracy changes.

-   Report a valid value for SENSOR\_DATA\_TYPE\_ERROR\_RADIUS\_METERS before raising events or changing the value for SENSOR\_PROPERTY\_STATE to SENSOR\_STATE\_READY.

-   Do not provide incomplete data reports.

-   You might not have current data for the required data fields, such as when a GPS sensor has lost its fix. In this case, you might still want to provide notifications about updates to extended data fields, such as SENSOR\_DATA\_TYPE\_NMEA\_SENTENCE. To provide such notifications, you must use a custom event type and raise only the custom event until data for the required data fields becomes available. For information about how to define custom types, see [Defining Custom Values for Constants](https://docs.microsoft.com/windows-hardware/drivers/sensors/defining-custom-values-for-constants).

## Related topics

[Location Driver Guidelines for Power and Performance](location-driver-guidelines-for-power-and-performance.md)  
