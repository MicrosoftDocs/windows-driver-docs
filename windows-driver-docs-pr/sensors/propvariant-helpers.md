---
title: PropVariant helpers
description: The PropVariant helper functions are used by the v2 sensor drivers for manipulating the PROPVARIANT structures associated with the sensors.
ms.assetid: 5A5A008A-399F-4464-ADD0-7F2DDACB6D4B
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# PropVariant helpers


The PropVariant helper functions are used by the v2 sensor drivers for manipulating the [PROPVARIANT](https://docs.microsoft.com/windows/desktop/api/propidl/ns-propidl-tagpropvariant) structures associated with the sensors.

The helper functions are used along with the sensor device driver software interface (DDSI).

**InitPropVariantFromFloat**

Usage by sensor DDSI

-   Initializes a [PROPVARIANT](https://docs.microsoft.com/windows/desktop/api/propidl/ns-propidl-tagpropvariant) structure.

Comments

-   This function receives a FLOAT, and then based on that variable, it creates and initializes a [PROPVARIANT](https://docs.microsoft.com/windows/desktop/api/propidl/ns-propidl-tagpropvariant) structure.

**PropKeyFindKeyGetPropVariant**

Usage by sensor DDSI

-   Retrieves a [PROPVARIANT](https://docs.microsoft.com/windows/desktop/api/propidl/ns-propidl-tagpropvariant) structure.

Comments

-   None.

**PropKeyFindKeySetPropVariant**

Usage by sensor DDSI

-   Sets a [PROPVARIANT](https://docs.microsoft.com/windows/desktop/api/propidl/ns-propidl-tagpropvariant) structure.

Comments

-   None.

**PropKeyFindKeyGetFileTime**

Usage by sensor DDSI

-   Retrieves the time stamp associated with a data file.

Comments

-   This is the *filetime* member of the [PROPVARIANT](https://docs.microsoft.com/windows/desktop/api/propidl/ns-propidl-tagpropvariant) structure that matches the supplied property key.

**PropKeyFindKeyGetGuid**

Usage by sensor DDSI

-   Retrieves the GUID for the sensor.

Comments

-   This is the *puuid* member of the [PROPVARIANT](https://docs.microsoft.com/windows/desktop/api/propidl/ns-propidl-tagpropvariant) structure that matches the supplied property key.

**PropKeyFindKeyGetBool**

Usage by sensor DDSI

-   Retrieves a BOOL value from the [PROPVARIANT](https://docs.microsoft.com/windows/desktop/api/propidl/ns-propidl-tagpropvariant) structure associated with the sensor.

Comments

-   None.

**PropKeyFindKeyGetUlong**

Usage by sensor DDSI

-   Retrieves a ULONG value from the [PROPVARIANT](https://docs.microsoft.com/windows/desktop/api/propidl/ns-propidl-tagpropvariant) structure associated with the sensor.

Comments

-   None.

**PropKeyFindKeyGetUshort**

Usage by sensor DDSI

-   Retrieves a USHORT value from the [PROPVARIANT](https://docs.microsoft.com/windows/desktop/api/propidl/ns-propidl-tagpropvariant) structure associated with the sensor.

Comments

-   None.

**PropKeyFindKeyGetFloat**

Usage by sensor DDSI

-   Retrieves a FLOAT value from the [PROPVARIANT](https://docs.microsoft.com/windows/desktop/api/propidl/ns-propidl-tagpropvariant) structure associated with the sensor.

Comments

-   None.

**PropKeyFindKeyGetDouble**

Usage by sensor DDSI

-   Retrieves a DOUBLE value from the [PROPVARIANT](https://docs.microsoft.com/windows/desktop/api/propidl/ns-propidl-tagpropvariant) structure associated with the sensor.

Comments

-   None.

**PropKeyFindKeyGetInt32**

Usage by sensor DDSI

-   Retrieves a 32-bit value from the [PROPVARIANT](https://docs.microsoft.com/windows/desktop/api/propidl/ns-propidl-tagpropvariant) structure associated with the sensor.

Comments

-   None.

**PropKeyFindKeyGetInt64**

Usage by sensor DDSI

-   Retrieves a 64-bit value from the [PROPVARIANT](https://docs.microsoft.com/windows/desktop/api/propidl/ns-propidl-tagpropvariant) structure associated with the sensor.

Comments

-   None.

**PropKeyFindKeyGetNthUlong**

Usage by sensor DDSI

-   Retrieves the Nth ULONG value from a [PROPVARIANT](https://docs.microsoft.com/windows/desktop/api/propidl/ns-propidl-tagpropvariant) within a collection list that is based on the supplied property key.

Comments

-   None.

**PropKeyFindKeyGetNthUshort**

Usage by sensor DDSI

-   Retrieves the Nth UShort value from a [PROPVARIANT](https://docs.microsoft.com/windows/desktop/api/propidl/ns-propidl-tagpropvariant) within a collection list that is based on the supplied property key.

Comments

-   None.

**PropKeyFindKeyGetNthInt64**

Usage by sensor DDSI

-   Retrieves the Nth Int64 value from a [PROPVARIANT](https://docs.microsoft.com/windows/desktop/api/propidl/ns-propidl-tagpropvariant) within a collection list that is based on the supplied property key.

Comments

-   None.

**IsKeyPresentInPropertyList**

Usage by sensor DDSI

-   Returns a BOOL value.

Comments

-   The BOOL value indicates whether or not the property key was found in the [**SENSOR\_PROPERTY\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ns-sensorsdef-sensor_property_list) structure associated with the sensor.

**IsKeyPresentInCollectionList**

Usage by sensor DDSI

-   Returns a BOOL value.

Comments

-   The BOOL value indicates whether or not the property key was found in the [**SENSOR\_COLLECTION\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ns-sensorsdef-sensor_collection_list) structure. associated with the sensor.

**IsCollectionListSame**

Usage by sensor DDSI

-   Returns a BOOL value.

Comments

-   Compares two [**SENSOR\_COLLECTION\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ns-sensorsdef-sensor_collection_list) structures to determine if they're the same.

**PropVariantGetInformation**

Usage by sensor DDSI

-   Retrieves size, offset and other information about the [PROPVARIANT](https://docs.microsoft.com/windows/desktop/api/propidl/ns-propidl-tagpropvariant) structure associated with the sensor.

Comments

-   None.

**PropertiesListCopy**

Usage by sensor DDSI

-   Copies information from a source property list to a target one.

Comments

-   See [**SENSOR\_PROPERTY\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ns-sensorsdef-sensor_property_list) for more information.

**PropertiesListGetFillableCount**

Usage by sensor DDSI

-   Returns the number of elements that a buffer of a certain size can possibly hold.

Comments

-   None.

## Requirements


|                          |                        |
|--------------------------|------------------------|
| Minimum supported client | Windows 8.1            |
| Minimum supported server | Windows Server 2012 R2 |
| Header                   | Sensorsutils.h         |

 

## Related topics


[Marshalling helper functions](marshalling-helper-functions.md)

 

 






