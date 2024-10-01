---
title: Publishing restrictions
description: The following items are restricted during publication. You can still create a shipping label for them, but the request requires another Microsoft review.
ms.topic: article
ms.date: 09/19/2024
---

# Publishing restrictions

The following items are restricted during publication. You can still create a shipping label for them, but the request requires another Microsoft review.

The Partner Center enforces these publication restrictions. Publication restrictions ensure that partners can't publish drivers that overwrite Microsoft class drivers or generic bus hardware ID (HWID) strings. They also ensure that devices don't receive incorrect drivers due to generic non-Microsoft or reused HWIDs.

Examples of these restrictions include, but aren't limited to the list in the following table.

| Type of restriction | Additional information |
|--|--|
| Invalid driver submission category types | UNCLASSIFIED |
| Invalid Architecture | ia64 |
| HWIDs with no bus enumerator | N/A |
| Invalid bus enumerators | ActivCardBus<br>CIRCLASS<br>Hid\irdevice<br>Irbus<br>PS2_<br>MIDI<br>PNP<br>ACP<br>IAN<br>AVM<br>STREAM<br>DISPLAY |
| Classcode declarations | \CLASS<br>\CC<br>& |
| Two-part HWIDs | Enforced on PCI and HDAUDIO buses |
| Bluetooth HWIDs with service UUIDs and no vendor ID or product ID | N/A |
| Invalid PCI Vendor Codes | 0000<br>FFFF |
| Missing device codes or product ID codes | Enforced on PCI and USB buses |
| Invalid HWID string starts | HID_DEVI<br>SERIAL_M<br>ISAPNP\PNP<br>SERENUM\PNP<br>PNP<br><em>PNP<br>BIOS\PNP<br>ACPI\PNP |
| System reserved HWIDs | BIOS\PNP<br>ACPI\PNP |
| Invalid HWIDs | </em>DONTUSE<br>SERIAL_MOUSE<br>Root\circlass<br>Hid\irdevice<br>Storage\VolumeSnapshot<br>Storage\Volume |
| Attestation signed drivers | Attestation signed drivers must target a test audience by setting one of the following criteria:<ul><li>CoDev<li>Restricted Audience\Test Registry Key |

For more information about the driver publishing workflow, see [Windows 10 Driver Publishing Workflow](https://go.microsoft.com/fwlink/p/?LinkId=617374).
