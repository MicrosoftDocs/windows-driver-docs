---
title: Using a System-Defined Callback Object
author: windows-driver-content
description: Using a System-Defined Callback Object
MS-HAID:
- 'Synchro\_589ac7e9-aa71-475a-9bd2-4cefa1ad097b.xml'
- 'kernel.using\_a\_system\_defined\_callback\_object'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1f1a2fc1-e698-41f7-84e4-9db091def690
keywords: ["callback objects WDK kernel", "system-defined callback objects WDK kernel"]
---

# Using a System-Defined Callback Object


## <a href="" id="ddk-using-a-system-defined-callback-object-kg"></a>


The system defines three callback objects for driver use:

**\\Callback\\SetSystemTime**

**\\Callback\\PowerState**

**\\Callback\\ProcessorAdd**

Drivers that use the system time (for example, file system drivers) might register for the **\\Callback\\SetSystemTime** callback object. This callback provides for notification when the system time changes.

The **\\Callback\\PowerState** callback object provides for notification when one of the following occurs:

-   The system switches from AC to DC power or vice versa.

-   The system power policy changes as the result of a user or application request.

-   A transition to a system sleep or shutdown state is imminent. A driver can request notification so that it can lock code into memory in anticipation of shutdown. Callback routines will be notified before the power manager sends the system set-power IRP.

The **\\Callback\\ProcessorAdd** callback provides notification when a new processor is added to the system.

To use a system-defined callback, a driver initializes an attribute block ([**InitializeObjectAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff547804)) with the callback's name, then opens the callback object ([**ExCreateCallback**](https://msdn.microsoft.com/library/windows/hardware/ff544560)), just as for a driver-defined callback. The driver should not request that the callback object be created.

With the handle returned by **ExCreateCallback**, the driver calls [**ExRegisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff545534) to register a notification routine, passing a pointer to an arbitrary context and a pointer to its routine. A driver can register its callback routine any time. When the specified condition occurs, the system calls the registered callback routine at IRQL&lt;=DISPATCH\_LEVEL.

When the driver no longer requires notification, it should call [**ExUnregisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff545649) to delete its callback routine from the list of registered callbacks and to remove its reference to the callback object.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20a%20System-Defined%20Callback%20Object%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


