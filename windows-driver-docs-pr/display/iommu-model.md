---
title: IoMmu model
description: In the IoMmu model each process has a single virtual address space that is shared between the CPU and graphics processing unit (GPU) and is managed by the OS memory manager.
ms.assetid: D8D5A2A8-F43A-4EC5-9355-C144EC15E754
---

# IoMmu model


In the *IoMmu* model each process has a single virtual address space that is shared between the CPU and graphics processing unit (GPU) and is managed by the OS memory manager.

To access memory, the GPU sends a data request to a compliant *IoMmu*. The request includes a shared virtual address and a *process address space identifier* (PASID). The *IoMmu* unit performs the address translation using the shared page table. This is illustrated below:

![iommu process address space translation](images/iommu-model.1.png)

The kernel mode driver expresses support for the *IoMmu* model by setting the [**DXGK\_VIDMMCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff562072)::**IoMmuSupported** caps. When this flags is set, the video memory manager will automatically register any process using the GPU with the *IoMmu* and obtain a *PASID* for that process address space. The *PASID* is passed to the driver during device creation.

Primary allocations are mapped by the video memory manager into the aperture segment before being displayed, ensuring that the display controller has physical access to these allocations.

In the *IoMmu* model, the driver continues to allocate video memory for the GPU using the video memory manager's [*Allocate*](https://msdn.microsoft.com/library/windows/hardware/ff568893) service. This allow the user mode driver to follow the residency model, support the Microsoft DirectX resource sharing model, ensure that primary surfaces are visible to the kernel, and are mapped into aperture before being displayed.

The first level of translation (*tile resource address* to *shared CPU/GPU address*) is entirely managed in user mode by the user mode driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20IoMmu%20model%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




