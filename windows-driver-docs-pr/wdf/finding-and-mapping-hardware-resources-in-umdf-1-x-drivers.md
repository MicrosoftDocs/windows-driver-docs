---
title: Finding and Mapping Hardware Resources in UMDF 1.x Drivers
description: Finding and Mapping Hardware Resources in UMDF 1.x Drivers
ms.assetid: 51CB254D-1B2C-43F5-925A-209810E2F5FC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Finding and Mapping Hardware Resources in UMDF 1.x Drivers


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

If you are using UMDF version 2.0 or later, see [Finding and Mapping Hardware Resources](finding-and-mapping-hardware-resources.md).

A UMDF 1.x driver receives hardware resources in its [**IPnpCallbackHardware2::OnPrepareHardware**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nf-wudfddi-ipnpcallbackhardware2-onpreparehardware) callback method. The driver uses the [**IWDFCmResourceList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nn-wudfddi-iwdfcmresourcelist) interface to review the translated resource list and identify memory-mapped registers, I/O ports, and interrupts.

The driver iterates through the resource list by calling [**IWDFCmResourceList::GetCount**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nf-wudfddi-iwdfcmresourcelist-getcount) and [**IWDFCmResourceList::GetDescriptor**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nf-wudfddi-iwdfcmresourcelist-getdescriptor).

If the driver receives memory-mapped registers, the driver must call [**IWDFDevice3::MapIoSpace**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nf-wudfddi-iwdfdevice3-mapiospace) to map the registers before it can access them. Typically, a driver maps its registers in its [**IPnpCallbackHardware2::OnPrepareHardware**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nf-wudfddi-ipnpcallbackhardware2-onpreparehardware) method. The driver unmaps the registers in its [**IPnpCallbackHardware2::OnReleaseHardware**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nf-wudfddi-ipnpcallbackhardware2-onreleasehardware) callback by calling [**IWDFDevice3::UnmapIoSpace**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nf-wudfddi-iwdfdevice3-unmapiospace). Note that mapping is not needed for I/O ports.

For an example that shows how a driver finds and maps memory-mapped register resources, see [**IWDFDevice3::MapIoSpace**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wudfddi/nf-wudfddi-iwdfdevice3-mapiospace).

 

 





