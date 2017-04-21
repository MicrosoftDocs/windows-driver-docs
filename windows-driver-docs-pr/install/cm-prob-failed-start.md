---
title: CM_PROB_FAILED_START
description: CM_PROB_FAILED_START
ms.assetid: a7759bcd-1806-4d7a-8ff0-3b03abcae08b
keywords:
- CM_PROB_FAILED_START
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CM_PROB_FAILED_START


## <a href="" id="ddk-cm-prob-failed-start-dg"></a>


The device failed to start.

### Error Code

10

### Display Message (Windows 2000 and later versions of Windows)

If the device's hardware key contains a "FailReasonString" value, the value string is displayed as the error message. (A driver or enumerator supplies this registry string value.) If the hardware key does not contain a "FailReasonString" value, the following generic error message is displayed:

"This device cannot start. (Code 10)"

"Try upgrading the device drivers for this device."

### Recommended Resolution (Windows 2000 and later versions of Windows)

Select **Update Driver**, which starts the Hardware Update wizard.

This error code is set when one of the drivers in the device's driver stack fails IRP_MN_START_DEVICE. If there are many drivers in the stack, it can be difficult to determine the one that failed.

 

 





