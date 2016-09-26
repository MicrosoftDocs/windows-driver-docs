---
title: Windows Precision Touchpad Implementation Guide
description: This topic describes how to implement a Windows Precision Touchpad. It provides guidelines for how to use the Human Interface Device (HID) protocol to communicate with the Windows host. This information applies to Windows 8.1.
ms.assetid: 424BEE67-B45F-428B-BF58-43C018D20334
---

# Windows Precision Touchpad Implementation Guide


This topic describes how to implement a Windows Precision Touchpad. It provides guidelines for how to use the Human Interface Device (HID) protocol to communicate with the Windows host. This information applies to Windows 8.1.

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[Device Bus Connectivity](windows-precision-touchpad-device-bus-connectivity.md)</p></td>
<td align="left"><p>A Windows Precision Touchpad can use either USB or I²C for host connectivity. This topic includes examples of device configurations.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Power Management](windows-precision-touchpad-power-management.md)</p></td>
<td align="left"><p>This topic describes power management for a Windows Precision Touchpad implementation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Protocol Implementation](windows-precision-touchpad-protocol-implementation.md)</p></td>
<td align="left"><p>Windows Precision Touchpads are expected to use the Human Interface Device (HID) protocol to communicate with the host. This topic describes how to implement the HID protocol for Windows Precision Touchpads.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Device Integration](windows-precision-touchpad-device-integration.md)</p></td>
<td align="left"><p>Windows Precision Touchpads define an experience. Integration of the module has a significant impact on how well that experience is realized. This topic describes Windows Precision Touchpads integration.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Module Design for Windows HCK Requirements](windows-precision-touchpad-module-design-for-windows-hck-requirements.md)</p></td>
<td align="left"><p>The Windows Hardware Certification Kit (HCK) requirements for Windows Precision Touchpads are designed to provide a consistent user experience where precision and reliability are at the forefront. These requirements shall influence all aspects of the module, including the sensor, controller IC and associated mechanics.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Enable or Disable Toggle Button](windows-precision-touchpad-enable-or-disable-toggle-button.md)</p></td>
<td align="left"><p>Windows Precision Touchpads (or legacy touchpads that have opted in for enable/disable control in Windows 8.1) can have their enable/disable state toggled by using a hardware button or keyboard combination.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Windows Precision Touchpad Industrial Design Guide](windows-precision-touchpad-industrial-design-guide.md)</p></td>
<td align="left"><p>This topic provides industrial design guidance for Windows Precision Touchpads. Many of these guidelines are part of the [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?LinkID=330443) and are identified as such in this topic. Additional industrial design characteristics are provided as suggested guidance and reference for hardware manufacturers. This information applies to Windows 8.1.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Legacy Touchpad PC Settings Opt-In](windows-precision-touchpad-legacy-touchpad-pc-settings-opt-in.md)</p></td>
<td align="left"><p>This topic describes how devices that are not Windows Precision Touchpads can opt in to various settings that are exposed in Windows 8.1 to provide a simple and easy-to-navigate inbox solution to manage the most common touchpad settings.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Glossary"></span><span id="glossary"></span><span id="GLOSSARY"></span>Glossary


| Term/Acronym                                    | Definition                                                                                                                                                                         |
|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Global Items                                    | Entries in a report descriptor that describe the properties of a data field. Unlike local items, global items remain the same across multiple main items until they are changed.   |
| Human Interface Device (HID)                    | Human interface device (HID) refers to either the protocol or the device itself. In this document, HID refers to the device and HID protocol refers to the protocol in definition. |
| I<sup>²</sup>C - I²C (Inter-Integrated Circuit) | I²C is a multi-master serial single-ended bus that is used to attach low-speed peripherals to the motherboard, embedded.                                                           |
| Local Items                                     | Entries in a report descriptor that describe certain properties of a data field. Local items are only associated with the main items they precede in the report descriptor.        |
| Main Items                                      | Entries in a report descriptor that define data fields.                                                                                                                            |
| Usage                                           | The name of a value, button, or collection in a HID report.                                                                                                                        |
| USB                                             | Universal Serial Bus                                                                                                                                                               |

 

## <span id="related_topics"></span>Related topics


[Windows pointer device data delivery protocol](http://go.microsoft.com/fwlink/p/?LinkID=324191)

[USB HID Information](http://go.microsoft.com/fwlink/p/?LinkID=155096)

[HID I2C v1.0 Protocol Specification](http://go.microsoft.com/fwlink/p/?LinkID=286770)

[Advanced Configuration and Power Interface Specification](http://www.acpi.info/spec.md)

 

 




