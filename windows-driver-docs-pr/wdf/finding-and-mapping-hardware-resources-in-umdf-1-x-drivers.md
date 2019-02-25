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

A UMDF 1.x driver receives hardware resources in its [**IPnpCallbackHardware2::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/hh439734) callback method. The driver uses the [**IWDFCmResourceList**](https://msdn.microsoft.com/library/windows/hardware/hh439762) interface to review the translated resource list and identify memory-mapped registers, I/O ports, and interrupts.

The driver iterates through the resource list by calling [**IWDFCmResourceList::GetCount**](https://msdn.microsoft.com/library/windows/hardware/hh439767) and [**IWDFCmResourceList::GetDescriptor**](https://msdn.microsoft.com/library/windows/hardware/hh439771).

If the driver receives memory-mapped registers, the driver must call [**IWDFDevice3::MapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/hh451225) to map the registers before it can access them. Typically, a driver maps its registers in its [**IPnpCallbackHardware2::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/hh439734) method. The driver unmaps the registers in its [**IPnpCallbackHardware2::OnReleaseHardware**](https://msdn.microsoft.com/library/windows/hardware/hh439739) callback by calling [**IWDFDevice3::UnmapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/hh451237). Note that mapping is not needed for I/O ports.

For an example that shows how a driver finds and maps memory-mapped register resources, see [**IWDFDevice3::MapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/hh451225).

 

 





