---
title: Implementing IPowerNotify
description: Implementing IPowerNotify
keywords:
- IPowerNotify interface
- notifications WDK audio
- power-state change notifications WDK audio
ms.date: 04/20/2017
---

# Implementing IPowerNotify


## <span id="implementing_ipowernotify"></span><span id="IMPLEMENTING_IPOWERNOTIFY"></span>


If your driver's miniport objects (see [Audio Miniport Object Interfaces](./audio-miniport-object-interfaces.md)) or stream objects (see [Audio Stream Object Interfaces](./audio-stream-object-interfaces.md)) need to know about power-state changes, they can support the [IPowerNotify](/windows-hardware/drivers/ddi/portcls/nn-portcls-ipowernotify) interface in their **QueryInterface** methods and receive notification from the PortCls system driver each time a power change occurs.

When the power state changes, PortCls calls the [**IPowerNotify::PowerChangeNotify**](/windows-hardware/drivers/ddi/portcls/nf-portcls-ipowernotify-powerchangenotify) method to individually notify each of the miniport and stream objects that support the **IPowerNotify** interface. During the **PowerChangeNotify** call, a miniport object should cache the new device power state. During the **CAdapterCommon::Init** call (for example, see the implementation in the Msvad sample adapter in the Microsoft Windows Driver Kit \[WDK\]), the miniport driver should set its cached power state to the initial value PowerDeviceD0.

Before calling **PowerChangeState** to power down, PortCls calls **IPowerNotify::PowerChangeNotify** to give the miniport driver an opportunity to save any necessary device context. This context might include the hardware-register values that embody the current filter topology and mixer-line settings, for example. After calling **PowerChangeState** to power up, PortCls calls **PowerChangeNotify** so that the miniport driver can restore the saved context.

When powering down, PortCls pauses any active audio data streams before calling **PowerChangeNotify**. When powering up, PortCls calls **PowerChangeNotify** before restarting any paused audio data streams.

Your miniport driver's miniport and stream object classes can inherit from the **IPowerNotify** interface and support this interface in their **NonDelegatingQueryInterface** method. You can use the IMP\_IPowerNotify definition from header file Portcls.h to add the function declaration for the **PowerChangeNotify** method to the class definition for your driver's miniport and stream objects.

 

