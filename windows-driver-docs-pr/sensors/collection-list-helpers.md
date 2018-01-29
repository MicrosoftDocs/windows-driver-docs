---
title: Collection list helpers
description: The collection list helper functions are used by the v2 sensor drivers, for working with SENSOR\_COLLECTION\_LIST structures.
ms.assetid: 9BE06FA6-A171-4760-9D3E-C0183F3C3EFA
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Collection list helpers


The collection list helper functions are used by the v2 sensor drivers, for working with [**SENSOR\_COLLECTION\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn957092) structures.

The helper functions are used along with the sensor device driver software interface (DDSI).

**SensorCollectionGetAt**

Usage by sensor DDSI

-   Retrieves property key and PROPVARIANT-related attributes of a collection list.

Comments

-   See [**SENSOR\_COLLECTION\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn957092) for more information.

-   See [**SENSOR\_VALUE\_PAIR**](https://msdn.microsoft.com/library/windows/hardware/dn946708) for more information.

**CollectionsListGetFillableCount**

Usage by sensor DDSI

-   Returns buffer size in bytes.

Comments

-   None.

**EvaluateActivityThresholds**

Usage by sensor DDSI

-   Compares activity thresholds in old and new data samples, and returns a Boolean value.

Comments

-   None.

**CollectionsListSortSubscribedActivitiesByConfidence**

Usage by sensor DDSI

-   Sorts the collection lists for the possible activities in order of confidence levels.

Comments

-   None.

### <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements

|                          |                        |
|--------------------------|------------------------|
| Minimum supported client | Windows 8.1            |
| Minimum supported server | Windows Server 2012 R2 |
| Header                   | Sensorsutils.h         |

 

## <span id="related_topics"></span>Related topics


[Marshalling helper functions](marshalling-helper-functions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Collection%20list%20helpers%20%20RELEASE:%20%2811/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





