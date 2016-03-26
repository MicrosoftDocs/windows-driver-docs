---
title: Finding and Mapping Hardware Resources in UMDF 1.x Drivers
description: Finding and Mapping Hardware Resources in UMDF 1.x Drivers
ms.assetid: 51CB254D-1B2C-43F5-925A-209810E2F5FC
---

# Finding and Mapping Hardware Resources in UMDF 1.x Drivers


\[This topic applies to UMDF 1.*x*.\]

If you are using UMDF version 2.0 or later, see [Finding and Mapping Hardware Resources](finding-and-mapping-hardware-resources.md).

A UMDF 1.x driver receives hardware resources in its [**IPnpCallbackHardware2::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/hh439734) callback method. The driver uses the [**IWDFCmResourceList**](https://msdn.microsoft.com/library/windows/hardware/hh439762) interface to review the translated resource list and identify memory-mapped registers, I/O ports, and interrupts.

The driver iterates through the resource list by calling [**IWDFCmResourceList::GetCount**](https://msdn.microsoft.com/library/windows/hardware/hh439767) and [**IWDFCmResourceList::GetDescriptor**](https://msdn.microsoft.com/library/windows/hardware/hh439771).

If the driver receives memory-mapped registers, the driver must call [**IWDFDevice3::MapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/hh451225) to map the registers before it can access them. Typically, a driver maps its registers in its [**IPnpCallbackHardware2::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/hh439734) method. The driver unmaps the registers in its [**IPnpCallbackHardware2::OnReleaseHardware**](https://msdn.microsoft.com/library/windows/hardware/hh439739) callback by calling [**IWDFDevice3::UnmapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/hh451237). Note that mapping is not needed for I/O ports.

For an example that shows how a driver finds and maps memory-mapped register resources, see [**IWDFDevice3::MapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/hh451225).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Finding%20and%20Mapping%20Hardware%20Resources%20in%20UMDF%201.x%20Drivers%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




