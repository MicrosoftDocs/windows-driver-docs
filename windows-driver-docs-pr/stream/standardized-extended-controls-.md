---
title: Extended camera controls
description: Extended controls use the KSPROPERTY mechanism to expose camera controls to the application.
ms.date: 06/19/2020
---

# Extended camera controls

Extended controls use the **KSPROPERTY** mechanism to expose camera controls to the application.

The following list of standardized extended controls (defined by Media Foundation) enable additional Windows camera features:

- [Metadata](#metadata)

- [Focus priority](#focus-priority)

- [Focus state](#focus-state)

- [Extended region of interest (ROI)](#extended-region-of-interest-roi)

- [Photo confirmation](#photo-confirmation)

- [Photo sequence submode](#photo-sequence-submode)

- [EXIF and HW JPEG encoder](#exif-and-hw-jpeg-encoder)

- [Integer ISO](#integer-iso)

- [Advanced focus](#advanced-focus)

- [Flash](#flash)

- [Zoom](#zoom)

- [Scene mode](#scene-mode)

Some of the controls are exposed to applications as asynchronous controls and others are exposed as synchronous controls.

## Synchronous controls

For these controls, the capture pipeline issues a **KSPROPERTY** camera control structure and expects the driver to synchronously return the request.

## Asynchronous controls

For these controls, the capture pipeline issues a **KSPROPERTY**, enables a **KSEVENT** associated with that property, and waits on the event to get signaled. The driver must complete the **KSPROPERTY** synchronously and use that as a trigger to start the asynchronous operation. Upon the completion of the asynchronous operation, the driver must signal the associated **KSEVENT** on which the capture pipeline is waiting on. The capture pipeline notifies the application about the completion of the operation when it receives the signal.

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

The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_METADATA**](./ksproperty-cameracontrol-extended-metadata.md) property ID that is defined in the [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_cameracontrol_extended_property) enumeration is used by the client to query for the metadata buffer requirements, such as required metadata size, memory alignment requirements, and desired memory allocation type, for metadata buffer allocation.

Once user mode component has obtained the metadata buffer requirements from the driver, it allocates the appropriately sized metadata buffer with the desired memory alignment from the desired memory pool. This metadata buffer, along with the actual frame buffer, will be sent to the driver to fulfill and then returned back to the user mode component when filled. For multishot scenarios, a corresponding metadata buffer is allocated and delivered to the camera driver for each frame buffer allocated.

The [**KSSTREAM\_METADATA\_INFO**](/windows-hardware/drivers/ddi/ks/ns-ks-ksstream_metadata_info) structure, along with the following flag, is used to send the metadata buffer to the driver.

```cpp
#define KSSTREAM_HEADER_OPTIONSF_METADATA           0x00001000
```

Once the buffer (metadata + frame) is queued to the driver, DevProxy sends a standard [**KSSTREAM\_HEADER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksstream_header) structure, followed by a [**KS\_FRAME\_INFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_frame_info) structure, and followed by a **KSSTREAM\_METADATA\_INFO** structure. DevProxy will further mask **KSSTREAM\_HEADER.OptionFlags** with **KSSTREAM\_HEADER\_OPTIONSF\_METADATA** before it passes the buffer down to the driver.

If the driver does not support metadata, or if **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_METADATA** is not implemented, the **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_METADATA** property control will fail. In this case, DevProxy will not allocate a metadata buffer and the payload that is passed down to the driver from DevProxy will not contain the **KSSTREAM\_METADATA\_INFO** structure.

If the driver supports metadata and the client does not want any metadata, DevProxy will neither allocate metadata buffer nor pass down **KSSTREAM\_METADATA\_INFO** when sending the buffer to the driver. This behavior reduces the unnecessary metadata memory allocation if an app does not want metadata on a given pin.

The following structures describe the layout of the metadata items to be filled by the camera driver in the metadata buffer.

- [**KSCAMERA\_MetadataId**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-kscamera_metadataid)

- [**KSCAMERA\_METADATA\_ITEMHEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_metadata_itemheader)

- [**KSCAMERA\_METADATA\_PHOTOCONFIRMATION**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_metadata_photoconfirmation)

The list below contains the layout of a metadata item. This must be 8-byte aligned.

- [**KSCAMERA\_METADATA\_ITEMHEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_metadata_itemheader)

- Metadata

The photo confirmation metadata is identified by **MetadataId\_PhotoConfirmation**. When present, it indicates that the preview frame associated is a photo confirmation frame. Photo confirmation metadata is parsed by the DevProxy.

The custom metadata is identified by a **MetadataId** that starts from **MetadataId\_Custom\_Start**. The custom metadata item can contain a blob of metadata that can be a focus state and/or faces detected for the preview pin, EXIF and/or the OEM metadata for an image pin. The exact format of the custom blob is determined by the OEM who implements the driver and MFT0. The MFT0 is responsible for parsing the custom blob and attaching each metadata item as an attribute grouped under the **MFSampleExtension\_CaptureMetadata** attribute bag in a format that is readable by the MF capture pipeline and/or WinRT.

The following IMFAttributes are defined in **mfapi.h**. These are required by the MF capture pipeline and/or WinRT. Note that MFT0 does not set any IMFAttributes for photo confirmation since the photo confirmation frame will not flow beyond DevProxy.

| Attribute (GUID) | Data type |
|--|--|
| **MF\_CAPTURE\_METADATA\_FOCUSSTATE** | UINT32 |
| **MF\_CAPTURE\_METADATA\_FACEROIS** | Blob |
| **MF\_CAPTURE\_METADATA\_FRAME\_RAWSTREAM** | IUnknown |

The **MF\_CAPTURE\_METADATA\_FRAME\_RAWSTREAM** IMFAttributes are created and attached to **MFSampleExtension\_CaptureMetadata** by the DevProxy, which contains a pointer to the IMFMediaBuffer interface associated with the raw metadata buffer (**KSSTREAM\_METADATA\_INFO.Data**).

When the MFT0 receives an IMFSample, it gets the raw metadata buffer from the **MF\_CAPTURE\_METADATA\_FRAME\_RAWSTREAM** and parses any additional custom metadata items such as focus state and converts them into corresponding IMFAttributes defined above and attaches them to the **MFSampleExtension\_CaptureMetadata** attribute bag.
The following IMFAttributes must be carried over by the MF pipeline and any third-party supplied MFTs:

| Name | Type |
|--|--|
| **MFSampleExtension\_CaptureMetadata** | **IUnknown** (IMFAttributes) |
| **MFSampleExtension\_EOS** | **UINT32** (Boolean) |
| **MFSampleExtension\_PhotoThumbnail** | **IUnknown** (IMFMediaBuffer) |
| **MFSampleExtension\_PhotoThumbnailMediaType** | **IUnknown** (IMFMediaType) |

To access the raw metadata buffer, the MFT0 does the following:

1. Calls **GetUnknown** on **MFSampleExtension\_CaptureMetadata** from the IMFSample interface to get the IMFAttributes interface for the attribute bag.

1. Calls **GetUnknown** on **MF\_CAPTURE\_METADATA\_FRAME\_RAWSTREAM** from the IMFAttributes interface obtained from the previous step to get the IMFMediaBuffer interface.

1. Calls Lock to get the raw metadata buffer associated with IMFMediaBuffer.

To add the required IMFAttributes to the **MFSampleExtension\_CaptureMetadata** attribute bag, the MFT0 does the following:

1. Calls **GetUnknown** on **MFSampleExtension\_CaptureMetadata** from the IMFSample interface to get the IMFAttributes interface for the attribute bag.

1. Calls **SetUINT32**, **SetBlob**, or **SetUnknown** on **MF\_CAPTURE\_METADATA\_XXX** from the IMFAttributes interface obtained from the previous step based on the GUID and data type specified in the table above.

### Mandatory metadata attributes

The full list of metadata attributes available can be found at [Capture Stats Metadata Attributes](mf-capture-metadata.md)

## Focus priority

The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSPRIORITY**](./ksproperty-cameracontrol-extended-focuspriority.md) property ID is the only control that is associated with the focus priority DDI.

## Focus state

The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSSTATE**](./ksproperty-cameracontrol-extended-focusstate.md) property ID is the only control that is associated with the focus state DDI.

## Extended region of interest ROI

The following property IDs are the controls that are associated with the ROI DDI:

- [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_CONFIGCAPS**](./ksproperty-cameracontrol-extended-roi-configcaps.md)

- [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ROI\_ISPCONTROL**](./ksproperty-cameracontrol-extended-roi-ispcontrol.md)

## Photo confirmation

The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOCONFIRMATION**](./ksproperty-cameracontrol-extended-photoconfirmation.md) property ID is the only control that is associated with the photo confirmation DDI.

## Photo sequence submode

The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE**](./ksproperty-cameracontrol-extended-photomode.md) property ID is the only control associated with the photo sequence DDI.

## EXIF and HW JPEG encoder

The pipeline is not required to process or warp any EXIF data for the HW JPEG encoder; therefore, the EXIF data format is provided by the driver, MFT0, and OEM HW JPEG encoder. OEMs partners can define any custom attribute GUID and variant type for the EXIF attribute and attach it to the **MFSampleExtension\_CaptureMetaData** attribute bag for it to be consumed by the OEM components. If a HW JPEG encoder is available, the pipeline photo sink component will load the HW JPEG encoder and set the EXIF data held in the **MFSampleExtension\_CaptureMetaData** attribute bag onto the HW JPEG encoder as an EXIF encoder option using the [IPropertyBag2::Write](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768195(v=vs.85)) method.

The encoder option property bag contains an array of PROPBAG2 structures that specify the available encoding option properties. The EXIF encoder option set onto HW JPEG encoder is identified by the following property in the encoder option property bag:

| Property name | VARTYPE | Value | Applicable codecs |
|--|--|--|--|
| **SampleMetaData** | **VT\_UNKNOWN** | Pointer to an IMFAttributes interface for **MFSampleExtension\_CaptureMetaData** attribute bag that contains an OEM sub attribute containing the EXIF data. | JPEG |

The **MFSampleExtension\_CaptureMetaData** attribute bag can only contain any OEM defined EXIF sub attribute that the MFT0 and HW JPEG encoder can read to hold the EXIF data. To pass EXIF data from the driver to the HW JPEG encoder, the driver and MFT0 must do the following:

1. The driver provides custom EXIF metadata in the metadata buffer supplied by the pipeline. This is attached to **MFSampleExtension\_CaptureMetadata** as an **MF\_CAPTURE\_METADATA\_FRAME\_RAWSTREAM** IMFAttribute by DevProxy when the sample is returned back to DevProxy.

1. When the MFT0 receives an IMFSample, it gets the raw metadata buffer from **MF\_CAPTURE\_METADATA\_FRAME\_RAWSTREAM** and parses the custom EXIF metadata item and converts it to an OEM defined IMFAttribute and attaches it to the **MFSampleExtension\_CaptureMetadata** attribute bag.

To pass EXIF data from the MFT0 to the HW JPEG encoder, the pipeline photo sink does the following:

1. Calls **GetUnknown** on **MFSampleExtension\_CaptureMetadata** from IMFSample to get the IMFAttributes interface for the attribute bag when IMFSample is received.

1. Calls [IPropertyBag2::Write](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768195(v=vs.85)) to set the encoder option property, identified by SampleMetadata, to the HW JPEG encoder. The encoder option property contains the IMFAttributes interface obtained from the previous step. This interface contains all custom sub attributes including the OEM EXIF sub attribute, and the standardized sub attributes in the **Metadata** section discussed earlier in this topic.

To retrieve the EXIF data for further processing, the HW JPEG encoder does the following:

1. Calls **IPropertyBag2::Read** to retrieve the property value for the property identified by the SampleMetadata property name and **VT\_UNKNOWN** type. When returned, the **VARIANT.punkVal** receives the IMFAttributes interface for **MFSampleExtension\_CaptureMetadata**.

1. Calls **GetBlob** or **GetUnknown** on the OEM EXIF sub attribute from the interface obtained from the previous step to get the EXIF data blob based on the GUID and data type of the OEM EXIF sub attribute.

## Thumbnail

MFT0 is not required to produce any thumbnail for the camera driver. The camera app is expected to generate its own thumbnail. The thumbnail could be produced from the photo confirmation image, HW JPEG encoder, or resizing a full size image. This is up to the app developers. To maintain API and app compatibility with Windows 8.1 apps, the camera driver must not implement the **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOTHUMBNAIL** control.

## Integer ISO

The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ISO\_ADVANCED**](./ksproperty-cameracontrol-extended-iso-advanced.md) property ID is the only control associated with the integer ISO DDI.

## Advanced focus

The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSMODE**](./ksproperty-cameracontrol-extended-focusmode.md) property ID is the only control associated with the integer ISO DDI.

## Flash

The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE**](./ksproperty-cameracontrol-extended-flashmode.md) property ID is the only control that is associated with the flash DDI.

## Zoom

The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ZOOM**](./ksproperty-cameracontrol-extended-zoom.md) property ID is the only control that is associated with the zoom DDI.

## Scene mode

The [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE**](./ksproperty-cameracontrol-extended-scenemode.md) property ID is the only control associated with the scene mode DDI.
