---
title: Storage Requirements for AdapterControl Routines
author: windows-driver-content
description: Storage Requirements for AdapterControl Routines
MS-HAID:
- 'ioprogdma\_6f6f6cd1-999d-4283-8b3b-20b38103a482.xml'
- 'kernel.storage\_requirements\_for\_adaptercontrol\_routines'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5e5711df-9acd-4ac5-b6b2-4e90299afb24
keywords: ["AdapterControl routines, storage", "AdapterControl routines, writing", "adapter objects WDK kernel , writing AdapterControl routines", "DMA transfers WDK kernel , writing AdapterControl routines", "storage WDK DMA"]
---

# Storage Requirements for AdapterControl Routines


## <a href="" id="ddk-storage-requirements-for-adaptercontrol-routines-kg"></a>


If it has an [*AdapterControl*](https://msdn.microsoft.com/library/windows/hardware/ff540504) routine, a driver must provide resident storage for the following:

-   Context information to be used in its DMA operations

-   An adapter object pointer returned by [**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220)

-   A ULONG-type variable to hold the system-determined maximum *NumberOfMapRegisters* available for any given DMA transfer request

The driver can provide the necessary storage in a device extension, in a controller extension, or in nonpaged pool allocated by the driver.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Storage%20Requirements%20for%20AdapterControl%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


