---
title: Properties for WIA Scanner Minidrivers
description: Properties for WIA Scanner Minidrivers
ms.assetid: 9de8694a-0d19-4945-b0c1-a3c4bc71dad3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Properties for WIA Scanner Minidrivers





The following lists contains all of the WIA properties that are unique to WIA scanner minidrivers.

### Required Properties on Scanner Root Items (Microsoft Windows XP and Windows Me)

A WIA minidriver supplies the following properties:

[**WIA\_DPS\_OPTICAL\_XRES**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-optical-xres)

[**WIA\_DPS\_OPTICAL\_YRES**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-optical-yres)

### Optional Properties on Scanner Root Items (Windows XP and Windows Me)

A WIA minidriver supplies the following properties:

[**WIA\_DPS\_DITHER\_PATTERN\_DATA**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-dither-pattern-data)

[**WIA\_DPS\_DITHER\_SELECT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-dither-select)

[**WIA\_DPS\_FILTER\_SELECT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-filter-select)

[**WIA\_DPS\_MAX\_SCAN\_TIME**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-max-scan-time)

[**WIA\_DPS\_PAD\_COLOR**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-pad-color)

[**WIA\_DPS\_PLATEN\_COLOR**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-platen-color)

[**WIA\_DPS\_SHOW\_PREVIEW\_CONTROL**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-show-preview-control)

### Required Properties on Scanner Child Items Able to Transfer Data

A WIA minidriver supplies the following properties:

[**WIA\_IPS\_BRIGHTNESS**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-brightness)

[**WIA\_IPS\_CONTRAST**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-contrast)

[**WIA\_IPS\_CUR\_INTENT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-cur-intent)

[**WIA\_IPS\_PHOTOMETRIC\_INTERP**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-photometric-interp)

[**WIA\_IPS\_XEXTENT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-xextent)

[**WIA\_IPS\_XPOS**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-xpos)

[**WIA\_IPS\_XRES**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-xres)

[**WIA\_IPS\_YEXTENT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-yextent)

[**WIA\_IPS\_YPOS**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-ypos)

[**WIA\_IPS\_YRES**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-yres)

### Optional Properties on Scanner Child Items Able to Transfer Data

A WIA minidriver supplies the following properties:

[**WIA\_DPS\_PAGE\_HEIGHT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-page-height)

[**WIA\_DPS\_PAGE\_SIZE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-page-size)

[**WIA\_DPS\_PAGE\_WIDTH**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-page-width)

[**WIA\_IPS\_INVERT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-invert)

[**WIA\_IPS\_MIRROR**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-mirror)

[**WIA\_IPS\_ORIENTATION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-orientation)

[**WIA\_IPS\_ROTATION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-rotation)

[**WIA\_IPS\_THRESHOLD**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-threshold)

[**WIA\_IPS\_WARM\_UP\_TIME**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-warm-up-time)

### Required Properties on Flatbed Scanner Root Items (Windows XP and Windows Me)

A WIA minidriver supplies the following properties:

[**WIA\_DPS\_HORIZONTAL\_BED\_REGISTRATION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-horizontal-bed-registration)

[**WIA\_DPS\_HORIZONTAL\_BED\_SIZE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-horizontal-bed-size)

[**WIA\_DPS\_PREVIEW**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-preview)

[**WIA\_DPS\_VERTICAL\_BED\_REGISTRATION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-vertical-bed-registration)

[**WIA\_DPS\_VERTICAL\_BED\_SIZE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-vertical-bed-size)

### Required Properties on Document Feeder Scanner Root Items (Windows XP and Windows Me)

A WIA minidriver supplies the following properties:

[**WIA\_DPS\_DOCUMENT\_HANDLING\_CAPABILITIES**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-document-handling-capabilities)

[**WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-document-handling-select)

[**WIA\_DPS\_DOCUMENT\_HANDLING\_STATUS**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-document-handling-status)

[**WIA\_DPS\_HORIZONTAL\_SHEET\_FEED\_SIZE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-horizontal-sheet-feed-size)

[**WIA\_DPS\_MIN\_HORIZONTAL\_SHEET\_FEED\_SIZE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-min-horizontal-sheet-feed-size)

[**WIA\_DPS\_MIN\_VERTICAL\_SHEET\_FEED\_SIZE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-min-vertical-sheet-feed-size)

[**WIA\_DPS\_PAGES**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-pages)

[**WIA\_DPS\_SHEET\_FEEDER\_REGISTRATION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-sheet-feeder-registration)

[**WIA\_DPS\_VERTICAL\_SHEET\_FEED\_SIZE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-vertical-sheet-feed-size)

### Properties on Transparency Scanner Root Items (Windows XP and Windows Me)

A WIA minidriver supplies the following properties:

[**WIA\_DPS\_TRANSPARENCY**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-transparency)

[**WIA\_DPS\_TRANSPARENCY\_SELECT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-transparency-select)

 

 




