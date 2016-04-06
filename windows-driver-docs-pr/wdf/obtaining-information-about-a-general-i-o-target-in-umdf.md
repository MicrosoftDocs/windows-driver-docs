---
title: Obtaining Information About a General I/O Target in UMDF
description: Obtaining Information About a General I/O Target in UMDF
ms.assetid: 306a7f46-423a-4647-846d-76f917ca0f7c
keywords: ["general I/O targets WDK UMDF , information about", "status information WDK I/O targets"]
---

# Obtaining Information About a General I/O Target in UMDF


\[This topic applies to UMDF 1.*x*.\]

To obtain information about an I/O target, a UMDF driver can call the following methods that the I/O target object defines:

<a href="" id="iwdfiotarget--gettargetfile"></a>[**IWDFIoTarget::GetTargetFile**](https://msdn.microsoft.com/library/windows/hardware/ff559243)  
Returns the framework file object that is associated with the I/O target.

<a href="" id="iwdfiotargetstatemanagement--getstate"></a>[**IWDFIoTargetStateManagement::GetState**](https://msdn.microsoft.com/library/windows/hardware/ff559202)  
Returns state information for a local I/O target.

<a href="" id="iwdfremotetarget--getstate"></a>[**IWDFRemoteTarget::GetState**](https://msdn.microsoft.com/library/windows/hardware/ff560265)  
Returns state information for a remote I/O target.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Obtaining%20Information%20About%20a%20General%20I/O%20Target%20in%20UMDF%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




