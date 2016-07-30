---
title: CM\_PROB\_FAILED\_POST\_START
description: CM\_PROB\_FAILED\_POST\_START
ms.assetid: 82d43c8b-d5de-4395-9ca0-34d2258b9772
keywords: ["CM_PROB_FAILED_POST_START"]
---

# CM\_PROB\_FAILED\_POST\_START


## <a href="" id="ddk-cm-prob-failed-post-start-dg"></a>


A driver has reported a device failure.

### Error Code

43

### Display Message (Windows XP and later versions of Windows)

"Windows has stopped this device because it has reported problems. (Code 43)"

### Recommended Resolution (Windows XP and later versions of Windows)

Uninstall and reinstall the device.

One of the drivers controlling the device told the operating system the device failed in some manner in response to IRP\_MN\_QUERY\_PNP\_DEVICE\_STATE.

 

 





