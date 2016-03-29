---
title: Wi-Fi Direct Printing
description: Windows 8.1 and later versions of Windows support printing over Wi-Fi Direct (WFD).
ms.assetid: B2FC1293-F9E4-43A4-84BF-21EF8C3D27E0
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
<th align="left">Term</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>WFD</p></td>
<td align="left"><p>Wi-Fi Direct</p></td>
</tr>
<tr class="even">
<td align="left"><p>DAF</p></td>
<td align="left"><p>Device Association Framework</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DAS</p></td>
<td align="left"><p>Device Association Service</p></td>
</tr>
<tr class="even">
<td align="left"><p>GO</p></td>
<td align="left"><p>Group Owner</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PBC</p></td>
<td align="left"><p>Push-Button Connect</p></td>
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

-   [Multifunction Device Support and Device Container Groupings](https://msdn.microsoft.com/library/windows/hardware/ff540024)
-   [PnP-X: Plug and Play Extensions for Windows Specification](http://msdn.microsoft.com/en-US/windows/hardware/gg463082)
-   [Wi-Fi Alliance - Wi-Fi Direct Industry Whitepaper](http://www.wi-fi.org/knowledge-center/white-papers/wi-fi-certified-wi-fi-direct%E2%84%A2-personal-portable-wi-fi%C2%AE-technology-2010)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Wi-Fi%20Direct%20Printing%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




