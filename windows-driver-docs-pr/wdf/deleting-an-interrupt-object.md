---
title: Deleting an Interrupt Object
description: Deleting an Interrupt Object
ms.assetid: B72DA452-B22F-47CD-8C5D-E741F09F556E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deleting an Interrupt Object


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

If the driver creates an interrupt object by calling [**IWDFDevice3::CreateInterrupt**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nf-wudfddi-iwdfdevice3-createinterrupt), the driver does not need to delete the interrupt object. The framework deletes the interrupt object automatically because the interrupt object is a child object of the framework device object.

The framework uses the following rules:

-   If the driver calls [**CreateInterrupt**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nf-wudfddi-iwdfdevice3-createinterrupt) from its [**OnPrepareHardware**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nf-wudfddi-ipnpcallbackhardware2-onpreparehardware) callback method, the framework deletes the interrupt object after the driver returns from its [**OnReleaseHardware**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nf-wudfddi-ipnpcallbackhardware2-onreleasehardware) callback.

-   If the driver calls [**CreateInterrupt**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nf-wudfddi-iwdfdevice3-createinterrupt) from its [**OnDeviceAdd**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) callback method, the framework deletes the interrupt object when the device is removed.

Optionally, the driver can call [**IWDFObject::DeleteWdfObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nf-wudfddi-iwdfobject-deletewdfobject) to delete an interrupt object at any time. Because a driver cannot create a new interrupt object outside of [**OnDeviceAdd**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) or [**OnPrepareHardware**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nf-wudfddi-ipnpcallbackhardware2-onpreparehardware), manual deletion of the object should not be used unless the driver must remove the object before the framework deletes it.

 

 





