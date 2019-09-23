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

The driver can also choose to perform a camera control operation asynchronously, meaning that all requests for an operation are rejected until the first request is completed. If the driver has successfully performed asynchronous camera control operations, it should trigger the [**KSEVENTSETID\_CameraAsyncControl**](https://docs.microsoft.com/windows-hardware/drivers/stream/kseventsetid-cameraasynccontrol) event. See [**KSPROPERTY\_CAMERACONTROL\_S\_EX**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s_ex) for more information.

UWP apps can access these properties to configure the camera:

## Properties


<a href="" id="ksproperty-cameracontrol-flash-property"></a>[**KSPROPERTY\_CAMERACONTROL\_FLASH\_PROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-flash-property)  
Used to turn the camera's flash on or off, or to put the flash into automatic mode.

<a href="" id="ksproperty-cameracontrol-image-pin-capability-property"></a>[**KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_PROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-image-pin-capability-property)  
Used to identify whether the camera's image pin and record pin are mutually exclusive.

<a href="" id="ksproperty-cameracontrol-region-of-interest-property"></a>[**KSPROPERTY\_CAMERACONTROL\_REGION\_OF\_INTEREST\_PROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-region-of-interest-property)  
Used to get or set the characteristic of a camera's region of interest.

<a href="" id="ksproperty-cameracontrol-video-stabilization-mode-property"></a>[**KSPROPERTY\_CAMERACONTROL\_VIDEO\_STABILIZATION\_MODE\_PROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-video-stabilization-mode-property)  
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
<td><p><a href="" id="ksproperty-cameracontrol-extended-photomode"></a><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-photomode" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMODE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-photomode)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMODE</strong></a></p></td>
<td><p>Used to get or set a normal still or photo sequence mode for the camera.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-photoframerate"></a><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-photoframerate" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOFRAMERATE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-photoframerate)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOFRAMERATE</strong></a></p></td>
<td><p>Used to get the current photo capture frame rate when the photo mode for the camera is sequence mode.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-photomaxframerate"></a><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-photomaxframerate" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMAXFRAMERATE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-photomaxframerate)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOMAXFRAMERATE</strong></a></p></td>
<td><p>Used to get or set maximum capture frame rate for a camera when it is in photo sequence mode.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-phototriggertime"></a><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-phototriggertime" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOTRIGGERTIME&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-phototriggertime)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOTRIGGERTIME</strong></a></p></td>
<td><p>Used to get or set the trigger time for the camera driver.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-warmstart"></a><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-warmstart" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_WARMSTART&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-warmstart)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_WARMSTART</strong></a></p></td>
<td><p>Used to get or set the warm start (camera ready) state.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-maxvidfps-photores"></a><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-maxvidfps-photores" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_MAXVIDFPS_PHOTORES&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-maxvidfps-photores)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_MAXVIDFPS_PHOTORES</strong></a></p></td>
<td><p>Used to get or set the maximum possible frame rate possible on the video capture pins at a certain resolution.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-photothumbnail"></a><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-photothumbnail" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOTHUMBNAIL&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-photothumbnail)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOTHUMBNAIL</strong></a></p></td>
<td><p>Used to get or set the thumbnail capability for the camera.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-scenemode"></a><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-scenemode" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_SCENEMODE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-scenemode)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_SCENEMODE</strong></a></p></td>
<td><p>Used to get or set a driver defined mode which represents a collection of preset controls.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-torchmode"></a><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-torchmode" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_TORCHMODE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-torchmode)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_TORCHMODE</strong></a></p></td>
<td><p>Used to get or set the method a camera’s flash is used in low light conditions.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-flashmode"></a><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-flashmode" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_FLASHMODE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-flashmode)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_FLASHMODE</strong></a></p></td>
<td><p>Used to get or set the flash mode operation for both normal and sequence photo mode of the camera.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-optimizationhint"></a><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-optimizationhint" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_OPTIMIZATIONHINT&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-optimizationhint)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_OPTIMIZATIONHINT</strong></a></p></td>
<td><p>Used to get or set whether auto processing occurs for white balance or for a manual temperature value.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-whitebalancemode"></a><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-whitebalancemode" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_WHITEBALANCEMODE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-whitebalancemode)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_WHITEBALANCEMODE</strong></a></p></td>
<td><p>Used to get or set whether the camera is optimized for photo or video operation.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-exposuremode"></a><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-exposuremode" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_EXPOSUREMODE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-exposuremode)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_EXPOSUREMODE</strong></a></p></td>
<td><p>Used to get or set whether auto processing occurs for exposure or a manual time value is used.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-focusmode"></a><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-focusmode" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSMODE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-focusmode)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSMODE</strong></a></p></td>
<td><p>Used to get or set the auto, manual, and preset focus modes of the camera.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-iso"></a><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-iso" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_ISO&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-iso)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_ISO</strong></a></p></td>
<td><p>Used to get or set the preset or automatic ISO setting for the camera.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-fieldofview"></a><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-fieldofview" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-fieldofview)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_FIELDOFVIEW</strong></a></p></td>
<td><p>Used to get the field of view and pitch angle of the camera position.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="ksproperty-cameracontrol-extended-evcompensation"></a><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-evcompensation" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_EVCOMPENSATION&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-evcompensation)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_EVCOMPENSATION</strong></a></p></td>
<td><p>Used to get or set the exposure control adjustment setting.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="ksproperty-cameracontrol-extended-cameraangleoffset"></a><a href="https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-cameraangleoffset" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_CAMERAANGLEOFFSET&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-cameraangleoffset)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_CAMERAANGLEOFFSET</strong></a></p></td>
<td><p>Used to get the pitch and yaw angle of the camera position.</p></td>
</tr>
</tbody>
</table>

 

These structures and enumerations support the extended camera control interface:

## Structures


-   [**KSPROPERTY\_CAMERACONTROL\_S\_EX**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s_ex)
-   [**KSPROPERTY\_CAMERACONTROL\_FLASH\_S**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_cameracontrol_flash_s)
-   [**KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_S**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_cameracontrol_image_pin_capability_s)
-   [**KSPROPERTY\_CAMERACONTROL\_REGION\_OF\_INTEREST\_S**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_cameracontrol_region_of_interest_s)
-   [**KSPROPERTY\_CAMERACONTROL\_VIDEOSTABILIZATION\_MODE\_S**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_cameracontrol_videostabilization_mode_s)
-   [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)
-   [**KSCAMERA\_EXTENDEDPROP\_VALUE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value)
-   [**KSCAMERA\_EXTENDEDPROP\_PHOTOMODE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_photomode)
-   [**KSCAMERA\_MAXVIDEOFPS\_FORPHOTORES**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_maxvideofps_forphotores)
-   [**KSCAMERA\_EXTENDEDPROP\_VIDEOPROCSETTING**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_videoprocsetting)
-   [**KSCAMERA\_EXTENDEDPROP\_FIELDOFVIEW**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_fieldofview)

## Enumerations


-   [**KS\_CameraControlAsyncOperation**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ks_cameracontrolasyncoperation)
-   [**KSEVENT\_CAMERACONTROL**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ksevent_cameracontrol)
-   [**KSPROPERTY\_CAMERACONTROL\_FLASH**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ksproperty_cameracontrol_flash)
-   [**KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ksproperty_cameracontrol_image_pin_capability)
-   [**KSPROPERTY\_CAMERACONTROL\_REGION\_OF\_INTEREST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ksproperty_cameracontrol_region_of_interest)
-   [**KSPROPERTY\_CAMERACONTROL\_VIDEO\_STABILIZATION\_MODE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ksproperty_cameracontrol_video_stabilization_mode)

Example driver code that implements this interface is given in [How To Implement Extended Camera Control Properties](how-to-implement-extended-camera-control-properties.md).

 

 




