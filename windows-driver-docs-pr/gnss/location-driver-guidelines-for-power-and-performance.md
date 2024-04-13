---
title: Location Driver Guidelines for Power and Performance
description: The following sections describe guidelines to ensure that your location driver conserves power and provides data efficiently.
ms.date: 03/21/2023
---

# Location driver guidelines for power and performance

The following sections describe guidelines to ensure that your location driver conserves power and provides data efficiently.

## Tracking the Number of Connected Clients and Radio State

Location sensors must track the number of connected applications, and must track the value of both the SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY and SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL properties for each subscribed application.

When the number of connected clients is zero, the location sensor should enter the lowest possible power state, preferably D3. When an event indicates that a client is connected, the sensor should exit the low-power state and acquire data.

Also, if the location device contains a radio, like a GPS location sensor, then the radio state must also be tracked using [Radio Management](/previous-versions/windows/hardware/radio/hh406615(v=vs.85)). The driver writer must create a Radio Management implementation that communicates with the driver to set the radio state. An example of the Radio Management implementation and how to communicate with the driver is in the [Sensors Geolocation Driver Sample](sensors-geolocation-driver-sample.md).

When tracking connected clients and radio state, the location sensor should enter the lowest possible power state, preferably D3, at any time there isn't a connected client while the radio is on. The diagram below illustrates a state machine for connected clients, radio state, and the suggested corresponding device state.

![state machine.](images/state-diagram-with-radio.png)

The following table provides another view of the various input combinations and the resulting outputs (including power state).

| Client exists (input) | Radio state (input) | CRI (input) | Position reported (input) | ASIC state (output) | Sensor state (output) | Power state (output) |
|--|--|--|--|--|--|--|
| No | Any | Any | Any | Off | N/A | D3 |
| Yes | On | <=120 seconds | No | On | Initializing | D0 |
| Yes | On | <=120 seconds | Yes | On | Ready | D0 |
| Yes | Off | Any | Any | Off | Not available | D3 |
| Yes | On | >120 seconds | Any | Off | Ready | D3 |
| Yes | On | >120 seconds | Any | On | Ready | D0 |

The [Sensors Geolocation Driver Sample](sensors-geolocation-driver-sample.md) in the WDK provides an example of a driver that tracks the number of connected clients and the radio state.

## Tracking Report Intervals

Applications that consume location data by subscribing to events request the maximum frequency for data-updated events by setting the SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL property. To conserve power, your driver should send data reports no more frequently than the lowest requested report interval.

For more information on how to track values for each application, see [Filtering data](../sensors/filtering-data.md). You can also find example of tracking report intervals in the [Sensors Geolocation Driver Sample](sensors-geolocation-driver-sample.md) in the WDK.

## Tracking Desired Accuracy

Just as report intervals are tracked per client, the accuracy level requested by each client must be tracked.

The [Sensors Geolocation Driver Sample](sensors-geolocation-driver-sample.md) in the WDK provides an example of a driver that tracks the desired accuracy requested by clients.

Location sensor drivers must support the SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY as a settable property. The driver should monitor the desired accuracy property of the connected clients and set SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY based on the highest requested desired accuracy.

If the highest accuracy requested by an app is DESIRED_ACCURACY_DEFAULT, the location sensor should optimize power and other cost considerations. The Location API won't use GPS sensors if location data is available from other providers on the system and data accuracy is 500 m or better.

If any app requests DESIRED_ACCURACY_HIGH, the sensor should deliver the highest accuracy report possible. The Location API will always connect to all location sensors (including GPS) in order to acquire the most accurate position possible.

## Detecting Idle States

Your driver should detect an idle state and enter a low-power state. For example, an idle state may occur when the location of a GPS device isn't changing, there are no pending I/O requests, or data isn't available. If your GPS or Global Navigation Satellite System (GNSS) device is implemented over USB, it must support selective suspend. See [Supporting Idle Power-Down in UMDF-based Drivers](../wdf/supporting-idle-power-down-in-umdf-drivers.md) for more info.

## Position Injection for GPS and Global Navigation Satellite System (GNSS)

GPS or Global Navigation Satellite System (GNSS) sensors can use data from triangulation sensors on the system to shorten the time to first fix. This is known as *position injection*.

This use of sensor-to-sensor communication is supported only during the acquisition phase. A Global Navigation Satellite System (GNSS) driver may open a connection to any triangulation sensor, including the Windows Location Provider, through the Sensor API. The driver can then get a coarse position, if position data is available. The driver should close the connection immediately after getting the position.

If the Global Navigation Satellite System (GNSS) driver doesn't get a position from the Sensor API within 15 seconds, it should time out and close the connection to the Sensor API. Don't continue subscribing to events.

A persistent connection to the Windows Location Provider (or any other sensor through the Sensor API) shouldn't be kept open.

Don't instantiate [**ILocation**](/windows/win32/api/locationapi/nn-locationapi-ilocation) to get data from other location sensors. Instead, use the Sensor API ([**ISensorManager**](/windows/win32/api/sensorsapi/nn-sensorsapi-isensormanager)).

Sensors shouldn't get data from location sensors of the same type. For instance, a triangulation sensor shouldn't use data from other triangulation sensors.

To access triangulation sensors, call [**ISensorManager::GetSensorByType**](/windows/win32/api/sensorsapi/nf-sensorsapi-isensormanager-getsensorsbytype) with type SENSOR_TYPE_LOCATION_TRIANGULATION. This will return all triangulation sensors, including the Windows Location Provider that is built into Windows 8. Your GPS driver needs to be able to handle anywhere from zero sensors returned to multiple sensors. See [Retrieving a Sensor Object](/windows/desktop/SensorsAPI/retrieving-a-sensor) for more information on the use of **GetSensorsByType**.

The Windows Location Provider doesn't provide any guarantee of accuracy or availability.

The use of the Sensor API for sensor-to-sensor communication to enable location fusion (for example, the use of accelerometer or gyro magnetometer data to estimate physical location) isn't supported.

## Related articles

[Writing a Location Sensor Driver](writing-a-location-sensor-driver.md)  

[The Sensors Geolocation Driver Sample](sensors-geolocation-driver-sample.md)
