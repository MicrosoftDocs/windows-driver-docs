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

 

 






