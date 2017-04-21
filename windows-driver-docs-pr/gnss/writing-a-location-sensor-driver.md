---
title: Writing a location sensor driver for Windows 8.1
author: windows-driver-content
description: Writing a location sensor driver for Windows 8.1
ms.assetid: 18852282-6529-4934-a448-b699e01987de
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Writing a location sensor driver for Windows 8.1


This section provides specific guidance for writing drivers for devices that provide location data. In addition to the information that is contained in this section, location driver authors must also understand and apply the information that is provided in [Writing a Sensor Device Driver](https://msdn.microsoft.com/library/windows/hardware/ff545927).

The Sensor and Location Platform provides the Windows Location API to enable software developers to add location features to their programs easily. If you are writing a driver for a location sensor, you must understand how to make the driver compatible with the Location API and follow the guidelines in [Location Driver Guidelines for Power and Performance](location-driver-guidelines-for-power-and-performance.md).

### <a href="" id="windows-logo-program-requirements"></a>Windows Hardware Certification Program requirements

The Windows Hardware Certification Program enables hardware manufacturers to receive certification that their devices meet the required standards for working with Windows. The certification program describes the requirements for location sensors and other types of sensors. You should make your location sensor driver comply with all the certification program requirements. These requirements include the following:

-   Location sensors must support the required set of data and sensor properties.

-   Location sensors must support the required data fields for at least one built-in data report type.

Generally, the recommendations in this WDK documentation match the Certification Program requirements. However, you must review the official Certification Program documentation when you create sensor drivers that you intend to submit for approval. For more information about the Windows Hardware Certification Program, see the [Windows Hardware Developer Central](http://go.microsoft.com/fwlink/p/?linkid=8772) website.

### Location API requirements

You create drivers for location sensors by using the same driver model and class extension as for any other category of sensor. At a minimum, to work as a location sensor, the driver must:

-   Identify the location sensor as belonging to the Location category.

-   Set the sensor type to one of the location sensor types.

-   Identify the location report data fields the sensor provides.

-   Support the required properties.

-   Provide data, when it is requested.

-   Manage state transitions.

-   Raise data-updated and state-changed events.

The rest of this section describes these minimum requirements

### Identifying the category

When it is called through [**ISensorDriver::OnGetProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545610), set the **WPD\_FUNCTIONAL\_OBJECT\_CATEGORY** property value to **SENSOR\_CATEGORY\_LOCATION**. The following code example shows how to set this constant through a pointer to [IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=131486) named pValues.

```ManagedCPlusPlus
hr = pValues->SetGuidValue(WPD_FUNCTIONAL_OBJECT_CATEGORY, SENSOR_CATEGORY_LOCATION);
```

### Setting the location sensor type

When it is called through [**ISensorDriver::OnGetProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545610), set the **SENSOR\_PROPERTY\_TYPE** property value to the correct value. The following code example shows how to set the sensor type by using the **SENSOR\_TYPE\_LOCATION\_GPS** constant through a pointer to [IPortableDeviceValues](http://go.microsoft.com/fwlink/p/?linkid=131486) named pValues.

```ManagedCPlusPlus
hr = pValues->SetGuidValue(SENSOR_PROPERTY_TYPE, SENSOR_TYPE_LOCATION_GPS);
```

### Identifying the supported data fields

The Location API defines two kinds of location reports. These are objects that organize location data. LatLong reports contain latitude, longitude, and altitude data fields, together with data fields that contain error range information. Civic address reports contain street address data fields, such as city and postal code. Your location driver must support the required data fields for at least one of these two data report types.

To support a LatLong report, the following data fields are required:

-   SENSOR\_DATA\_TYPE\_LATITUDE\_DEGREES
-   SENSOR\_DATA\_TYPE\_LONGITUDE\_DEGREES
-   SENSOR\_DATA\_TYPE\_ERROR\_RADIUS\_METERS

To support a civic address report, at least one of the following data fields is required:

-   SENSOR\_DATA\_TYPE\_COUNTRY\_REGION

(To view the complete set of platform-defined location data fields, see [**SENSOR\_CATEGORY\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/dn265186) in the [Windows Sensor Reference](https://msdn.microsoft.com/library/windows/hardware/ff545907) section.)

When they are called through [**ISensorDriver::OnGetSupportedDataFields**](https://msdn.microsoft.com/library/windows/hardware/ff545620), add the supported data field property key constants to the [IPortableDeviceKeyCollection](http://go.microsoft.com/fwlink/p/?linkid=131484) that you return through the *ppSupportedDataFields* parameter. The following code example shows how to add the postal code data field to [IPortableDeviceKeyCollection](http://go.microsoft.com/fwlink/p/?linkid=131484) through a variable named pKeyCollection.

```ManagedCPlusPlus
pKeyCollection->Add(SENSOR_DATA_TYPE_POSTALCODE);
```

### Support the required properties

Like other sensor drivers, location drivers provide information about the sensor itself through a set of properties. The Windows Hardware Certification Program specifies the minimum required set of properties that a location sensor must support. For more information about sensor properties, their meanings, and which properties are required for sensor drivers, see [**Sensor Properties**](https://msdn.microsoft.com/library/windows/hardware/ff545859). The following list contains the required properties:

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

### Providing data

Location drivers provide data through the same mechanisms as other sensor drivers. That is, the sensor class extension calls the driver through [**ISensorDriver::OnGetDataFields**](https://msdn.microsoft.com/library/windows/hardware/ff545607) and the driver returns the values through the *ppDataValues* parameter.

The following requirements apply to providing data from a location sensor:

-   Provide data both through synchronous requests and by [raising events](https://msdn.microsoft.com/library/windows/hardware/ff545695).

-   Maintain a copy of your most recent data report. If new data is not available when you request it, return the cached report. Do not update the time stamp.

-   Do not provide values for SENSOR\_DATA\_TYPE\_LATITUDE\_DEGREES and SENSOR\_DATA\_TYPE\_LONGITUDE\_DEGREES that fall outside the range of real-world latitudes and longitudes.

-   Do not report a value for SENSOR\_DATA\_TYPE\_ERROR\_RADIUS\_METERS that is zero or less.

-   Set the value for SENSOR\_DATA\_TYPE\_COUNTRY\_REGION to a valid ISO 3166 1-alpha-2 country code.

-   If your driver supports both latitude/longitude and civic address reports, the location data in these reports should correspond to the same physical location.

The following table describes the [sensor data fields](https://msdn.microsoft.com/library/windows/hardware/ff545718) that correspond to Location API data report fields. Use these data field constants when you provide data reports for a location.

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
<td><p>[ICivicAddressReport::GetAddressLine1](http://go.microsoft.com/fwlink/p/?linkid=157816)</p>
<p>[LocationDisp.DispCivicAddressReport.AddressLine1](http://go.microsoft.com/fwlink/p/?linkid=157817)</p></td>
</tr>
<tr class="even">
<td><p><strong>SENSOR_DATA_TYPE_ADDRESS2</strong></p></td>
<td><p>[ICivicAddressReport::GetAddressLine2](http://go.microsoft.com/fwlink/p/?linkid=157818)</p>
<p>[LocationDisp.DispCivicAddressReport.AddressLine2](http://go.microsoft.com/fwlink/p/?linkid=157820)</p></td>
</tr>
<tr class="odd">
<td><p><strong>SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_ERROR_METERS</strong></p></td>
<td><p>[ILatLongReport::GetAltitudeError](http://go.microsoft.com/fwlink/p/?linkid=157823)</p>
<p>[LocationDisp.DispLatLongReport.AltitudeError](http://go.microsoft.com/fwlink/p/?linkid=157824)</p></td>
</tr>
<tr class="even">
<td><p><strong>SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_METERS</strong></p></td>
<td><p>[ILatLongReport::GetAltitude](http://go.microsoft.com/fwlink/p/?linkid=157825)</p>
<p>[LocationDisp.DispLatLongReport.Altitude](http://go.microsoft.com/fwlink/p/?linkid=157827)</p></td>
</tr>
<tr class="odd">
<td><p><strong>SENSOR_DATA_TYPE_CITY</strong></p></td>
<td><p>[ICivicAddressReport::GetCity](http://go.microsoft.com/fwlink/p/?linkid=157828)</p>
<p>[LocationDisp.DispCivicAddressReport.City](http://go.microsoft.com/fwlink/p/?linkid=157830)</p>
<p>[Windows.Devices. Geolocation.CivicAddress](http://msdn.microsoft.com/library/windows/apps/windows.devices.geolocation.civicaddress.city.aspx)</p></td>
</tr>
<tr class="even">
<td><p><strong>SENSOR_DATA_TYPE_COUNTRY_REGION</strong></p></td>
<td><p>[ICivicAddressReport::GetCountryRegion](http://go.microsoft.com/fwlink/p/?linkid=157831)</p>
<p>[LocationDisp.DispCivicAddressReport.CountryRegion](http://go.microsoft.com/fwlink/p/?linkid=157832)</p></td>
</tr>
<tr class="odd">
<td><p><strong>SENSOR_DATA_TYPE_ERROR_RADIUS_METERS</strong></p></td>
<td><p>[ILatLongReport::GetErrorRadius](http://go.microsoft.com/fwlink/p/?linkid=157834)</p>
<p>[LocationDisp.DispLatLongReport.ErrorRadius](http://go.microsoft.com/fwlink/p/?linkid=157835)</p></td>
</tr>
<tr class="even">
<td><p><strong>SENSOR_DATA_TYPE_LATITUDE_DEGREES</strong></p></td>
<td><p>[ILatLongReport::GetLatitude](http://go.microsoft.com/fwlink/p/?linkid=157836)</p>
<p>[LocationDisp.DispLatLongReport.Latitude](http://go.microsoft.com/fwlink/p/?linkid=157839)</p></td>
</tr>
<tr class="odd">
<td><p><strong>SENSOR_DATA_TYPE_LONGITUDE_DEGREES</strong></p></td>
<td><p>[ILatLongReport::GetLongitude](http://go.microsoft.com/fwlink/p/?linkid=157840)</p>
<p>[LocationDisp.DispLatLongReport.Longitude](http://go.microsoft.com/fwlink/p/?linkid=157841)</p></td>
</tr>
<tr class="even">
<td><p><strong>SENSOR_DATA_TYPE_POSTALCODE</strong></p></td>
<td><p>[ICivicAddressReport::GetPostalCode](http://go.microsoft.com/fwlink/p/?linkid=157842)</p>
<p>[LocationDisp.DispCivicAddressReport.PostalCode](http://go.microsoft.com/fwlink/p/?linkid=157844)</p></td>
</tr>
<tr class="odd">
<td><p><strong>SENSOR_DATA_TYPE_STATE_PROVINCE</strong></p></td>
<td><p>[ICivicAddressReport::GetStateProvince](http://go.microsoft.com/fwlink/p/?linkid=157846)</p>
<p>[LocationDisp.DispCivicAddressReport.StateProvince](http://go.microsoft.com/fwlink/p/?linkid=157847)</p></td>
</tr>
</tbody>
</table>

 

### Managing state transitions

At any time, a sensor driver can be in one of a number of states. Sensor states are defined by the [**SensorState**](https://msdn.microsoft.com/library/windows/hardware/ff545708) enumeration. To work correctly with the Location API, location sensors must follow these rules for handling state transitions.

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

### Raising data-updated and state-changed events

The Location API, requires location sensors, such as GPS sensors, to raise events that provide data and state-change information. For more information about raising sensor events, see [About Sensor Driver Events](https://msdn.microsoft.com/library/windows/hardware/ff545385).

When raising these events, location drivers must follow these rules:

-   Raise state change events by calling the sensor class extension's [**ISensorClassExtension::PostStateChange**](https://msdn.microsoft.com/library/windows/hardware/ff545523) method. Do not call [**PostEvent**](https://msdn.microsoft.com/library/windows/hardware/ff545519) to raise state change events.

-   Raise data-updated events by calling [**PostEvent**](https://msdn.microsoft.com/library/windows/hardware/ff545519).
-   Raise a data-updated event only if the data is up to date and accurate.

-   Do not raise a data-updated event twice. This means that you should not raise a data-updated event by using cached data. You can provide cached data in response to a synchronous request for data.

-   Always include all the required data fields when you send a latitude/longitude report through an event.

-   Always raise a data-updated event when the sensor accuracy changes.

-   Report a valid value for SENSOR\_DATA\_TYPE\_ERROR\_RADIUS\_METERS before raising events or changing the value for SENSOR\_PROPERTY\_STATE to SENSOR\_STATE\_READY.

-   Do not provide incomplete data reports.

-   You might not have current data for the required data fields, such as when a GPS sensor has lost its fix. In this case, you might still want to provide notifications about updates to extended data fields, such as SENSOR\_DATA\_TYPE\_NMEA\_SENTENCE. To provide such notifications, you must use a custom event type and raise only the custom event until data for the required data fields becomes available. For information about how to define custom types, see [Defining Custom Values for Constants](https://msdn.microsoft.com/library/windows/hardware/ff545437).

## Related topics
[Location Driver Guidelines for Power and Performance](location-driver-guidelines-for-power-and-performance.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Writing%20a%20location%20sensor%20driver%20for%20Windows%208.1%20%20RELEASE:%20%281/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


