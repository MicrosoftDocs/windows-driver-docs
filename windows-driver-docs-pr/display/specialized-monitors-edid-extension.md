---
title: EDID Extension for Head-Mounted and Specialized Monitors
description: EDID extension for head-mounted and specialized monitors
keywords:
- display devices WDK
- monitor drivers WDK
- display drivers WDK , monitor drivers
- monitors
- HMD
- virtual reality
ms.date: 04/24/2025
---

# EDID extension for head-mounted and specialized monitors

This article describes how a display manufacturer can implement an [EDID](https://en.wikipedia.org/wiki/Extended_Display_Identification_Data) CTA (Consumer Technology Association) extension in HMD (Head Mounted Display) or specialized display firmware. The audience is primarily display manufacturers. The terms display and monitor are synonymous in this article.

The implemented extension allows Windows to recognize the display as special and thus enable each layer in the Windows OS to treat them correctly. Without this EDID extension, HMDs and specialized displays have the following problems:

* The Windows desktop is extended to the display, apps can launch onto it, and the mouse cursor can roam onto the display. If the users aren't expecting this behavior, it can be confusing to recover from.
* Non-Microsoft compositors must use HWND-based or CoreWindow-based presentation APIs, which don't allow for exclusive access to the display. The Windows desktop compositor is responsible for routing windowed presentation APIs to the display, which can incur extra nondeterministic latency in some scenarios.

To solve these problems, both of the following conditions must be met:

1. The firmware in the display that contains the [EDID](https://en.wikipedia.org/wiki/Extended_Display_Identification_Data) must be modified to contain a [Vendor Specific Data Block](https://en.wikipedia.org/wiki/Extended_Display_Identification_Data#EIA.2FCEA-861_extension_block) (VSDB) to identify the Windows-specific use-case of the display.
2. The Windows display subsystem correctly recognizes the Vendor Specific Data Block outlined in this article and treats the displays appropriately. Different versions of the Windows OS might have different behaviors, as described later in this article.

This two-step solution results in the correct Windows behavior from the moment the display is first plugged in. In particular:

* HMDs and certain specialized displays aren't included in the regular Windows desktop environment.
* Access to the display with the [Windows.Devices.Display.Core](/uwp/api/windows.devices.display.core) APIs becomes available to non-Microsoft compositors.

The Video Electronics Standards Association (VESA) defines standardized fields in [DisplayId v2.](https://vesa.org/featured-articles/vesa-rolls-out-displayid-version-2-0-standard-to-optimize-plug-and-play-connectivity-for-leading-edge-displays/). These fields provide access to similar information as the VSDB defined in this article. DisplayID v2.0 or later is the preferred mechanism to deliver this data for HMDs. However, if a device must use an EDID for other reasons, this VSDB should be used.

## Vendor-specific data block (VSDB)

The party responsible for writing the firmware code that contains the EDID must include a CTA extension block with a Microsoft-defined VSDB. The structure of EDIDs is described in the "VESA Enhanced Extended Display Identification Data Standard" ([E-EDID](https://vesa.org/standards-specifications/)), see version 1.4, release A, revision 2 with section 2.2 describing extension blocks. The CTA extension block is defined in the CTA's 861 series document *A DTV Profile for Uncompressed High-Speed Digital Interfaces*. VSDBs are described in [ANSI/CTA-861-G](https://webstore.ansi.org/Standards/ANSI/CTA8612016ANSI) including the order of VSDB relative to other data blocks.

The VSDB structure must have the format and values that are outlined in the following table.

:::image type="content" source="images/specialized-displays-vsdb.png" alt-text="Table showing the VSDB structure and values for specialized displays.":::

### Vendor specific tag code [3 bits]

This field must be set to `0x3`.

### Length [5 bits]

Total length of data block, not including this byte. This field must be set to `0x15`.

### IEEE OUI [3 bytes]

The IEEE Organizationally Unique Identifier (OUI) assigned to Microsoft for identifying displays: `0x5C`, `0x12`, `0xCA`, in sequential byte order.

### Version [1 byte]

The version number associated with the contents of the Microsoft Display VSDB.

| Recommended Use-Case | Version | Supported Windows Release |
|----------------------|---------|---------------------------|
| For HMD (VR/AR) display devices used by the Windows Mixed Reality experience | `0x1` | Windows 10 version 1703 and later |
| For HMD (VR/AR) display devices used by non-Microsoft compositors (other than the Windows Mixed Reality experience) | `0x2` | Windows 10 version 1809 and later |
| For specialized display devices that aren't HMDs | `0x3` | Supported in Windows 10 version 1903 and later |

### Desktop usage flag [1 bit]

On version `0x3` and later of this VSDB, this bit indicates whether the display should be part of the desktop.

* If the display should be part of the desktop, set to `0x1`.
* If the display shouldn't be part of the desktop, set to `0x0`.

In version `0x1` and `0x2` of this VSDB, this value should always be set to `0x0`.

### Non-Microsoft usage flag [1 bit]

On version `0x3` and later of this VSDB, this bit indicates whether the display should be usable by non-Microsoft compositors, or only the Microsoft-provided Windows compositor.

* If the display should be usable by non-Windows software compositors, set to `0x1`.
* If the display should only be used by the Windows compositor, set to `0x0`.

In version `0x1` and `0x2` of this VSDB, this value should always be set to `0x0`.

### Display product primary use case [5 bits]

The primary use case of the display device:

* Test equipment - `0x1`
* Generic display - `0x2`
* Television display - `0x3`
* Desktop productivity display - `0x4`
* Desktop gaming display - `0x5`
* Presentation display - `0x6`
* Virtual reality headsets - `0x7`
* Augmented reality - `0x8`
* Video wall display - `0x10`
* Medical imaging display - `0x11`
* Dedicated gaming display - `0x12`
* Dedicated video monitor display - `0x13`
* Accessory display - `0x14`

### Container ID [16 bytes]

The 16-byte Universally Unique Identifier that is unique to each device. This identifier is burned in on the factory floor.

## Remarks

In order to maintain maximum compatibility with earlier operating systems, HMDs should continue to use version `0x1` and `0x2` of this EDID extension. See [Version](#version-1-byte) for which values to use for HMDs.
