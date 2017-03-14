---
title: Deinterlace Container Device for ProcAmp Control
description: Deinterlace Container Device for ProcAmp Control
ms.assetid: ce179efe-9e92-4407-8e90-896e4b9a2e84
keywords: ["container device WDK DirectX VA", "deinterlacing WDK DirectX VA , ProcAmp control", "ProcAmp WDK DirectX VA , deinterlace container device"]
---

# Deinterlace Container Device for ProcAmp Control


## <span id="ddk_deinterlace_container_device_for_procamp_control_gg"></span><span id="DDK_DEINTERLACE_CONTAINER_DEVICE_FOR_PROCAMP_CONTROL_GG"></span>


The [sample functions for ProcAmp control](sample-functions-for-procamp-control.md) can only be used in the context of a DirectX VA device, so it is necessary to first define and create a deinterlace container device.

The [deinterlace container device for deinterlacing](deinterlace-container-device-for-deinterlacing.md) can also be used for ProcAmp control to determine the capabilities of a ProcAmp control device (if the driver supports ProcAmp control adjustments). If supported, the driver creates the ProcAmp control device when the VMR initiates a call to do so.

**Note**   The deinterlace container device is a software construct only and does not represent any functional hardware contained on a device.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Deinterlace%20Container%20Device%20for%20ProcAmp%20Control%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




