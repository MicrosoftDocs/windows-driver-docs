---
title: WDF Architecture
description: WDF Architecture
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: e5e2ed4a-5faf-4879-965f-7316fe64edf9
keywords: ["kernel mode drivers WDK KMDF architecture", "KMDF WDK architecture", "Kernel Mode Driver Framework WDK architecture", "object methods WDK KMDF", "architecture WDK KMDF", "object event callback functions WDK KMDF", "event callback functions WDK KMDF", "object properties WDK KMDF", "object handles WDK KMDF", "interfaces WDK KMDF", "objects WDK KMDF", "framework objects WDK KMDF architecture", "framework based drivers WDK KMDF architecture"]
---

# WDF Architecture


## <a href="" id="ddk-windows-driver-framework-architecture-df"></a>


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WDF%20Architecture%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




