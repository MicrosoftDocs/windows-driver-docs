---
title: Extended Camera Control Properties
author: windows-driver-content
ms.assetid: 27D94D73-D190-4C01-B082-7798CA71EDB4
description: The extended camera control interface is used to control camera features during image capture.
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Extended Camera Control Properties


The extended camera control interface, available starting in Windows 8, is used to control camera features during image capture. The driver can control these camera features:

-   the camera's flash
-   whether image pin and record pin are mutually exclusive
-   the region of interest in the image
-   video stabilization

The driver can also choose to perform a camera control operation asynchronously, meaning that all requests for an operation are rejected until the first request is completed. If the driver has successfully performed asynchronous camera control operations, it should trigger the [**KSEVENTSETID\_CameraAsyncControl**](https://msdn.microsoft.com/library/windows/hardware/jj714740) event. See [**KSPROPERTY\_CAMERACONTROL\_S\_EX**](https://msdn.microsoft.com/library/windows/hardware/jj151593) for more information.

Windows Store apps can access these properties to configure the camera:

## Properties


<a href="" id="ksproperty-cameracontrol-flash-property"></a>[**KSPROPERTY\_CAMERACONTROL\_FLASH\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/jj156041)  
Used to turn the camera's flash on or off, or to put the flash into automatic mode.

<a href="" id="ksproperty-cameracontrol-image-pin-capability-property"></a>[**KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/jj553706)  
Used to identify whether the camera's image pin and record pin are mutually exclusive.

<a href="" id="ksproperty-cameracontrol-region-of-interest-property"></a>[**KSPROPERTY\_CAMERACONTROL\_REGION\_OF\_INTEREST\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/jj156042)  
Used to get or set the characteristic of a camera's region of interest.

<a href="" id="ksproperty-cameracontrol-video-stabilization-mode-property"></a>[**KSPROPERTY\_CAMERACONTROL\_VIDEO\_STABILIZATION\_MODE\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/jj156043)  
Used to get or set a camera's video stabilization characteristics.

The following properties are available starting with Windows 8.1.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-photomode"></a>[<strong>KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMODE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567582)</p></td>
<td><p>Used to get or set a normal still or photo sequence mode for the camera.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-photoframerate"></a>[<strong>KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOFRAMERATE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567580)</p></td>
<td><p>Used to get the current photo capture frame rate when the photo mode for the camera is sequence mode.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-photomaxframerate"></a>[<strong>KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMAXFRAMERATE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567581)</p></td>
<td><p>Used to get or set maximum capture frame rate for a camera when it is in photo sequence mode.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-phototriggertime"></a>[<strong>KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOTRIGGERTIME</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567584)</p></td>
<td><p>Used to get or set the trigger time for the camera driver.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-warmstart"></a>[<strong>KSPROPERTY_CAMERACONTROL_EXTENDED_WARMSTART</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567587)</p></td>
<td><p>Used to get or set the warm start (camera ready) state.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-maxvidfps-photores"></a>[<strong>KSPROPERTY_CAMERACONTROL_EXTENDED_MAXVIDFPS_PHOTORES</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567578)</p></td>
<td><p>Used to get or set the maximum possible frame rate possible on the video capture pins at a certain resolution.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-photothumbnail"></a>[<strong>KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOTHUMBNAIL</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567583)</p></td>
<td><p>Used to get or set the thumbnail capability for the camera.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-scenemode"></a>[<strong>KSPROPERTY_CAMERACONTROL_EXTENDED_SCENEMODE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567585)</p></td>
<td><p>Used to get or set a driver defined mode which represents a collection of preset controls.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-torchmode"></a>[<strong>KSPROPERTY_CAMERACONTROL_EXTENDED_TORCHMODE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567586)</p></td>
<td><p>Used to get or set the method a camera’s flash is used in low light conditions.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-flashmode"></a>[<strong>KSPROPERTY_CAMERACONTROL_EXTENDED_FLASHMODE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567575)</p></td>
<td><p>Used to get or set the flash mode operation for both normal and sequence photo mode of the camera.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-optimizationhint"></a>[<strong>KSPROPERTY_CAMERACONTROL_EXTENDED_OPTIMIZATIONHINT</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567579)</p></td>
<td><p>Used to get or set whether auto processing occurs for white balance or for a manual temperature value.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-whitebalancemode"></a>[<strong>KSPROPERTY_CAMERACONTROL_EXTENDED_WHITEBALANCEMODE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567588)</p></td>
<td><p>Used to get or set whether the camera is optimized for photo or video operation.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-exposuremode"></a>[<strong>KSPROPERTY_CAMERACONTROL_EXTENDED_EXPOSUREMODE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567573)</p></td>
<td><p>Used to get or set whether auto processing occurs for exposure or a manual time value is used.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-focusmode"></a>[<strong>KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSMODE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567576)</p></td>
<td><p>Used to get or set the auto, manual, and preset focus modes of the camera.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-iso"></a>[<strong>KSPROPERTY_CAMERACONTROL_EXTENDED_ISO</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567577)</p></td>
<td><p>Used to get or set the preset or automatic ISO setting for the camera.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-fieldofview"></a>[<strong>KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567574)</p></td>
<td><p>Used to get the field of view and pitch angle of the camera position.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-evcompensation"></a>[<strong>KSPROPERTY_CAMERACONTROL_EXTENDED_EVCOMPENSATION</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567572)</p></td>
<td><p>Used to get or set the exposure control adjustment setting.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-cameraangleoffset"></a>[<strong>KSPROPERTY_CAMERACONTROL_EXTENDED_CAMERAANGLEOFFSET</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567571)</p></td>
<td><p>Used to get the pitch and yaw angle of the camera position.</p></td>
</tr>
</tbody>
</table>

 

These structures and enumerations support the extended camera control interface:

## Structures


-   [**KSPROPERTY\_CAMERACONTROL\_S\_EX**](https://msdn.microsoft.com/library/windows/hardware/jj151593)
-   [**KSPROPERTY\_CAMERACONTROL\_FLASH\_S**](https://msdn.microsoft.com/library/windows/hardware/jj151590)
-   [**KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_S**](https://msdn.microsoft.com/library/windows/hardware/jj553707)
-   [**KSPROPERTY\_CAMERACONTROL\_REGION\_OF\_INTEREST\_S**](https://msdn.microsoft.com/library/windows/hardware/jj151592)
-   [**KSPROPERTY\_CAMERACONTROL\_VIDEOSTABILIZATION\_MODE\_S**](https://msdn.microsoft.com/library/windows/hardware/jj151594)
-   [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563)
-   [**KSCAMERA\_EXTENDEDPROP\_VALUE**](https://msdn.microsoft.com/library/windows/hardware/dn567565)
-   [**KSCAMERA\_EXTENDEDPROP\_PHOTOMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567564)
-   [**KSCAMERA\_MAXVIDEOFPS\_FORPHOTORES**](https://msdn.microsoft.com/library/windows/hardware/dn567567)
-   [**KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING**](https://msdn.microsoft.com/library/windows/hardware/dn567566)
-   [**KSCAMERA\_EXTENDEDPROP\_FIELDOFVIEW**](https://msdn.microsoft.com/library/windows/hardware/dn567562)

## Enumerations


-   [**KS\_CameraControlAsyncOperation**](https://msdn.microsoft.com/library/windows/hardware/jj151596)
-   [**KSEVENT\_CAMERACONTROL**](https://msdn.microsoft.com/library/windows/hardware/jj151587)
-   [**KSPROPERTY\_CAMERACONTROL\_FLASH**](https://msdn.microsoft.com/library/windows/hardware/jj151589)
-   [**KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY**](https://msdn.microsoft.com/library/windows/hardware/jj553705)
-   [**KSPROPERTY\_CAMERACONTROL\_REGION\_OF\_INTEREST**](https://msdn.microsoft.com/library/windows/hardware/jj151591)
-   [**KSPROPERTY\_CAMERACONTROL\_VIDEO\_STABILIZATION\_MODE**](https://msdn.microsoft.com/library/windows/hardware/jj151595)

Example driver code that implements this interface is given in [How To Implement Extended Camera Control Properties](how-to-implement-extended-camera-control-properties.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Extended%20Camera%20Control%20Properties%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


