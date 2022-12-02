---
title: SENSOR_CATEGORY_LOCATION
description: The SENSOR_CATEGORY_LOCATION category contains sensors that provide geographic location information.
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
ms.date: 12/01/2022
---

# SENSOR_CATEGORY_LOCATION

The SENSOR_CATEGORY_LOCATION category contains sensors that provide geographic location information.

## Platform-defined sensor types

This category includes the following platform-defined sensor types.

| Sensor type | Description |
|---|---|
| **SENSOR_TYPE_LOCATION_BROADCAST** {D26988CF-5162-4039-BB17-4C58B698E44A} | Sensors that transmit location information by using transmissions such as television or radio frequencies. |
| **SENSOR_TYPE_LOCATION_DEAD_RECKONING** {1A37D538-F28B-42DA-9FCE-A9D0A2A6D829} | Dead-reckoning sensors. These sensors first calculate the current location and then update the current location by using motion data. |
| **SENSOR_TYPE_LOCATION_GPS** {ED4CA589-327A-4FF9-A560-91DA4B48275E} | Global positioning system sensors. |
| **SENSOR_TYPE_LOCATION_LOOKUP** {3B2EAE4A-72CE-436D-96D2-3C5B8570E987} | Lookup sensors, such as those that provide information based on the user's IP address. |
| **SENSOR_TYPE_LOCATION_OTHER** {9B2D0566-0368-4F71-B88D-533F132031DE} | Other location sensors. |
| **SENSOR_TYPE_LOCATION_STATIC** {095F8184-0FA9-4445-8E6E-B70F320B6B4C} | Fixed-location sensors, such as those that use preset, user-provided information. |
| **SENSOR_TYPE_LOCATION_TRIANGULATION** {691C341A-5406-4FE1-942F-2246CBEB39E0} | Triangulation sensors, such as those that determine current location based on cellular phone tower proximities. |

## Platform-defined data fields

Platform-defined property keys for this category are based on **SENSOR_DATA_TYPE_LOCATION_GUID**: {055C74D8-CA6F-47D6-95C6-1ED3637A0FF4}

This category includes the following platform-defined data fields.

| Data field name and PID | Data type | Description |
|---|---|---|
| **SENSOR_DATA_TYPE_ADDRESS1** (PID = 23) | **VT_LPWSTR** | Street address, first line. |
| **SENSOR_DATA_TYPE_ADDRESS2** (PID = 24) | **VT_LPWSTR** | Street address, second line. |
| **SENSOR_DATA_TYPE_ALTITUDE_ANTENNA_SEALEVEL_METERS** (PID = 36) | **VT_R8** | Altitude of the antenna, referenced to sea level, in meters. |
| **SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_ERROR_METERS** (PID = 29) | **VT_R8** | Altitude error referenced to the World Geodetic System (WGS 84) reference ellipsoid, in meters. |
| **SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_METERS** (PID = 5) | **VT_R8** | Altitude referenced to the World Geodetic System (WGS 84) reference ellipsoid, in meters. |
| **SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_ERROR_METERS** (PID = 30) | **VT_R8** | Altitude error referenced to sea level, in meters. |
| **SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_METERS** (PID = 4) | **VT_R8** | Altitude referenced to sea level, in meters. |
| **SENSOR_DATA_TYPE_CITY** (PID = 25) | **VT_LPWSTR** | City |
| **SENSOR_DATA_TYPE_COUNTRY_REGION** (PID = 28) | **VT_LPWSTR** | Country or region, represented as an ISO 3166 1-alpha-2 country/region code. |
| **SENSOR_DATA_TYPE_DGPS_DATA_AGE** (PID = 35) | **VT_R8** | Age of differential GPS data, in seconds. |
| **SENSOR_DATA_TYPE_DIFFERENTIAL_REFERENCE_STATION_ID** (PID = 37) | **VT_I4** | ID of the differential reference station. The range is 0000 to 1023. |
| **SENSOR_DATA_TYPE_ERROR_RADIUS_METERS** (PID = 22) | **VT_R8** | Accuracy of latitude and longitude values, in meters. A value of zero means that the accuracy level is not known. The Location API gives priority to sensors that provide a non-zero value for this field. |
| **SENSOR_DATA_TYPE_FIX_QUALITY** (PID = 10) | **VT_I4** | Fix quality</br></br>0 = no fix</br>1 = GPS</br>2 = DGPS |
| **SENSOR_DATA_TYPE_FIX_TYPE** (PID = 11) | **VT_I4** | Fix type</br></br>0 = no fix</br>1 = GPS SPS Mode, fix valid</br>2 = DGPS SPS Mode, fix valid</br>3 = GPS PPS Mode, fix valid</br>4 = Real Time Kinematic</br>5 = Float RTK</br>6 = Estimated (dead reckoned)</br>7 = Manual Input Mode</br>8 = Simulator Mode |
| **SENSOR_DATA_TYPE_GEOIDAL_SEPARATION** (PID = 34) | **VT_R8** | The difference between the WGS-84 ellipsoid and mean sea level. Values less than zero indicate that mean sea level is below the reference ellipsoid. |
| **SENSOR_DATA_TYPE_GPS_OPERATION_MODE** (PID = 32) | **VT_I4** | Operation mode.</br></br>0 = Manual. The GPS sensor is set to operate in 2-D or 3-D mode.</br>1 = Automatic. The GPS sensor can automatically switch between 2-D and 3-D modes. |
| **SENSOR_DATA_TYPE_GPS_SELECTION_MODE** (PID = 31) | **VT_I4** | Selection mode.</br></br>0 = Autonomous.</br>1 = DGPS.</br>2 = Estimated (dead reckoned).</br>3 = Manual input.</br>4 = Simulator.</br>5 = Data not valid. |
| **SENSOR_DATA_TYPE_GPS_STATUS** (PID = 33) | **VT_I4** | Current data status.</br></br>1 = Data is valid.</br>2 = Data is not valid. |
| **SENSOR_DATA_TYPE_HORIZONAL_DILUTION_OF_PRECISION** (PID = 13) | **VT_R8** | Horizontal dilution of precision. |
| **SENSOR_DATA_TYPE_LATITUDE_DEGREES** (PID = 2) | **VT_R8** | Degrees latitude. North is positive. |
| **SENSOR_DATA_TYPE_LONGITUDE_DEGREES** (PID = 3) | **VT_R8** | Degrees longitude. East is positive. |
| **SENSOR_DATA_TYPE_MAGNETIC_HEADING_DEGREES** (PID = 8) | **VT_R8** | Heading, in relation to magnetic north, in degrees. |
| **SENSOR_DATA_TYPE_MAGNETIC_VARIATION** (PID = 9) | **VT_R8** | Magnetic variation. East is positive. |
| **SENSOR_DATA_TYPE_NMEA_SENTENCE** (PID = 38) | **VT_LPWSTR** | The current NMEA sentence string. |
| **SENSOR_DATA_TYPE_POSITION_DILUTION_OF_PRECISION** (PID = 12) | **VT_R8** | Position dilution of precision. |
| **SENSOR_DATA_TYPE_POSTALCODE** (PID = 27) | **VT_LPWSTR** | Postal code. |
| **SENSOR_DATA_TYPE_SATELLITES_IN_VIEW** (PID = 17) | **VT_I4** | Number of satellites in view. |
| **SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_AZIMUTH** (PID = 20) | **VT_VECTOR\|VT_UI1** | Counted array that contains the azimuth of each satellite in view.</br></br>Data for vector types is always serialized as VT_UI1 (an array of unsigned, 1-byte characters). This data field actually contains each value as an IEEE 8-byte real value (VT_ R8). Use -1 as a placeholder for empty values.</br></br>For information about working with arrays, see [Retrieving Vector Types](/windows/desktop/SensorsAPI/retrieving-vector-types). |
| **SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ELEVATION** (PID = 19) | **VT_VECTOR\|VT_UI1** | Counted array that contains the elevation of each satellite in view.</br></br>Data for vector types is always serialized as VT_UI1 (an array of unsigned, 1-byte characters). This data field actually contains each value as an IEEE 8-byte real value (VT_R8). Use -91 as a placeholder for empty values.</br></br>For information about working with arrays, see [Retrieving Vector Types](/windows/desktop/SensorsAPI/retrieving-vector-types). |
| **SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ID** (PID = 39) | **VT_VECTOR\|VT_UI1** | Counted array that contains the ID of each satellite in view.</br></br>Data for vector types is always serialized as VT_UI1 (an array of unsigned, 1-byte characters). This data field actually contains each value as a 4-byte unsigned integer (VT_UI4).</br></br>For information about working with arrays, see [Retrieving Vector Types](/windows/desktop/SensorsAPI/retrieving-vector-types). |
| **SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_PRNS** (PID = 18) | **VT_VECTOR\|VT_UI1** | Counted array that contains pseudorandom noise codes for satellites in view.</br></br>Data for vector types is always serialized as VT_UI1 (an array of unsigned, 1-byte characters). This data field actually contains each value as a 4-byte unsigned integer (VT_UI4). Use zero (0) as a placeholder for empty values.</br></br>For information about working with arrays, see [Retrieving Vector Types](/windows/desktop/SensorsAPI/retrieving-vector-types). |
| **SENSOR_DATA_TYPE_SATELLITES_USED_PRNS_AND_CONSTELLATIONS** (PID = 41) | **VT_VECTOR\|VT_UI2** | Counted array that contains pseudorandom noise codes for satellites that are used in a solution.</br></br>Data for vector types is always serialized as VT_UI2 (an array of unsigned, 2-byte characters). This data field must contain each value as a 4-byte unsigned integer (VT_UI4). Use zero (0) as a placeholder for empty values.</br></br>For information about working with arrays, see [Retrieving Vector Types](/windows/desktop/SensorsAPI/retrieving-vector-types). |
| **SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_STN_RATIO** (PID = 21) | **VT_VECTOR\|VT_UI1** | Counted array that contains the signal-to-noise ratio for satellites in view.</br></br>Data for vector types is always serialized as VT_UI1 (an array of unsigned, 1-byte characters). This data field actually contains each value as an IEEE 8-byte real value (VT_R8). Use zero (0) as a placeholder for empty values.</br></br>This property is required and must be supported by all GPS devices.</br></br>For information about working with arrays, see [Retrieving Vector Types](/windows/desktop/SensorsAPI/retrieving-vector-types). |
| **SENSOR_DATA_TYPE_SATELLITES_USED_COUNT** (PID = 15) | **VT_I4** | Number of satellites that are used in a solution. |
| **SENSOR_DATA_TYPE_SATELLITES_USED_PRNS** (PID = 16) | **VT_VECTOR\|VT_UI1** | Counted array that contains pseudorandom noise codes for satellites that are used in a solution.</br></br>Data for vector types is always serialized as VT_UI1 (an array of unsigned, 1-byte characters). This data field must contain each value as a 4-byte unsigned integer (VT_UI4). Use zero (0) as a placeholder for empty values.</br></br>For information about working with arrays, see [Retrieving Vector Types](/windows/desktop/SensorsAPI/retrieving-vector-types). |
| **SENSOR_DATA_TYPE_SPEED_KNOTS** (PID = 6) | **VT_R8** | Speed, in knots. |
| **SENSOR_DATA_TYPE_STATE_PROVINCE** (PID = 26) | **VT_LPWSTR** | State/province. |
| **SENSOR_DATA_TYPE_TRUE_HEADING_DEGREES** (PID = 7) | **VT_R8** | Heading, in relation to true north, in degrees. |
| **SENSOR_DATA_TYPE_VERTICAL_DILUTION_OF_PRECISION** (PID = 14) | **VT_R8** | Vertical dilution of precision. |
