---
title: Defining a Callback Object
author: windows-driver-content
description: Defining a Callback Object
MS-HAID:
- 'Synchro\_e954f515-e536-4e12-8419-e7e54c4a963b.xml'
- 'kernel.defining\_a\_callback\_object'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9717795b-dd62-4f17-b931-5ca2b1237e60
keywords: ["callback objects WDK kernel", "registering callback notifications"]
---

# Defining a Callback Object


## <a href="" id="ddk-defining-a-callback-object-kg"></a>


A driver can create a callback object, through which other drivers can request notification of conditions defined by the creating driver. The following figure shows the steps involved in defining a callback object.

![diagram illustrating defining a callback object](images/3crt-cbk.png)

Before creating the object, the driver calls [**InitializeObjectAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff547804) to set its attributes. A callback object must have a name, which cannot match the name of a system-defined callback; it can have whatever other attributes its creator deems appropriate, typically OBJ\_CASE\_INSENSITIVE. Next the driver calls [**ExCreateCallback**](https://msdn.microsoft.com/library/windows/hardware/ff544560), passing a pointer to the initialized attributes and a location at which to receive a handle to the callback object. It also passes two Booleans, indicating whether the system should create the callback object if such a named object does not already exist, and whether the object should allow more than one registered callback routine.

The driver defines the conditions for which it will call the registered callback routines. The conditions take the form of two arguments, each pointing to a parameter defined by the driver that creates the callback. You should document these conditions, along with the name of the callback object and the IRQL at which it requests notification, for clients of the driver.

When the callback condition occurs, the driver calls [**ExNotifyCallback**](https://msdn.microsoft.com/library/windows/hardware/ff545489), passing its handle to the callback object and the two arguments. The system then calls all callback routines registered for the callback object, in the order in which they were registered, passing the two arguments and a pointer to the context supplied when the routine was registered. The driver must call **ExNotifyCallback** at IRQL &lt;= DISPATCH\_LEVEL; the system calls the callback routines at the same IRQL at which the driver made this call.

After all operations have been completed with the callback object, the driver that created the callback should call [**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724) to decrement its reference count and ensure that the object is deleted.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Defining%20a%20Callback%20Object%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


