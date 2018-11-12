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
ms.date: 04/20/2017
ms.localizationpriority: medium
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

[Performing COPP Operations](performing-copp-operations-example.md)

[Deleting Instances of DirectX VA Device Objects](deleting-instances-of-directx-va-device-objects.md)

 

 





