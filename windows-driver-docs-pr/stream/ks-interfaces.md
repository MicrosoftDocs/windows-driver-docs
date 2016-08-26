---
title: KS Interfaces
author: windows-driver-content
description: KS Interfaces
MS-HAID:
- 'ks-overview\_66fbd820-9191-4a1f-ba6e-07913ed402e0.xml'
- 'stream.ks\_interfaces'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cc6fad32-0587-44a8-92d1-54bc0370e5c0
keywords: ["interfaces WDK kernel streaming", "KSPIN_INTERFACE", "kernel streaming WDK , interfaces", "KS WDK , interfaces"]
---

# KS Interfaces


## <a href="" id="ddk-ks-interfaces-ksg"></a>


An *Interface* is a descriptor parameter that defines how a pin communicates. The minidriver indicates which interfaces a pin supports by providing a pointer to an array of [**KSPIN\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff563537) structures in the relevant [**KSPIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563533) structure. KS then uses this information for determining potential connectivity and graph building.

Like mediums, interfaces are also described as a set and as an element of that set. The KSPIN\_INTERFACE structure defines a specific interface within an interface set.

The user-mode client then specifies the type of interface for a connection by using the **Interface** member of the relevant [**KSPIN\_CONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff563531) structure. The client passes this KSPIN\_CONNECT instance in a call to [**KsCreatePin**](https://msdn.microsoft.com/library/windows/hardware/ff561652), which results in an IRP\_MJ\_CREATE being sent to the minidriver.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KS%20Interfaces%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


