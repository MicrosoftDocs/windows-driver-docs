---
title: Using the sensor class extension
description: The sensor class extension supports the linkage between a sensor driver and the Sensor API.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: F9632F86-10E8-4006-8FB7-97FA5EED492D
---

# Using the sensor class extension


The sensor class extension supports the linkage between a sensor driver and the Sensor API.

Sensor applications would retrieve the ADXL345 data fields by registering to receive event notifications from the driver. Once an application registers for data-update events, the driver raises these events each time it receives data from the sensor. The frequency of these event notifications correspond to the current report-interval property.

When the driver invokes the **ISensorClassExtension::PostEvent** method from within the **CSensorDdi::PostDataEvent** method, the class extension forwards the notification to the Sensor API. The sample driver supports an eventing thread. The code associated with this thread receives data updates from the sensor and ensures that the driver is posting data at the specified report interval. This code invokes the **CSensorDdi::ReportIntervalExpired** method which, in turn, invokes the **PostDataEvent** method.

## Related topics


[SpbAccelerometer driver sample](spbaccelerometer-driver-sample.md)

[The driver I/O model](the-driver-i-o-model.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Using%20the%20sensor%20class%20extension%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





