---
title: Minimum UEFI Requirements for Windows on SoC Platforms
description: Provides information about minimum UEFI requirements for Windows on SoC platforms.
ms.date: 03/23/2023
---

# Minimum UEFI requirements for Windows on SoC platforms

Unified Extensible Firmware Interface (UEFI) is the required boot firmware for SoC platforms running Windows. This section describes UEFI implementation requirements for running Windows on SoC platforms. Observation and adherence to these requirements will help ensure proper functionality of Windows.

This set of requirements applies to any SoC-based computing system, with some limitations. This guidance assumes a full Windows feature set, with support for both traditional netbook form-factors and wireless, multitouch-only mobile devices. It therefore limits itself to technologies expected to be widely used on such systems. For systems that implement technologies not covered in this document, refer to the UEFI specification at [UEFI specifications](https://uefi.org/specifications).

Windows supports firmware revisions based on the Unified Extensible Firmware Interface (UEFI) Version 2.3.1 or later.

Windows supports a subset of functionality defined in the UEFI 2.3.1 specification. The Windows implementation does not have an explicit check against higher revisions of the firmware. The operating system will support higher revisions of the firmware if they contain the necessary support described in this document.

## In this section

| Topic | Description |
|--|--|
| [UEFI requirements that apply to all Windows editions on SoC platforms](uefi-requirements-that-apply-to-all-windows-platforms.md) | Describes UEFI requirements that apply to Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows 10 Mobile. |
| [UEFI requirements for Windows 10 Mobile](uefi-requirements-specific-to-windows-mobile.md) | Devices that run Windows 10 Mobile must meet additional requirements described in this topic. |
| [UEFI requirements for USB flashing support](uefi-requirements-for-usb-flashing-support.md) | Microsoft provides several USB-based flashing solutions for use in engineering and manufacturing environments. In order for a device to be used with these tools, the UEFI environment on the device must meet the requirements listed in this topic. |
