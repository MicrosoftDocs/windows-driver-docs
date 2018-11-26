---
title: Pscript Support for Stapling
description: Pscript Support for Stapling
ms.assetid: 75fc11e1-5cd9-4e95-b062-989fe493fdb5
keywords:
- minidrivers WDK Pscript , stapling
- stapling WDK Pscript
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pscript Support for Stapling





The Microsoft Pscript driver supports the following standard stapling features in [*PPD*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-postscript-printer-description--ppd-) files.

-   \*StapleLocation

-   \*StapleOrientation

-   \*StapleWhen

-   \*StapleX

-   \*StapleY

For more information about these standard stapling features, see *PostScript Printer Description File Format Specification*, Version 4.3, 9 February 1996. (This resource may not be available in some languages and countries.)

To determine whether the device supports stapling, the Pscript driver uses the following logic:

1.  If none of the previously-listed standard stapling features is defined in the PPD file, then stapling is not supported.

2.  If \*StapleOrientation is the only stapling feature that is defined in the PPD file, then stapling is supported.

3.  If one or more of the previously-listed standard stapling features (other than \*StapleOrientation) are defined in the PPD file and if any of the defined features is constrained by the current configuration of an installable feature, then stapling is not supported. For example, if the NotInstalled option of the DuplexerUnit installable feature places a constraint on \*StapleLocation, and the printer's current configuration for DuplexerUnit is NotInstalled, then stapling is not supported.

 

 




