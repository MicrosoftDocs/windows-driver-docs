---
title: Deinterlace Container Device for ProcAmp Control
description: Deinterlace Container Device for ProcAmp Control
ms.assetid: ce179efe-9e92-4407-8e90-896e4b9a2e84
keywords:
- container device WDK DirectX VA
- deinterlacing WDK DirectX VA , ProcAmp control
- ProcAmp WDK DirectX VA , deinterlace container device
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deinterlace Container Device for ProcAmp Control


## <span id="ddk_deinterlace_container_device_for_procamp_control_gg"></span><span id="DDK_DEINTERLACE_CONTAINER_DEVICE_FOR_PROCAMP_CONTROL_GG"></span>


The [sample functions for ProcAmp control](sample-functions-for-procamp-control.md) can only be used in the context of a DirectX VA device, so it is necessary to first define and create a deinterlace container device.

The [deinterlace container device for deinterlacing](deinterlace-container-device-for-deinterlacing.md) can also be used for ProcAmp control to determine the capabilities of a ProcAmp control device (if the driver supports ProcAmp control adjustments). If supported, the driver creates the ProcAmp control device when the VMR initiates a call to do so.

**Note**   The deinterlace container device is a software construct only and does not represent any functional hardware contained on a device.

 

 

 





