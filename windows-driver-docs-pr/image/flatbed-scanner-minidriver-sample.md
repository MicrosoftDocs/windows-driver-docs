---
title: Flatbed Scanner Minidriver Sample
description: Flatbed Scanner Minidriver Sample
ms.assetid: 8c1ad90a-cff9-45a0-b2d9-e2605436f128
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Flatbed Scanner Minidriver Sample





The *wiascanr* directory in the Windows DDK contains a sample WIA minidriver for a flatbed scanner with a document feeder.

This sample shows how to write a WIA user-mode minidriver for a scanner. It simulates scanning by producing a test-pattern image. This sample driver can be used as a starting point for your development, but your driver should access the scanner hardware through one of the kernel-mode drivers provided with Windows. The preferred kernel-mode drivers are *usbscan.sys* and *scsiscan.sys*.

### Sample Features

-   Automatic Document Feeder Capabilities

    This sample shows an example for a flatbed scanner with an automatic document feeder (ADF) and a scroll-fed scanner (a feeder that cannot determine the page length).

-   Scan, Copy, and Fax Button Support (interrupt events only)

    Run the small application, *Scanpanl.exe* (which is provided with the Windows DDK) to simulate button presses.

 

 




