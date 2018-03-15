---
title: Common data fields
description: This topic shows the common data fields that are included in all sensor-specific data fields.
ms.assetid: 5F9F7987-E898-404A-96F9-F5CF88F01393
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Common data fields


This topic shows the common data fields that are included in all sensor-specific data fields.

Clients can use the ReadFile function to retrieve information from these data fields.

The following table shows the common data fields.

For more information about the types shown in the type column, see [MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395).

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Property key</th>
<th>Type</th>
<th>Required/Optional</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PKEY_SensorData_Timestamp</p></td>
<td><p>VT_FILETIME</p></td>
<td><p>Required</p></td>
<td><p>The file time computed by the driver in UTC format. The class extension (CX) provides a helper function to convert ticks from boot to FILETIME so that remote systems don’t have to synchronize to the system clock.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[MSDN PROPVARIANT structure](http://go.microsoft.com/fwlink/p/?linkid=313395)

 

 






