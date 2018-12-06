---
title: Driver Interface
description: Driver Interface
ms.assetid: cb5e06c3-6add-4eba-b794-861d567a3047
keywords: ["force feedback drivers WDK HID , methods supported"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Driver Interface





If the force-feedback driver is COM-based, an instance of the driver is created by DirectInput. If the interface specified is "VJoyD", then the VJoyD minidriver is loaded by VJoyD. Both driver paths support the following exported methods:

[*DestroyEffect*](https://msdn.microsoft.com/library/windows/hardware/ff538410)

[*Initialize*](https://msdn.microsoft.com/library/windows/hardware/ff541025)

[*DownloadEffect*](https://msdn.microsoft.com/library/windows/hardware/ff538601)

[*GetEffectStatus*](https://msdn.microsoft.com/library/windows/hardware/ff538772)

[*GetForceFeedbackState*](https://msdn.microsoft.com/library/windows/hardware/ff538776)

[*Escape*](https://msdn.microsoft.com/library/windows/hardware/ff538680)

[*SendForceFeedbackCommand*](https://msdn.microsoft.com/library/windows/hardware/ff543387)

[*SetGain*](https://msdn.microsoft.com/library/windows/hardware/ff543406)

[*StartEffect*](https://msdn.microsoft.com/library/windows/hardware/ff543458)

[*StopEffect*](https://msdn.microsoft.com/library/windows/hardware/ff543460)

This functionality is supported by all force feedback devices.

 

 




