---
title: Implementing IAdapterPowerManagement
description: Implementing IAdapterPowerManagement
ms.assetid: 654b86a7-845c-415b-99e4-c7be92cb9b9c
keywords:
- IAdapterPowerManagement
- adapter drivers WDK audio , power management
- audio adapter drivers WDK , power management
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Implementing IAdapterPowerManagement


## <span id="implementing_iadapterpowermanagement"></span><span id="IMPLEMENTING_IADAPTERPOWERMANAGEMENT"></span>


When implementing the [IAdapterPowerManagement](https://msdn.microsoft.com/library/windows/hardware/ff536485) interface for your driver, refer to the implementation of the **CAdapterCommon** class in the sample audio drivers in the Microsoft Windows Driver Kit (WDK). This class handles device interrupts and performs other functions that are common to all audio adapter drivers. Your adapter's **CAdapterCommon** class should inherit from the **IAdapterPowerManagement** interface and support this interface in its **NonDelegatingQueryInterface** method. (For details on nondelegating interfaces, see the description of the **INonDelegatingUnknown** interface in the MSDN library.)

You can use the IMP\_IAdapterPowerManagement definition from header file Portcls.h to add the function declarations for the [**IAdapterPowerManagement::PowerChangeState**](https://msdn.microsoft.com/library/windows/hardware/ff536488), [**IAdapterPowerManagement::QueryPowerChangeState**](https://msdn.microsoft.com/library/windows/hardware/ff536490), and [**IAdapterPowerManagement::QueryDeviceCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff536489) methods to your driver's **CAdapterCommon** class definition.

During the PortCls system driver's call to an adapter's device-startup routine (see [Starting a Device](https://msdn.microsoft.com/library/windows/hardware/ff563849)), the adapter should register its **IAdapterPowerManagement** interface with PortCls by calling [**PcRegisterAdapterPowerManagement**](https://msdn.microsoft.com/library/windows/hardware/ff537724). For a code example, see the **StartDevice** function in the Sb16 sample adapter driver in the WDK. The **PcRegisterAdapterPowerManagement** function's first parameter is an **IUnknown** pointer to the adapter driver's **CAdapterCommon** object. PortCls queries this object for its **IAdapterPowerManagement** interface.

When PortCls calls the adapter driver's **IAdapterPowerManagement::PowerChangeState** method to change the device's power state, the adapter driver should cache the device's new power state in the adapter's **CAdapterCommon** object. During the **CAdapterCommon::Init** call (see the implementation in the WDK's sample adapter drivers), the driver should set the initial power state to PowerDeviceD0 (described in [DeviceState](https://msdn.microsoft.com/library/windows/hardware/ff543087)) before returning from a successful initialization. The driver should write to the hardware only if it is known to be in an appropriate power state. In the Sb16 sample driver in the WDK, for example, the driver writes to the hardware only in the PowerDeviceD0 state.

Before powering down in response to a **PowerChangeState** call, the adapter driver should place the audio outputs in a state that prevents speaker noise from occurring when the power switches off. For example, the shutdown process might include ramping the DAC outputs to zero, turning off the DACs, and muting the MIDI lines.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Implementing%20IAdapterPowerManagement%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


