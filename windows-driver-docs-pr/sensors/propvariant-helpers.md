---
title: PropVariant helpers
description: The PropVariant helper functions are used by the v2 sensor drivers for manipulating the PROPVARIANT structures associated with the sensors.
ms.assetid: 5A5A008A-399F-4464-ADD0-7F2DDACB6D4B
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PropVariant helpers


The PropVariant helper functions are used by the v2 sensor drivers for manipulating the [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) structures associated with the sensors.

The helper functions are used along with the sensor device driver software interface (DDSI).

**InitPropVariantFromFloat**

Usage by sensor DDSI

-   Initializes a [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) structure.

Comments

-   This function receives a FLOAT, and then based on that variable, it creates and initializes a [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) structure.

**PropKeyFindKeyGetPropVariant**

Usage by sensor DDSI

-   Retrieves a [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) structure.

Comments

-   None.

**PropKeyFindKeySetPropVariant**

Usage by sensor DDSI

-   Sets a [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) structure.

Comments

-   None.

**PropKeyFindKeyGetFileTime**

Usage by sensor DDSI

-   Retrieves the time stamp associated with a data file.

Comments

-   This is the *filetime* member of the [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) structure that matches the supplied property key.

**PropKeyFindKeyGetGuid**

Usage by sensor DDSI

-   Retrieves the GUID for the sensor.

Comments

-   This is the *puuid* member of the [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) structure that matches the supplied property key.

**PropKeyFindKeyGetBool**

Usage by sensor DDSI

-   Retrieves a BOOL value from the [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) structure associated with the sensor.

Comments

-   None.

**PropKeyFindKeyGetUlong**

Usage by sensor DDSI

-   Retrieves a ULONG value from the [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) structure associated with the sensor.

Comments

-   None.

**PropKeyFindKeyGetUshort**

Usage by sensor DDSI

-   Retrieves a USHORT value from the [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) structure associated with the sensor.

Comments

-   None.

**PropKeyFindKeyGetFloat**

Usage by sensor DDSI

-   Retrieves a FLOAT value from the [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) structure associated with the sensor.

Comments

-   None.

**PropKeyFindKeyGetDouble**

Usage by sensor DDSI

-   Retrieves a DOUBLE value from the [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) structure associated with the sensor.

Comments

-   None.

**PropKeyFindKeyGetInt32**

Usage by sensor DDSI

-   Retrieves a 32-bit value from the [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) structure associated with the sensor.

Comments

-   None.

**PropKeyFindKeyGetInt64**

Usage by sensor DDSI

-   Retrieves a 64-bit value from the [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) structure associated with the sensor.

Comments

-   None.

**PropKeyFindKeyGetNthUlong**

Usage by sensor DDSI

-   Retrieves the Nth Ulong vlaue from a [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) within a collection list that is based on the supplied property key.

Comments

-   None.

**PropKeyFindKeyGetNthUshort**

Usage by sensor DDSI

-   Retrieves the Nth UShort value from a [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) within a collection list that is based on the supplied property key.

Comments

-   None.

**PropKeyFindKeyGetNthInt64**

Usage by sensor DDSI

-   Retrieves the Nth Int64 value from a [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) within a collection list that is based on the supplied property key.

Comments

-   None.

**IsKeyPresentInPropertyList**

Usage by sensor DDSI

-   Returns a BOOL value.

Comments

-   The BOOL value indicates whether or not the property key was found in the [**SENSOR\_PROPERTY\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn946699) structure associated with the sensor.

**IsKeyPresentInCollectionList**

Usage by sensor DDSI

-   Returns a BOOL value.

Comments

-   The BOOL value indicates whether or not the property key was found in the [**SENSOR\_COLLECTION\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn957092) structure. associated with the sensor.

**IsCollectionListSame**

Usage by sensor DDSI

-   Returns a BOOL value.

Comments

-   Compares two [**SENSOR\_COLLECTION\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn957092) structures to determine if they're the same.

**PropVariantGetInformation**

Usage by sensor DDSI

-   Retrieves size, offset and other information about the [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072.aspx) structure associated with the sensor.

Comments

-   None.

**PropertiesListCopy**

Usage by sensor DDSI

-   Copies information from a source property list to a target one.

Comments

-   See [**SENSOR\_PROPERTY\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn946699) for more information.

**PropertiesListGetFillableCount**

Usage by sensor DDSI

-   Returns the number of elements that a buffer of a certain size can possibly hold.

Comments

-   None.

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


|                          |                        |
|--------------------------|------------------------|
| Minimum supported client | Windows 8.1            |
| Minimum supported server | Windows Server 2012 R2 |
| Header                   | Sensorsutils.h         |

 

## <span id="related_topics"></span>Related topics


[Marshalling helper functions](marshalling-helper-functions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20PropVariant%20helpers%20%20RELEASE:%20%2811/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





