---
title: PROPSETID\_VIDCAP\_CAMERACONTROL
description: PROPSETID\_VIDCAP\_CAMERACONTROL
keywords: ["KSPROPERTY_VIDCAP_CAMERACONTROL"]
ms.date: 06/18/2020
---

# PROPSETID\_VIDCAP\_CAMERACONTROL

The PROPSETID\_VIDCAP\_CAMERACONTROL property set controls camera device settings. The controls it provides are a subset of the ITU T.RDC standard.

The KSPROPERTY\_VIDCAP\_CAMERACONTROL enumeration in Ksmedia.h specifies the properties of this set.

Support for this property set is optional and should be implemented only by minidrivers of devices that offer camera control settings. For more information, see the [ITU](https://www.itu.int/) website.

Prior to USB video class, this enumeration contained the following properties:

[**KSPROPERTY\_CAMERACONTROL\_EXPOSURE**](ksproperty-cameracontrol-exposure.md)

[**KSPROPERTY\_CAMERACONTROL\_FOCUS**](ksproperty-cameracontrol-focus.md)

[**KSPROPERTY\_CAMERACONTROL\_IRIS**](ksproperty-cameracontrol-iris.md)

[**KSPROPERTY\_CAMERACONTROL\_ZOOM**](ksproperty-cameracontrol-zoom.md)

[**KSPROPERTY\_CAMERACONTROL\_PAN**](ksproperty-cameracontrol-pan.md)

[**KSPROPERTY\_CAMERACONTROL\_ROLL**](ksproperty-cameracontrol-roll.md)

[**KSPROPERTY\_CAMERACONTROL\_TILT**](ksproperty-cameracontrol-tilt.md)

With the introduction of the [USB Video Class Driver](./usb-video-class-driver.md), the following properties were added to the KSPROPERTY\_VIDCAP\_CAMERACONTROL enumeration.

[**KSPROPERTY\_CAMERACONTROL\_SCANMODE**](ksproperty-cameracontrol-scanmode.md)

[**KSPROPERTY\_CAMERACONTROL\_PRIVACY**](ksproperty-cameracontrol-privacy.md)

[**KSPROPERTY\_CAMERACONTROL\_PANTILT**](ksproperty-cameracontrol-pantilt.md)

[**KSPROPERTY\_CAMERACONTROL\_PAN\_RELATIVE**](ksproperty-cameracontrol-pan-relative.md)

[**KSPROPERTY\_CAMERACONTROL\_TILT\_RELATIVE**](ksproperty-cameracontrol-tilt-relative.md)

[**KSPROPERTY\_CAMERACONTROL\_ROLL\_RELATIVE**](ksproperty-cameracontrol-roll-relative.md)

[**KSPROPERTY\_CAMERACONTROL\_ZOOM\_RELATIVE**](ksproperty-cameracontrol-zoom-relative.md)

[**KSPROPERTY\_CAMERACONTROL\_EXPOSURE\_RELATIVE**](ksproperty-cameracontrol-exposure-relative.md)

[**KSPROPERTY\_CAMERACONTROL\_IRIS\_RELATIVE**](ksproperty-cameracontrol-iris-relative.md)

[**KSPROPERTY\_CAMERACONTROL\_FOCUS\_RELATIVE**](ksproperty-cameracontrol-focus-relative.md)

[**KSPROPERTY\_CAMERACONTROL\_PANTILT\_RELATIVE**](ksproperty-cameracontrol-pantilt-relative.md)

[**KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH**](ksproperty-cameracontrol-focal-length.md)

[**KSPROPERTY\_CAMERACONTROL\_AUTO\_EXPOSURE\_PRIORITY**](ksproperty-cameracontrol-auto-exposure-priority.md)

The DirectShow **IAMCameraControl** interface (see the Microsoft DirectShow documentation in the Windows Software Development Kit (SDK)) provides access to the properties of this set.

## Windows 8 extended camera control properties

Starting with Windows 8, these additional properties are supported for user-mode clients to get or set a camera's control settings:

[**KSPROPERTY\_CAMERACONTROL\_FLASH\_PROPERTY**](ksproperty-cameracontrol-flash-property.md)

[**KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_image_pin_capability_s)

[**KSPROPERTY\_CAMERACONTROL\_REGION\_OF\_INTEREST\_PROPERTY**](ksproperty-cameracontrol-region-of-interest-property.md)

[**KSPROPERTY\_CAMERACONTROL\_VIDEO\_STABILIZATION\_MODE\_PROPERTY**](ksproperty-cameracontrol-video-stabilization-mode-property.md)
