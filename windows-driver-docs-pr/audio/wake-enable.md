---
title: Wake Enable
description: Wake Enable
ms.assetid: f4a2d4b1-d3a0-449a-ac65-a448d2bcab5c
keywords: ["HD Audio, wake enable", "High Definition Audio (HD Audio), wake enable", "wake enable WDK audio", "status-change events WDK audio", "power management WDK audio"]
---

# Wake Enable


Before powering down a codec, the codec function driver typically enables the codec to wake up the system if a status-change event occurs while the codec is in the powered-down state. For an audio codec, such an event can be triggered when the user inserts a plug into an input jack or removes a plug from a jack. For a modem codec, a status-change event can occur when the phone rings to indicate an incoming call. For more information about status-change events, see the *Intel High Definition Audio Specification* at the [Intel HD Audio](http://go.microsoft.com/fwlink/p/?linkid=42508) website.

To prepare for powering down, the function driver first configures the codec to signal the HD Audio bus controller when a status-change event occurs. Next, the function driver sends an [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) power-management IRP to the HD Audio bus driver to tell it to enable the wake-up signal from the codec. Later, if the wake-up signal is enabled, and the codec transmits a status-change event over the codec's SDI line, the controller generates a wake-up signal to the system and the bus driver notifies the function driver by completing the IRP\_MN\_WAIT\_WAKE IRP.

Following a wake event, the bus driver determines which codec generated the wake-up signal and completes any pending IRP\_MN\_WAIT\_WAKE IRPs on that codec. However, if the codec contains both audio and modem function groups, for example, the bus driver has no way to determine which function group is the source of the wake-up signal. In this case, the function driver must send its own queries to the codec to verify the source of the wake-up signal.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Wake%20Enable%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


