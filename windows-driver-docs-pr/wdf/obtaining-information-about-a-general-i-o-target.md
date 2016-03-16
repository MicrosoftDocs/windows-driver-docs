---
title: Obtaining Information About a General I/O Target
description: Obtaining Information About a General I/O Target
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 70ae920e-de2d-4014-bae4-74058b26e7c0
keywords: ["general I/O targets WDK KMDF information about", "status information WDK KMDF general I/O targets"]
---

# Obtaining Information About a General I/O Target


To obtain information about an I/O target, your driver can call the following methods that the I/O target object defines:

<a href="" id="---------wdfiotargetgetdevice--------"></a>[**WdfIoTargetGetDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548625)  
Returns the framework device object that is associated with a local or remote I/O target.

<a href="" id="wdfiotargetquerytargetproperty-or-wdfiotargetallocandquerytargetproperty"></a>[**WdfIoTargetQueryTargetProperty**](https://msdn.microsoft.com/library/windows/hardware/ff548646) or [**WdfIoTargetAllocAndQueryTargetProperty**](https://msdn.microsoft.com/library/windows/hardware/ff548585)  
Retrieves device properties that are associated with a local or remote I/O target's device.

<a href="" id="---------wdfiotargetgetstate--------"></a>[**WdfIoTargetGetState**](https://msdn.microsoft.com/library/windows/hardware/ff548631)  
Returns state information for a local or remote I/O target.

<a href="" id="---------wdfiotargetwdmgettargetdeviceobject--------"></a>[**WdfIoTargetWdmGetTargetDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff548682)  
Returns a pointer to the Windows Driver Model (WDM) device object that is associated with a local or remote I/O target.

<a href="" id="---------wdfiotargetwdmgettargetphysicaldevice--------"></a>[**WdfIoTargetWdmGetTargetPhysicalDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548691)  
Returns a pointer to the WDM physical device object (PDO) that represents a remote I/O target's device.

<a href="" id="---------wdfiotargetwdmgettargetfileobject--------"></a>[**WdfIoTargetWdmGetTargetFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff548686)  
Returns a pointer to the WDM file object that is associated with a remote I/O target.

<a href="" id="wdfiotargetwdmgettargetfilehandle"></a>[**WdfIoTargetWdmGetTargetFileHandle**](https://msdn.microsoft.com/library/windows/hardware/ff548683)  
Returns a handle to the file that is associated with a remote I/O target.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Obtaining%20Information%20About%20a%20General%20I/O%20Target%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




