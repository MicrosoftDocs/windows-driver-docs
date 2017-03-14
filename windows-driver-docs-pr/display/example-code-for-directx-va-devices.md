---
title: Example Code for DirectX VA Devices
description: Example Code for DirectX VA Devices
ms.assetid: 3afdb99b-8a26-4caf-8285-1aff791a8123
keywords: ["DirectX Video Acceleration WDK Windows 2000 display , example code", "Video Acceleration WDK DirectX , example code", "VA WDK DirectX , example code", "examples WDK DirectX VA", "templates WDK DirectX VA"]
---

# Example Code for DirectX VA Devices


## <span id="ddk_example_code_for_directx_va_devices_gg"></span><span id="DDK_EXAMPLE_CODE_FOR_DIRECTX_VA_DEVICES_GG"></span>


The example code provided in this section shows implementations of a [motion-compensation](motion-compensation-callbacks.md) code template and a Certified Output Protection Protocol (COPP) video miniport driver template. The motion-compensation code template is used to access ProcAmp control, deinterlacing, and COPP functionality. The COPP video miniport driver template is used to access COPP functionality. Using these templates can simplify your display driver and video miniport driver development. However, you are not required to implement access to ProcAmp control, deinterlacing, and COPP functionality in this manner for your drivers to work correctly.

This section includes:

[Motion Compensation Code Template](motion-compensation-code-template.md)

[COPP Video Miniport Driver Template](copp-video-miniport-driver-template.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Example%20Code%20for%20DirectX%20VA%20Devices%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




