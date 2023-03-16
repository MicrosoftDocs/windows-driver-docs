---
title: KSEVENTSETID\_LoopedStreaming
description: KSEVENTSETID\_LoopedStreaming
keywords: ["KSEVENTSETID_LoopedStreaming"]
ms.date: 03/06/2023
---

# KSEVENTSETID\_LoopedStreaming


This event set is intended only for internal use by the system.

The `KSEVENTSETID_LoopedStreaming` event set defines position events in audio streams that use looped buffers. A looped buffer is a data buffer for an audio stream of type [**KSINTERFACE\_STANDARD\_LOOPED\_STREAMING**](../stream/ksinterface-standard-looped-streaming.md). Through a position event, a client can receive notification from a driver when an audio stream reaches a specified position in a looped buffer.

In Microsoft Windows Server 2003, Windows XP, Windows 2000, Windows Me, and Windows 98, the only system components that implement driver support for this event set are KMixer and PortCls (Kmixer.sys and Portcls.sys). DirectSound (Dsound.dll) is the only system component that uses this event set as a client. Custom audio drivers typically do not implement support for this event set.

In Windows Vista and later, no system components use or support the `KSEVENTSETID_LoopedStreaming` event set.

The event items in this set are specified as KSEVENT\_LOOPEDSTREAMING enumeration values.

The only event in this set is [**KSEVENT\_LOOPEDSTREAMING\_POSITION**](ksevent-loopedstreaming-position.md).

 

