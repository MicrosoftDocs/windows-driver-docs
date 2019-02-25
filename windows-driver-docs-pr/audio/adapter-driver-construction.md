---
title: Adapter Driver Construction
description: Adapter Driver Construction
ms.assetid: e4a151b9-57aa-402f-8a0d-70547eb67917
keywords:
- audio miniport drivers WDK , adapter drivers
- miniport drivers WDK audio , adapter drivers
- adapter drivers WDK audio , miniport drivers
- kernel-mode driver services WDK audio
- port class drivers WDK audio
- PortCls WDK audio , adapter drivers
- audio adapters WDK
- audio adapters WDK , constructing
- adapter drivers WDK audio , constructing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adapter Driver Construction


## <span id="adapter_driver_construction"></span><span id="ADAPTER_DRIVER_CONSTRUCTION"></span>


Driver support for a particular audio adapter card takes the form of an adapter driver. An adapter driver consists of the following:

-   General adapter code that performs driver startup and initialization, and that implements any operations that are common to all audio functions on the adapter card.

-   A set of miniport drivers that manage specific audio functions on the adapter card.

The hardware vendor supplies both the general adapter code and the code for any miniport drivers that are not provided by the system.

For an example of the general adapter code, see the implementation of the **CAdapterCommon** interface in the Sb16, Msvad, and Ac97 sample audio drivers in the Microsoft Windows Driver Kit (WDK).

By using a layered approach, the vendor can write an adapter driver that operates on one of several levels, depending on the adapter's hardware functionality. When determining the level of support that a given hardware function requires, the vendor should first determine whether a system-supplied miniport driver already exists that supports the function (see the [**PcNewMiniport**](https://msdn.microsoft.com/library/windows/hardware/ff537714) function's list of system-supplied miniport drivers). If not, the vendor must implement a proprietary miniport driver but might still be able to use one of the system-supplied port drivers (see the [**PcNewPort**](https://msdn.microsoft.com/library/windows/hardware/ff537715) function's list of system-supplied port drivers).

To implement WDM support for a device, follow these steps:

1.  If a system-supplied miniport driver already supports the hardware function, use the existing miniport driver to manage the function.

2.  If the hardware function is not compatible with a system-supplied miniport driver, then determine whether the function is compatible with at least one of the system-supplied port drivers. If a system-supplied port driver supports the hardware function, write the portion of the miniport driver that manages the function. That miniport driver should comply with the specification for the miniport interface that the owning port driver expects.

3.  If no system-supplied port driver supports the hardware function, write a minidriver to support the function. The minidriver should comply with the interface specification for the streaming class driver.

This section discusses the following topics:

[Startup Sequence](startup-sequence.md)

[Subdevice Creation](subdevice-creation.md)

 

 




