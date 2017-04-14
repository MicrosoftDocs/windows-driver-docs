---
title: Processing Mutex in AVStream
author: windows-driver-content
description: Processing Mutex in AVStream
ms.assetid: dd84fe3f-352e-4641-99d7-792ccecb0b40
keywords: ["AVStream mutexes WDK", "mutexes WDK AVStream", "processing mutex WDK AVStream"]
---

# Processing Mutex in AVStream


## <a href="" id="ddk-processing-mutex-in-avstream-ksg"></a>


The third mutex is the processing mutex. Individual filters and pins have their own processing mutexes. AVStream independently acquires the processing mutex before processing at the filter and pin level, in order to synchronize access to processing-related structures. AVStream also acquires the processing mutex during other operations including binding pins to a pipe section, sleep or wake power operations, and changing descriptors. Minidrivers can manually acquire the mutex to perform a synchronous operation, such as processing or descriptor modification. A minidriver should obtain the processing mutex before it makes any change that cannot happen at the same time as processing.

Like the other two types of mutexes, processing mutexes are not obtained recursively. This means that if a minidriver attempts to grab the processing mutex while processing, a deadlock occurs.

Do not use the processing mutex to suspend processing for long periods of time. Instead, manipulate the processing control gate directly by using the **KSGATE*Xxx*** functions.

A thread that has acquired a processing mutex should not subsequently attempt to acquire the filter control mutex.

To manipulate the processing mutex, use the following functions:

[**KsFilterAcquireProcessingMutex**](https://msdn.microsoft.com/library/windows/hardware/ff562524), [**KsPinAcquireProcessingMutex**](https://msdn.microsoft.com/library/windows/hardware/ff563488), [**KsFilterReleaseProcessingMutex**](https://msdn.microsoft.com/library/windows/hardware/ff562552), [**KsPinReleaseProcessingMutex**](https://msdn.microsoft.com/library/windows/hardware/ff563527)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Processing%20Mutex%20in%20AVStream%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


