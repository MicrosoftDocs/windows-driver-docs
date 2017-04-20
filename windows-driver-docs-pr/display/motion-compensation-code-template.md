---
title: Motion Compensation Code Template
description: Motion Compensation Code Template
ms.assetid: 2632f84d-7ebb-4c55-9ba7-996f0cb891bd
keywords:
- motion-compensation code template WDK DirectX VA
- ProcAmp WDK DirectX VA , motion-compensation code template
- deinterlacing WDK DirectX VA , motion-compensation code template
- COPP WDK DirectX VA , motion-compensation code template
- copy protection WDK COPP , motion-compensation code template
- video copy protection WDK COPP , motion-compensation code template
- protected video WDK COPP , motion-compensation code template
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Motion Compensation Code Template


## <span id="ddk_motion_compensation_code_template_gg"></span><span id="DDK_MOTION_COMPENSATION_CODE_TEMPLATE_GG"></span>


The example code provided in this section shows an implementation of a [motion-compensation](motion-compensation-callbacks.md) code template that is used to access ProcAmp control, deinterlacing, and Certified Output Protection Protocol (COPP) functionality. Using this template can simplify your display driver development. However, you are not required to implement access to ProcAmp control, deinterlacing, and COPP functionality in this manner for your display driver to work correctly.

If your driver supports other DirectX VA functions, such as decoding MPEG-2 video streams, then extend the example code to include processing of additional DirectX VA GUIDs.

This section includes:

[Defining DirectX VA Device Classes](defining-directx-va-device-classes.md)

[Retrieving DirectX VA Devices](retrieving-directx-va-devices.md)

[Creating Instances of DirectX VA Device Objects](creating-instances-of-directx-va-device-objects.md)

[Performing ProcAmp Control and Deinterlacing Operations](performing-procamp-control-and-deinterlacing-operations.md)

[Performing Deinterlacing with Substream Compositing Operations](performing-deinterlacing-with-substream-compositing-operations.md)

[Performing COPP Operations](performing-copp-operations2.md)

[Deleting Instances of DirectX VA Device Objects](deleting-instances-of-directx-va-device-objects.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Motion%20Compensation%20Code%20Template%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




