---
title: Multifunction Device Limits
description: Multifunction Device Limits
ms.assetid: 9375c451-b83f-4655-b1e2-cbd693eaaf5f
keywords:
- multifunction audio devices WDK , limits
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Multifunction Device Limits


## <span id="multifunction_device_limits"></span><span id="MULTIFUNCTION_DEVICE_LIMITS"></span>


The number of audio functions per multifunction device is limited by the following factors:

-   When the adapter driver calls [**PcAddAdapterDevice**](https://msdn.microsoft.com/library/windows/hardware/ff537683), the function's fourth parameter, *MaxObjects*, specifies the maximum number of miniport driver objects that the driver can support. The sample adapter drivers in the Microsoft Windows Driver Kit (WDK) set this parameter to the integer constant MAX\_MINIPORTS, which is typically defined to be a small value (five or less). You might need to increase this value if you plan to support multiple stereo pairs or other types of audio subdevices.

 

 




