---
title: Collection list legacy helpers
description: The collection list legacy helper functions are used by v2 sensor drivers for interacting with SENSOR\_COLLECTION\_LIST structures.
ms.assetid: AD5AB3EE-5AD7-4576-8E8E-3FEA08930DD7
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Collection list legacy helpers


The collection list legacy helper functions are used by v2 sensor drivers for interacting with [**SENSOR\_COLLECTION\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn957092) structures.

The helper functions are used along with the sensor device driver software interface (DDSI).

**Note:** These legacy collection list helper functions are architecture-specific. So if you implement your own collection list helper functions, the sensor driver must not use them for transferring data across process boundaries.

**CollectionsListGetMarshalledSize**

Usage by sensor DDSI

-   Sets the value of the PKEY\_Sensor\_MaximumDataFieldSize\_Bytes property.

-   Returns the *pSize* value from [EvtSensorGetProperties](https://msdn.microsoft.com/library/windows/hardware/dn957032).

-   Returns the *pSize* value from [*EvtSensorGetDataFieldProperties*](https://msdn.microsoft.com/library/windows/hardware/dn957029).

-   Returns the *pSize* value from [*EvtSensorGetDataThresholds*](https://msdn.microsoft.com/library/windows/hardware/dn957031).

Comments

-   See [**SENSOR\_COLLECTION\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn957092) for more information about the *pSize* member.

-   Also, see [Common sensor properties](common-sensor-properties.md) for more information.

**CollectionsListCopyAndMarshall**

Usage by sensor DDSI

-   Populates the collection list in [*EvtSensorGetProperties*](https://msdn.microsoft.com/library/windows/hardware/dn957032)

-   Populates the collection list in [*EvtSensorGetDataFieldProperties*](https://msdn.microsoft.com/library/windows/hardware/dn957029)

-   Populates the collection list in [*EvtSensorGetDataThresholds*](https://msdn.microsoft.com/library/windows/hardware/dn957031)

Comments

-   See [**SENSOR\_COLLECTION\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn957092) for more information.

**CollectionsListMarshall**

Usage by sensor DDSI

-   Returns a pointer to a collections list.

Comments

-   See [**SENSOR\_COLLECTION\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn957092) for more information.

**CollectionsListGetMarshalledSizeWithoutSerialization**

Usage by sensor DDSI

-   Reports the **PKEY\_SensorHistory\_MaxSize\_Bytes** property.

-   Reports the **PKEY\_SensorHistory\_MaximumRecordSize\_Bytes** property.

Comments

-   See [Common sensor properties](common-sensor-properties.md) for more information.

**CollectionsListUpdateMarshalledPointer**

Usage by sensor DDSI

-   Passes a buffer to the sensor driver using [*EvtSensorSetDataThresholds*](https://msdn.microsoft.com/library/windows/hardware/dn957039).

-   Passes a buffer to the driver using [*EvtSensorDeviceIoControl*](https://msdn.microsoft.com/library/windows/hardware/dn957028).

Comments

-   See [**SENSOR\_COLLECTION\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn957092) for more information.

### <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements

|                          |                        |
|--------------------------|------------------------|
| Minimum supported client | Windows 8.1            |
| Minimum supported server | Windows Server 2012 R2 |
| Header                   | Sensorsutils.h         |

 

## <span id="related_topics"></span>Related topics


[Marshalling helper functions](marshalling-helper-functions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Collection%20list%20legacy%20helpers%20%20RELEASE:%20%2811/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





