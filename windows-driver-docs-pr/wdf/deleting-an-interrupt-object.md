---
title: Deleting an Interrupt Object
description: Deleting an Interrupt Object
ms.date: 04/20/2017
---

# Deleting an Interrupt Object


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

If the driver creates an interrupt object by calling [**IWDFDevice3::CreateInterrupt**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice3-createinterrupt), the driver does not need to delete the interrupt object. The framework deletes the interrupt object automatically because the interrupt object is a child object of the framework device object.

The framework uses the following rules:

-   If the driver calls [**CreateInterrupt**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice3-createinterrupt) from its [**OnPrepareHardware**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardware2-onpreparehardware) callback method, the framework deletes the interrupt object after the driver returns from its [**OnReleaseHardware**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardware2-onreleasehardware) callback.

-   If the driver calls [**CreateInterrupt**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice3-createinterrupt) from its [**OnDeviceAdd**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) callback method, the framework deletes the interrupt object when the device is removed.

Optionally, the driver can call [**IWDFObject::DeleteWdfObject**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfobject-deletewdfobject) to delete an interrupt object at any time. Because a driver cannot create a new interrupt object outside of [**OnDeviceAdd**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) or [**OnPrepareHardware**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardware2-onpreparehardware), manual deletion of the object should not be used unless the driver must remove the object before the framework deletes it.

 

