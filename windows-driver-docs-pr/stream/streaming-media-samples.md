---
title: Streaming Media Samples
author: windows-driver-content
description: Streaming Media Samples
ms.assetid: 797763a6-cd13-4d76-8ddb-75d812a8dde3
keywords:
- streaming media samples WDK
- samples WDK streaming media
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Streaming Media Samples


### <a href="" id="streaming-media-samples"></a>

Starting with Windows 10, the [Windows driver samples repository](http://go.microsoft.com/fwlink/p/?LinkId=616507) is available on GitHub.

The [Windows 8 driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616509) and the [Windows 8.1 driver samples](http://go.microsoft.com/fwlink/p/?LinkId=618052) can be downloaded from the [Windows Hardware Dev Center](http://go.microsoft.com/fwlink/p/?LinkId=616506).

In Windows 7, samples are included in the Windows Driver Kit (WDK).

<table style="width:100%;">
<colgroup>
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
</colgroup>
<thead>
<tr class="header">
<th>Sample name</th>
<th>Build environment</th>
<th>Target operating system</th>
<th>PnP driver</th>
<th>In-box driver</th>
<th>Sample description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>AVStream Filter-Centric Simulated Capture Driver (Avssamp)</p></td>
<td><p>Windows 8.1</p>
<p>Windows 8</p>
<p>Windows 7</p></td>
<td><p>Windows 8.1</p>
<p>Windows 8</p>
<p>Windows 7</p></td>
<td><p>No</p></td>
<td><p>No</p></td>
<td><p>Provides a filter-centric AVStream capture driver with functional audio. The driver performs captures at 320 x 240 resolution in RGB24 or YUV422 format while playing a user-provided pulse code modulation (PCM) wave audio file in a loop. The sample demonstrates how to write a filter-centric AVStream minidriver.</p></td>
</tr>
<tr class="even">
<td><p>AVStream Simulated Hardware Sample Driver (Avshws)</p></td>
<td><p>Windows 8.1</p>
<p>Windows 8</p>
<p>Windows 7</p></td>
<td><p>Windows 8.1</p>
<p>Windows 8</p>
<p>Windows 7</p></td>
<td><p>No</p></td>
<td><p>No</p></td>
<td><p>Provides a pin-centric AVStream capture driver for a simulated piece of hardware. The driver performs captures at 320 x 240 in either an RGB24 or YUV422 format through direct DMA into capture buffers.</p>
<p>The purpose of the sample is to demonstrate how to write a pin-centric AVStream minidriver. The sample also shows how to implement DMA by using the related functionality that AVStream provides.</p>
<p>This sample features enhanced parameter validation and overflow detection.</p></td>
</tr>
<tr class="odd">
<td><p>SonyDCam 1394 Webcam Driver</p></td>
<td><p>Windows 7</p></td>
<td><p>Windows 7</p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>A Microsoft Windows Driver Model (WDM) Stream class video capture driver that supports 1394-based digital cameras that conform to the Digital Camera Specification from the 1394 Trade Association.</p></td>
</tr>
<tr class="even">
<td><p>USBIntel Webcam Driver</p></td>
<td><p>Windows 7</p></td>
<td><p>Windows 7</p></td>
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>A Microsoft Windows Driver Model (WDM) stream class video capture driver.</p></td>
</tr>
<tr class="odd">
<td><p>SW Tuner</p></td>
<td><p>Windows 7</p></td>
<td><p>Windows 7</p></td>
<td><p>No</p></td>
<td><p>No</p></td>
<td><p>Demonstrates several digital network types.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Streaming%20Media%20Samples%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


