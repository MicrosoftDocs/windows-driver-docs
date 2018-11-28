---
title: Collection list legacy helpers
description: The collection list legacy helper functions are used by v2 sensor drivers for interacting with SENSOR\_COLLECTION\_LIST structures.
ms.assetid: AD5AB3EE-5AD7-4576-8E8E-3FEA08930DD7
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Collection list legacy helpers


The collection list legacy helper functions are used by v2 sensor drivers for interacting with [**SENSOR\_COLLECTION\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ns-sensorsdef-sensor_collection_list) structures.

The helper functions are used along with the sensor device driver software interface (DDSI).

**Note:** These legacy collection list helper functions are architecture-specific. So if you implement your own collection list helper functions, the sensor driver must not use them for transferring data across process boundaries.

**CollectionsListGetMarshalledSize**

Usage by sensor DDSI

-   Sets the value of the PKEY\_Sensor\_MaximumDataFieldSize\_Bytes property.

-   Returns the *pSize* value from [EvtSensorGetProperties](https://msdn.microsoft.com/library/windows/hardware/dn957032).

-   Returns the *pSize* value from [*EvtSensorGetDataFieldProperties*](https://msdn.microsoft.com/library/windows/hardware/dn957029).

-   Returns the *pSize* value from [*EvtSensorGetDataThresholds*](https://msdn.microsoft.com/library/windows/hardware/dn957031).

Comments

-   See [**SENSOR\_COLLECTION\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ns-sensorsdef-sensor_collection_list) for more information about the *pSize* member.

-   Also, see [Common sensor properties](common-sensor-properties.md) for more information.

**CollectionsListCopyAndMarshall**

Usage by sensor DDSI

-   Populates the collection list in [*EvtSensorGetProperties*](https://msdn.microsoft.com/library/windows/hardware/dn957032)

-   Populates the collection list in [*EvtSensorGetDataFieldProperties*](https://msdn.microsoft.com/library/windows/hardware/dn957029)

-   Populates the collection list in [*EvtSensorGetDataThresholds*](https://msdn.microsoft.com/library/windows/hardware/dn957031)

Comments

-   See [**SENSOR\_COLLECTION\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ns-sensorsdef-sensor_collection_list) for more information.

**CollectionsListMarshall**

Usage by sensor DDSI

-   Returns a pointer to a collections list.

Comments

-   See [**SENSOR\_COLLECTION\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ns-sensorsdef-sensor_collection_list) for more information.

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

-   See [**SENSOR\_COLLECTION\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ns-sensorsdef-sensor_collection_list) for more information.

## Requirements

|                          |                        |
|--------------------------|------------------------|
| Minimum supported client | Windows 8.1            |
| Minimum supported server | Windows Server 2012 R2 |
| Header                   | Sensorsutils.h         |

 

## Related topics


[Marshalling helper functions](marshalling-helper-functions.md)

 

 






