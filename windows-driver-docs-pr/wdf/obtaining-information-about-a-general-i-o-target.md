---
title: Obtaining Information About a General I/O Target
description: Obtaining Information About a General I/O Target
keywords:
- general I/O targets WDK KMDF , information about
- status information WDK KMDF , general I/O targets
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining Information About a General I/O Target


To obtain information about an I/O target, your driver can call the following methods that the I/O target object defines:

<a href="" id="---------wdfiotargetgetdevice--------"></a>[**WdfIoTargetGetDevice**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetgetdevice)  
Returns the framework device object that is associated with a local or remote I/O target.

<a href="" id="wdfiotargetquerytargetproperty-or-wdfiotargetallocandquerytargetproperty"></a>[**WdfIoTargetQueryTargetProperty**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetquerytargetproperty) or [**WdfIoTargetAllocAndQueryTargetProperty**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetallocandquerytargetproperty)  
Retrieves device properties that are associated with a local or remote I/O target's device.

<a href="" id="---------wdfiotargetgetstate--------"></a>[**WdfIoTargetGetState**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetgetstate)  
Returns state information for a local or remote I/O target.

<a href="" id="---------wdfiotargetwdmgettargetdeviceobject--------"></a>[**WdfIoTargetWdmGetTargetDeviceObject**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetwdmgettargetdeviceobject)  
Returns a pointer to the Windows Driver Model (WDM) device object that is associated with a local or remote I/O target.

<a href="" id="---------wdfiotargetwdmgettargetphysicaldevice--------"></a>[**WdfIoTargetWdmGetTargetPhysicalDevice**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetwdmgettargetphysicaldevice)  
Returns a pointer to the WDM physical device object (PDO) that represents a remote I/O target's device.

<a href="" id="---------wdfiotargetwdmgettargetfileobject--------"></a>[**WdfIoTargetWdmGetTargetFileObject**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetwdmgettargetfileobject)  
Returns a pointer to the WDM file object that is associated with a remote I/O target.

<a href="" id="wdfiotargetwdmgettargetfilehandle"></a>[**WdfIoTargetWdmGetTargetFileHandle**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetwdmgettargetfilehandle)  
Returns a handle to the file that is associated with a remote I/O target.

 

