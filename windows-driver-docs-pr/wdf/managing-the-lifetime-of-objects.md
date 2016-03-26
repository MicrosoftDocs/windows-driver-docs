---
title: Managing the Lifetime of Objects
description: Managing the Lifetime of Objects
ms.assetid: 55ad8133-a70a-462f-87cd-6aeaffb0aec8
keywords: ["UMDF objects WDK , lifetimes", "framework objects WDK UMDF , lifetimes", "lifetimes WDK UMDF", "callback objects WDK UMDF"]
---

# Managing the Lifetime of Objects


\[This topic applies to UMDF 1.*x*.\]

UMDF uses a reference-counting scheme to manage the lifetime of [callback objects](creating-callback-objects.md) and [framework objects](framework-objects.md).

## Managing References to Driver-Supplied Callback Objects


In most cases, a driver is not required to keep a reference to a callback object. If methods of the callback object interface are called only by the framework and by objects whose lifetimes depend on the callback object and the callback object's paired framework object, the driver does not have to keep a reference. In other words, the driver or framework can safely call methods of object interfaces that are higher up in the object hierarchy.

## Managing References to Framework Objects


In UMDF, general COM lifetime principles and the WDF-specific lifetime model determine the lifetime of framework objects. Your driver must satisfy criteria for both models so that framework objects are freed from memory at appropriate times.

### COM Lifetime Management

In COM, a caller typically keeps a reference to the object while the object is in use, and then the caller releases the reference when it no longer requires the object. However, a UMDF driver does not need to keep a reference to a framework object. In fact, the driver can release a framework object reference immediately after the driver creates the framework object.

For example, UMDF samples release the device object after they call [**IWDFDriver::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff558899). Although the reference is released early, the device object continues to exist until device is removed because the WDF object tree keeps a reference to it.

Because UMDF tracks all framework objects in an object tree, the driver does not need to keep a reference to framework objects.

However, if your driver keeps a reference to a framework object, the driver must release the reference when it no longer needs the object. A circular reference remains in place until the driver releases its reference. To avoid circular references, the driver typically should not keep an explicit reference to a framework object.

If the driver must keep a reference to a framework object, the driver's callback object must also implement the [IObjectCleanup](https://msdn.microsoft.com/library/windows/hardware/ff556754) interface. When the driver calls [**IWDFObject::DeleteWdfObject**](https://msdn.microsoft.com/library/windows/hardware/ff560210) on the framework object, the framework object calls its corresponding callback object's [**IObjectCleanup::OnCleanup**](https://msdn.microsoft.com/library/windows/hardware/ff556760) method. The implementation of **IObjectCleanup::OnCleanup** must release the reference to the framework object to enable the framework to complete tear down of the framework object.

### WDF Lifetime Management

If you are creating an object of a type that allows you to override the default parent, you should select a parent with a lifetime that matches the lifetime of your object. For more information about default parent objects and if the driver can override the default parent, see the table in [Framework Objects](framework-objects.md).

If you match object lifetimes, the framework deletes your object when the parent object is deleted. If you do not match object lifetimes and you want the object to be deleted before the default parent is deleted, you can explicitly delete the object by calling [**DeleteWdfObject**](https://msdn.microsoft.com/library/windows/hardware/ff560210) when the object is no longer needed.

For example, if you create a new request object and then call [**IWDFDriver::CreateWdfMemory**](https://msdn.microsoft.com/library/windows/hardware/ff558905) to create a memory object for this request, you can specify the request object as the parent of the new memory object. Because WDF deletes child objects when the parent object is deleted, the driver does not need to call [**DeleteWdfObject**](https://msdn.microsoft.com/library/windows/hardware/ff560210) to delete the memory object.

However, if there is no parent whose lifetime closely matches your object's lifetime, and if you want the object to be deleted before the default parent is deleted, you must use explicit deletion. For example, a driver could create several request objects that are used for a short duration. In this case, the driver can conserve memory by explicitly deleting the requests when they are no longer needed.

Similarly, if you are creating an object that does not allow you to override the default parent and if you want the object to be deleted before the default parent is deleted, the driver must explicitly delete the object.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Managing%20the%20Lifetime%20of%20Objects%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




