---
title: Using the sensor class extension
description: The sensor class extension supports the linkage between a sensor driver and the Sensor API.
ms.assetid: F9632F86-10E8-4006-8FB7-97FA5EED492D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the sensor class extension


The sensor class extension supports the linkage between a sensor driver and the Sensor API.

Sensor applications would retrieve the ADXL345 data fields by registering to receive event notifications from the driver. Once an application registers for data-update events, the driver raises these events each time it receives data from the sensor. The frequency of these event notifications correspond to the current report-interval property.

When the driver invokes the **ISensorClassExtension::PostEvent** method from within the **CSensorDdi::PostDataEvent** method, the class extension forwards the notification to the Sensor API. The sample driver supports an eventing thread. The code associated with this thread receives data updates from the sensor and ensures that the driver is posting data at the specified report interval. This code invokes the **CSensorDdi::ReportIntervalExpired** method which, in turn, invokes the **PostDataEvent** method.

## Related topics
[SpbAccelerometer driver sample](spbaccelerometer-driver-sample.md)  
[The driver I/O model](the-driver-i-o-model.md)  



