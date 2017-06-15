---
title: Flushing Cached Data during PIO Operations
author: windows-driver-content
description: Flushing Cached Data during PIO Operations
MS-HAID:
- 'ioprogpio\_dd3fb7f6-e0d9-476f-b7fa-1311621f5564.xml'
- 'kernel.flushing\_cached\_data\_during\_pio\_operations'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8b15f1c4-d3c9-4d61-be37-ee1593f9d5e5
keywords: ["flushing cached data", "KeFlushIoBuffers", "PIO transfer operations WDK kernel"]
---

# Flushing Cached Data during PIO Operations


## <a href="" id="ddk-flushing-cached-data-during-pio-operations-kg"></a>


On some platforms, the instruction and data caches in the processor exhibit cache coherency anomalies during PIO read operations.

**Note**   To maintain data integrity during their read operations, drivers that use PIO must follow this guideline:
Call [**KeFlushIoBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff552041) at the end of each read operation.

For example, a driver making a PIO transfer from its device to system memory should call **KeFlushIoBuffers** at the end of each device transfer operation. As another example, a driver that reads a sequence of device registers into system memory should call **KeFlushIoBuffers** at the end of the sequence. Otherwise, such a driver might attempt to access data that is still in the processor's data cache, rather than in system memory, on some platforms.

 

**KeFlushIoBuffers** does nothing if the processor can be relied on to maintain cache coherency, so calls to this support routine have almost no overhead in such a platform.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Flushing%20Cached%20Data%20during%20PIO%20Operations%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


