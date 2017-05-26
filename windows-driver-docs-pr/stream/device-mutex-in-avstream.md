---
title: Device Mutex in AVStream
author: windows-driver-content
description: Device Mutex in AVStream
ms.assetid: cec2a040-59d6-44ef-aef1-04f434811d60
keywords:
- AVStream mutexes WDK
- mutexes WDK AVStream
- device mutex WDK AVStream
- synchronization WDK AVStream
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Device Mutex in AVStream


## <a href="" id="ddk-device-mutex-in-avstream-ksg"></a>


Use the device mutex to synchronize objects in the hierarchy from the device down to the filters. Each AVStream device has a single associated device mutex. Creation and destruction of both filter factories and filters are synchronized with this mutex. Certain Plug and Play and power management operations are also synchronized with this mutex. The minidriver focuses on two main issues with regard to the device mutex.

The object hierarchy is guaranteed to be stable *only* from the device down to individual filters if the device mutex is held. As a result, the minidriver must obtain the device mutex before manually creating filter factories by calling [**KsCreateFilterFactory**](https://msdn.microsoft.com/library/windows/hardware/ff561650). The minidriver must also obtain the device mutex before traversing the object hierarchy by calling the **Ks***Xxx***GetFirstChild***Xxx* and **Ks***Xxx***GetNextSibling***Xxx* functions.

AVStream holds the device mutex on behalf of the minidriver when it receives the following requests:

-   [**IRP\_MN\_QUERY\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551725)

-   [**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551705)

-   [*PostStart dispatch*](https://msdn.microsoft.com/library/windows/hardware/ff554284)

-   [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749)

-   [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699)

-   [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744)

-   Sleep and wake notifications on filters and pins. See [**KsFilterRegisterPowerCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff562550) and [**KsPinRegisterPowerCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff563525).

It is important to note that the device mutex cannot be obtained recursively. Consider the following example. AVStream receives a sleep notification. As described above, it takes the device mutex on behalf of the minidriver. If AVStream then calls a minidriver-provided callback routine in the context of thread A, the minidriver must not subsequently attempt to obtain the device mutex in thread A. Doing so causes thread A to deadlock with itself.

AVStream often obtains filter control mutexes while the device mutex is already held. Consequently, as a general rule, a thread that has taken a filter control mutex should not subsequently take the device mutex.

To manipulate the device mutex, use the following functions:

[**KsAcquireDevice**](https://msdn.microsoft.com/library/windows/hardware/ff560911), [**KsReleaseDevice**](https://msdn.microsoft.com/library/windows/hardware/ff566783)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Device%20Mutex%20in%20AVStream%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


