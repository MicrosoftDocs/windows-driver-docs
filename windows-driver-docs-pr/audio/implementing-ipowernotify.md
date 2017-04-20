---
title: Implementing IPowerNotify
description: Implementing IPowerNotify
ms.assetid: 8bd8b4c8-1961-41ea-ba98-41e3a732ed37
keywords:
- IPowerNotify interface
- notifications WDK audio
- power-state change notifications WDK audio
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Implementing IPowerNotify


## <span id="implementing_ipowernotify"></span><span id="IMPLEMENTING_IPOWERNOTIFY"></span>


If your driver's miniport objects (see [Audio Miniport Object Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff536207)) or stream objects (see [Audio Stream Object Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff536217)) need to know about power-state changes, they can support the [IPowerNotify](https://msdn.microsoft.com/library/windows/hardware/ff536947) interface in their **QueryInterface** methods and receive notification from the PortCls system driver each time a power change occurs.

When the power state changes, PortCls calls the [**IPowerNotify::PowerChangeNotify**](https://msdn.microsoft.com/library/windows/hardware/ff536949) method to individually notify each of the miniport and stream objects that support the **IPowerNotify** interface. During the **PowerChangeNotify** call, a miniport object should cache the new device power state. During the **CAdapterCommon::Init** call (for example, see the implementation in the Msvad sample adapter in the Microsoft Windows Driver Kit \[WDK\]), the miniport driver should set its cached power state to the initial value PowerDeviceD0.

Before calling **PowerChangeState** to power down, PortCls calls **IPowerNotify::PowerChangeNotify** to give the miniport driver an opportunity to save any necessary device context. This context might include the hardware-register values that embody the current filter topology and mixer-line settings, for example. After calling **PowerChangeState** to power up, PortCls calls **PowerChangeNotify** so that the miniport driver can restore the saved context.

When powering down, PortCls pauses any active audio data streams before calling **PowerChangeNotify**. When powering up, PortCls calls **PowerChangeNotify** before restarting any paused audio data streams.

Your miniport driver's miniport and stream object classes can inherit from the **IPowerNotify** interface and support this interface in their **NonDelegatingQueryInterface** method. You can use the IMP\_IPowerNotify definition from header file Portcls.h to add the function declaration for the **PowerChangeNotify** method to the class definition for your driver's miniport and stream objects.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Implementing%20IPowerNotify%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


