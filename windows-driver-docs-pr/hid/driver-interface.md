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

[*DestroyEffect*](https://docs.microsoft.com/previous-versions/ff538410(v=vs.85))

[*Initialize*](https://docs.microsoft.com/previous-versions/ff541025(v=vs.85))

[*DownloadEffect*](https://docs.microsoft.com/previous-versions/ff538601(v=vs.85))

[*GetEffectStatus*](https://docs.microsoft.com/previous-versions/ff538772(v=vs.85))

[*GetForceFeedbackState*](https://docs.microsoft.com/previous-versions/ff538776(v=vs.85))

[*Escape*](https://docs.microsoft.com/previous-versions/ff538680(v=vs.85))

[*SendForceFeedbackCommand*](https://docs.microsoft.com/previous-versions/ff543387(v=vs.85))

[*SetGain*](https://docs.microsoft.com/previous-versions/ff543406(v=vs.85))

[*StartEffect*](https://docs.microsoft.com/previous-versions/ff543458(v=vs.85))

[*StopEffect*](https://docs.microsoft.com/previous-versions/ff543460(v=vs.85))

This functionality is supported by all force feedback devices.

 

 




