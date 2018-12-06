---
title: SENSOR\_CATEGORY\_LOCATION
description: The SENSOR\_CATEGORY\_LOCATION category contains sensors that provide geographic location information.
ms.assetid: 19B76F17-0575-42F2-ADEF-15932DCE7E06
topic_type:
- apiref
api_name:
- SENSOR_TYPE_LOCATION_BROADCAST
- SENSOR_TYPE_LOCATION_DEAD_RECKONING
- SENSOR_TYPE_LOCATION_GPS
- SENSOR_TYPE_LOCATION_LOOKUP
- SENSOR_TYPE_LOCATION_OTHER
- SENSOR_TYPE_LOCATION_STATIC
- SENSOR_TYPE_LOCATION_TRIANGULATION
- SENSOR_DATA_TYPE_ADDRESS1
- SENSOR_DATA_TYPE_ADDRESS2
- SENSOR_DATA_TYPE_ALTITUDE_ANTENNA_SEALEVEL_METERS
- SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_ERROR_METERS
- SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_METERS
- SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_ERROR_METERS
- SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_METERS
- SENSOR_DATA_TYPE_CITY
- SENSOR_DATA_TYPE_COUNTRY_REGION
- SENSOR_DATA_TYPE_DGPS_DATA_AGE
- SENSOR_DATA_TYPE_DIFFERENTIAL_REFERENCE_STATION_ID
- SENSOR_DATA_TYPE_ERROR_RADIUS_METERS
- SENSOR_DATA_TYPE_FIX_QUALITY
- SENSOR_DATA_TYPE_FIX_TYPE
- SENSOR_DATA_TYPE_GEOIDAL_SEPARATION
- SENSOR_DATA_TYPE_GPS_OPERATION_MODE
- SENSOR_DATA_TYPE_GPS_SELECTION_MODE
- SENSOR_DATA_TYPE_GPS_STATUS
- SENSOR_DATA_TYPE_HORIZONAL_DILUTION_OF_PRECISION
- SENSOR_DATA_TYPE_LATITUDE_DEGREES
- SENSOR_DATA_TYPE_LONGITUDE_DEGREES
- SENSOR_DATA_TYPE_MAGNETIC_HEADING_DEGREES
- SENSOR_DATA_TYPE_MAGNETIC_VARIATION
- SENSOR_DATA_TYPE_NMEA_SENTENCE
- SENSOR_DATA_TYPE_POSITION_DILUTION_OF_PRECISION
- SENSOR_DATA_TYPE_POSTALCODE
- SENSOR_DATA_TYPE_SATELLITES_IN_VIEW
- SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_AZIMUTH
- SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ELEVATION
- SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ID
- SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_PRNS
- SENSOR_DATA_TYPE_SATELLITES_USED_PRNS_AND_CONSTELLATIONS
- SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_STN_RATIO
- SENSOR_DATA_TYPE_SATELLITES_USED_COUNT
- SENSOR_DATA_TYPE_SATELLITES_USED_PRNS
- SENSOR_DATA_TYPE_SPEED_KNOTS
- SENSOR_DATA_TYPE_STATE_PROVINCE
- SENSOR_DATA_TYPE_TRUE_HEADING_DEGREES
- SENSOR_DATA_TYPE_VERTICAL_DILUTION_OF_PRECISION
api_type:
- NA
ms.date: 01/04/2018
ms.localizationpriority: medium
---

# SENSOR\_CATEGORY\_LOCATION


The SENSOR\_CATEGORY\_LOCATION category contains sensors that provide geographic location information.

**Platform-Defined Sensor Types**

This category includes the following platform-defined sensor types.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Sensor type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="SENSOR_TYPE_LOCATION_BROADCAST"></span><span id="sensor_type_location_broadcast"></span>
<strong>SENSOR_TYPE_LOCATION_BROADCAST</strong>
{D26988CF-5162-4039-BB17-4C58B698E44A}</td>
<td><p>Sensors that transmit location information by using transmissions such as television or radio frequencies.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_TYPE_LOCATION_DEAD_RECKONING"></span><span id="sensor_type_location_dead_reckoning"></span>
<strong>SENSOR_TYPE_LOCATION_DEAD_RECKONING</strong>
{1A37D538-F28B-42DA-9FCE-A9D0A2A6D829}</td>
<td><p>Dead-reckoning sensors. These sensors first calculate the current location and then update the current location by using motion data.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_TYPE_LOCATION_GPS"></span><span id="sensor_type_location_gps"></span>
<strong>SENSOR_TYPE_LOCATION_GPS</strong>
{ED4CA589-327A-4FF9-A560-91DA4B48275E}</td>
<td><p>Global positioning system sensors.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_TYPE_LOCATION_LOOKUP"></span><span id="sensor_type_location_lookup"></span>
<strong>SENSOR_TYPE_LOCATION_LOOKUP</strong>
{3B2EAE4A-72CE-436D-96D2-3C5B8570E987}</td>
<td><p>Lookup sensors, such as those that provide information based on the user&#39;s IP address.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_TYPE_LOCATION_OTHER"></span><span id="sensor_type_location_other"></span>
<strong>SENSOR_TYPE_LOCATION_OTHER</strong>
{9B2D0566-0368-4F71-B88D-533F132031DE}</td>
<td><p>Other location sensors.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_TYPE_LOCATION_STATIC"></span><span id="sensor_type_location_static"></span>
<strong>SENSOR_TYPE_LOCATION_STATIC</strong>
{095F8184-0FA9-4445-8E6E-B70F320B6B4C}</td>
<td><p>Fixed-location sensors, such as those that use preset, user-provided information.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_TYPE_LOCATION_TRIANGULATION"></span><span id="sensor_type_location_triangulation"></span>
<strong>SENSOR_TYPE_LOCATION_TRIANGULATION</strong>
{691C341A-5406-4FE1-942F-2246CBEB39E0}</td>
<td><p>Triangulation sensors, such as those that determine current location based on cellular phone tower proximities.</p></td>
</tr>
</tbody>
</table>

**Platform-Defined Data Fields**

Platform-defined property keys for this category are based on SENSOR\_DATA\_TYPE\_LOCATION\_GUID:

{055C74D8-CA6F-47D6-95C6-1ED3637A0FF4}

This category includes the following platform-defined data fields.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Data field name and PID</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_ADDRESS1"></span><span id="sensor_data_type_address1"></span>
<strong>SENSOR_DATA_TYPE_ADDRESS1</strong>
(PID = 23)</td>
<td><p><strong>VT_LPWSTR</strong></p>
<p>Street address, first line.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_ADDRESS2"></span><span id="sensor_data_type_address2"></span>
<strong>SENSOR_DATA_TYPE_ADDRESS2</strong>
(PID = 24)</td>
<td><p><strong>VT_LPWSTR</strong></p>
<p>Street address, second line.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_ALTITUDE_ANTENNA_SEALEVEL_METERS"></span><span id="sensor_data_type_altitude_antenna_sealevel_meters"></span>
<strong>SENSOR_DATA_TYPE_ALTITUDE_ANTENNA_SEALEVEL_METERS</strong>
(PID = 36)</td>
<td><p><strong>VT_R8</strong></p>
<p>Altitude of the antenna, referenced to sea level, in meters.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_ERROR_METERS"></span><span id="sensor_data_type_altitude_ellipsoid_error_meters"></span>
<strong>SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_ERROR_METERS</strong>
(PID = 29)</td>
<td><p><strong>VT_R8</strong></p>
<p>Altitude error referenced to the World Geodetic System (WGS 84) reference ellipsoid, in meters.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_METERS"></span><span id="sensor_data_type_altitude_ellipsoid_meters"></span>
<strong>SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_METERS</strong>
(PID = 5)</td>
<td><p><strong>VT_R8</strong></p>
<p>Altitude referenced to the World Geodetic System (WGS 84) reference ellipsoid, in meters.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_ERROR_METERS"></span><span id="sensor_data_type_altitude_sealevel_error_meters"></span>
<strong>SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_ERROR_METERS</strong>
(PID = 30)</td>
<td><p><strong>VT_R8</strong></p>
<p>Altitude error referenced to sea level, in meters.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_METERS"></span><span id="sensor_data_type_altitude_sealevel_meters"></span>
<strong>SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_METERS</strong>
(PID = 4)</td>
<td><p><strong>VT_R8</strong></p>
<p>Altitude referenced to sea level, in meters.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_CITY"></span><span id="sensor_data_type_city"></span>
<strong>SENSOR_DATA_TYPE_CITY</strong>
(PID = 25)</td>
<td><p><strong>VT_LPWSTR</strong></p>
<p>City.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_COUNTRY_REGION"></span><span id="sensor_data_type_country_region"></span>
<strong>SENSOR_DATA_TYPE_COUNTRY_REGION</strong>
(PID = 28)</td>
<td><p><strong>VT_LPWSTR</strong></p>
<p>Country or region, represented as an ISO 3166 1-alpha-2 country/region code.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_DGPS_DATA_AGE"></span><span id="sensor_data_type_dgps_data_age"></span>
<strong>SENSOR_DATA_TYPE_DGPS_DATA_AGE</strong>
(PID = 35)</td>
<td><p><strong>VT_R8</strong></p>
<p>Age of differential GPS data, in seconds.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_DIFFERENTIAL_REFERENCE_STATION_ID"></span><span id="sensor_data_type_differential_reference_station_id"></span>
<strong>SENSOR_DATA_TYPE_DIFFERENTIAL_REFERENCE_STATION_ID</strong>
(PID = 37)</td>
<td><p><strong>VT_I4</strong></p>
<p>ID of the differential reference station. The range is 0000 to 1023.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_ERROR_RADIUS_METERS"></span><span id="sensor_data_type_error_radius_meters"></span>
<strong>SENSOR_DATA_TYPE_ERROR_RADIUS_METERS</strong>
(PID = 22)</td>
<td><p><strong>VT_R8</strong></p>
<p>Accuracy of latitude and longitude values, in meters. A value of zero means that the accuracy level is not known. The Location API gives priority to sensors that provide a non-zero value for this field.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_FIX_QUALITY"></span><span id="sensor_data_type_fix_quality"></span>
<strong>SENSOR_DATA_TYPE_FIX_QUALITY</strong>
(PID = 10)</td>
<td><p><strong>VT_I4</strong></p>
<p>Fix quality</p>
<p>0 = no fix</p>
<p>1 = GPS</p>
<p>2 = DGPS</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_FIX_TYPE"></span><span id="sensor_data_type_fix_type"></span>
<strong>SENSOR_DATA_TYPE_FIX_TYPE</strong>
(PID = 11)</td>
<td><p><strong>VT_I4</strong></p>
<p>Fix type</p>
<p>0 = no fix</p>
<p>1 = GPS SPS Mode, fix valid</p>
<p>2 = DGPS SPS Mode, fix valid</p>
<p>3 = GPS PPS Mode, fix valid</p>
<p>4 = Real Time Kinematic</p>
<p>5 = Float RTK</p>
<p>6 = Estimated (dead reckoned)</p>
<p>7 = Manual Input Mode</p>
<p>8 = Simulator Mode</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_GEOIDAL_SEPARATION"></span><span id="sensor_data_type_geoidal_separation"></span>
<strong>SENSOR_DATA_TYPE_GEOIDAL_SEPARATION</strong>
(PID = 34)</td>
<td><p><strong>VT_R8</strong></p>
<p>The difference between the WGS-84 ellipsoid and mean sea level. Values less than zero indicate that mean sea level is below the reference ellipsoid.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_GPS_OPERATION_MODE"></span><span id="sensor_data_type_gps_operation_mode"></span>
<strong>SENSOR_DATA_TYPE_GPS_OPERATION_MODE</strong>
(PID = 32)</td>
<td><p><strong>VT_I4</strong></p>
<p>Operation mode.</p>
<p>0 = Manual. The GPS sensor is set to operate in 2-D or 3-D mode.</p>
<p>1 = Automatic. The GPS sensor can automatically switch between 2-D and 3-D modes.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_GPS_SELECTION_MODE"></span><span id="sensor_data_type_gps_selection_mode"></span>
<strong>SENSOR_DATA_TYPE_GPS_SELECTION_MODE</strong>
(PID = 31)</td>
<td><p><strong>VT_I4</strong></p>
<p>Selection mode.</p>
<p>0 = Autonomous.</p>
<p>1 = DGPS.</p>
<p>2 = Estimated (dead reckoned).</p>
<p>3 = Manual input.</p>
<p>4 = Simulator.</p>
<p>5 = Data not valid.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_GPS_STATUS"></span><span id="sensor_data_type_gps_status"></span>
<strong>SENSOR_DATA_TYPE_GPS_STATUS</strong>
(PID = 33)</td>
<td><p><strong>VT_I4</strong></p>
<p>Current data status.</p>
<p>1 = Data is valid.</p>
<p>2 = Data is not valid.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_HORIZONAL_DILUTION_OF_PRECISION"></span><span id="sensor_data_type_horizonal_dilution_of_precision"></span>
<strong>SENSOR_DATA_TYPE_HORIZONAL_DILUTION_OF_PRECISION</strong>
(PID = 13)</td>
<td><p><strong>VT_R8</strong></p>
<p>Horizontal dilution of precision.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_LATITUDE_DEGREES"></span><span id="sensor_data_type_latitude_degrees"></span>
<strong>SENSOR_DATA_TYPE_LATITUDE_DEGREES</strong>
(PID = 2)</td>
<td><p><strong>VT_R8</strong></p>
<p>Degrees latitude. North is positive.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_LONGITUDE_DEGREES"></span><span id="sensor_data_type_longitude_degrees"></span>
<strong>SENSOR_DATA_TYPE_LONGITUDE_DEGREES</strong>
(PID = 3)</td>
<td><p><strong>VT_R8</strong></p>
<p>Degrees longitude. East is positive.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_MAGNETIC_HEADING_DEGREES"></span><span id="sensor_data_type_magnetic_heading_degrees"></span>
<strong>SENSOR_DATA_TYPE_MAGNETIC_HEADING_DEGREES</strong>
(PID = 8)</td>
<td><p><strong>VT_R8</strong></p>
<p>Heading, in relation to magnetic north, in degrees.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_MAGNETIC_VARIATION"></span><span id="sensor_data_type_magnetic_variation"></span>
<strong>SENSOR_DATA_TYPE_MAGNETIC_VARIATION</strong>
(PID = 9)</td>
<td><p><strong>VT_R8</strong></p>
<p>Magnetic variation. East is positive.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_NMEA_SENTENCE"></span><span id="sensor_data_type_nmea_sentence"></span>
<strong>SENSOR_DATA_TYPE_NMEA_SENTENCE</strong>
(PID = 38)</td>
<td><p><strong>VT_LPWSTR</strong></p>
<p>The current NMEA sentence string.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_POSITION_DILUTION_OF_PRECISION"></span><span id="sensor_data_type_position_dilution_of_precision"></span>
<strong>SENSOR_DATA_TYPE_POSITION_DILUTION_OF_PRECISION</strong>
(PID = 12)</td>
<td><p><strong>VT_R8</strong></p>
<p>Position dilution of precision.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_POSTALCODE"></span><span id="sensor_data_type_postalcode"></span>
<strong>SENSOR_DATA_TYPE_POSTALCODE</strong>
(PID = 27)</td>
<td><p><strong>VT_LPWSTR</strong></p>
<p>Postal code.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_SATELLITES_IN_VIEW"></span><span id="sensor_data_type_satellites_in_view"></span>
<strong>SENSOR_DATA_TYPE_SATELLITES_IN_VIEW</strong>
(PID = 17)</td>
<td><p><strong>VT_I4</strong></p>
<p>Number of satellites in view.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_AZIMUTH"></span><span id="sensor_data_type_satellites_in_view_azimuth"></span>
<strong>SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_AZIMUTH</strong>
(PID = 20)</td>
<td><p><strong>VT_VECTOR|VT_UI1</strong></p>
<p>Counted array that contains the azimuth of each satellite in view.</p>
<p>Data for vector types is always serialized as <strong>VT_UI1</strong> (an array of unsigned, 1-byte characters). This data field actually contains each value as an IEEE 8-byte real value (<strong>VT_ R8</strong>). Use -1 as a placeholder for empty values.</p>
<p>For information about working with arrays, see <a href="https://msdn.microsoft.com/library/windows/desktop/ee264327" data-raw-source="[Retrieving Vector Types](https://msdn.microsoft.com/library/windows/desktop/ee264327)">Retrieving Vector Types</a>.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ELEVATION"></span><span id="sensor_data_type_satellites_in_view_elevation"></span>
<strong>SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ELEVATION</strong>
(PID = 19)</td>
<td><p><strong>VT_VECTOR|VT_UI1</strong></p>
<p>Counted array that contains the elevation of each satellite in view.</p>
<p>Data for vector types is always serialized as <strong>VT_UI1</strong> (an array of unsigned, 1-byte characters). This data field actually contains each value as an IEEE 8-byte real value (<strong>VT_R8</strong>). Use -91 as a placeholder for empty values.</p>
<p>For information about working with arrays, see <a href="https://msdn.microsoft.com/library/windows/desktop/ee264327" data-raw-source="[Retrieving Vector Types](https://msdn.microsoft.com/library/windows/desktop/ee264327)">Retrieving Vector Types</a>.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ID"></span><span id="sensor_data_type_satellites_in_view_id"></span>
<strong>SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ID</strong>
(PID = 39)</td>
<td><p><strong>VT_VECTOR|VT_UI1</strong></p>
<p>Counted array that contains the ID of each satellite in view.</p>
<p>Data for vector types is always serialized as <strong>VT_UI1</strong> (an array of unsigned, 1-byte characters). This data field actually contains each value as a 4-byte unsigned integer (<strong>VT_UI4</strong>).</p>
<p>For information about working with arrays, see <a href="https://msdn.microsoft.com/library/windows/desktop/ee264327" data-raw-source="[Retrieving Vector Types](https://msdn.microsoft.com/library/windows/desktop/ee264327)">Retrieving Vector Types</a>.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_PRNS"></span><span id="sensor_data_type_satellites_in_view_prns"></span>
<strong>SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_PRNS</strong>
(PID = 18)</td>
<td><p><strong>VT_VECTOR|VT_UI1</strong></p>
<p>Counted array that contains pseudorandom noise codes for satellites in view.</p>
<p>Data for vector types is always serialized as <strong>VT_UI1</strong> (an array of unsigned, 1-byte characters). This data field actually contains each value as a 4-byte unsigned integer (<strong>VT_UI4</strong>). Use zero (0) as a placeholder for empty values.</p>
<p>For information about working with arrays, see <a href="https://msdn.microsoft.com/library/windows/desktop/ee264327" data-raw-source="[Retrieving Vector Types](https://msdn.microsoft.com/library/windows/desktop/ee264327)">Retrieving Vector Types</a>.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_SATELLITES_USED_PRNS_AND_CONSTELLATIONS"></span><span id="sensor_data_type_satellites_used_prns_and_constellations"></span>
<strong>SENSOR_DATA_TYPE_SATELLITES_USED_PRNS_AND_CONSTELLATIONS</strong>
(PID = 41)</td>
<td><p><strong>VT_VECTOR|VT_UI2</strong></p>
<p>Counted array that contains pseudorandom noise codes for satellites that are used in a solution.</p>
<p>Data for vector types is always serialized as <strong>VT_UI2</strong> (an array of unsigned, 2-byte characters). This data field must contain each value as a 4-byte unsigned integer (<strong>VT_UI4</strong>). Use zero (0) as a placeholder for empty values.</p>
<p>For information about working with arrays, see <a href="https://msdn.microsoft.com/library/windows/desktop/ee264327" data-raw-source="[Retrieving Vector Types](https://msdn.microsoft.com/library/windows/desktop/ee264327)">Retrieving Vector Types</a>.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_STN_RATIO"></span><span id="sensor_data_type_satellites_in_view_stn_ratio"></span>
<strong>SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_STN_RATIO</strong>
(PID = 21)</td>
<td><p><strong>VT_VECTOR|VT_UI1</strong></p>
<p>Counted array that contains the signal-to-noise ratio for satellites in view.</p>
<p>Data for vector types is always serialized as <strong>VT_UI1</strong> (an array of unsigned, 1-byte characters). This data field actually contains each value as an IEEE 8-byte real value (<strong>VT_R8</strong>). Use zero (0) as a placeholder for empty values.</p>
<p>This property is required and must be supported by all GPS devices.</p>
<p>For information about working with arrays, see <a href="https://msdn.microsoft.com/library/windows/desktop/ee264327" data-raw-source="[Retrieving Vector Types](https://msdn.microsoft.com/library/windows/desktop/ee264327)">Retrieving Vector Types</a>.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_SATELLITES_USED_COUNT"></span><span id="sensor_data_type_satellites_used_count"></span>
<strong>SENSOR_DATA_TYPE_SATELLITES_USED_COUNT</strong>
(PID = 15)</td>
<td><p><strong>VT_I4</strong></p>
<p>Number of satellites that are used in a solution.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_SATELLITES_USED_PRNS"></span><span id="sensor_data_type_satellites_used_prns"></span>
<strong>SENSOR_DATA_TYPE_SATELLITES_USED_PRNS</strong>
(PID = 16)</td>
<td><p><strong>VT_VECTOR|VT_UI1</strong></p>
<p>Counted array that contains pseudorandom noise codes for satellites that are used in a solution.</p>
<p>Data for vector types is always serialized as <strong>VT_UI1</strong> (an array of unsigned, 1-byte characters). This data field must contain each value as a 4-byte unsigned integer (<strong>VT_UI4</strong>). Use zero (0) as a placeholder for empty values.</p>
<p>For information about working with arrays, see <a href="https://msdn.microsoft.com/library/windows/desktop/ee264327" data-raw-source="[Retrieving Vector Types](https://msdn.microsoft.com/library/windows/desktop/ee264327)">Retrieving Vector Types</a>.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_SPEED_KNOTS"></span><span id="sensor_data_type_speed_knots"></span>
<strong>SENSOR_DATA_TYPE_SPEED_KNOTS</strong>
(PID = 6)</td>
<td><p><strong>VT_R8</strong></p>
<p>Speed, in knots.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_STATE_PROVINCE"></span><span id="sensor_data_type_state_province"></span>
<strong>SENSOR_DATA_TYPE_STATE_PROVINCE</strong>
(PID = 26)</td>
<td><p><strong>VT_LPWSTR</strong></p>
<p>State/province.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_TRUE_HEADING_DEGREES"></span><span id="sensor_data_type_true_heading_degrees"></span>
<strong>SENSOR_DATA_TYPE_TRUE_HEADING_DEGREES</strong>
(PID = 7)</td>
<td><p><strong>VT_R8</strong></p>
<p>Heading, in relation to true north, in degrees.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_VERTICAL_DILUTION_OF_PRECISION"></span><span id="sensor_data_type_vertical_dilution_of_precision"></span>
<strong>SENSOR_DATA_TYPE_VERTICAL_DILUTION_OF_PRECISION</strong>
(PID = 14)</td>
<td><p><strong>VT_R8</strong></p>
<p>Vertical dilution of precision.</p></td>
</tr>
</tbody>
</table>

 

 





