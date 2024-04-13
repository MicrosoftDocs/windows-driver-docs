---
title: Pscript Support for Stapling
description: Pscript Support for Stapling
keywords:
- minidrivers WDK Pscript , stapling
- stapling WDK Pscript
ms.date: 01/30/2023
---

# Pscript Support for Stapling

[!include[Print Support Apps](../includes/print-support-apps.md)]

The Microsoft Pscript driver supports the following standard stapling features in *PPD* files.

- \*StapleLocation

- \*StapleOrientation

- \*StapleWhen

- \*StapleX

- \*StapleY

For more information about these standard stapling features, see *PostScript Printer Description File Format Specification*, Version 4.3, 9 February 1996. (This resource may not be available in some languages and countries.)

To determine whether the device supports stapling, the Pscript driver uses the following logic:

1. If none of the previously-listed standard stapling features is defined in the PPD file, then stapling is not supported.

1. If \*StapleOrientation is the only stapling feature that is defined in the PPD file, then stapling is supported.

1. If one or more of the previously-listed standard stapling features (other than \*StapleOrientation) are defined in the PPD file and if any of the defined features is constrained by the current configuration of an installable feature, then stapling is not supported. For example, if the NotInstalled option of the DuplexerUnit installable feature places a constraint on \*StapleLocation, and the printer's current configuration for DuplexerUnit is NotInstalled, then stapling is not supported.
