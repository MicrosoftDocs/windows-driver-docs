---
title: USBCAMD2 Minidriver Operation
description: USBCAMD2 Minidriver Operation
ms.assetid: 395612cd-3407-4b42-b3a5-0afa838e73d9
keywords:
- Windows 2000 Kernel Streaming Model WDK , USBCAMD2 minidriver library
- Streaming Model WDK Windows 2000 Kernel , USBCAMD2 minidriver library
- Kernel Streaming Model WDK , USBCAMD2 minidriver library
- USBCAMD2 minidriver operations WDK Windows 2000 Kernel Streaming
- USB-based streaming cameras WDK USBCAMD2
- cameras WDK USBCAMD2
- SRBs WDK USBCAMD2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USBCAMD2 Minidriver Operation

A USBCAMD2 camera minidriver generally operates as follows:

- The camera minidriver calls [**USBCAMD\_DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff568593) from its [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. When the minidriver calls **USBCAMD\_DriverEntry**, it passes to USBCAMD2 the minidriver's [*AdapterReceivePacket*](https://msdn.microsoft.com/library/windows/hardware/ff554080) callback function. USBCAMD2 then registers the minidriver with the *stream.sys* class driver.

- The camera minidriver can then receive various stream request blocks (SRBs) in its *AdapterReceivePacket* callback function to handle, including:
  - [**SRB\_INITIALIZE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff568185)
  - [**SRB\_INITIALIZATION\_COMPLETE**](https://msdn.microsoft.com/library/windows/hardware/ff568182)
  - [**SRB\_GET\_STREAM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568173)
  - [**SRB\_GET\_DEVICE\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff568170)
  - [**SRB\_SET\_DEVICE\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff568204)
  - [**SRB\_GET\_DATA\_INTERSECTION**](https://msdn.microsoft.com/library/windows/hardware/ff568168)
  - [**SRB\_OPEN\_STREAM**](https://msdn.microsoft.com/library/windows/hardware/ff568191)
- The camera minidriver determines how it must process each SRB. The minidriver can call routines in the USBCAMD2 minidriver library to assist with processing SRBs. These routines typically begin with the *USBCAMD\_* prefix.

For example, to specify the camera minidriver's other callback functions with USBCAMD2, the camera minidriver specifies their entry points in a [**USBCAMD\_DEVICE\_DATA2**](https://msdn.microsoft.com/library/windows/hardware/ff568590) structure. The minidriver then calls [**USBCAMD\_InitializeNewInterface**](https://msdn.microsoft.com/library/windows/hardware/ff568599) to pass the initialized USBCAMD\_DEVICE\_DATA2 structure to USBCAMD2. USBCAMD2 then calls the minidriver's callback functions when necessary.

> [!NOTE]
> The [**USBCAMD\_DEVICE\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff568585) structure is supported in USBCAMD2 only for purposes of backward compatibility.

The minidriver must call [**USBCAMD\_AdapterReceivePacket**](https://msdn.microsoft.com/library/windows/hardware/ff568574) to send any SRBs it does not handle to USBCAMD2 to process.

[USBCAMD Library Callback Functions](https://msdn.microsoft.com/library/windows/hardware/ff568608) describe the callback functions that the minidriver implements and whether they are optional or required.

The following list of procedures illustrates the general flow of processing for SRBs sent to the camera minidriver:

## Minidriver's SRB\_INITIALIZE\_DEVICE handler

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Component</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Camera minidriver</p></td>
<td><p>Initialize USBCAMD2 by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff568599" data-raw-source="[&lt;strong&gt;USBCAMD_InitializeNewInterface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568599)"><strong>USBCAMD_InitializeNewInterface</strong></a>, indicating video or still raw processing requirements in kernel mode, such as enabling device events.</p></td>
</tr>
<tr class="even">
<td><p>Camera minidriver</p></td>
<td><p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff568574" data-raw-source="[&lt;strong&gt;USBCAMD_AdapterReceivePacket&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568574)"><strong>USBCAMD_AdapterReceivePacket</strong></a>.</p></td>
</tr>
<tr class="odd">
<td><p>USBCAMD2</p></td>
<td><p>Acquire USB device and configuration descriptors.</p></td>
</tr>
<tr class="even">
<td><p>USBCAMD2</p></td>
<td><p>Call the minidriver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff557605" data-raw-source="[&lt;em&gt;CamConfigureEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557605)"><em>CamConfigureEx</em></a> callback function.</p></td>
</tr>
<tr class="odd">
<td><p>Camera minidriver</p></td>
<td><p>Complete the configuration. Choose an alternate setting and maximum transfer size. Fill in the array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568623" data-raw-source="[&lt;strong&gt;USBCAMD_Pipe_Config_Descriptor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568623)"><strong>USBCAMD_Pipe_Config_Descriptor</strong></a> structures.</p></td>
</tr>
<tr class="even">
<td><p>USBCAMD2</p></td>
<td><p>Parse the array of <strong>USBCAMD_Pipe_Config_Descriptor</strong> structures.</p></td>
</tr>
<tr class="odd">
<td><p>USBCAMD2</p></td>
<td><p>Call the minidriver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff557614" data-raw-source="[&lt;em&gt;CamInitialize&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557614)"><em>CamInitialize</em></a> callback function.</p></td>
</tr>
<tr class="even">
<td><p>Camera minidriver</p></td>
<td><p>Complete the initialization. Set the device power and activate the default setting on the camera.</p></td>
</tr>
<tr class="odd">
<td><p>USBCAMD2</p></td>
<td><p>Provide the number of streams and stream descriptor size to the <em>stream.sys</em> class driver.</p></td>
</tr>
</tbody>
</table>

## Minidriver's SRB\_GET\_STREAM\_INFO handler

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Component</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Camera minidriver</p></td>
<td><p>Provide the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559692" data-raw-source="[&lt;strong&gt;HW_STREAM_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559692)"><strong>HW_STREAM_INFORMATION</strong></a> stream information structure to the <em>stream.sys</em> class driver.</p></td>
</tr>
<tr class="even">
<td><p>Camera minidriver</p></td>
<td><p>Fill in the pointer to the array of device property sets in <em>stream.sys</em> class driver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff559690" data-raw-source="[&lt;strong&gt;HW_STREAM_HEADER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559690)"><strong>HW_STREAM_HEADER</strong></a> structure.</p></td>
</tr>
<tr class="odd">
<td><p>Camera minidriver</p></td>
<td><p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff568574" data-raw-source="[&lt;strong&gt;USBCAMD_AdapterReceivePacket&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568574)"><strong>USBCAMD_AdapterReceivePacket</strong></a>.</p></td>
</tr>
<tr class="even">
<td><p>USBCAMD2</p></td>
<td><p>Fill in the number of pins in the stream header.</p></td>
</tr>
<tr class="odd">
<td><p>USBCAMD2</p></td>
<td><p>Expose the device event table, if any.</p></td>
</tr>
<tr class="even">
<td><p>USBCAMD2</p></td>
<td><p>Fix entry values in the stream information table. Set category name (capture or still).</p></td>
</tr>
<tr class="odd">
<td><p>USBCAMD2</p></td>
<td><p>Fill in the pointer to the stream property array.</p></td>
</tr>
</tbody>
</table>

## Minidriver's SRB\_INITIALIZATION\_COMPLETE handler

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Component</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Camera minidriver</p></td>
<td><p>Acquire GUID_USBCAMD_INTERFACE for USBCAMD2 using IRP_MJ_PNP and IRP_MN_QUERY_INTERFACE.</p></td>
</tr>
</tbody>
</table>

## Minidriver's SRB\_GET\_DEVICE\_PROPERTY handler

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Component</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Camera minidriver</p></td>
<td><p>Get the properties that the camera minidriver handles, such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff568122" data-raw-source="[PROPSETID_VIDCAP_VIDEOPROCAMP](https://msdn.microsoft.com/library/windows/hardware/ff568122)">PROPSETID_VIDCAP_VIDEOPROCAMP</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff567802" data-raw-source="[PROPSETID_VIDCAP_CAMERACONTROL](https://msdn.microsoft.com/library/windows/hardware/ff567802)">PROPSETID_VIDCAP_CAMERACONTROL</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff568120" data-raw-source="[PROPSETID_VIDCAP_VIDEOCONTROL](https://msdn.microsoft.com/library/windows/hardware/ff568120)">PROPSETID_VIDCAP_VIDEOCONTROL</a>, as well as any other custom property sets.</p></td>
</tr>
</tbody>
</table>

## Minidriver's SRB\_SET\_DEVICE\_PROPERTY handler

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Component</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Camera minidriver</p></td>
<td><p>Set the properties the camera minidriver handles by acquiring the parameters of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568122" data-raw-source="[PROPSETID_VIDCAP_VIDEOPROCAMP](https://msdn.microsoft.com/library/windows/hardware/ff568122)">PROPSETID_VIDCAP_VIDEOPROCAMP</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff567802" data-raw-source="[PROPSETID_VIDCAP_CAMERACONTROL](https://msdn.microsoft.com/library/windows/hardware/ff567802)">PROPSETID_VIDCAP_CAMERACONTROL</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff568120" data-raw-source="[PROPSETID_VIDCAP_VIDEOCONTROL](https://msdn.microsoft.com/library/windows/hardware/ff568120)">PROPSETID_VIDCAP_VIDEOCONTROL</a>, and any other custom property sets.</p></td>
</tr>
</tbody>
</table>

## Minidriver's SRB\_GET\_DATA\_INTERSECTION handler

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Component</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Camera minidriver</p></td>
<td><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561656" data-raw-source="[&lt;strong&gt;KSDATAFORMAT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561656)"><strong>KSDATAFORMAT</strong></a> structure from a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561658" data-raw-source="[&lt;strong&gt;KSDATARANGE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561658)"><strong>KSDATARANGE</strong></a> structure.</p></td>
</tr>
<tr class="even">
<td><p>Camera minidriver</p></td>
<td><p>Check that the frame rate requested (<strong>VideoInfoHeader.AvgTimePerFrame</strong>) is within the upper and lower limits for the video format requested. If it exceeds the limits, the minidriver should correct the following values in pSrb-&gt;CommandData.IntersectInfo-&gt;Datarange: VideoInfoHeader.AvgTimePerFrame, VideoInfoHeader.dwBitRate.</p></td>
</tr>
</tbody>
</table>

## Minidriver's SRB\_OPEN\_STREAM handler

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Component</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Camera minidriver</p></td>
<td><p>Verify the video format.</p></td>
</tr>
<tr class="even">
<td><p>Camera minidriver</p></td>
<td><p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff568574" data-raw-source="[&lt;strong&gt;USBCAMD_AdapterReceivePacket&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568574)"><strong>USBCAMD_AdapterReceivePacket</strong></a>.</p></td>
</tr>
<tr class="odd">
<td><p>USBCAMD2</p></td>
<td><p>Save the video format accepted by the camera minidriver.</p></td>
</tr>
<tr class="even">
<td><p>USBCAMD2</p></td>
<td><p>Call the minidriver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff557600" data-raw-source="[&lt;em&gt;CamAllocateBandwidthEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557600)"><em>CamAllocateBandwidthEx</em></a> callback function to allocate bandwidth based on video-format data and get the maximum buffer size for the video format.</p></td>
</tr>
<tr class="odd">
<td><p>Camera minidriver</p></td>
<td><p>Calculate the isochronous channel&#39;s maximum packet size that satisfies the requested frame rate and output windows size.</p></td>
</tr>
<tr class="even">
<td><p>Camera minidriver</p></td>
<td><p>Choose the closest alternate setting by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff568625" data-raw-source="[&lt;strong&gt;USBCAMD_SelectAlternateInterface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568625)"><strong>USBCAMD_SelectAlternateInterface</strong></a>. The minidriver should provide USBCAMD2 with the maximum possible frame size that can be produced by the camera.</p></td>
</tr>
<tr class="odd">
<td><p>Camera minidriver</p></td>
<td><p>Set the hardware scaling on the camera. Set the camera controls to the stored values in the registry, or to the default setting if the first time.</p></td>
</tr>
<tr class="even">
<td><p>Camera minidriver</p></td>
<td><p>Ensure that the frame rate (VideoInfoHeader.AvgTimePerFrame) falls within the limits for the video format, and correct it if it does not.</p></td>
</tr>
<tr class="odd">
<td><p>USBCAMD2</p></td>
<td><p>Call the minidriver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff557640" data-raw-source="[&lt;em&gt;CamStartCaptureEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557640)"><em>CamStartCaptureEx</em></a> callback function.</p></td>
</tr>
<tr class="even">
<td><p>Camera minidriver</p></td>
<td><p>Set the hardware to capture mode.</p></td>
</tr>
<tr class="odd">
<td><p>USBCAMD2</p></td>
<td><p>Initialize isochronous or bulk transfer.</p></td>
</tr>
</tbody>
</table>

## Minidriver's SRB\_CLOSE\_STREAM handler

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Component</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Camera minidriver</p></td>
<td><p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff568574" data-raw-source="[&lt;strong&gt;USBCAMD_AdapterReceivePacket&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568574)"><strong>USBCAMD_AdapterReceivePacket</strong></a>.</p></td>
</tr>
<tr class="even">
<td><p>USBCAMD2</p></td>
<td><p>Cancel pending IRPs submitted to USBCAMD2. Return any pending data SRBs to the <em>stream.sys</em> class driver.</p></td>
</tr>
<tr class="odd">
<td><p>USBCAMD2</p></td>
<td><p>Call the minidriver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff557643" data-raw-source="[&lt;em&gt;CamStopCaptureEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557643)"><em>CamStopCaptureEx</em></a> callback function.</p></td>
</tr>
<tr class="even">
<td><p>Camera minidriver</p></td>
<td><p>Send a stop-capture command to the camera.</p></td>
</tr>
<tr class="odd">
<td><p>USBCAMD2</p></td>
<td><p>Call the minidriver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff557613" data-raw-source="[&lt;em&gt;CamFreeBandwidthEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557613)"><em>CamFreeBandwidthEx</em></a> callback function to free isochronous bus bandwidth, if applicable.</p></td>
</tr>
<tr class="even">
<td><p>Camera minidriver</p></td>
<td><p>Select an idle alternate setting.</p></td>
</tr>
<tr class="odd">
<td><p>USBCAMD2</p></td>
<td><p>Free resources associated with USB pipes.</p></td>
</tr>
</tbody>
</table>

## Minidriver's SRB\_UNINITIALIZE\_DEVICE handler

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Component</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Camera minidriver</p></td>
<td><p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff568574" data-raw-source="[&lt;strong&gt;USBCAMD_AdapterReceivePacket&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568574)"><strong>USBCAMD_AdapterReceivePacket</strong></a>.</p></td>
</tr>
<tr class="even">
<td><p>USBCAMD2</p></td>
<td><p>If any streams are still open, close them by calling the minidriver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff557643" data-raw-source="[&lt;em&gt;CamStopCaptureEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557643)"><em>CamStopCaptureEx</em></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff557613" data-raw-source="[&lt;em&gt;CamFreeBandwidthEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557613)"><em>CamFreeBandwidthEx</em></a> callback functions for each stream.</p></td>
</tr>
<tr class="odd">
<td><p>USBCAMD2</p></td>
<td><p>Call the minidriver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff557646" data-raw-source="[&lt;em&gt;CamUnInitialize&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557646)"><em>CamUnInitialize</em></a> callback function.</p></td>
</tr>
<tr class="even">
<td><p>Camera minidriver</p></td>
<td><p>Clean up and free resources.</p></td>
</tr>
</tbody>
</table>

## Minidriver's SRB\_SURPRISE\_REMOVAL handler

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Component</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Camera minidriver</p></td>
<td><p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff568574" data-raw-source="[&lt;strong&gt;USBCAMD_AdapterReceivePacket&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568574)"><strong>USBCAMD_AdapterReceivePacket</strong></a>.</p></td>
</tr>
<tr class="even">
<td><p>USBCAMD2</p></td>
<td><p>Cancel pending data SRBs and return the SRBs with STATUS_CANCELLED.</p></td>
</tr>
<tr class="odd">
<td><p>USBCAMD2</p></td>
<td><p>Call the minidriver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff557643" data-raw-source="[&lt;em&gt;CamStopCaptureEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557643)"><em>CamStopCaptureEx</em></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff557613" data-raw-source="[&lt;em&gt;CamFreeBandwidthEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557613)"><em>CamFreeBandwidthEx</em></a> callback functions on all opened streams.</p></td>
</tr>
<tr class="even">
<td><p>USBCAMD2</p></td>
<td><p>Return STATUS_CANCELLED on any read/write SRBs that come down after SRB_SURPRISE_REMOVAL.</p></td>
</tr>
</tbody>
</table>

## Minidriver's SRB\_SET\_DATA\_FORMAT handler

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Component</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Camera minidriver</p></td>
<td><p>Verify the new video format.</p></td>
</tr>
<tr class="even">
<td><p>Camera minidriver</p></td>
<td><p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff568634" data-raw-source="[&lt;em&gt;USBCAMD_SetVideoFormat&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568634)"><em>USBCAMD_SetVideoFormat</em></a>.</p></td>
</tr>
<tr class="odd">
<td><p>USBCAMD2</p></td>
<td><p>Save the new format with the associated stream extension.</p></td>
</tr>
</tbody>
</table>

## Minidriver's SRB\_CHANGE\_POWER\_STATE from Power ON to Power OFF handler

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Component</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Camera minidriver</p></td>
<td><p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff568574" data-raw-source="[&lt;strong&gt;USBCAMD_AdapterReceivePacket&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568574)"><strong>USBCAMD_AdapterReceivePacket</strong></a>.</p></td>
</tr>
<tr class="even">
<td><p>USBCAMD2</p></td>
<td><p>Stop streaming on isochronous pipe if applicable, or cancel pending bulk or interrupt transfers.</p></td>
</tr>
<tr class="odd">
<td><p>USBCAMD2</p></td>
<td><p>Call the minidriver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff557643" data-raw-source="[&lt;em&gt;CamStopCaptureEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557643)"><em>CamStopCaptureEx</em></a> callback function.</p></td>
</tr>
<tr class="even">
<td><p>Camera minidriver</p></td>
<td><p>Send stop capture command to hardware.</p></td>
</tr>
</tbody>
</table>

## Minidriver's SRB\_CHANGE\_POWER\_STATE from Power OFF to Power ON handler

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Component</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Camera minidriver</p></td>
<td><p>Call <a href="https://msdn.microsoft.com/library/windows/hardware/ff568574" data-raw-source="[&lt;strong&gt;USBCAMD_AdapterReceivePacket&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568574)"><strong>USBCAMD_AdapterReceivePacket</strong></a>.</p></td>
</tr>
<tr class="even">
<td><p>USBCAMD2</p></td>
<td><p>Restart streaming on isochronous pipe if applicable, or resubmit bulk or interrupt transfer to USB class.</p></td>
</tr>
<tr class="odd">
<td><p>Camera minidriver</p></td>
<td><p>Restore camera settings and camera power consumption to normal levels.</p></td>
</tr>
<tr class="even">
<td><p>USBCAMD2</p></td>
<td><p>Call the minidriver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff557643" data-raw-source="[&lt;em&gt;CamStopCaptureEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557643)"><em>CamStopCaptureEx</em></a> callback function.</p></td>
</tr>
<tr class="odd">
<td><p>USBCAMD2</p></td>
<td><p>Call the minidriver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff557640" data-raw-source="[&lt;em&gt;CamStartCaptureEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557640)"><em>CamStartCaptureEx</em></a> callback function.</p></td>
</tr>
</tbody>
</table>
