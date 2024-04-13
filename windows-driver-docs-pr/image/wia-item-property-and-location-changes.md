---
title: WIA Item Property and Location Changes
description: WIA Item Property and Location Changes
ms.date: 04/20/2017
---

# WIA Item Property and Location Changes





The simplest way to ensure application compatibility in Windows Vista and previous operating systems is to implement the WIA properties in the Windows XP and Windows Me locations *and* in the Windows Vista locations. Normally, WIA applications that are written for Windows Vista operate only with the WIA properties and locations added for Windows Vista, while applications that are written for Windows XP and Windows Me work only with the WIA properties and locations that are defined in those operating systems. Implementing the properties in both locations allows applications that are written for Windows Vista, Windows XP, and Windows Me to work with the same property set implementation.

In operating systems before Windows Vista, the following WIA properties were located on the root item of a scanner driver that supported flatbed platen scanning. In Windows Vista, they are located on the flatbed item.

-   [**WIA\_DPS\_HORIZONTAL\_BED\_SIZE**](./wia-dps-horizontal-bed-size.md) (known as [**WIA\_IPS\_MAX\_HORIZONTAL\_SIZE**](./wia-ips-max-horizontal-size.md) in Windows Vista)

-   [**WIA\_DPS\_VERTICAL\_BED\_SIZE**](./wia-dps-vertical-bed-size.md) (known as [**WIA\_IPS\_MAX\_VERTICAL\_SIZE**](./wia-ips-max-vertical-size.md) in Windows Vista)

-   [**WIA\_DPS\_OPTICAL\_XRES**](./wia-dps-optical-xres.md) (known as [**WIA\_IPS\_OPTICAL\_XRES**](./wia-ips-optical-xres.md) in Windows Vista)

-   [**WIA\_DPS\_OPTICAL\_YRES**](./wia-dps-optical-yres.md) (known as [**WIA\_IPS\_OPTICAL\_YRES**](./wia-ips-optical-yres.md) in Windows Vista)

-   [**WIA\_DPS\_PREVIEW**](./wia-dps-preview.md) (known as [**WIA\_IPS\_PREVIEW**](./wia-ips-preview.md) in Windows Vista)

-   [**WIA\_DPS\_SHOW\_PREVIEW\_CONTROL**](./wia-dps-show-preview-control.md) (known as [**WIA\_IPS\_SHOW\_PREVIEW\_CONTROL**](./wia-ips-show-preview-control.md) in Windows Vista)

**Note**   The duplication of WIA properties is needed only for scanners that support flatbed platen scanning or document feeder scanning. The paired properties have the same property identifier for compatibility. The driver can add WIA\_DPS\_*Xxx* properties for the root item and WIA\_IPS\_*Xxx* for other items.

 

 

