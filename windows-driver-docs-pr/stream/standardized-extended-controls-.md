---
title: Extended camera controls
description: Extended controls use the KSPROPERTY mechanism to expose camera controls to the application.
ms.assetid: B480C007-7DCA-4CFB-9169-BE2D0B2D2137
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Extended camera controls


Extended controls use the **KSPROPERTY** mechanism to expose camera controls to the application.

The following list of standardized extended controls (defined by Media Foundation) enable additional Windows camera features:

-   [Metadata](#metadata)
-   [Focus priority](#focus-priority)
-   [Focus state](#focus-state)
-   [Extended region of interest (ROI)](#extended-region-of-interest-roi)
-   [Photo confirmation](#photo-confirmation)
-   [Photo sequence submode](#photo-sequence-submode)
-   [Photo capture feedback applied device settings](#photo-capture-feedback-applied-device-settings)
-   [Integer ISO](#integer-iso)
-   [Advanced focus](#advanced-focus)
-   [Flash](#flash)
-   [Zoom](#zoom)
-   [Scene mode](#scene-mode)

Some of the controls are exposed to applications as asynchronous controls and others are exposed as synchronous controls.

-   **Synchronous controls** – For these controls, the capture pipeline issues a **KSPROPERTY** camera control structure and expects the driver to synchronously return the request.

-   **Asynchronous controls** – For these controls, the capture pipeline issues a **KSPROPERTY**, enables a **KSEVENT** associated with that property, and waits on the event to get signaled. The driver must complete the **KSPROPERTY** synchronously and use that as a trigger to start the asynchronous operation. Upon the completion of the asynchronous operation, the driver must signal the associated **KSEVENT** on which the capture pipeline is waiting on. The capture pipeline notifies the application about the completion of the operation when it receives the signal.

    If an asynchronous control can be cancelled, it must specify the flag **KSCAMERA\_EXTENDEDPROP\_FLAG\_CANCELOPERATION** in the control. If the control cannot be cancelled, the control's operation must not exceed 5 ms.

These extended controls are part of the following KS property set defined in ksmedia.h:

```cpp
#define STATIC_KSPROPERTYSETID_ExtendedCameraControl \
     0x1CB79112, 0xC0D2, 0x4213, 0x9C, 0xA6, 0xCD, 0x4F, 0xDB, 0x92, 0x79, 0x72
DEFINE_GUIDSTRUCT("1CB79112-C0D2-4213-9CA6-CD4FDB927972", KSPROPERTYSETID_ExtendedCameraControl);
#define KSPROPERTYSETID_ExtendedCameraControl DEFINE_GUIDNAMED(KSPROPERTYSETID_ExtendedCameraControl);
```

## Metadata


To retrieve metadata, the user mode component (DevProxy) must query the driver for the metadata buffer requirement. Once the user mode component has this information, it allocates the appropriate metadata buffer for the driver to fill and return back to the user mode component.

The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_METADATA**](https://msdn.microsoft.com/library/windows/hardware/dn917952) property ID that is defined in the [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/dn917962) enumeration is used by the client to query for the metadata buffer requirements, such as required metadata size, memory alignment requirements, and desired memory allocation type, for metadata buffer allocation.

Once user mode component has obtained the metadata buffer requirements from the driver, it allocates the appropriately sized metadata buffer with the desired memory alignment from the desired memory pool. This metadata buffer, along with the actual frame buffer, will be sent to the driver to fulfill and then returned back to the user mode component when filled. For multishot scenarios, a corresponding metadata buffer is allocated and delivered to the camera driver for each frame buffer allocated.

The [**KSSTREAM\_METADATA\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn936959) structure, along with the following flag, is used to send the metadata buffer to the driver.

```cpp
#define KSSTREAM_HEADER_OPTIONSF_METADATA           0x00001000
```

Once the buffer (metadata + frame) is queued to the driver, DevProxy sends a standard [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138) structure, followed by a [**KS\_FRAME\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567645) structure, and followed by a **KSSTREAM\_METADATA\_INFO** structure. DevProxy will further mask **KSSTREAM\_HEADER.OptionFlags** with **KSSTREAM\_HEADER\_OPTIONSF\_METADATA** before it passes the buffer down to the driver.

If the driver does not support metadata, or if **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_METADATA** is not implemented, the **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_METADATA** property control will fail. In this case, DevProxy will not allocate a metadata buffer and the payload that is passed down to the driver from DevProxy will not contain the **KSSTREAM\_METADATA\_INFO** structure.

If the driver supports metadata and the client does not want any metadata, DevProxy will neither allocate metadata buffer nor pass down **KSSTREAM\_METADATA\_INFO** when sending the buffer to the driver. This behavior reduces the unnecessary metadata memory allocation if an app does not want metadata on a given pin.

The following structures describe the layout of the metadata items to be filled by the camera driver in the metadata buffer.

-   [**KSCAMERA\_MetadataId**](https://msdn.microsoft.com/library/windows/hardware/dn925181)

-   [**KSCAMERA\_METADATA\_ITEMHEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925184)

-   [**KSCAMERA\_METADATA\_PHOTOCONFIRMATION**](https://msdn.microsoft.com/library/windows/hardware/dn925187)

The list below contains the layout of a metadata item. This must be 8-byte aligned.

-   [**KSCAMERA\_METADATA\_ITEMHEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925184)

-   Metadata

The photo confirmation metadata is identified by **MetadataId\_PhotoConfirmation**. When present, it indicates that the preview frame associated is a photo confirmation frame. Photo confirmation metadata is parsed by the DevProxy.

The custom metadata is identified by a **MetadataId** that starts from **MetadataId\_Custom\_Start**. The custom metadata item can contain a blob of metadata that can be a focus state and/or faces detected for the preview pin, EXIF and/or the OEM metadata for an image pin. The exact format of the custom blob is determined by the OEM who implements the driver and MFT0. The MFT0 is responsible for parsing the custom blob and attaching each metadata item as an attribute grouped under the **MFSampleExtension\_CaptureMetadata** attribute bag in a format that is readable by the MF capture pipeline and/or WinRT.

The following IMFAttributes are defined in **mfapi.h**. These are required by the MF capture pipeline and/or WinRT. Note that MFT0 does not set any IMFAttributes for photo confirmation since the photo confirmation frame will not flow beyond DevProxy.

| Attribute (GUID)                            | Data type |
|---------------------------------------------|-----------|
| **MF\_CAPTURE\_METADATA\_FOCUSSTATE**       | UINT32    |
| **MF\_CAPTURE\_METADATA\_FACEROIS**         | Blob      |
| **MF\_CAPTURE\_METADATA\_FRAME\_RAWSTREAM** | IUnknown  |

 

The **MF\_CAPTURE\_METADATA\_FRAME\_RAWSTREAM** IMFAttributes are created and attached to **MFSampleExtension\_CaptureMetadata** by the DevProxy, which contains a pointer to the IMFMediaBuffer interface associated with the raw metadata buffer (**KSSTREAM\_METADATA\_INFO.Data**). When the MFT0 receives an IMFSample, it gets the raw metadata buffer from the **MF\_CAPTURE\_METADATA\_FRAME\_RAWSTREAM** and parses any additional custom metadata items such as focus state and converts them into corresponding IMFAttributes defined above and attaches them to the **MFSampleExtension\_CaptureMetadata** attribute bag.

To access the raw metadata buffer, the MFT0 does the following:

1.  Calls **GetUnknown** on **MFSampleExtension\_CaptureMetadata** from the IMFSample interface to get the IMFAttributes interface for the attribute bag.

2.  Calls **GetUnknown** on **MF\_CAPTURE\_METADATA\_FRAME\_RAWSTREAM** from the IMFAttributes interface obtained from the previous step to get the IMFMediaBuffer interface.

3.  Calls Lock to get the raw metadata buffer associated with IMFMediaBuffer.

To add the required IMFAttributes to the **MFSampleExtension\_CaptureMetadata** attribute bag, the MFT0 does the following:

1.  Calls **GetUnknown** on **MFSampleExtension\_CaptureMetadata** from the IMFSample interface to get the IMFAttributes interface for the attribute bag.

2.  Calls **SetUINT32**, **SetBlob**, or **SetUnknown** on **MF\_CAPTURE\_METADATA\_XXX** from the IMFAttributes interface obtained from the previous step based on the GUID and data type specified in the table above.

## Focus priority


The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSPRIORITY**](https://msdn.microsoft.com/library/windows/hardware/dn917942) property ID is the only control that is associated with the focus priority DDI.

## Focus state


The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSSTATE**](https://msdn.microsoft.com/library/windows/hardware/dn917944) property ID is the only control that is associated with the focus state DDI.

## Extended region of interest ROI


The following property IDs are the controls that are associated with the ROI DDI:

-   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_CONFIGCAPS**](https://msdn.microsoft.com/library/windows/hardware/dn917964)

-   [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_ISPCONTROL**](https://msdn.microsoft.com/library/windows/hardware/dn917966)

## Photo confirmation


The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOCONFIRMATION**](https://msdn.microsoft.com/library/windows/hardware/dn917957) property ID is the only control that is associated with the photo confirmation DDI.

## Photo sequence submode


The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567582) property ID is the only control associated with the photo sequence DDI.

## Photo capture feedback applied device settings


The MFT0 parses the metadata buffer provided by the driver and attaches the required applied device settings IMFAttributes to the **MFSampleExtension\_CaptureMetadata** attribute bag associated with each IMFSample. The following IMFAttributes must be carried over by the MF pipeline and any third-party supplied MFTs:

| Name                                           | Type                          |
|------------------------------------------------|-------------------------------|
| **MFSampleExtension\_CaptureMetadata**         | **IUnknown** (IMFAttributes)  |
| **MFSampleExtension\_EOS**                     | **UINT32** (Boolean)          |
| **MFSampleExtension\_PhotoThumbnail**          | **IUnknown** (IMFMediaBuffer) |
| **MFSampleExtension\_PhotoThumbnailMediaType** | **IUnknown** (IMFMediaType)   |

 

**Mandatory metadata attributes**

**MFSampleExtension\_CaptureMetaData** is a metadata attribute bag that can have the following attributes:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>MF_CAPTURE_METADATA_REQUESTED_FRAME_SETTING_ID</strong></td>
<td><strong>UINT32</strong></td>
<td>This attribute contains the frame ID for the corresponding frame in the variable photo sequence. This attribute is only set for a variable photo sequence capture.</td>
</tr>
<tr class="even">
<td><strong>MF_CAPTURE_METADATA_EXPOSURE_TIME</strong></td>
<td><strong>UINT64</strong></td>
<td>This attribute contains the exposure time applied in 100 nanoseconds.</td>
</tr>
<tr class="odd">
<td><strong>MF_CAPTURE_METADATA_EXPOSURE_COMPENSATION</strong></td>
<td><strong>Blob</strong></td>
<td>This attribute contains an EV compensation step flag and an EV compensation value in units of the step that was applied to the driver when the photo was captured. The <a href="https://msdn.microsoft.com/library/windows/hardware/dn897242" data-raw-source="[&lt;strong&gt;CapturedMetadataExposureCompensation&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn897242)"><strong>CapturedMetadataExposureCompensation</strong></a> data structure describes the blob format for this attribute only. The metadata item structure format for EV compensation (<strong>KSCAMERA_METADATA_ITEMHEADER</strong> + EV compensation metadata payload) is provided by the driver and must be 8 byte aligned.</td>
</tr>
<tr class="even">
<td><strong>MF_CAPTURE_METADATA_ISO_SPEED</strong></td>
<td><strong>UINT32</strong></td>
<td>This attribute contains the ISO speed value applied as an integer.</td>
</tr>
<tr class="odd">
<td><strong>MF_CAPTURE_METADATA_LENS_POSITION</strong></td>
<td><strong>UINT32</strong></td>
<td>This attribute contains the logical lens position when focus was applied to the photo captured. This value does not have a specific unit.</td>
</tr>
<tr class="even">
<td><strong>MF_CAPTURE_METADATA_SCENE_MODE</strong></td>
<td><strong>UINT64</strong></td>
<td>This attribute contains the scene mode applied as a <strong>UINT64KSCAMERA_EXTENDEDPROP_SCENEMODE_XXX</strong> flag.</td>
</tr>
<tr class="odd">
<td><strong>MF_CAPTURE_METADATA_FLASH</strong></td>
<td><p><strong>UINT32</strong></p>
<p>(Boolean)</p></td>
<td>This attribute contains a Boolean value that contains the flash state. A value of 1 specifies that the flash is on and a value of 0 specifies that the flash is off for the photo captured.</td>
</tr>
<tr class="even">
<td><strong>MF_CAPTURE_METADATA_FLASH_POWER</strong></td>
<td><p><strong>UINT32</strong></p></td>
<td>This attribute contains the flash power applied as a percentage value between 0 and 100.</td>
</tr>
<tr class="odd">
<td><strong>MF_CAPTURE_METADATA_WHITEBALANCE</strong></td>
<td><p><strong>UINT32</strong></p>
<p>(Kelvin)</p></td>
<td>This attribute contains the white balance applied as a value in kelvin.</td>
</tr>
<tr class="even">
<td><strong>MF_CAPTURE_METADATA_ZOOMFACTOR</strong></td>
<td><p><strong>UINT32</strong></p>
<p>(Q16)</p></td>
<td>This attribute contains the zoom value applied and is the same value that can be queried from <a href="https://msdn.microsoft.com/library/windows/hardware/dn936756" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_EXTENDED_ZOOM&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn936756)"><strong>KSPROPERTY_CAMERACONTROL_EXTENDED_ZOOM</strong></a> in a GET call. The value must be in Q16.</td>
</tr>
<tr class="odd">
<td><strong>MF_CAPTURE_METADATA_FRAME_ILLUMINATION</strong></td>
<td><strong>UINT64</strong></td>
<td><p>The <strong>MF_CAPTURE_METADATA_FRAME_ILLUMINATION</strong> attribute for IR cameras specifies whether the frames are using active IR illumination and should be used in conjunction with <strong>FACEAUTH_MODE_ALTERNATIVE_FRAME_ILLUMINATION</strong>. It is only used for IR samples and should not be present on RGB frames if the camera supports both IR and color samples.</p>
<p>The value should be set to 0xXXXXXXXXXXXXXXX1 if the frame was captured when active illumination was on and set to 0xXXXXXXXXXXXXXXX0 if no illumination was present when capturing the frame.</p></td>
</tr>
<tr class="even">
<td>Any Custom GUID</td>
<td>Any variant type</td>
<td>This attribute contains the custom data associated with the custom GUID.</td>
</tr>
</tbody>
</table>

 

**EXIF and HW JPEG encoder**

The pipeline is not required to process or warp any EXIF data for the HW JPEG encoder; therefore, the EXIF data format is provided by the driver, MFT0, and OEM HW JPEG encoder. OEMs partners can define any custom attribute GUID and variant type for the EXIF attribute and attach it to the **MFSampleExtension\_CaptureMetaData** attribute bag for it to be consumed by the OEM components. If a HW JPEG encoder is available, the pipeline photo sink component will load the HW JPEG encoder and set the EXIF data held in the **MFSampleExtension\_CaptureMetaData** attribute bag onto the HW JPEG encoder as an EXIF encoder option using the [IPropertyBag2::Write](http://go.microsoft.com/fwlink/?LinkId=331589) method.

The encoder option property bag contains an array of PROPBAG2 structures that specify the available encoding option properties. The EXIF encoder option set onto HW JPEG encoder is identified by the following property in the encoder option property bag:

| Property name      | VARTYPE         | Value                                                                                                                                                       | Applicable codecs |
|--------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| **SampleMetaData** | **VT\_UNKNOWN** | Pointer to an IMFAttributes interface for **MFSampleExtension\_CaptureMetaData** attribute bag that contains an OEM sub attribute containing the EXIF data. | JPEG              |

 

The **MFSampleExtension\_CaptureMetaData** attribute bag can only contain any OEM defined EXIF sub attribute that the MFT0 and HW JPEG encoder can read to hold the EXIF data. To pass EXIF data from the driver to the HW JPEG encoder, the driver and MFT0 must do the following:

1.  The driver provides custom EXIF metadata in the metadata buffer supplied by the pipeline. This is attached to **MFSampleExtension\_CaptureMetadata** as an **MF\_CAPTURE\_METADATA\_FRAME\_RAWSTREAM** IMFAttribute by DevProxy when the sample is returned back to DevProxy.

2.  When the MFT0 receives an IMFSample, it gets the raw metadata buffer from **MF\_CAPTURE\_METADATA\_FRAME\_RAWSTREAM** and parses the custom EXIF metadata item and converts it to an OEM defined IMFAttribute and attaches it to the **MFSampleExtension\_CaptureMetadata** attribute bag.

To pass EXIF data from the MFT0 to the HW JPEG encoder, the pipeline photo sink does the following:

1.  Calls **GetUnknown** on **MFSampleExtension\_CaptureMetadata** from IMFSample to get the IMFAttributes interface for the attribute bag when IMFSample is received.

2.  Calls [IPropertyBag2::Write](http://go.microsoft.com/fwlink/?LinkId=331589) to set the encoder option property, identified by SampleMetadata, to the HW JPEG encoder. The encoder option property contains the IMFAttributes interface obtained from the previous step. This interface contains all custom sub attributes including the OEM EXIF sub attribute, and the standardized sub attributes in the **Metadata** section discussed earlier in this topic.

To retrieve the EXIF data for further processing, the HW JPEG encoder does the following:

1.  Calls **IPropertyBag2::Read** to retrieve the property value for the property identified by the SampleMetadata property name and **VT\_UNKNOWN** type. When returned, the **VARIANT.punkVal** receives the IMFAttributes interface for **MFSampleExtension\_CaptureMetadata**.

2.  Calls **GetBlob** or **GetUnknown** on the OEM EXIF sub attribute from the interface obtained from the previous step to get the EXIF data blob based on the GUID and data type of the OEM EXIF sub attribute.

**Thumbnail**

MFT0 is not required to produce any thumbnail for the camera driver. The camera app is expected to generate its own thumbnail. The thumbnail could be produced from the photo confirmation image, HW JPEG encoder, or resizing a full size image. This is up to the app developers. To maintain API and app compatibility with Windows 8.1 apps, the camera driver must not implement the **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOTHUMBNAIL** control.

## Integer ISO


The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO\_ADVANCED**](https://msdn.microsoft.com/library/windows/hardware/dn917947) property ID is the only control associated with the integer ISO DDI.

## Advanced focus


The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567576) property ID is the only control associated with the integer ISO DDI.

## Flash


The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567575) property ID is the only control that is associated with the flash DDI.

## Zoom


The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ZOOM**](https://msdn.microsoft.com/library/windows/hardware/dn936756) property ID is the only control that is associated with the zoom DDI.

## Scene mode


The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567585) property ID is the only control associated with the scene mode DDI.

 

 




