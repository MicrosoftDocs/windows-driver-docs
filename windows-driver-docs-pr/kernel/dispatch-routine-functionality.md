---
title: Dispatch Routine Functionality
author: windows-driver-content
description: Dispatch Routine Functionality
MS-HAID:
- 'DrvComps\_3f0e8810-b24b-4337-8980-e3bfd40baf3f.xml'
- 'kernel.dispatch\_routine\_functionality'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cfc191af-2b65-465b-972e-9617a8f7d8b7
---

# Dispatch Routine Functionality


## <a href="" id="ddk-dispatch-routine-functionality-kg"></a>


The required functionality of a particular dispatch routine varies, depending on the I/O function code it handles, on the individual driver's position in a chain of drivers, and on the type of underlying physical device.

Most dispatch routines process incoming I/O request packets (IRPs) as follows:

1.  Check the driver's I/O stack location in the IRP to determine what to do and check the parameters, if any, for validity.

    Whether a driver must check its I/O stack location to determine what to do and to check parameters depends on the given **IRP\_MJ\_***XXX*, as well as on whether that driver set up a separate Dispatch routine for each **IRP\_MJ\_***XXX* that the driver handles.

2.  Satisfy the request and complete the IRP if possible; otherwise, pass it on for further processing by lower-level drivers or by other device driver routines.

    Whether a driver must pass on an IRP for further processing depends on the validity of the parameters, if any, as well as on the **IRP\_MJ\_***XXX* and on the driver's level, if any, in a chain of layered drivers.

For more information about IRPs, see [Handling IRPs](handling-irps.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Dispatch%20Routine%20Functionality%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


