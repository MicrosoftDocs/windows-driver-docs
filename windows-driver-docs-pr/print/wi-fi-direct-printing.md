---
title: Wi-Fi Direct Printing
description: Windows 8.1 and later versions of Windows support printing over Wi-Fi Direct (WFD).
ms.assetid: B2FC1293-F9E4-43A4-84BF-21EF8C3D27E0
ms.date: 01/30/2018
ms.localizationpriority: medium
---

# Wi-Fi Direct Printing


Windows 8.1 and later versions of Windows support printing over Wi-Fi Direct (WFD).

Print devices implementing Windows Wi-Fi Direct support for printing must implement the following:

-   Wi-Fi Direct Vertical Pairing
-   Matching Container ID’s for all logical devices in the physical device
-   WSD/WS-Print

Definitions used in this topic and its subtopics:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WFD</p></td>
<td><p>Wi-Fi Direct</p></td>
</tr>
<tr class="even">
<td><p>DAF</p></td>
<td><p>Device Association Framework</p></td>
</tr>
<tr class="odd">
<td><p>DAS</p></td>
<td><p>Device Association Service</p></td>
</tr>
<tr class="even">
<td><p>GO</p></td>
<td><p>Group Owner</p></td>
</tr>
<tr class="odd">
<td><p>PBC</p></td>
<td><p>Push-Button Connect</p></td>
</tr>
</tbody>
</table>

 

General information about Wi-Fi Direct Printing support is described in the [Wi-Fi Direct Printing Overview](wfd-overview.md). See [Wi-Fi Direct Printing Implementation](wfd-implementation.md) for details about how to implement Wi-Fi Direct Printing.

## Certification Requirements


No new certification requirements are associated with this feature. See **Related Documents** below, for applicable existing requirements.

## HCK Requirements


Devices must have Wi-Fi Alliance Certification for Wi-Fi Direct if implemented.

All existing Certification Requirements for Print devices apply including requirement to run applicable HCK tests across all available transports. Partners should always refer to the official Certification Requirements documents published by the Windows Certification team in case there are any changes.

**Note**  The Wi-Fi Alliance Certification requirement is for Wi-Fi Direct. Wi-Fi Alliance Wi-Fi Direct Services is a separate specification and is not supported in Windows at this time.

 

## Related Documents


Please see the following topics for related information:

[Overview of Container IDs](https://docs.microsoft.com/windows-hardware/drivers/install/overview-of-container-ids)
[PnP-X: Plug and Play Extensions for Windows Specification](https://msdn.microsoft.com/windows/hardware/gg463082)
[Wi-Fi Alliance - Wi-Fi Direct Industry Whitepaper](http://go.microsoft.com/fwlink/p/?LinkId=784967)
 

 




