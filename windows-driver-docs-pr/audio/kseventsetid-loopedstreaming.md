---
title: KSEVENTSETID\_LoopedStreaming
description: KSEVENTSETID\_LoopedStreaming
ms.assetid: 88baf1f0-d18f-4601-9ba3-fea957712cd6
keywords: ["KSEVENTSETID_LoopedStreaming"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSEVENTSETID\_LoopedStreaming


This event set is intended only for internal use by the system.

The `KSEVENTSETID_LoopedStreaming` event set defines position events in audio streams that use looped buffers. A looped buffer is a data buffer for an audio stream of type [**KSINTERFACE\_STANDARD\_LOOPED\_STREAMING**](https://msdn.microsoft.com/library/windows/hardware/ff563381). Through a position event, a client can receive notification from a driver when an audio stream reaches a specified position in a looped buffer.

In Microsoft Windows Server 2003, Windows XP, Windows 2000, Windows Me, and Windows 98, the only system components that implement driver support for this event set are KMixer and PortCls (Kmixer.sys and Portcls.sys). DirectSound (Dsound.dll) is the only system component that uses this event set as a client. Custom audio drivers typically do not implement support for this event set.

In Windows Vista and later, no system components use or support the `KSEVENTSETID_LoopedStreaming` event set.

The event items in this set are specified as KSEVENT\_LOOPEDSTREAMING enumeration values.

The only event in this set is [**KSEVENT\_LOOPEDSTREAMING\_POSITION**](ksevent-loopedstreaming-position.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSEVENTSETID_LoopedStreaming%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




