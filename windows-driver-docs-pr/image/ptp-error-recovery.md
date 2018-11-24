---
title: PTP Error Recovery
description: PTP Error Recovery
ms.assetid: 0f89d6b6-9d95-4e98-aa90-08c9508a2228
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PTP Error Recovery





During initialization of the Microsoft PTP class minidriver (that is, on initial retrieval of the DeviceInfo and ObjectInfo datasets, and the property descriptions), any error is treated as a catastrophic failure, and the WIA minidriver fails to initialize.

During later processing (for example, while retrieving an image), when an unrecognized error occurs, the Microsoft PTP minidriver first attempts to send the Get Device Status USB class-specific request (described in the USB Still Image Capture Device Definition). If that request succeeds, the driver clears any stalled endpoints and continues.

If the Get Device Status request fails, the PTP minidriver attempts to reset the device using the Device Reset class-specific request (described in the USB Still Image Capture Device Definition). If the Device Reset class-specific request succeeds, it returns S\_FALSE instead of S\_OK. If resetting the device fails, the Device Reset class-specific request returns an error code.

 

 




