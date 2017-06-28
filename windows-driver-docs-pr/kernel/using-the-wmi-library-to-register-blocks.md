---
title: Using the WMI Library to Register Blocks
author: windows-driver-content
description: Using the WMI Library to Register Blocks
ms.assetid: 1f4b773d-ca24-47f5-87e8-84c98dad9267
keywords: ["WMI WDK kernel , registering with WMI", "registering WMI data providers", "data providers WDK WMI", "driver registrations WDK WMI", "event blocks WDK WMI", "blocks WDK WMI", "IRP_MN_REGINFO", "IRP_MN_REGINFO_EX", "registering blocks"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using the WMI Library to Register Blocks


## <a href="" id="ddk-using-the-wmi-library-to-register-blocks-kg"></a>


A driver can use the WMI Library to handle [**IRP\_MN\_REGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551731) and [**IRP\_MN\_REGINFO\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff551734) requests if it is registering blocks that do not use dynamic instance names, or that use static instance names based on a PDO or driver-defined base name string. In this case, the driver:

1.  Calls [**WmiSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff565834) with a pointer to the driver's device object, a pointer to a [**WMILIB\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff565813) structure, and a pointer to the IRP

    The **WMILIB\_CONTEXT** structure indicates the number of blocks to register (**GuidCount**) and points to a list of [**WMIGUIDREGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff565811) structures (**GuidList**) that specify the GUID, the number of instances, and registration flags that pertain to the corresponding block. It also defines entry points for the driver's required and optional *DpWmiXxx* callback routines.

2.  When WMI calls the driver's [*DpWmiQueryReginfo*](https://msdn.microsoft.com/library/windows/hardware/ff544097) routine, the driver specifies the driver's registry path, its MOF resource name, registration flags that pertain to all of its blocks, and information that WMI uses to name instances of the driver's data blocks, which could be either a pointer to the physical device object passed to the driver's [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine or a string on which to base static instance names.

A driver must initialize entry points for its *DpWmiXxx* callback routines in the **WMILIB\_CONTEXT** structure before calling **WmiSystemControl**, but can postpone initialization of **GuidCount** and **GuidList** in the **WMILIB\_CONTEXT** structure until WMI calls the driver's *DpWmiQueryReginfo* routine.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20the%20WMI%20Library%20to%20Register%20Blocks%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


