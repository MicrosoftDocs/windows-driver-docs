---
title: Extended Camera Control Properties
ms.assetid: 27D94D73-D190-4C01-B082-7798CA71EDB4
description: The extended camera control interface is used to control camera features during image capture.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Extended Camera Control Properties


The extended camera control interface, available starting in Windows 8, is used to control camera features during image capture. The driver can control these camera features:

-   the camera's flash
-   whether image pin and record pin are mutually exclusive
-   the region of interest in the image
-   video stabilization

The driver can also choose to perform a camera control operation asynchronously, meaning that all requests for an operation are rejected until the first request is completed. If the driver has successfully performed asynchronous camera control operations, it should trigger the [**KSEVENTSETID\_CameraAsyncControl**](https://msdn.microsoft.com/library/windows/hardware/jj714740) event. See [**KSPROPERTY\_CAMERACONTROL\_S\_EX**](https://msdn.microsoft.com/library/windows/hardware/jj151593) for more information.

UWP apps can access these properties to configure the camera:

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
<td><p><a href="" id="ksproperty-cameracontrol-extended-photomode"></a><a href="https://msdn.microsoft.com/library/windows/hardware/dn567582" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567582)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMODE</strong></a></p></td>
<td><p>Used to get or set a normal still or photo sequence mode for the camera.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-photoframerate"></a><a href="https://msdn.microsoft.com/library/windows/hardware/dn567580" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOFRAMERATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567580)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOFRAMERATE</strong></a></p></td>
<td><p>Used to get the current photo capture frame rate when the photo mode for the camera is sequence mode.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-photomaxframerate"></a><a href="https://msdn.microsoft.com/library/windows/hardware/dn567581" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMAXFRAMERATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567581)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMAXFRAMERATE</strong></a></p></td>
<td><p>Used to get or set maximum capture frame rate for a camera when it is in photo sequence mode.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-phototriggertime"></a><a href="https://msdn.microsoft.com/library/windows/hardware/dn567584" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOTRIGGERTIME&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567584)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOTRIGGERTIME</strong></a></p></td>
<td><p>Used to get or set the trigger time for the camera driver.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-warmstart"></a><a href="https://msdn.microsoft.com/library/windows/hardware/dn567587" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_WARMSTART&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567587)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_WARMSTART</strong></a></p></td>
<td><p>Used to get or set the warm start (camera ready) state.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-maxvidfps-photores"></a><a href="https://msdn.microsoft.com/library/windows/hardware/dn567578" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_MAXVIDFPS_PHOTORES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567578)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_MAXVIDFPS_PHOTORES</strong></a></p></td>
<td><p>Used to get or set the maximum possible frame rate possible on the video capture pins at a certain resolution.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-photothumbnail"></a><a href="https://msdn.microsoft.com/library/windows/hardware/dn567583" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOTHUMBNAIL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567583)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOTHUMBNAIL</strong></a></p></td>
<td><p>Used to get or set the thumbnail capability for the camera.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-scenemode"></a><a href="https://msdn.microsoft.com/library/windows/hardware/dn567585" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_SCENEMODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567585)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_SCENEMODE</strong></a></p></td>
<td><p>Used to get or set a driver defined mode which represents a collection of preset controls.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-torchmode"></a><a href="https://msdn.microsoft.com/library/windows/hardware/dn567586" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_TORCHMODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567586)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_TORCHMODE</strong></a></p></td>
<td><p>Used to get or set the method a camera’s flash is used in low light conditions.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-flashmode"></a><a href="https://msdn.microsoft.com/library/windows/hardware/dn567575" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_FLASHMODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567575)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_FLASHMODE</strong></a></p></td>
<td><p>Used to get or set the flash mode operation for both normal and sequence photo mode of the camera.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-optimizationhint"></a><a href="https://msdn.microsoft.com/library/windows/hardware/dn567579" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_OPTIMIZATIONHINT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567579)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_OPTIMIZATIONHINT</strong></a></p></td>
<td><p>Used to get or set whether auto processing occurs for white balance or for a manual temperature value.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-whitebalancemode"></a><a href="https://msdn.microsoft.com/library/windows/hardware/dn567588" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_WHITEBALANCEMODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567588)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_WHITEBALANCEMODE</strong></a></p></td>
<td><p>Used to get or set whether the camera is optimized for photo or video operation.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-exposuremode"></a><a href="https://msdn.microsoft.com/library/windows/hardware/dn567573" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_EXPOSUREMODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567573)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_EXPOSUREMODE</strong></a></p></td>
<td><p>Used to get or set whether auto processing occurs for exposure or a manual time value is used.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-focusmode"></a><a href="https://msdn.microsoft.com/library/windows/hardware/dn567576" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSMODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567576)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSMODE</strong></a></p></td>
<td><p>Used to get or set the auto, manual, and preset focus modes of the camera.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-iso"></a><a href="https://msdn.microsoft.com/library/windows/hardware/dn567577" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_ISO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567577)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_ISO</strong></a></p></td>
<td><p>Used to get or set the preset or automatic ISO setting for the camera.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-fieldofview"></a><a href="https://msdn.microsoft.com/library/windows/hardware/dn567574" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567574)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW</strong></a></p></td>
<td><p>Used to get the field of view and pitch angle of the camera position.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-evcompensation"></a><a href="https://msdn.microsoft.com/library/windows/hardware/dn567572" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_EVCOMPENSATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567572)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_EVCOMPENSATION</strong></a></p></td>
<td><p>Used to get or set the exposure control adjustment setting.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-cameraangleoffset"></a><a href="https://msdn.microsoft.com/library/windows/hardware/dn567571" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_CAMERAANGLEOFFSET&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn567571)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_CAMERAANGLEOFFSET</strong></a></p></td>
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
-   [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)
-   [**KSCAMERA\_EXTENDEDPROP\_VALUE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value)
-   [**KSCAMERA\_EXTENDEDPROP\_PHOTOMODE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_photomode)
-   [**KSCAMERA\_MAXVIDEOFPS\_FORPHOTORES**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_maxvideofps_forphotores)
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

 

 




