---
title: Finding and Mapping Hardware Resources in UMDF 1.x Drivers
description: Finding and Mapping Hardware Resources in UMDF 1.x Drivers
ms.date: 04/20/2017
---

# Finding and Mapping Hardware Resources in UMDF 1.x Drivers


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

If you are using UMDF version 2.0 or later, see [Finding and Mapping Hardware Resources](finding-and-mapping-hardware-resources.md).

A UMDF 1.x driver receives hardware resources in its [**IPnpCallbackHardware2::OnPrepareHardware**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardware2-onpreparehardware) callback method. The driver uses the [**IWDFCmResourceList**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfcmresourcelist) interface to review the translated resource list and identify memory-mapped registers, I/O ports, and interrupts.

The driver iterates through the resource list by calling [**IWDFCmResourceList::GetCount**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfcmresourcelist-getcount) and [**IWDFCmResourceList::GetDescriptor**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfcmresourcelist-getdescriptor).

If the driver receives memory-mapped registers, the driver must call [**IWDFDevice3::MapIoSpace**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice3-mapiospace) to map the registers before it can access them. Typically, a driver maps its registers in its [**IPnpCallbackHardware2::OnPrepareHardware**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardware2-onpreparehardware) method. The driver unmaps the registers in its [**IPnpCallbackHardware2::OnReleaseHardware**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardware2-onreleasehardware) callback by calling [**IWDFDevice3::UnmapIoSpace**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice3-unmapiospace). Note that mapping is not needed for I/O ports.

For an example that shows how a driver finds and maps memory-mapped register resources, see [**IWDFDevice3::MapIoSpace**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice3-mapiospace).

 

