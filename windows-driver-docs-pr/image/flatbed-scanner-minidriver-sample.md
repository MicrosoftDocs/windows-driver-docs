---
title: Flatbed Scanner Minidriver Sample
author: windows-driver-content
description: Flatbed Scanner Minidriver Sample
ms.assetid: 8c1ad90a-cff9-45a0-b2d9-e2605436f128
---

# Flatbed Scanner Minidriver Sample


## <a href="" id="ddk-flatbed-scanner-minidriver-sample-si"></a>


The *wiascanr* directory in the Windows DDK contains a sample WIA minidriver for a flatbed scanner with a document feeder.

This sample shows how to write a WIA user-mode minidriver for a scanner. It simulates scanning by producing a test-pattern image. This sample driver can be used as a starting point for your development, but your driver should access the scanner hardware through one of the kernel-mode drivers provided with Windows. The preferred kernel-mode drivers are *usbscan.sys* and *scsiscan.sys*.

### Sample Features

-   Automatic Document Feeder Capabilities

    This sample shows an example for a flatbed scanner with an automatic document feeder (ADF) and a scroll-fed scanner (a feeder that cannot determine the page length).

-   Scan, Copy, and Fax Button Support (interrupt events only)

    Run the small application, *Scanpanl.exe* (which is provided with the Windows DDK) to simulate button presses.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Flatbed%20Scanner%20Minidriver%20Sample%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


