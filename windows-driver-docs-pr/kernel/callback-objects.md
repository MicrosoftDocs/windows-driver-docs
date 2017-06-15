---
title: Callback Objects
author: windows-driver-content
description: Callback Objects
MS-HAID:
- 'Synchro\_28a0b6f1-b5eb-4c4e-81dd-efd4724b29a7.xml'
- 'kernel.callback\_objects'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d6ccb064-5936-4996-a5cd-795803958b5d
keywords: ["synchronization WDK kernel , callback objects", "callback objects WDK kernel", "objects WDK callback objects", "kernel callback mechanism WDK"]
---

# Callback Objects


## <a href="" id="ddk-callback-objects-kg"></a>


The kernel's callback mechanism provides a general way for drivers to request and provide notification when certain conditions are satisfied.

A driver can create a callback object, and other drivers can request notification for conditions associated with this driver-defined callback. In addition, the system defines two callback objects for driver use.

Every callback object has a name and a set of attributes, defined when the object is created. The system-defined callback objects are named **\\Callback\\SetSystemTime**, **\\Callback\\PowerState**, and **\\Callback\\ProcessorAdd**; driver-defined callbacks must not duplicate these names.

To request notification from a system- or driver-defined callback, a driver opens the callback object and registers a callback routine. When the conditions defined for the callback become true, its creator triggers notification. In turn, the system calls all the callback routines registered for the callback.

This section contains the following topics:

[Defining a Callback Object](defining-a-callback-object.md)

[Using a Driver-Defined Callback Object](using-a-driver-defined-callback-object.md)

[Using a System-Defined Callback Object](using-a-system-defined-callback-object.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Callback%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


