---
title: Implementing IAdapterPowerManagement
description: Implementing IAdapterPowerManagement
keywords:
- IAdapterPowerManagement
- adapter drivers WDK audio , power management
- audio adapter drivers WDK , power management
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementing IAdapterPowerManagement


## <span id="implementing_iadapterpowermanagement"></span><span id="IMPLEMENTING_IADAPTERPOWERMANAGEMENT"></span>


When implementing the [IAdapterPowerManagement](/windows-hardware/drivers/ddi/portcls/nn-portcls-iadapterpowermanagement) interface for your driver, refer to the implementation of the **CAdapterCommon** class in the sample audio drivers in the Microsoft Windows Driver Kit (WDK). This class handles device interrupts and performs other functions that are common to all audio adapter drivers. Your adapter's **CAdapterCommon** class should inherit from the **IAdapterPowerManagement** interface and support this interface in its **NonDelegatingQueryInterface** method. (For details on nondelegating interfaces, see the description of the **INonDelegatingUnknown** interface.)

You can use the IMP\_IAdapterPowerManagement definition from header file Portcls.h to add the function declarations for the [**IAdapterPowerManagement::PowerChangeState**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iadapterpowermanagement-powerchangestate), [**IAdapterPowerManagement::QueryPowerChangeState**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iadapterpowermanagement-querypowerchangestate), and [**IAdapterPowerManagement::QueryDeviceCapabilities**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iadapterpowermanagement-querydevicecapabilities) methods to your driver's **CAdapterCommon** class definition.

During the PortCls system driver's call to an adapter's device-startup routine (see [Starting a Device](../kernel/starting-a-device.md)), the adapter should register its **IAdapterPowerManagement** interface with PortCls by calling [**PcRegisterAdapterPowerManagement**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregisteradapterpowermanagement). For a code example, see the **StartDevice** function in the Sysvad sample driver, which is discussed in [Sample Audio Drivers](sample-audio-drivers.md). The **PcRegisterAdapterPowerManagement** function's first parameter is an **IUnknown** pointer to the adapter driver's **CAdapterCommon** object. PortCls queries this object for its **IAdapterPowerManagement** interface.

When PortCls calls the adapter driver's **IAdapterPowerManagement::PowerChangeState** method to change the device's power state, the adapter driver should cache the device's new power state in the adapter's **CAdapterCommon** object. During the **CAdapterCommon::Init** call (see the implementation in the WDK's sample adapter drivers), the driver should set the initial power state to PowerDeviceD0 (described in [DeviceState](../kernel/devicestate.md)) before returning from a successful initialization. The driver should write to the hardware only if it is known to be in an appropriate power state. 

Before powering down in response to a **PowerChangeState** call, the adapter driver should place the audio outputs in a state that prevents speaker noise from occurring when the power switches off. For example, the shutdown process might include ramping the DAC outputs to zero, turning off the DACs, and muting the MIDI lines.

 

