---
title: Streaming Media Samples
description: Streaming Media Samples
ms.assetid: 797763a6-cd13-4d76-8ddb-75d812a8dde3
keywords:
- streaming media samples WDK
- samples WDK streaming media
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 

 




