---
title: Firmware Windows Engineering Guide (WEG)
description: The Firmware Windows Engineering Guide (WEG) provides a roadmap to follow through in implementing system firmware-related best practices.
ms.author: windowsdriverdev
ms.date: 05/01/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Firmware Windows Engineering Guide (WEG)

The Firmware Windows Engineering Guide (WEG) provides a roadmap to follow through in implementing system firmware-related best practices.


## In this section

[UEFI security](uefi-security.md)
[Firmware update](firmware-update.md)
[SMBIOS](smbios.md)
[HTTPS](https-boot.md)
[Wi-Fi support in firmware](wi-fi-support-in-firmware.md)
[Switch from legacy MBR disk to GPT disk with Windows 10](switch-from-legacy-mbr-disk-to-gpt-disk-with-windows-10.md)
[Frequently asked questions](frequently-asked-questions.md)
[Configure system firmware for Windows 7 and later update for Windows 10](configure-system-firmware-for-windows-7-and-later-update-for-windows-10.md)
[Sample PowerShell script to query SMBIOS locally](sample-powershell-script-to-query-smbios-locally.md)

                                           





### Acronyms


ACPI - Advanced Configuration and Power Interface

BCD - Boot Configuration Data

BIOS - Basic Input/output System

CSM - Compatibility Support Module

eMMC - embedded Multi-Media Controller

ESRT – EFI System Resource Table

GPT - GUID Partition Table

GUID – Globally Unique Identification

HDD - Hard Disk Drive

HSTI / HSTS – Hardware Security Testability Interface / Specification

HVCI- HyperVisor Code Integrity

IOMMU - Input–output memory management unit

[INT10](https://en.wikipedia.org/wiki/INT_10H) - BIOS interrupt call used for video basic display

MAT/MADT – Memory A

MBR - Master Boot Record

MOR – Memory Overwrite Request

OEM - Original Equipment Manufacturer/Manufacturing

RPMC – Replay Protected Monotonic Counter

SMBIOS – System Management Basic Input Output System

SPI - Serial Peripheral Interface

TCG - Trusted Computing Group

TPM – Trusted platform Module

UEFI - Unified Extensible Firmware Interface

WEG – Windows Engineering Guide

WinPE- Windows Pre-installation Environment

WinRE - Windows Recovery Environment

WSMT-Windows SMM Security Mitigations Table







--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


