---
title: Obtaining Information About a General I/O Target
description: Obtaining Information About a General I/O Target
ms.assetid: 70ae920e-de2d-4014-bae4-74058b26e7c0
keywords:
- general I/O targets WDK KMDF , information about
- status information WDK KMDF , general I/O targets
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





