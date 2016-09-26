---
title: Supporting Usages in Multi-touch Digitizer Drivers (Windows 7)
description: Supporting Usages in Multi-touch Digitizer Drivers (Windows 7)
ms.assetid: b744cf65-38c2-4296-a443-8797dbc62a09
keywords: ["Windows Touch WDK , multitouch digitizer drivers", "Windows Touch WDK , multitouch digitizer drivers, HID usages", "Windows Touch WDK , multitouch digitizer drivers, HID additions", "multitouch digitizer drivers WDK"]
---

# Supporting Usages in Multi-touch Digitizer Drivers (Windows 7)


In the context of Windows Touch, *multi-touch* refers to support of a two or more trackable contact points. This topic outlines required and optional usages for a multi-touch digitizer driver. If your digitizer device supports only a single contact point, see [Supporting Usages in Touch Digitizer Drivers](supporting-usages-in-touch-digitizer-drivers.md).

Usage identifier values are defined in the [Device Class Definition for HID 1.11](http://go.microsoft.com/fwlink/p/?linkid=155094).

### <span id="required_and_optional_hid_usages"></span><span id="REQUIRED_AND_OPTIONAL_HID_USAGES"></span> Required and Optional HID Usages

The report descriptor for a multi-touch digitizer must specify that the device is a HID touch screen (page 0x0D, usage 0x04).

In addition to the existing HID touch usages, multi-touch digitizer drivers must implement the following usages:

-   X (page 0x01, usage 0x30) and Y (page 0x01, usage 0x31)

-   Contact identifier (page 0x0D, usage 0x51)

-   Tip switch (page 0x0D, usage 0x42)

-   In-range (page 0x0D, usage 0x32)

-   Contact count maximum (page 0x0D, usage 0x55)

The following usages are optional, but multi-touch digitizer drivers should implement them if the digitizer hardware supports them. These usages were ratified in the Windows Vista timeframe:

-   Confidence (page 0x0D, usage 0x47)

-   Width and height (page 0x0D, usages 0x48 and 0x49)

-   Pressure (page 0x0D, usage 0x30)

### <span id="hid_additions_to_support_multitouch"></span><span id="HID_ADDITIONS_TO_SUPPORT_MULTITOUCH"></span> HID Additions to Support Multi-touch

The HID Usage Tables define the following usages for multi-touch input from digitizers. Windows 7 supports these multi-touch usages, and vendors should implement them in devices and drivers.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Name</th>
<th align="left">Description</th>
<th align="left">Page</th>
<th align="left">Type</th>
<th align="left">ID</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Contact identifier</p></td>
<td align="left"><p>Contact identifier</p></td>
<td align="left"><p>Digitizer</p></td>
<td align="left"><p>Dynamic Value (DV)</p></td>
<td align="left"><p>0x51</p></td>
</tr>
<tr class="even">
<td align="left"><p>Configuration</p></td>
<td align="left"><p>Configuration</p></td>
<td align="left"><p>Digitizer</p></td>
<td align="left"><p>Collection Application (CA)</p></td>
<td align="left"><p>0x0E</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Device mode</p></td>
<td align="left"><p>Input mode</p></td>
<td align="left"><p>Digitizer</p></td>
<td align="left"><p>DV</p></td>
<td align="left"><p>0x52</p></td>
</tr>
<tr class="even">
<td align="left"><p>Device settings</p></td>
<td align="left"><p>Device settings</p></td>
<td align="left"><p>Digitizer</p></td>
<td align="left"><p>Collection Logical (CL)</p></td>
<td align="left"><p>0x23</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Device Identifier</p></td>
<td align="left"><p>Device index</p></td>
<td align="left"><p>Digitizer</p></td>
<td align="left"><p>SV/DV</p></td>
<td align="left"><p>0x53</p></td>
</tr>
<tr class="even">
<td align="left"><p>Contact count</p></td>
<td align="left"><p>Actual contact count</p></td>
<td align="left"><p>Digitizer</p></td>
<td align="left"><p>DV</p></td>
<td align="left"><p>0x54</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Contact count maximum</p></td>
<td align="left"><p>Maximum number of contacts supported</p></td>
<td align="left"><p>Digitizer</p></td>
<td align="left"><p>DV</p></td>
<td align="left"><p>0x55</p></td>
</tr>
</tbody>
</table>

 

-   Contact identifier

    Specifies the identifier of the current contact. An identifier must remain constant while the contact is detected by the device. Each separate concurrent contact must have a unique identifier. Identifiers can be reused if a contact is no longer detected. If the device supports "in-air" packets (the contact is hovering above the surface), the identifier must persist from the time that the contact is detected until the time that it goes out of range. In the report descriptor in the EloMT sample, the comment for this usage is "Temp Identifier."

-   Configuration

    The Collection Application for the top-level collection that contains the feature report.

-   Device Mode

    A read/write value feature to get and set the current input configuration of a device. In the EloMT sample, the comment for this usage is "Input Mode."

-   Device settings

    The logical collection that contains the device configuration usages (Device Identifier and Device Mode).

-   Device Identifier

    The top-level collection for which the configuration is intended. Use Device Identifier if the report descriptor contains more than one multiple input top-level collection. For more information that is specific to this scenario, see [Using Report Descriptors to Support Capability Discovery](using-report-descriptors-to-support-capability-discovery.md).

-   Contact count

    Specifies the number of valid contacts in the current packet. Drivers that use [parallel or hybrid mode](selecting-packet-reporting-modes-in-multitouch-drivers.md) should include this usage. A device that cannot provide this value must use **NULL** for all values in the first position that do not contain valid contact information.

-   Contact count maximum

    Specifies the total number of contacts that a multi-touch device supports. This usage must be included in the multi-touch top-level collection and not in any child collection.

    The vendor-supplied driver may be queried dynamically for this value.

You can see examples of the previous usages in the [EloMT](elotouch-driver.md) sample in the WDK.

 

 




