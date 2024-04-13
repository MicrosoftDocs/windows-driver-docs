---
title: Sensor Driver Best Practices
description: Sensor driver best practices
ms.date: 01/11/2024
---

# Sensor driver best practices

This section describes best practices for sensor drivers.

## Windows Hardware Certification Program Requirements

The Windows Hardware Certification Program enables hardware manufacturers to receive certification that their devices meet the required standards for working with Windows. The program provides the requirements for all sensors, and specific requirements for location sensors and ambient-light sensors. You should make your sensor driver comply with all the Windows Hardware Certification Program requirements.

Generally, the recommendations in this WDK documentation match the program requirements. However, you must review the official Windows Hardware Certification Program documentation when you create sensor drivers that you intend to submit for certification. For more information about the Windows Hardware Certification Program, see the [Windows Hardware Developer Central](/previous-versions/windows/hardware/hck/jj124227(v=vs.85)) website.

## Performance

Follow these recommendations to optimize the performance of your sensor when you use the Location API and Sensor API:

- Use the calls to [**ISensorDriver::OnClientSubscribeToEvents**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-onclientsubscribetoevents) and [**ISensorDriver::OnClientUnsubscribeFromEvents**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-onclientunsubscribefromevents) to keep track of whether any programs are monitoring events. Stop raising events when no clients are subscribed.

- Use the value that is provided for the SENSOR\_PROPERTY\_CURRENT\_REPORT\_INTERVAL as a hint for how often to raise events. Raise events only during or after the suggested interval to prevent filtering of the data your driver provides.

- For information about setting the current report interval, see the [Filtering data](filtering-data.md) topic.

- Raise events no more frequently than the shortest report interval requested, if you can do this.

- Provide data when requested. Although we recommend that programs refrain from polling for data, the APIs do not limit these synchronous requests. You can provide cached data, when it is appropriate.

## Properties and data fields

The following requirements apply to properties and data fields.

- Your driver must use the correct type when setting, or returning, a [property](sensor-properties.md).

- Your driver must use the correct type when returning a [data field](common-data-fields.md).

## Events

The following recommendations apply to sensor events:

- Raise data-updated events only when the current report interval has elapsed and the change sensitivity is exceeded. This is largely a function of the device firmware. However, the driver must arbitrate among multiple clients. For more information, see [About Sensor Driver Events](about-sensor-driver-events.md).

## Related topics

- [Writing a Location Sensor Driver](../gnss/writing-a-location-sensor-driver.md)
- [Supporting Ambient Light Sensors](supporting-ambient-light-sensors.md)
- [The Sensors Geolocation Driver Sample](../gnss/sensors-geolocation-driver-sample.md)
