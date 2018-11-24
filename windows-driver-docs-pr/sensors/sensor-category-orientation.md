---
title: SENSOR\_CATEGORY\_ORIENTATION
description: The SENSOR\_CATEGORY\_ORIENTATION category contains sensors that provide information about physical orientation.
ms.assetid: F8089596-C68F-48B2-B4EF-FB7B8777F212
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
ms.date: 01/04/2018
ms.localizationpriority: medium
---

# SENSOR\_CATEGORY\_ORIENTATION


The SENSOR\_CATEGORY\_ORIENTATION category contains sensors that provide information about physical orientation. Compasses provide navigational orientation, such as those based on magnetic north. Inclinometers measure slope or elevation. Distance sensors measure the proximity of some object to the sensor.

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
<td><span id="SENSOR_TYPE_AGGREGATED_DEVICE_ORIENTATION"></span><span id="sensor_type_aggregated_device_orientation"></span>
<strong>SENSOR_TYPE_AGGREGATED_DEVICE_ORIENTATION</strong></td>
<td><p>Specifies the current device orientation by returning a Quaternion and, in some cases, a rotation matrix. (The rotation matrix is optional.)</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_TYPE_AGGREGATED_QUADRANT_ORIENTATION"></span><span id="sensor_type_aggregated_quadrant_orientation"></span>
<strong>SENSOR_TYPE_AGGREGATED_QUADRANT_ORIENTATION</strong></td>
<td><p>Specifies the current device orientation in degrees.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_TYPE_AGGREGATED_SIMPLE_DEVICE_ORIENTATION"></span><span id="sensor_type_aggregated_simple_device_orientation"></span>
<strong>SENSOR_TYPE_AGGREGATED_SIMPLE_DEVICE_ORIENTATION</strong></td>
<td><p>Specifies the device orientation as an enumeration. (This type specifies the device orientation using one of four general quadrants: 0 degrees, 90-degrees counter clockwise, 180-counter clockwise, and 270-degrees counter clockwise.)</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_TYPE_COMPASS_1D"></span><span id="sensor_type_compass_1d"></span>
<strong>SENSOR_TYPE_COMPASS_1D</strong>
{A415F6C5-CB50-49D0-8E62-A8270BD7A26C}</td>
<td><p>One-axis compasses.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_TYPE_COMPASS_2D"></span><span id="sensor_type_compass_2d"></span>
<strong>SENSOR_TYPE_COMPASS_2D</strong>
{15655CC0-997A-4D30-84DB-57CABA3648BB}</td>
<td><p>Two-axis compasses.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_TYPE_COMPASS_3D"></span><span id="sensor_type_compass_3d"></span>
<strong>SENSOR_TYPE_COMPASS_3D</strong>
{76B5CE0D-17DD-414D-93A1-E127F40BDF6E}</td>
<td><p>Three-axis compasses.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_TYPE_DISTANCE_1D"></span><span id="sensor_type_distance_1d"></span>
<strong>SENSOR_TYPE_DISTANCE_1D</strong>
{5F14AB2F-1407-4306-A93F-B1DBABE4F9C0}</td>
<td><p>One-axis distance sensors.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_TYPE_DISTANCE_2D"></span><span id="sensor_type_distance_2d"></span>
<strong>SENSOR_TYPE_DISTANCE_2D</strong>
{5CF9A46C-A9A2-4E55-B6A1-A04AAFA95A92}</td>
<td><p>Two-axis distance sensors.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_TYPE_DISTANCE_3D"></span><span id="sensor_type_distance_3d"></span>
<strong>SENSOR_TYPE_DISTANCE_3D</strong>
{A20CAE31-0E25-4772-9FE5-96608A1354B2}</td>
<td><p>Three-axis distance sensors.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_TYPE_INCLINOMETER_1D"></span><span id="sensor_type_inclinometer_1d"></span>
<strong>SENSOR_TYPE_INCLINOMETER_1D</strong>
{B96F98C5-7A75-4BA7-94E9-AC868C966DD8}</td>
<td><p>One-axis inclinometers.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_TYPE_INCLINOMETER_2D"></span><span id="sensor_type_inclinometer_2d"></span>
<strong>SENSOR_TYPE_INCLINOMETER_2D</strong>
{AB140F6D-83EB-4264-B70B-B16A5B256A01}</td>
<td><p>Two-axis inclinometers.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_TYPE_INCLINOMETER_3D"></span><span id="sensor_type_inclinometer_3d"></span>
<strong>SENSOR_TYPE_INCLINOMETER_3D</strong>
{B84919FB-EA85-4976-8444-6F6F5C6D31DB}</td>
<td><p>Three-axis inclinometers.</p></td>
</tr>
</tbody>
</table>

**Platform-Defined Data Fields**

Platform-defined property keys for this category are based on SENSOR\_DATA\_TYPE\_ORIENTATION\_GUID:

{1637D8A2-4248-4275-865D-558DE84AEDFD}

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
<td><span id="SENSOR_DATA_TYPE_ANGULAR_VELOCITY_X_DEGREES_PER_SECOND"></span><span id="sensor_data_type_angular_velocity_x_degrees_per_second"></span>
<strong>SENSOR_DATA_TYPE_ANGULAR_VELOCITY_X_DEGREES_PER_SECOND</strong>
(PID = 10)</td>
<td><p><strong>VT_R8</strong></p>
<p>Gyrometer x-axis velocity, in degrees per second.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Y_DEGREES_PER_SECOND"></span><span id="sensor_data_type_angular_velocity_y_degrees_per_second"></span>
<strong>SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Y_DEGREES_PER_SECOND</strong>
(PID = 11)</td>
<td><p><strong>VT_R8</strong></p>
<p>Gyrometer y-axis velocity, in degrees per second.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Z_DEGREES_PER_SECOND"></span><span id="sensor_data_type_angular_velocity_z_degrees_per_second"></span>
<strong>SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Z_DEGREES_PER_SECOND</strong>
(PID = 12)</td>
<td><p><strong>VT_R8</strong></p>
<p>Gyrometer z-axis velocity, in degrees per second.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_TILT_X_DEGREES"></span><span id="sensor_data_type_tilt_x_degrees"></span>
<strong>SENSOR_DATA_TYPE_TILT_X_DEGREES</strong>
(PID = 2)</td>
<td><p><strong>VT_R4</strong></p>
<p>Inclinometer x-axis angle, in degrees.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_TILT_Y_DEGREES"></span><span id="sensor_data_type_tilt_y_degrees"></span>
<strong>SENSOR_DATA_TYPE_TILT_Y_DEGREES</strong>
(PID = 3)</td>
<td><p><strong>VT_R4</strong></p>
<p>Inclinometer y-axis angle, in degrees.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_TILT_Z_DEGREES"></span><span id="sensor_data_type_tilt_z_degrees"></span>
<strong>SENSOR_DATA_TYPE_TILT_Z_DEGREES</strong>
(PID = 4)</td>
<td><p><strong>VT_R4</strong></p>
<p>Inclinometer z-axis angle, in degrees.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_DISTANCE_X_METERS"></span><span id="sensor_data_type_distance_x_meters"></span>
<strong>SENSOR_DATA_TYPE_DISTANCE_X_METERS</strong>
(PID = 8)</td>
<td><p><strong>VT_R4</strong></p>
<p>X-axis distance, in meters.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_DISTANCE_Y_METERS"></span><span id="sensor_data_type_distance_y_meters"></span>
<strong>SENSOR_DATA_TYPE_DISTANCE_Y_METERS</strong>
(PID = 9)</td>
<td><p><strong>VT_R4</strong></p>
<p>Y-axis distance, in meters.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_DISTANCE_Z_METERS"></span><span id="sensor_data_type_distance_z_meters"></span>
<strong>SENSOR_DATA_TYPE_DISTANCE_Z_METERS</strong>
(PID = 10)</td>
<td><p><strong>VT_R4</strong></p>
<p>Z-axis distance, in meters.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_X_MILLIGAUSS"></span><span id="sensor_data_type_magnetic_field_strength_x_milligauss"></span>
<strong>SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_X_MILLIGAUSS</strong>
(PID = 19)</td>
<td><p><strong>VT_R8</strong></p>
<p>Magnetometer x-axis field strength, in milligauss.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Y_MILLIGAUSS"></span><span id="sensor_data_type_magnetic_field_strength_y_milligauss"></span>
<strong>SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Y_MILLIGAUSS</strong>
(PID = 20)</td>
<td><p><strong>VT_R8</strong></p>
<p>Magnetometer y-axis field strength, in milligauss.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Z_MILLIGAUSS"></span><span id="sensor_data_type_magnetic_field_strength_z_milligauss"></span>
<strong>SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Z_MILLIGAUSS</strong>
(PID = 21)</td>
<td><p><strong>VT_R8</strong></p>
<p>Magnetometer z-axis field strength, in milligauss.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_MAGNETIC_HEADING_X_DEGREES"></span><span id="sensor_data_type_magnetic_heading_x_degrees"></span>
<strong>SENSOR_DATA_TYPE_MAGNETIC_HEADING_X_DEGREES</strong>
(PID = 5)</td>
<td><p><strong>VT_R4</strong></p>
<p>Compass x-axis heading, in degrees.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_MAGNETIC_HEADING_Y_DEGREES"></span><span id="sensor_data_type_magnetic_heading_y_degrees"></span>
<strong>SENSOR_DATA_TYPE_MAGNETIC_HEADING_Y_DEGREES</strong>
(PID = 6)</td>
<td><p><strong>VT_R4</strong></p>
<p>Compass y-axis heading, in degrees.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_MAGNETIC_HEADING_Z_DEGREES"></span><span id="sensor_data_type_magnetic_heading_z_degrees"></span>
<strong>SENSOR_DATA_TYPE_MAGNETIC_HEADING_Z_DEGREES</strong>
(PID = 7)</td>
<td><p><strong>VT_R4</strong></p>
<p>Compass z-axis heading, in degrees.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_MAGNETIC_NORTH_DEGREES_"></span><span id="sensor_data_type_magnetic_heading_compensated_magnetic_north_degrees_"></span>
<strong>SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_MAGNETIC_NORTH_DEGREES</strong>
(PID = 11)</td>
<td><p><strong>VT_R8</strong></p>
<p>Compensated compass heading relative to magnetic North in degrees. This compensation causes the measurement of the heading angle to be represented as if a compass device is laying flat on level ground where the PC is located.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_TRUE_NORTH_DEGREES_"></span><span id="sensor_data_type_magnetic_heading_compensated_true_north_degrees_"></span>
<strong>SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_TRUE_NORTH_DEGREES</strong>
(PID = 12)</td>
<td><p><strong>VT_R8</strong></p>
<p>Compensated compass heading relative to true North in degrees. This compensation causes the measurement of the heading angle to be represented as if a compass device is laying flat on level ground where the PC is located.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_MAGNETIC_HEADING_MAGNETIC_NORTH_DEGREES__"></span><span id="sensor_data_type_magnetic_heading_magnetic_north_degrees__"></span>
<strong>SENSOR_DATA_TYPE_MAGNETIC_HEADING_MAGNETIC_NORTH_DEGREES</strong>
(PID = 13)</td>
<td><p><strong>VT_R8</strong></p>
<p>Uncompensated compass heading relative to magnetic North in degrees. The measurement of the heading angle is represented as measured on the plane that the compass device is installed relative to.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_MAGNETIC_HEADING_TRUE_NORTH_DEGREES___"></span><span id="sensor_data_type_magnetic_heading_true_north_degrees___"></span>
<strong>SENSOR_DATA_TYPE_MAGNETIC_HEADING_TRUE_NORTH_DEGREES</strong>
(PID = 14)</td>
<td><p><strong>VT_R8</strong></p>
<p>Uncompensated compass heading relative to true North in degrees. The measurement of the heading angle is represented as measured on the plane that the compass device is installed relative to.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_QUADRANT_ANGLE_DEGREES"></span><span id="sensor_data_type_quadrant_angle_degrees"></span>
<strong>SENSOR_DATA_TYPE_QUADRANT_ANGLE_DEGREES</strong>
(PID = 15)</td>
<td><p><strong>VT_R8</strong></p>
<p>Aggregated quadrant-orientation, in degrees.</p></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_ROTATION_MATRIX"></span><span id="sensor_data_type_rotation_matrix"></span>
<strong>SENSOR_DATA_TYPE_ROTATION_MATRIX</strong>
(PID = 16)</td>
<td><p><strong>VT_VECTOR|VT_UI1</strong></p>
<p>Counted array representing the orientation of the device in 3D space as a 3x3 rotation matrix (VT_VECTOR|VT_UI1).</p>
<p>Data for vector types is always serialized as VT_UI1 (an array of unsigned, 1-byte characters). This data field must contain each value as a single-precision float (VT_R4).</p>
<p>This array is expressed as a matrix:</p>
<img src="images/sensor-data-type-rotation-matrix.png" alt="rotation matrix" />
<p>These values are ordered in the rotation matrix data field array as follows: M11,M12,M13,M21,M22,M23,M31,M32,M33</p>
<p>Note that for devices implementing support for the in-box Windows 8 HID sensor class driver, this data field is optional. If only <strong>SENSOR_DATA_TYPE_QUATERNION</strong> is implemented, <strong>SENSOR_DATA_TYPE_ROTATION_MATRIX</strong> will be calculated and populated for each data report sent. Devices not using the in-box HID sensor class driver need to calculate and expose both <strong>SENSOR_DATA_TYPE_QUATERNION</strong> and <strong>SENSOR_DATA_TYPE_ROTATION_MATRIX</strong> sensor data fields.</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_QUATERNION"></span><span id="sensor_data_type_quaternion"></span>
<strong>SENSOR_DATA_TYPE_QUATERNION</strong>
(PID = 17)</td>
<td><p><strong>VT_VECTOR|VT_UI1</strong></p>
<p>The x, y, z, w values of a quaternion representing the orientation of the device in 3D space. (VT_VECTOR|VT_UI1).</p>
<p>Data for vector types is always serialized as VT_UI1 (an array of unsigned, 1-byte characters).</p>
<p>This data field must contain each value as a single-precision float (VT_R4).</p>
<p>The order of the values in this array is as follows: [x,y,z,w]</p>
<p>The W value of a quaternion is limited to [0,1] instead of the full [-1, 1].</p>
<p>All rotations must be stated in the forward direction (and not the reverse).</p>
<p>Note: The output of quaternion should be in normalized format. When quaternions are expressed in normalized format, the values will satisfy the following:</p>
<img src="images/sensor-data-type-quaternion-formula.png" alt="quaternion formula" /></td>
</tr>
<tr class="odd">
<td><span id="SENSOR_DATA_TYPE_SIMPLE_DEVICE_ORIENTATION"></span><span id="sensor_data_type_simple_device_orientation"></span>
<strong>SENSOR_DATA_TYPE_SIMPLE_DEVICE_ORIENTATION</strong>
(PID = 18)</td>
<td><p><strong>VT_UI4</strong></p>
<p>Aggregated device-orientation, specified as an enumeration. (The enumeration values correspond to one of four quadrants.)</p></td>
</tr>
<tr class="even">
<td><span id="SENSOR_DATA_TYPE_MAGNETOMETER_ACCURACY"></span><span id="sensor_data_type_magnetometer_accuracy"></span>
<strong>SENSOR_DATA_TYPE_MAGNETOMETER_ACCURACY</strong>
(PID = 22)</td>
<td><p><strong>VT_I4</strong></p>
<p>Magnetometer accuracy reading, specified as an enumeration.</p></td>
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
<td><p>Header</p></td>
<td>Sensors.h</td>
</tr>
</tbody>
</table>

 

 





