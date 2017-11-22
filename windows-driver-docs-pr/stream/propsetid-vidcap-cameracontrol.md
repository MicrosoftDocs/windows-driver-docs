---
title: PROPSETID\_VIDCAP\_CAMERACONTROL
description: PROPSETID\_VIDCAP\_CAMERACONTROL
MS-HAID:
- 'vidcapprop\_f5058946-de27-422e-a2a8-af307b9a33d1.xml'
- 'stream.propsetid\_vidcap\_cameracontrol'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8899a474-fa6f-4d5c-bd68-2433428bb5c5
keywords: ["KSPROPERTY_VIDCAP_CAMERACONTROL"]
---

# PROPSETID\_VIDCAP\_CAMERACONTROL


## <span id="ddk_propsetid_vidcap_cameracontrol_ks"></span><span id="DDK_PROPSETID_VIDCAP_CAMERACONTROL_KS"></span>


The PROPSETID\_VIDCAP\_CAMERACONTROL property set controls camera device settings. The controls it provides are a subset of the ITU T.RDC standard.

The KSPROPERTY\_VIDCAP\_CAMERACONTROL enumeration in Ksmedia.h specifies the properties of this set.

Support for this property set is optional and should be implemented only by minidrivers of devices that offer camera control settings. For more information, see the [ITU](http://go.microsoft.com/fwlink/p/?linkid=8741) website.

Prior to USB video class, this enumeration contained the following properties:

[**KSPROPERTY\_CAMERACONTROL\_EXPOSURE**](ksproperty-cameracontrol-exposure.md)

[**KSPROPERTY\_CAMERACONTROL\_FOCUS**](ksproperty-cameracontrol-focus.md)

[**KSPROPERTY\_CAMERACONTROL\_IRIS**](ksproperty-cameracontrol-iris.md)

[**KSPROPERTY\_CAMERACONTROL\_ZOOM**](ksproperty-cameracontrol-zoom.md)

[**KSPROPERTY\_CAMERACONTROL\_PAN**](ksproperty-cameracontrol-pan.md)

[**KSPROPERTY\_CAMERACONTROL\_ROLL**](ksproperty-cameracontrol-roll.md)

[**KSPROPERTY\_CAMERACONTROL\_TILT**](ksproperty-cameracontrol-tilt.md)

With the introduction of the [USB Video Class Driver](https://msdn.microsoft.com/library/windows/hardware/ff568649), the following properties were added to the KSPROPERTY\_VIDCAP\_CAMERACONTROL enumeration. These properties are supported in Windows Vista and later versions of Windows:

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

## <span id="Windows_8_extended_camera_control_properties"></span><span id="windows_8_extended_camera_control_properties"></span><span id="WINDOWS_8_EXTENDED_CAMERA_CONTROL_PROPERTIES"></span>Windows 8 extended camera control properties


Starting with Windows 8, these additional properties are supported for user-mode clients to get or set a camera's control settings:

[**KSPROPERTY\_CAMERACONTROL\_FLASH\_PROPERTY**](ksproperty-cameracontrol-flash-property.md)

[**KSPROPERTY\_CAMERACONTROL\_IMAGE\_PIN\_CAPABILITY\_S**](https://msdn.microsoft.com/library/windows/hardware/jj553707)

[**KSPROPERTY\_CAMERACONTROL\_REGION\_OF\_INTEREST\_PROPERTY**](ksproperty-cameracontrol-region-of-interest-property.md)

[**KSPROPERTY\_CAMERACONTROL\_VIDEO\_STABILIZATION\_MODE\_PROPERTY**](ksproperty-cameracontrol-video-stabilization-mode-property.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20PROPSETID_VIDCAP_CAMERACONTROL%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




