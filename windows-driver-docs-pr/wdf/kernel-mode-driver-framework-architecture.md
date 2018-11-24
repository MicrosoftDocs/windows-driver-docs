---
title: WDF Architecture
description: WDF Architecture
ms.assetid: e5e2ed4a-5faf-4879-965f-7316fe64edf9
keywords:
- kernel-mode drivers WDK KMDF , architecture
- KMDF WDK , architecture
- Kernel-Mode Driver Framework WDK , architecture
- object methods WDK KMDF
- architecture WDK KMDF
- object event callback functions WDK KMDF
- event callback functions WDK KMDF
- object properties WDK KMDF
- object handles WDK KMDF
- interfaces WDK KMDF
- objects WDK KMDF
- framework objects WDK KMDF , architecture
- framework-based drivers WDK KMDF , architecture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDF Architecture





WDF provides object-based interfaces for drivers. Framework-defined object interfaces consist of:

<a href="" id="object-methods"></a>*Object methods*  
Methods are functions that a driver can call to perform an operation on the object or to get or set an object property. Methods are named **Wdf***ObjectAction*, where *Object* describes the object and *Action* indicates what the function does. For example, [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) creates a device object.

<a href="" id="object-event-callback-functions"></a>*Object event callback functions*  
Event callback functions are functions that a driver provides. Each event callback function is associated with a specific event that can occur on an object. The framework calls the event callback function when the associated event occurs. By convention, the placeholders for event callback functions are called Evt*ObjectEvent*, although you can name these callbacks anything you choose in your driver. For example, a driver registers the [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) event callback to be notified when its device enters the working state.

<a href="" id="object-properties"></a>*Object properties*  
Properties are values that are stored within an object and that a driver can *get* (that is, obtain) and *set* (that is, change). In many cases, properties map directly to the fields in the corresponding WDM objects. Properties that cannot fail are named **Wdf***Object***Get***Value* and **Wdf***Object***Set***Value*, and properties that can fail are named **Wdf***Object***Retrieve***Value* and **Wdf***Object***Assign***Value*. *Object* describes the object, and *Value* identifies the data that the function sets or returns. For example, [**WdfDeviceGetDriver**](https://msdn.microsoft.com/library/windows/hardware/ff545998) returns a handle to the driver object that is associated with the device object.

<a href="" id="object-handles"></a>*Object handles*  
A framework-based driver never directly accesses framework objects. Instead, the driver receives object handles, which it can pass to an object's methods.

The framework defines several object types that framework-based drivers use:

-   A *framework driver object* represents each driver.

-   A *framework device object* represents each device that a driver supports.

-   *Framework queue objects* represent I/O queues that receive a device's I/O requests.

-   *Framework request objects* represent I/O requests that each I/O queue receives.

For a list of all of the objects that the framework defines, see [Summary of Framework Objects](summary-of-framework-objects.md).

 

 





