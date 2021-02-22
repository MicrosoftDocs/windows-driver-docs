---
title: Marshalling helper functions
description: This topic provides information about the marshaling helper functions in the sensorsutils.h header file.
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Marshalling helper functions

This topic provides information about the marshaling helper functions in the *sensorsutils.h* header file.

These helper functions are used by the v2 sensor drivers, and they're used along with the sensor device driver software interface (DDSI).

If you implement your own marshaling helper functions, remember that helper functions must not be used when populating the enumeration list in the [**SENSOR\_CONFIG**](/windows-hardware/drivers/ddi/sensorscx/ns-sensorscx-_sensor_config) structure, or when reporting updated data with the [**SensorsCxSensorDataReady**](/windows-hardware/drivers/ddi/sensorscx/nf-sensorscx-sensorscxsensordataready) function.

## In this section

|Topic|Description|
|--|--|
|[Time stamp helper](timestamp-helper.md)|The time stamp helper function is used by v2 sensor drivers, and it's used with the sensor device driver software interface (DDSI).|
|[PropVariant helpers](propvariant-helpers.md)|The PropVariant helper functions are used by the v2 sensor drivers for manipulating the [PROPVARIANT](/windows/win32/api/propidl/ns-propidl-propvariant) structures associated with the sensors.|
|[Collection list helpers](collection-list-helpers.md)|The collection list helper functions are used by the v2 sensor drivers, for working with [SENSOR_COLLECTION_LIST](/windows-hardware/drivers/ddi/sensorsdef/ns-sensorsdef-sensor_collection_list) structures.|
|[Collection list serialization helpers](collection-list-serialization-helpers.md)|The collection list serialization helper functions are used by the v2 sensor drivers, for performing serialization-related operations on [SENSOR_COLLECTION_LIST](/windows-hardware/drivers/ddi/sensorsdef/ns-sensorsdef-sensor_collection_list) structures.|
|[Collection list legacy helpers](collection-list-legacy-helpers.md)|The collection list legacy helper functions are used by v2 sensor drivers for interacting with [SENSOR_COLLECTION_LIST](/windows-hardware/drivers/ddi/sensorsdef/ns-sensorsdef-sensor_collection_list) structures.|

## Requirements

**Header:** Sensorsutils.h
