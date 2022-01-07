---
title: Collection list legacy helpers
description: The collection list legacy helper functions are used by v2 sensor drivers for interacting with SENSOR\_COLLECTION\_LIST structures.
ms.date: 07/20/2018
---

# Collection list legacy helpers


The collection list legacy helper functions are used by v2 sensor drivers for interacting with [**SENSOR\_COLLECTION\_LIST**](/windows-hardware/drivers/ddi/sensorsdef/ns-sensorsdef-sensor_collection_list) structures.

The helper functions are used along with the sensor device driver software interface (DDSI).

**Note:** These legacy collection list helper functions are architecture-specific. So if you implement your own collection list helper functions, the sensor driver must not use them for transferring data across process boundaries.

**CollectionsListGetMarshalledSize**

Usage by sensor DDSI

-   Sets the value of the PKEY\_Sensor\_MaximumDataFieldSize\_Bytes property.

-   Returns the *pSize* value from [EvtSensorGetProperties](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config).

-   Returns the *pSize* value from [*EvtSensorGetDataFieldProperties*](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config).

-   Returns the *pSize* value from [*EvtSensorGetDataThresholds*](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config).

Comments

-   See [**SENSOR\_COLLECTION\_LIST**](/windows-hardware/drivers/ddi/sensorsdef/ns-sensorsdef-sensor_collection_list) for more information about the *pSize* member.

-   Also, see [Common sensor properties](common-sensor-properties.md) for more information.

**CollectionsListCopyAndMarshall**

Usage by sensor DDSI

-   Populates the collection list in [*EvtSensorGetProperties*](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config)

-   Populates the collection list in [*EvtSensorGetDataFieldProperties*](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config)

-   Populates the collection list in [*EvtSensorGetDataThresholds*](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config)

Comments

-   See [**SENSOR\_COLLECTION\_LIST**](/windows-hardware/drivers/ddi/sensorsdef/ns-sensorsdef-sensor_collection_list) for more information.

**CollectionsListMarshall**

Usage by sensor DDSI

-   Returns a pointer to a collections list.

Comments

-   See [**SENSOR\_COLLECTION\_LIST**](/windows-hardware/drivers/ddi/sensorsdef/ns-sensorsdef-sensor_collection_list) for more information.

**CollectionsListGetMarshalledSizeWithoutSerialization**

Usage by sensor DDSI

-   Reports the **PKEY\_SensorHistory\_MaxSize\_Bytes** property.

-   Reports the **PKEY\_SensorHistory\_MaximumRecordSize\_Bytes** property.

Comments

-   See [Common sensor properties](common-sensor-properties.md) for more information.

**CollectionsListUpdateMarshalledPointer**

Usage by sensor DDSI

-   Passes a buffer to the sensor driver using [*EvtSensorSetDataThresholds*](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config).

-   Passes a buffer to the driver using [*EvtSensorDeviceIoControl*](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_controller_config).

Comments

-   See [**SENSOR\_COLLECTION\_LIST**](/windows-hardware/drivers/ddi/sensorsdef/ns-sensorsdef-sensor_collection_list) for more information.

## Requirements

**Minimum supported client**: Windows 8.1

**Minimum supported server**: Windows Server 2012 R2

**Header**: Sensorsutils.h


 

## Related topics


[Marshalling helper functions](marshalling-helper-functions.md)

 

