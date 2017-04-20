---
title: Supporting multiple sensors
author: windows-driver-content
description: The SpbAccelerometer sample demonstrates how to write a driver for a single sensor device.
ms.assetid: 633B7CB5-EF4A-42BE-A60E-7D12BDAFA34F
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting multiple sensors


The SpbAccelerometer sample demonstrates how to write a driver for a single sensor device. However, the sensor class extension and sensor DDI accommodate multiple sensor devices. Consider the following modifications to the sample driver to support multiple sensors.

Separate SensorDdi into two classes:

1.  SensorDdi
2.  Sensor

The SensorDdi class will continue to facilitate communication with the sensor class extension by implementing the **ISensorDriver** interface and making calls via the **ISensorClassExtension** interface. This class should also maintain a list of current sensors, indexed by the sensor ID string.

For each sensor, create a new Sensor class instance. This class will maintain: state, properties, and data fields. Each Sensor instance will also have its own ClientManager and ReportManager.

When receiving one of the sensor DDI callbacks, the SensorDDI class will match the sensor ID and invoke the corresponding method in the appropriate Sensor instance.

The left side of the following illustration depicts the sample driver as it exists upon download. The right side of the illustration depicts the this driver after the modifications in this topic were applied and support was added for a second device.

![multiple sensor support](images/multi-sensor.png)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Supporting%20multiple%20sensors%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


