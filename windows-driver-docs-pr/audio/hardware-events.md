---
title: Hardware Events
description: Hardware Events
ms.assetid: b91e02dd-0de4-4de3-ade6-778339ce47a8
keywords:
- audio events WDK , hardware
- WDM audio events WDK
- hardware events WDK audio
- events WDK audio
- manual control events WDK audio
- volume-control events WDK audio
- mute switch events WDK audio
- port drivers WDK audio , events
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hardware Events


## <span id="hardware_events"></span><span id="HARDWARE_EVENTS"></span>


Some audio devices provide hardware volume-control knobs, mute switches, or other types of manual controls. Applications can respond to changes in these controls by adjusting the volume or otherwise changing the way that the audio stream is played. When the user adjusts a hardware control, the miniport driver uses the [IPortEvents](https://msdn.microsoft.com/library/windows/hardware/ff536884) interface to inform the port driver that a hardware event has occurred. The port driver, in turn, notifies the application of the event so that it can read the new control setting from the device.

Your miniport driver can query the port driver for the **IPortEvents** interface at the time that it services the **Init** call (see [**IMiniportWavePci::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536734), for example) from the port driver. On Microsoft Windows 98 SE, Windows Me, and Windows 2000 and later, that query succeeds. For a code example, see the Sb16 sample audio adapter in the Windows Driver Kit (WDK).

When the port driver calls your driver's [**IMiniport::GetDescription**](https://msdn.microsoft.com/library/windows/hardware/ff536765) method, the method outputs a [**PCFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff537694) structure that specifies, among other things, the events that your device supports. Events can be specified in the automation tables for the **Pins** and **Nodes** members of PCFILTER\_DESCRIPTOR, and in the **AutomationTable** member, which points to the automation table for the filter itself. Each event is specified by a [**PCEVENT\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff537692) structure. Your driver should set the PCEVENT\_ITEM structure's **Set** and **Id** members to [KSEVENTSETID\_AudioControlChange](https://msdn.microsoft.com/library/windows/hardware/ff537122) and [**KSEVENT\_CONTROL\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/ff537128), and should load a pointer to your driver's [**EventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff536374) routine into the **Handler** member. Your driver should also set the PCEVENT\_ITEM\_FLAG\_BASICSUPPORT bit in the **Flags** member to indicate basic support for control-change events, and it should set the PCEVENT\_ITEM\_FLAG\_ONESHOT and/or PCEVENT\_ITEM\_FLAG\_ENABLE bits to indicate that it supports one-shot and/or recurring notification.

When an application later calls the **mixerOpen** function (described in the Microsoft Windows SDK documentation) to request notification of a particular event, the port driver then calls your driver's **EventHandler** routine with a pointer to a [**PCEVENT\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff537693) structure. This structure's **Verb** member is set to PCEVENT\_VERB\_ADD and its **EventItem** member specifies the event that is to be enabled. The PCEVENT\_REQUEST structure also contains a pointer to a [**KSEVENT\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff561853) structure that your driver should treat as opaque system data. After enabling the event, your handler should call [**IPortEvents::AddEventToEventList**](https://msdn.microsoft.com/library/windows/hardware/ff536886) with the same KSEVENT\_ENTRY pointer. With this call, the handler acknowledges that the event is enabled.

When the hardware event occurs and your driver's interrupt-service routine detects a mute or a volume change, your driver signals the event to the port driver by calling [**IPortEvents::GenerateEventList**](https://msdn.microsoft.com/library/windows/hardware/ff536889) with a set of parameters that describe the event. For example, the following call describes a control change in a lineout-volume node:

```cpp
    pPE->GenerateEventList(NULL, KSEVENT_CONTROL_CHANGE,
                           FALSE, ULONG(-1), TRUE, LINEOUT_VOL);
```

During this call, the port driver searches its event list for all events that match the call parameters and sends notification to the clients that are monitoring these events. In this example, pPE is a pointer to the **IPortEvents** object, and LINEOUT\_VOL is the node ID that the miniport driver assigns to the lineout-volume node. Unspecified parameters (such as the event-set GUID and pin ID in the preceding example) are treated as wildcards and always match the corresponding parameters in the list.

 

 




