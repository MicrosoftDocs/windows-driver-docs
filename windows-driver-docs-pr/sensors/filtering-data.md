---
title: Filtering data
description: In order to optimize data throughput, your sensor device must apply filter criteria to the data-update events so that they are only raised when needed.
ms.assetid: 1895EC5C-08C1-4976-83F2-CD5A2B55338D
keywords:
- change sensitivity
- sensor change sensitivity
- CS
- current report interval
- sensor current report interval
- CRI
- data update event
- sensor event
- sensor events
- filtering data
- data filtering
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Filtering data


In order to optimize data throughput, your sensor device must apply filter criteria to the data-update events so that they are only raised when needed. This filtering results in lower CPU utilization (due to reduced sensor throughput) and less power consumption (both for the sensor and the CPU).

There are two values (or properties) that support a sensor device’s filter criteria. The first is the current report interval (CRI) and the second is the change sensitivity (CS). Both of these properties can be set by a sensor application.

The current report interval is the minimum period, in milliseconds, between data updates which a client wishes to receive when meaningful change has occurred. The change sensitivity is the value (or percentage) used to specify meaningful change.

So, a weather-station application may specify a current report interval (CRI) for a temperature sensor of 60,000 (or one minute). And, the temperature sensor would require a change-sensitivity value (as opposed to a percentage). For example, if this temperature sensor returns degrees Celsius and the change sensitivity value temperature was 2.0, this particular sensor would only raise the data-updated event when the temperature increased, or decreased, by 2.0 degrees Celsius over the requested report interval (in this case, one minute).

An ambient light sensor (ALS) is an example of a sensor that would require change-sensitivity to be specified as a percentage. For example, if the change sensitivity value for Illuminance was 2.0, this sensor would interpret the value as a percentage and only raise the data-updated event when the LUX value had either dropped or increased by 2%.

The following table lists six common sensors, the data associated with each, and the corresponding change sensitivity.

| Sensor             | Datafield              | Change Sensitivity Value           |
|--------------------|------------------------|------------------------------------|
| Light Sensor       | LUX                    | % change in lux                    |
| Accelerometer      | Acceleration X         | Acceleration G-force               |
|                    | Acceleration Y         | Acceleration G-force               |
|                    | Acceleration Z         | Acceleration G-force               |
| 3D Gyrometer       | Angular Speed X        | Angular Speed (degrees per second) |
|                    | Angular Speed Y        | Angular Speed (degrees per second) |
|                    | Angular Speed Z        | Angular Speed (degrees per second) |
| Compass            | Magnetic North Heading | Degrees                            |
|                    | True North Heading     | Degrees                            |
| Inclinometer       | Yaw                    | Degrees                            |
|                    | Pitch                  | Degrees                            |
|                    | Roll                   | Degrees                            |
| Device Orientation | Quaternion             | Degrees Movement                   |
|                    | Rotation Matrix        | Degrees Movement                   |

 

The following table lists the recommended Current Report Interval (CRI) defaults.

| Sensor Type   | Recommended default report interval |
|---------------|-------------------------------------|
| Ambient Light | 5000                                |
| Accelerometer | 100                                 |
| Gyrometer     | 100                                 |
| Compass       | 100                                 |
| Inclinometer  | 50                                  |
| Orientation   | 50                                  |

 

The following table lists the recommended Change Sensitivity (CS) defaults.

|  Sensor Type  | Recommended default change sensitivity |
|---------------|----------------------------------------|
| Ambient Light | 50                                     |
| Accelerometer | 0.02                                   |
| Gyrometer     | 0.50                                   |
| Compass       | 0.20                                   |
| Inclinometer  | 0.50                                   |
| Orientation   | 0.50                                   |


## Change Sensitivity (CS) for the Inclinometer and Orientation Sensors


Change sensitivity for the inclinometer and orientation sensor should be calculated as the angle between two quaternions. Mathematically, this expressed as:

2\*cos⁻¹(dot product(q1, q2))

This calculation ensures consistency across various tablet (or device) orientations.

## Effective Current Report Interval (CRI) and Change Sensitivity (CS)


Multiple applications can set both the Current Report Interval (CRI) and the Change Sensitivity (CS) properties for a given sensor. It is the responsibility of your driver to determine which requested property applies. The properties set by the driver are referred to as the Effective Current Report-Interval (E-CRI) and the Effective Change-Sensitivity (E-CS).

## Setting the E-CRI and E-CS for Client Applications


Whenever a client application establishes a connection to a sensor, your driver needs to set the E-CRI and E-CS values. These values are stored in what’s referred to as a client container. The following table lists six methods supported by a sensor driver and specifies what your driver should do with its client container and the E-CRI and E-CS properties.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Event of Interest</td>
<td>Event Handler Activities</td>
</tr>
<tr class="even">
<td>ISensorDriver::OnClientConnect</td>
<td><p>Add client item to client container</p>
<p>Read default CRI and CS values as appropriate, store in client container</p></td>
</tr>
<tr class="odd">
<td>ISensorDriver::OnClientDisconnect</td>
<td><p>Remove client from client container and set the E-CRI and E-CS as appropriate based on the remaining clients</p></td>
</tr>
<tr class="even">
<td>ISensorDriver::OnClientSubscribeToEvents</td>
<td><p>Update “subscribed to events” field – (set to true) for the sensor in question. Turn on event reporting from the sensor.</p></td>
</tr>
<tr class="odd">
<td>ISensorDriver::OnClientUnSubscribeToEvents</td>
<td><p>Update “subscribed to events” field – (set to false) for the sensor in question. If no subscribers remain, turn off event reporting from the device.</p></td>
</tr>
<tr class="even">
<td>ISensorDriver::OnSetProperties</td>
<td><p>If CS or CRI properties are set, update appropriate client container fields.</p></td>
</tr>
<tr class="odd">
<td>IFileCallbackCleanup::OnCleanupFile</td>
<td><p>The client has crashed or stopped responding. The client should be removed from the client container.</p></td>
</tr>
</tbody>
</table>

 

The following table represents the client container for a 3D accelerometer with 4 connected client applications. Two of these client apps (corresponding to the 2nd and 4th row) have subscribed to events.

| Client File Handle | Subscribed To Events | CRI | CS (X) | CX (Y) | CS (Z) |
|--------------------|----------------------|-----|--------|--------|--------|
| FF80A267           | FALSE                | 50  | .001   | .001   | .001   |
| FF802489           | TRUE                 | 70  | .02    | .02    | .02    |
| FF80D345           | FALSE                | 15  | NULL   | NULL   | NULL   |
| FF803287           | TRUE                 | 100 | .005   | .005   | .005   |

 

After the driver evaluated this set of connected clients, it chose the following values for E-CRI and E-CS:

-   E-CRI: 70ms
-   E-CS values: (could collapse to single value using smallest threshold)
    -   X:.005
    -   Y:.005
    -   Z: .005

Notice in this example that clients that do not have an event sink set (first and third rows) are disregarded since event filtering does not apply to those clients.

## Filtering data update events by evaluating the effective CRI and CS values (E-CRI, E-CS)


Once the current E-CRI and E-CS values have been determined and are updated as sensor connection states change, your sensor device will use these values to filter events that are raised to connected client applications. These values are compared against the difference between the “current” data value(s) and the previous data value(s). If the E-CS values have been exceeded for a time period equal to or greater than the E-CRI, then, and only then, should a data event be raised. The only exception to this is sensor device startup when the default value(s) are applied so that clients can receive the proper notification.

The following illustration demonstrates how time filtering of raw sensor data is evaluated in order to determine when data events should be raised.

![time-filtered sensor data](images/cri-cs.png)

In the previous illustration, the red data in the lower portion of the diagram represents the raw sensor data. The green line represents data that would be returned to clients that poll for data (one of many ways to implement this behavior) and the “X” values represent when data events are fired. Blue lines are the thresholds for the E-CS boundaries (+/- E-CS relative to last data event value).

By implementing this event filtering logic, the number of data updated events can be greatly reduced, and applications can still get notified when meaningful changes in sensor data occur.

## Device runtime optimizations for data filtering


This section describes several runtime optimizations you should consider as you develop a sensor driver.

### Support interrupts

Your driver should rely on interrupts instead of polling the device. This will result in performance and power-management improvements. These improvements include the following.

1.  Your device can enter a lower power state based on the current change sensitivity and report interval.
2.  Using interrupts will reduce unnecessary code execution in both the driver and the sensor firmware.
3.  Using interrupts will reduce bus activity.

**Note**  If a driver relies on interrupts but the current report interval and change-sensitivity logic exists in the driver, the driver will potentially receive a significant number of interrupts between data updates. As a result, the driver may need to disable (or mask) interrupts until the current-report interval expires.

 

### Move change-sensitivity support to the device

If your sensor hardware, or firmware, supports threshold detection you should use this feature to support change sensitivity. By moving the support to the device, and then responding to the corresponding interrupt, you reduce processing overhead in your driver.

### Move report-interval support to the devices

If your sensor hardware, or firmware, supports the notion of a report interval you should use this feature.

If your sensor does not provide native report-interval support, consider disabling interrupts for a subset of the current report interval. Then, once this time elapses, retrieve the current device data.

## Related topics
[The Sensors Geolocation Driver Sample](https://docs.microsoft.com/windows-hardware/drivers/gnss/sensors-geolocation-driver-sample)



