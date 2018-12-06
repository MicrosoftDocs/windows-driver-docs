---
title: HIDClass Hardware IDs for Top-Level Collections
description: This section specifies the hardware IDs that the HID class driver generates for top-level collections.
ms.assetid: a90eea17-0a63-4786-a31f-740bcc670c2a
keywords:
- Human Interface Devices WDK , hardware IDs
- HID WDK , hardware IDs
- interactive input devices WDK , hardware IDs
- input devices WDK , hardware IDs
- vendor hardware IDs WDK HID
- hardware IDs WDK HID
- ID formats WDK HID
- Human Interface Devices WDK , collections
- HID WDK , collections
- interactive input devices WDK , collections
- input devices WDK , collections
- collections WDK HID , hardware IDs
- top-level collections WDK HID
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HIDClass Hardware IDs for Top-Level Collections


This section specifies the hardware IDs that the HID class driver generates for top-level collections.

Vendors must use the formats that are designated as *vendor hardware ID formats* to identify top-level collections. All other [*device ID*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-id) formats are reserved for internal use only.




The hardware IDs that the HID class driver generates for a devnode depends on the following:

1.  Number of functions supported by the underlying transport
2.  Number of Top Level Collections in the Report Descriptor

Based on these factors, there are 4 categories of hardware IDs

|                 | Single TLC | Multiple TLC |
|-----------------|------------|--------------|
| Single-Function | Case 1     | Case 2       |
| Multi-Function  | Case 3     | Case 4       |

 

## Case 1: Single-function device with single TLC


Condition under which this Hardware ID format is used:

1.  Number of functions supported by the underlying transport = 1 &&
2.  Number of TLC = 1

Hardware ID Format:

-   HID\\Vid\_v(4)&Pid\_d(4)&Rev\_r(4)
-   HID\\Vid\_v(4)&Pid\_d(4)
-   HID\_DEVICE\_UP:p(4)\_U:u(4)
-   HID\_DEVICE

## Case 2: Single-function device with multiple TLC


Condition under which this Hardware ID format is used:

1.  Number of functions supported by the underlying transport = 1 &&
2.  Number of TLC &gt; 1

Hardware ID Format:

-   HID\\Vid\_v(4)&Pid\_d(4)&Rev\_r(4)&Colb(2)
-   HID\\Vid\_v(4)&Pid\_d(4)&Colb(2)
-   HID\_DEVICE\_UP:p(4)\_U:u(4) \[RESERVED FOR WINDOWS INFs ONLY\]
-   HID\_DEVICE \[RESERVED FOR WINDOWS INFs ONLY\]

## Case 3: Multi-function device with single TLC


Condition under which this Hardware ID format is used:

1.  Number of functions supported by the underlying transport &gt; 1 &&
2.  Number of TLC = 1

Hardware ID Format:

-   HID\\Vid\_v(4)&Pid\_d(4)&Rev\_r(4)&MI\_z(2)
-   HID\\Vid\_v(4)&Pid\_d(4)&MI\_z(2)
-   HID\_DEVICE\_UP:p(4)\_U:u(4) \[RESERVED FOR WINDOWS INFs ONLY\]
-   HID\_DEVICE \[RESERVED FOR WINDOWS INFs ONLY\]

## Case 4: Multi-function device with multiple TLC


Condition under which this Hardware ID format is used:

1.  Number of functions supported by the underlying transport &gt; 1 &&
2.  Number of TLC &gt; 1

Hardware ID Format:

-   HID\\Vid\_v(4)&Pid\_d(4)&Rev\_r(4)&MI\_z(2)&Colb(2)
-   HID\\Vid\_v(4)&Pid\_d(4)&MI\_z(2)&Colb(2)
-   HID\_DEVICE\_UP:p(4)\_U:u(4) \[RESERVED FOR WINDOWS INFs ONLY\]
-   HID\_DEVICE \[RESERVED FOR WINDOWS INFs ONLY\]

## Special purpose hardware ID


The following are hardware IDs (for internal use only) that Windows uses to provide default system functionality.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Device Type</th>
<th>Usage Page</th>
<th>Usage</th>
<th>Hardware ID</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Pointer</p></td>
<td><p>0x01</p></td>
<td><p>0x01</p></td>
<td><p>HID_DEVICE_SYSTEM_MOUSE</p></td>
</tr>
<tr class="even">
<td><p>Mouse</p></td>
<td><p>0x01</p></td>
<td><p>0x02</p></td>
<td><p>HID_DEVICE_SYSTEM_MOUSE</p></td>
</tr>
<tr class="odd">
<td><p>Joystick</p></td>
<td><p>0x01</p></td>
<td><p>0x04</p></td>
<td><p>HID_DEVICE_SYSTEM_GAME</p></td>
</tr>
<tr class="even">
<td><p>Game pad</p></td>
<td><p>0x01</p></td>
<td><p>0x05</p></td>
<td><p>HID_DEVICE_SYSTEM_GAME</p></td>
</tr>
<tr class="odd">
<td><p>Keyboard</p></td>
<td><p>0x01</p></td>
<td><p>0x06</p></td>
<td><p>HID_DEVICE_SYSTEM_KEYBOARD</p></td>
</tr>
<tr class="even">
<td><p>Keypad</p></td>
<td><p>0x01</p></td>
<td><p>0x07</p></td>
<td><p>HID_DEVICE_SYSTEM_KEYBOARD</p></td>
</tr>
<tr class="odd">
<td><p>System control</p></td>
<td><p>0x01</p></td>
<td><p>0x80</p></td>
<td><p>HID_DEVICE_SYSTEM_CONTROL</p></td>
</tr>
<tr class="even">
<td><p>Consumer audio control</p></td>
<td><p>0x0C</p></td>
<td><p>0x01</p></td>
<td><p>HID_DEVICE_SYSTEM_CONSUMER</p></td>
</tr>
</tbody>
</table>

 

Important notes:

-   There are no compatible IDs generated by HIDClass
-   Vendor 3rd party INFs must only match against the hardware IDs
-   Hardware IDs that contain HID\_DEVICE\_SYSTEM\_\* are “special” devices that the operating system opens for its use. Vendor provided INF must not match on these special hardware IDs.
-   Vendor provided 3rd party HID transport minidrivers must provided the fields listed below to ensure that HIDClass can generate the appropriate hardware IDs.

Legend:

|       |                 |                   |                                                          |
|-------|-----------------|-------------------|----------------------------------------------------------|
| Field | Contains        | Hexadecimal Value | Meaning                                                  |
| v(4)  | four hex digits | 0x0000-0xFFFF     | Vendor ID                                                |
| d(4)  | four hex digits | 0x0000-0xFFFF     | Product ID                                               |
| r(4)  | four hex digits | 0x0000-0xFFFF     | Revision Number                                          |
| z(2)  | two hex digits  | 0x00-0xFF         | Interface number (only used with composite USB devices.) |
| b(2)  | two hex digits  | 0x00-0xFF         | Collection number (only used with multiple-TLC devices.) |
| p(4)  | four hex digits | 0x0000-0xFFFF     | Usage Page Number for TLC                                |
| u(4)  | four hex digits | 0x0000-0xFFFF     | Usage Number of TLC                                      |

 

 

 




