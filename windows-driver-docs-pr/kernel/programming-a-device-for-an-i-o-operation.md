---
title: Programming a Device for an I/O Operation
author: windows-driver-content
description: Programming a Device for an I/O Operation
MS-HAID:
- 'Intrupts\_4e6e480f-ef75-4ef2-a1ed-72b8255f034d.xml'
- 'kernel.programming\_a\_device\_for\_an\_i\_o\_operation'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 952b07d8-81e3-40ec-8acd-be1143a7d2a2
keywords: ["critical section routines WDK kernel", "I/O WDK kernel , device programming"]
---

# Programming a Device for an I/O Operation


## <a href="" id="ddk-programming-a-device-for-an-i-o-operation-kg"></a>


Use the following general guidelines for designing, writing, and calling [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routines that program a device for I/O operations:

-   A *SynchCritSection* routine that programs the device for I/O operations must return control as quickly as possible.

    For this reason, the *SynchCritSection* routine should do only what is necessary to set up the device for I/O. Therefore, the driver should perform all IRP preprocessing, initializing state information for other driver routines, and acquiring hardware resources before it calls the *SynchCritSection* routine.

-   A device driver can have multiple *SynchCritSection* routines to program the device.

    For example, the driver of a device for which setting up a read request differs markedly from setting up certain device control requests might have separate *SynchCritSection* routines to program its device for each type of request.

-   Every *SynchCritSection* routine must return control as quickly as possible, because running any *SynchCritSection* routine prevents the driver's ISR from executing.

    You should not write a single, large, general-purpose *SynchCritSection* routine with a **switch** statement or many nested **if..then..else** statements to determine what operations it will carry out or what state information to update. On the other hand, you should avoid writing numerous *SynchCritSection* routines that program only a single device register.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Programming%20a%20Device%20for%20an%20I/O%20Operation%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


