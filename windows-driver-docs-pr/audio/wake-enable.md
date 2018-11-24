---
title: Wake Enable
description: Wake Enable
ms.assetid: f4a2d4b1-d3a0-449a-ac65-a448d2bcab5c
keywords:
- HD Audio, wake enable
- High Definition Audio (HD Audio), wake enable
- wake enable WDK audio
- status-change events WDK audio
- power management WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Wake Enable


Before powering down a codec, the codec function driver typically enables the codec to wake up the system if a status-change event occurs while the codec is in the powered-down state. For an audio codec, such an event can be triggered when the user inserts a plug into an input jack or removes a plug from a jack. For a modem codec, a status-change event can occur when the phone rings to indicate an incoming call. For more information about status-change events, see the *Intel High Definition Audio Specification* at the [Intel HD Audio](https://go.microsoft.com/fwlink/p/?linkid=42508) website.

To prepare for powering down, the function driver first configures the codec to signal the HD Audio bus controller when a status-change event occurs. Next, the function driver sends an [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) power-management IRP to the HD Audio bus driver to tell it to enable the wake-up signal from the codec. Later, if the wake-up signal is enabled, and the codec transmits a status-change event over the codec's SDI line, the controller generates a wake-up signal to the system and the bus driver notifies the function driver by completing the IRP\_MN\_WAIT\_WAKE IRP.

Following a wake event, the bus driver determines which codec generated the wake-up signal and completes any pending IRP\_MN\_WAIT\_WAKE IRPs on that codec. However, if the codec contains both audio and modem function groups, for example, the bus driver has no way to determine which function group is the source of the wake-up signal. In this case, the function driver must send its own queries to the codec to verify the source of the wake-up signal.

 

 




