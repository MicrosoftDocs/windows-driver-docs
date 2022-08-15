---
title: PROPSETID_VIDCAP_CAMERACONTROL
description: The PROPSETID_VIDCAP_CAMERACONTROL property set controls camera device settings. The controls it provides are a subset of the ITU T.RDC standard.
keywords: ["KSPROPERTY_VIDCAP_CAMERACONTROL"]
ms.date: 06/06/2022
---

# PROPSETID_VIDCAP_CAMERACONTROL

The PROPSETID_VIDCAP_CAMERACONTROL property set controls camera device settings. The controls it provides are a subset of the ITU T.RDC standard.

The KSPROPERTY_VIDCAP_CAMERACONTROL enumeration in Ksmedia.h specifies the properties of this set.

Support for this property set is optional and should be implemented only by minidrivers of devices that offer camera control settings. For more information, see the [ITU](https://www.itu.int/) website.

Prior to USB video class, this enumeration contained the following properties:

[**KSPROPERTY_CAMERACONTROL_EXPOSURE**](ksproperty-cameracontrol-exposure.md)

[**KSPROPERTY_CAMERACONTROL_FOCUS**](ksproperty-cameracontrol-focus.md)

[**KSPROPERTY_CAMERACONTROL_IRIS**](ksproperty-cameracontrol-iris.md)

[**KSPROPERTY_CAMERACONTROL_ZOOM**](ksproperty-cameracontrol-zoom.md)

[**KSPROPERTY_CAMERACONTROL_PAN**](ksproperty-cameracontrol-pan.md)

[**KSPROPERTY_CAMERACONTROL_ROLL**](ksproperty-cameracontrol-roll.md)

[**KSPROPERTY_CAMERACONTROL_TILT**](ksproperty-cameracontrol-tilt.md)

With the introduction of the [USB Video Class Driver](./usb-video-class-driver.md), the following properties were added to the KSPROPERTY_VIDCAP_CAMERACONTROL enumeration.

[**KSPROPERTY_CAMERACONTROL_SCANMODE**](ksproperty-cameracontrol-scanmode.md)

[**KSPROPERTY_CAMERACONTROL_PRIVACY**](ksproperty-cameracontrol-privacy.md)

[**KSPROPERTY_CAMERACONTROL_PANTILT**](ksproperty-cameracontrol-pantilt.md)

[**KSPROPERTY_CAMERACONTROL_PAN_RELATIVE**](ksproperty-cameracontrol-pan-relative.md)

[**KSPROPERTY_CAMERACONTROL_TILT_RELATIVE**](ksproperty-cameracontrol-tilt-relative.md)

[**KSPROPERTY_CAMERACONTROL_ROLL_RELATIVE**](ksproperty-cameracontrol-roll-relative.md)

[**KSPROPERTY_CAMERACONTROL_ZOOM_RELATIVE**](ksproperty-cameracontrol-zoom-relative.md)

[**KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE**](ksproperty-cameracontrol-exposure-relative.md)

[**KSPROPERTY_CAMERACONTROL_IRIS_RELATIVE**](ksproperty-cameracontrol-iris-relative.md)

[**KSPROPERTY_CAMERACONTROL_FOCUS_RELATIVE**](ksproperty-cameracontrol-focus-relative.md)

[**KSPROPERTY_CAMERACONTROL_PANTILT_RELATIVE**](ksproperty-cameracontrol-pantilt-relative.md)

[**KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH**](ksproperty-cameracontrol-focal-length.md)

[**KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY**](ksproperty-cameracontrol-auto-exposure-priority.md)

The DirectShow **IAMCameraControl** interface (see the Microsoft DirectShow documentation in the Windows Software Development Kit (SDK)) provides access to the properties of this set.

> [!NOTE]
> Face-based ROI coordinates for 3A are calculated relative to the active field of view of the camera. If the field of view has been modified due to ue of a control such as Zoom, Pan or Tilt or [Digital Window](./digital-window-overview.md), the camera is responsible for mapping the provided 3A ROI coordinates back to the sensor's full field of view, considering the current zoom/pan window.

## Windows 8 extended camera control properties

Starting with Windows 8, these additional properties are supported for user-mode clients to get or set a camera's control settings:

[**KSPROPERTY_CAMERACONTROL_FLASH_PROPERTY**](ksproperty-cameracontrol-flash-property.md)

[**KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_image_pin_capability_s)

[**KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_PROPERTY**](ksproperty-cameracontrol-region-of-interest-property.md)

[**KSPROPERTY_CAMERACONTROL_VIDEO_STABILIZATION_MODE_PROPERTY**](ksproperty-cameracontrol-video-stabilization-mode-property.md)