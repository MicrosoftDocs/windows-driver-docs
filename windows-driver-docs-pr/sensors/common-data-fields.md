---
title: Common data fields
description: This topic shows the common data fields that are included in all sensor-specific data fields.
ms.assetid: 5F9F7987-E898-404A-96F9-F5CF88F01393
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Common data fields


This topic shows the common data fields that are included in all sensor-specific data fields.

Clients can use the ReadFile function to retrieve information from these data fields.

The following table shows the common data fields.

For more information about the types shown in the type column, see [PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

|Property key|Type|Required/Optional|Description|
| --- | --- | --- | --- |
|PKEY_SensorData_Timestamp|VT_FILETIME|Required|The file time computed by the driver in UTC format. The class extension (CX) provides a helper function to convert ticks from boot to FILETIME so that remote systems don’t have to synchronize to the system clock.|

 

## Related topics


[PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 






