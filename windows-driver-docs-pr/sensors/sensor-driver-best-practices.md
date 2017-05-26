---
title: Sensor driver best practices
author: windows-driver-content
description: Sensor driver best practices
ms.assetid: adb20558-aa94-41a9-9d26-9d757bdb0999
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Sensor driver best practices


This section describes best practices for sensor drivers.

### <a href="" id="windows-logo-program-requirements"></a>Windows Hardware Certification Program Requirements

The Windows Hardware Certification Program enables hardware manufacturers to receive certification that their devices meet the required standards for working with Windows. The program provides the requirements for all sensors, and specific requirements for location sensors and ambient-light sensors. You should make your sensor driver comply with all the Windows Hardware Certification Program requirements.

Generally, the recommendations in this WDK documentation match the program requirements. However, you must review the official Windows Hardware Certification Program documentation when you create sensor drivers that you intend to submit for certification. For more information about the Windows Hardware Certification Program, see the [Windows Hardware Developer Central](http://go.microsoft.com/fwlink/p/?linkid=8772) website.

### Performance

Follow these recommendations to optimize the performance of your sensor when you use the Location API and Sensor API:

-   Use the calls to [**ISensorDriver::OnClientSubscribeToEvents**](https://msdn.microsoft.com/library/windows/hardware/ff545589) and [**ISensorDriver::OnClientUnsubscribeFromEvents**](https://msdn.microsoft.com/library/windows/hardware/ff545598) to keep track of whether any programs are monitoring events. Stop raising events when no clients are subscribed.

-   Use the value that is provided for the SENSOR\_PROPERTY\_CURRENT\_REPORT\_INTERVAL as a hint for how often to raise events. Raise events only during or after the suggested interval to prevent filtering of the data your driver provides.

-   For information about setting the current report interval, see the [Filtering data](filtering-data.md) topic.

-   Raise events no more frequently than the shortest report interval requested, if you can do this.

-   Provide data when requested. Although we recommend that programs refrain from polling for data, the APIs do not limit these synchronous requests. You can provide cached data, when it is appropriate.

### Properties and data fields

The following requirements apply to properties and data fields.

-   Your driver must use the correct type when setting, or returning, a [property](https://msdn.microsoft.com/library/windows/hardware/ff545859).

-   Your driver must use the correct type when returning a [data field](https://msdn.microsoft.com/library/windows/hardware/ff545718).

### Events

The following recommendations apply to sensor events:

-   Raise data-updated events only when the current report interval has elapsed and the change sensitivity is exceeded. This is largely a function of the device firmware. However, the driver must arbitrate among multiple clients. For more information, see [About Sensor Driver Events](about-sensor-driver-events.md).

## Related topics
[Writing a Location Sensor Driver](https://msdn.microsoft.com/library/windows/hardware/ff545919)  
[Supporting Ambient Light Sensors](supporting-ambient-light-sensors.md)  
[The Sensors Geolocation Driver Sample](https://msdn.microsoft.com/library/windows/hardware/hh768273)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Sensor%20driver%20best%20practices%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


