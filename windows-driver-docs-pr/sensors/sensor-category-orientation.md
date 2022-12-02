---
title: SENSOR_CATEGORY_ORIENTATION
description: The SENSOR_CATEGORY_ORIENTATION category contains sensors that provide information about physical orientation.
topic_type:
- apiref
api_name:
- SENSOR_TYPE_AGGREGATED_DEVICE_ORIENTATION
- SENSOR_TYPE_AGGREGATED_QUADRANT_ORIENTATION
- SENSOR_TYPE_AGGREGATED_SIMPLE_DEVICE_ORIENTATION
- SENSOR_TYPE_COMPASS_1D
- SENSOR_TYPE_COMPASS_2D
- SENSOR_TYPE_COMPASS_3D
- SENSOR_TYPE_DISTANCE_1D
- SENSOR_TYPE_DISTANCE_2D
- SENSOR_TYPE_DISTANCE_3D
- SENSOR_TYPE_INCLINOMETER_1D
- SENSOR_TYPE_INCLINOMETER_2D
- SENSOR_TYPE_INCLINOMETER_3D
- SENSOR_DATA_TYPE_ANGULAR_VELOCITY_X_DEGREES_PER_SECOND
- SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Y_DEGREES_PER_SECOND
- SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Z_DEGREES_PER_SECOND
- SENSOR_DATA_TYPE_TILT_X_DEGREES
- SENSOR_DATA_TYPE_TILT_Y_DEGREES
- SENSOR_DATA_TYPE_TILT_Z_DEGREES
- SENSOR_DATA_TYPE_DISTANCE_X_METERS
- SENSOR_DATA_TYPE_DISTANCE_Y_METERS
- SENSOR_DATA_TYPE_DISTANCE_Z_METERS
- SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_X_MILLIGAUSS
- SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Y_MILLIGAUSS
- SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Z_MILLIGAUSS
- SENSOR_DATA_TYPE_MAGNETIC_HEADING_X_DEGREES
- SENSOR_DATA_TYPE_MAGNETIC_HEADING_Y_DEGREES
- SENSOR_DATA_TYPE_MAGNETIC_HEADING_Z_DEGREES
- SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_MAGNETIC_NORTH_DEGREES
- SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_TRUE_NORTH_DEGREES
- SENSOR_DATA_TYPE_MAGNETIC_HEADING_MAGNETIC_NORTH_DEGREES
- SENSOR_DATA_TYPE_MAGNETIC_HEADING_TRUE_NORTH_DEGREES
- SENSOR_DATA_TYPE_QUADRANT_ANGLE_DEGREES
- SENSOR_DATA_TYPE_ROTATION_MATRIX
- SENSOR_DATA_TYPE_QUATERNION
- SENSOR_DATA_TYPE_SIMPLE_DEVICE_ORIENTATION
- SENSOR_DATA_TYPE_MAGNETOMETER_ACCURACY
api_location:
- Sensors.h
api_type:
- HeaderDef
ms.date: 12/02/2022
---

# SENSOR_CATEGORY_ORIENTATION

The SENSOR_CATEGORY_ORIENTATION category contains sensors that provide information about physical orientation. Compasses provide navigational orientation, such as those based on magnetic north. Inclinometers measure slope or elevation. Distance sensors measure the proximity of some object to the sensor.

## Platform-defined sensor types

This category includes the following platform-defined sensor types.

| Sensor type | Description |
|---|---|
| **SENSOR_TYPE_AGGREGATED_DEVICE_ORIENTATION** | Specifies the current device orientation by returning a Quaternion and, in some cases, a rotation matrix. (The rotation matrix is optional.) |
| **SENSOR_TYPE_AGGREGATED_QUADRANT_ORIENTATION** | Specifies the current device orientation in degrees. |
| **SENSOR_TYPE_AGGREGATED_SIMPLE_DEVICE_ORIENTATION** | Specifies the device orientation as an enumeration. (This type specifies the device orientation using one of four general quadrants: 0 degrees, 90-degrees counter clockwise, 180-counter clockwise, and 270-degrees counter clockwise.) |
| **SENSOR_TYPE_COMPASS_1D**</br>{A415F6C5-CB50-49D0-8E62-A8270BD7A26C} | One-axis compasses. |
| **SENSOR_TYPE_COMPASS_2D**</br>{15655CC0-997A-4D30-84DB-57CABA3648BB} | Two-axis compasses. |
| **SENSOR_TYPE_COMPASS_3D**</br>{76B5CE0D-17DD-414D-93A1-E127F40BDF6E} | Three-axis compasses. |
| **SENSOR_TYPE_DISTANCE_1D**</br>{5F14AB2F-1407-4306-A93F-B1DBABE4F9C0} | One-axis distance sensors. |
| **SENSOR_TYPE_DISTANCE_2D**</br>{5CF9A46C-A9A2-4E55-B6A1-A04AAFA95A92} | Two-axis distance sensors. |
| **SENSOR_TYPE_DISTANCE_3D**</br>{A20CAE31-0E25-4772-9FE5-96608A1354B2} | Three-axis distance sensors. |
| **SENSOR_TYPE_INCLINOMETER_1D**</br>{B96F98C5-7A75-4BA7-94E9-AC868C966DD8} | One-axis inclinometers. |
| **SENSOR_TYPE_INCLINOMETER_2D**</br>{AB140F6D-83EB-4264-B70B-B16A5B256A01} | Two-axis inclinometers. |
| **SENSOR_TYPE_INCLINOMETER_3D**</br>{B84919FB-EA85-4976-8444-6F6F5C6D31DB} | Three-axis inclinometers. |

## Platform-defined data fields

Platform-defined property keys for this category are based on **SENSOR_DATA_TYPE_ORIENTATION_GUID**: {1637D8A2-4248-4275-865D-558DE84AEDFD}

This category includes the following platform-defined data fields.

| Data field name and PID | Type | Description |
|---|---|---|
| **SENSOR_DATA_TYPE_ANGULAR_VELOCITY_X_DEGREES_PER_SECOND**</br>(PID = 10) | **VT_R8** | Gyrometer x-axis velocity, in degrees per second. |
| **SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Y_DEGREES_PER_SECOND**</br>(PID = 11) | **VT_R8** | Gyrometer y-axis velocity, in degrees per second. |
| **SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Z_DEGREES_PER_SECOND**</br>(PID = 12) | **VT_R8** | Gyrometer z-axis velocity, in degrees per second. |
| **SENSOR_DATA_TYPE_TILT_X_DEGREES**</br>(PID = 2) | **VT_R4** | Inclinometer x-axis angle, in degrees. |
| **SENSOR_DATA_TYPE_TILT_Y_DEGREES**</br>(PID = 3) | **VT_R4** | Inclinometer y-axis angle, in degrees. |
| **SENSOR_DATA_TYPE_TILT_Z_DEGREES**</br>(PID = 4) | **VT_R4** | Inclinometer z-axis angle, in degrees. |
| **SENSOR_DATA_TYPE_DISTANCE_X_METERS**</br>(PID = 8) | **VT_R4** | X-axis distance, in meters. |
| **SENSOR_DATA_TYPE_DISTANCE_Y_METERS**</br>(PID = 9) | **VT_R4** | Y-axis distance, in meters. |
| **SENSOR_DATA_TYPE_DISTANCE_Z_METERS**</br>(PID = 10) | **VT_R4** | Z-axis distance, in meters. |
| **SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_X_MILLIGAUSS**</br>(PID = 19) | **VT_R8** | Magnetometer x-axis field strength, in milligauss. |
| **SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Y_MILLIGAUSS**</br>(PID = 20) | **VT_R8** | Magnetometer y-axis field strength, in milligauss. |
| **SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Z_MILLIGAUSS**</br>(PID = 21) | **VT_R8** | Magnetometer z-axis field strength, in milligauss. |
| **SENSOR_DATA_TYPE_MAGNETIC_HEADING_X_DEGREES**</br>(PID = 5) | **VT_R4** | Compass x-axis heading, in degrees. |
| **SENSOR_DATA_TYPE_MAGNETIC_HEADING_Y_DEGREES**</br>(PID = 6) | **VT_R4** | Compass y-axis heading, in degrees. |
| **SENSOR_DATA_TYPE_MAGNETIC_HEADING_Z_DEGREES**</br>(PID = 7) | **VT_R4** | Compass z-axis heading, in degrees. |
| **SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_MAGNETIC_NORTH_DEGREES**</br>(PID = 11) | **VT_R8** | Compensated compass heading relative to magnetic North in degrees. This compensation causes the measurement of the heading angle to be represented as if a compass device is laying flat on level ground where the PC is located. |
| **SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_TRUE_NORTH_DEGREES**</br>(PID = 12) | **VT_R8** | Compensated compass heading relative to true North in degrees. This compensation causes the measurement of the heading angle to be represented as if a compass device is laying flat on level ground where the PC is located. |
| **SENSOR_DATA_TYPE_MAGNETIC_HEADING_MAGNETIC_NORTH_DEGREES**</br>(PID = 13) | **VT_R8** | Uncompensated compass heading relative to magnetic North in degrees. The measurement of the heading angle is represented as measured on the plane that the compass device is installed relative to. |
| **SENSOR_DATA_TYPE_MAGNETIC_HEADING_TRUE_NORTH_DEGREES**</br>(PID = 14) | **VT_R8** | Uncompensated compass heading relative to true North in degrees. The measurement of the heading angle is represented as measured on the plane that the compass device is installed relative to. |
| **SENSOR_DATA_TYPE_QUADRANT_ANGLE_DEGREES**</br>(PID = 15) | **VT_R8** | Aggregated quadrant-orientation, in degrees. |
| **SENSOR_DATA_TYPE_ROTATION_MATRIX**</br>(PID = 16) | **VT_VECTOR\|VT_UI1** | Counted array representing the orientation of the device in 3D space as a 3x3 rotation matrix (VT_VECTOR\|VT_UI1).</br></br>Data for vector types is always serialized as VT_UI1 (an array of unsigned, 1-byte characters). This data field must contain each value as a single-precision float (VT_R4).</br></br>This array is expressed as a matrix:</br>![rotation matrix](images/sensor-data-type-rotation-matrix.png)</br></br>These values are ordered in the rotation matrix data field array as follows:</br>M11,M12,M13,M21,M22,M23,M31,M32,M33</br></br>Note that for devices implementing support for the in-box Windows 8 HID sensor class driver, this data field is optional. If only **SENSOR_DATA_TYPE_QUATERNION** is implemented, **SENSOR_DATA_TYPE_ROTATION_MATRIX** will be calculated and populated for each data report sent. Devices not using the in-box HID sensor class driver need to calculate and expose both **SENSOR_DATA_TYPE_QUATERNION** and **SENSOR_DATA_TYPE_ROTATION_MATRIX** sensor data fields. |
| **SENSOR_DATA_TYPE_QUATERNION**</br>(PID = 17) | **VT_VECTOR\|VT_UI1** | The x, y, z, w values of a quaternion representing the orientation of the device in 3D space. (VT_VECTOR\|VT_UI1).</br></br>Data for vector types is always serialized as VT_UI1 (an array of unsigned, 1-byte characters).</br></br>This data field must contain each value as a single-precision float (VT_R4).The order of the values in this array is as follows: [x,y,z,w]</br></br>The W value of a quaternion is limited to [0,1] instead of the full [-1, 1].</br></br>All rotations must be stated in the forward direction (and not the reverse).</br></br>Note: The output of quaternion should be in normalized format. When quaternions are expressed in normalized format, the values will satisfy the following:</br>![quaternion formula](images/sensor-data-type-quaternion-formula.png) |
| **SENSOR_DATA_TYPE_SIMPLE_DEVICE_ORIENTATION**</br>(PID = 18) | **VT_UI4** | Aggregated device-orientation, specified as an enumeration. (The enumeration values correspond to one of four quadrants.) |
| **SENSOR_DATA_TYPE_MAGNETOMETER_ACCURACY**</br>(PID = 22) | **VT_I4** | Magnetometer accuracy reading, specified as an enumeration. |

## Requirements

| &nbsp; | &nbsp; |
|---|---|
| **Minimum supported client** | Windows 7 |
| **Minimum supported server** | None supported |
| **Header** | sensors.h |
