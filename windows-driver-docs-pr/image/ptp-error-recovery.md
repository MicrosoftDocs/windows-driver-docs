---
title: PTP Error Recovery
author: windows-driver-content
description: PTP Error Recovery
ms.assetid: 0f89d6b6-9d95-4e98-aa90-08c9508a2228
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PTP Error Recovery


## <a href="" id="ddk-ptp-error-recovery-si"></a>


During initialization of the Microsoft PTP class minidriver (that is, on initial retrieval of the DeviceInfo and ObjectInfo datasets, and the property descriptions), any error is treated as a catastrophic failure, and the WIA minidriver fails to initialize.

During later processing (for example, while retrieving an image), when an unrecognized error occurs, the Microsoft PTP minidriver first attempts to send the Get Device Status USB class-specific request (described in the USB Still Image Capture Device Definition). If that request succeeds, the driver clears any stalled endpoints and continues.

If the Get Device Status request fails, the PTP minidriver attempts to reset the device using the Device Reset class-specific request (described in the USB Still Image Capture Device Definition). If the Device Reset class-specific request succeeds, it returns S\_FALSE instead of S\_OK. If resetting the device fails, the Device Reset class-specific request returns an error code.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20PTP%20Error%20Recovery%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


