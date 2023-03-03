---
title: PropVariant helpers
description: The PropVariant helper functions are used by the v2 sensor drivers for manipulating the PROPVARIANT structures associated with the sensors.
ms.date: 03/02/2023
ms.topic: reference
---

# Sensor PropVariant helpers

The PropVariant helper functions are used by the v2 sensor drivers for manipulating the [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structures associated with sensors.

The helper functions are used along with the sensor device driver software interface (DDSI).

| Helper Function | Action | Comments |
|---|---|---|
| InitPropVariantFromFloat | Initializes a [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure. | This function receives a FLOAT, and then based on that variable, it creates and initializes a [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure. |
| PropKeyFindKeyGetPropVariant | Retrieves a [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure. | |
| PropKeyFindKeySetPropVariant | Sets a [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure. | |
| PropKeyFindKeyGetFileTime | Retrieves the time stamp associated with a data file. |This is the *filetime* member of the [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure that matches the supplied property key. |
| PropKeyFindKeyGetGuid | Retrieves the GUID for the sensor. | This is the *puuid* member of the [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure that matches the supplied property key. |
| PropKeyFindKeyGetBool | Retrieves a BOOL value from the [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure associated with the sensor. | |
| PropKeyFindKeyGetUlong | Retrieves a ULONG value from the [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure associated with the sensor. | |
| PropKeyFindKeyGetUshort | Retrieves a USHORT value from the [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure associated with the sensor. | |
| PropKeyFindKeyGetFloat | Retrieves a FLOAT value from the [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure associated with the sensor. | |
| PropKeyFindKeyGetDouble | Retrieves a DOUBLE value from the [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure associated with the sensor. | |
| PropKeyFindKeyGetInt32 | Retrieves a 32-bit value from the [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure associated with the sensor. | |
| PropKeyFindKeyGetInt64 | Retrieves a 64-bit value from the [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure associated with the sensor. | |
| PropKeyFindKeyGetNthUlong | Retrieves the Nth ULONG value from a [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) within a collection list that is based on the supplied property key. | |
| PropKeyFindKeyGetNthUshort | Retrieves the Nth UShort value from a [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) within a collection list that is based on the supplied property key. | |
| PropKeyFindKeyGetNthInt64 | Retrieves the Nth Int64 value from a [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) within a collection list that is based on the supplied property key. | |
| IsKeyPresentInPropertyList | Returns a BOOL value. | The BOOL value indicates whether or not the property key was found in the [**SENSOR\_PROPERTY\_LIST**](/windows-hardware/drivers/ddi/sensorsdef/ns-sensorsdef-sensor_property_list) structure associated with the sensor.|
| IsKeyPresentInCollectionList | Returns a BOOL value. | The BOOL value indicates whether or not the property key was found in the [**SENSOR\_COLLECTION\_LIST**](/windows-hardware/drivers/ddi/sensorsdef/ns-sensorsdef-sensor_collection_list) structure. associated with the sensor. |
| IsCollectionListSame | Returns a BOOL value. | Compares two [**SENSOR\_COLLECTION\_LIST**](/windows-hardware/drivers/ddi/sensorsdef/ns-sensorsdef-sensor_collection_list) structures to determine if they're the same. |
| PropVariantGetInformation | Retrieves size, offset and other information about the [PROPVARIANT](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure associated with the sensor. | |
| PropertiesListCopy | Copies information from a source property list to a target one. | See [**SENSOR\_PROPERTY\_LIST**](/windows-hardware/drivers/ddi/sensorsdef/ns-sensorsdef-sensor_property_list) for more information. |
|PropertiesListGetFillableCount | Returns the number of elements that a buffer of a certain size can possibly hold. | |

## Requirements

| &nbsp; |&nbsp; |
|---|---|
| **Minimum supported client** | Windows 8.1 |
| **Minimum supported server** | Windows Server 2012 R2 |
| **Header** | Sensorsutils.h |

## Related topics

- [Marshalling helper functions](marshalling-helper-functions.md)
