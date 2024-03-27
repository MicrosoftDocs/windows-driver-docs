---
title: Identifiers for High Definition Audio (HDAUDIO) Devices
description: Describes the device identification string formats that are used to  report High Definition Audio HDAUDIO hardware device IDs.
keywords:
- device identification strings WDK , Audio devices
- identification strings WDK device , Audio devices
- identifiers WDK device , Audio devices
- Audio device identifiers WDK device installations
- hardware IDs WDK device installations
- compatible IDs WDK device installations
ms.date: 05/11/2023
---

# Identifiers for High Definition Audio (HDAUDIO) devices

This section describes the elements that make up the  High Definition Audio (HDAUDIO) device identification strings.

For general information about High Definition Audio, see the [HD Audio Specification](https://www.intel.com/content/www/us/en/standards/high-definition-audio-specification.html) from Intel.

High Definition Audio (HDAUDIO) devices are identified using the following syntax.

`HDAUDIO\FUNC_01&VEN_vvvv&DEV_dddd&SUBSYS_ssssssss&REV_rrrr`

Each element is described here.

`HDAUDIO`

Identifies this entry as an HD audio device.

`FUNC_nn`

Identifies the HDAudio Function Group Type for this node. “01” is Audio Function Group, which is used by audio drivers. Refer to Table 137 *Node Type* in the HD Audio Specification for additional information.

`&VEN_vvvv`

v(4) is the four-character PCI SIG-assigned identifier for the vendor of the device, where the term *device*, following PCI SIG usage, refers to a specific Audio Codec unit. As specified in [Publishing restrictions](../dashboard/publishing-restrictions.md), `0000` and `FFFF` are invalid codes for the vendor identifier.

`&DEV_dddd`

d(4) is the four-character vendor-defined identifier for the device.

`SUBSYS_ssssssss`

s(8) is the eight-character Implementation Identification Value as defined by the High Definition Audio Specification. The SUBSYS is either the Board Implementation ID (31:8) and Assembly ID (7:0) or the Board Manufacturer Identification (31:16), Board SKU (15:8), and Assembly ID (7:0)

`&REV_rrrr`

R(4) is the four-character Revision ID as defined by the High Definition Audio Specification.

- 31:24 – reserved
- 23:20 – Major revision number of the spec “to which the codec is fully compliant”
- 19:16 – Minor revision number of the spec
- 15:8 – vendor’s revision number for the device ID
- 7:0 – vendor stepping number within the given revision number

## PnPUtil

To list IDs on Windows, use `pnputil /enum-devices /bus HDAUDIO /deviceids`.

For more information, see [PnPUtil Command Syntax](/windows-hardware/drivers/devtest/pnputil-command-syntax).

## Reporting hardware and compatible IDs

The [Device identification string](device-identification-strings.md) is used by the High Definition Audio bus driver to report [hardware IDs](hardware-ids.md). The driver advertises the hardware IDs as a list in order of increasing generality. The first hwid is the device id and the second hwid is the more general reference without the revision number.

The compatible IDs are a list of IDs including different components from the full hardware ID in order of increasing generality. The compatible ID list also includes IDs that reference the High Definition Audio bus device vendor and device numbers as CTRL_VEN_vvvv and CTRL_DEV_dddd, allowing a driver package to target a combined codec device and controller device.
