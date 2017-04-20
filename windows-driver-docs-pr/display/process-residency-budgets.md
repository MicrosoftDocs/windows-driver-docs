---
title: Process residency budgets
description: In Windows Display Driver Model (WDDM) v2, processes will be assigned budgets for how much memory they can keep resident.
ms.assetid: 9A93E110-4D3F-4D08-8379-222A2D7DEFBB
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Process residency budgets


In Windows Display Driver Model (WDDM) v2, processes will be assigned budgets for how much memory they can keep resident. This budget can change over time, but generally will only be imposed when the system is under memory pressure. Prior to Microsoft Direct3D 12, the budget is handled by the user mode driver in the form of *Trim* notifications and *MakeResident* failures with **STATUS\_NO\_MEMORY**. *TrimToBudget* notification, [*Evict*](https://msdn.microsoft.com/library/windows/hardware/dn906355), and failed [*MakeResident*](https://msdn.microsoft.com/library/windows/hardware/dn906357) calls all return the latest budget in the form of an integer **NumBytesToTrim** value that indicates how much needs to be trimmed in order to fit in the new budget.

For Direct3D 12 applications, the budget is handled completely by the application. The size of the budget is meant as a cue to let the application know what to size itself to. By using the budget size as a hint, the application can decide how many resources to keep resident, what resolution and quality of resources to keep.

To properly manage these budgets, the kernel needs to know what memory should participate in the budget. There is a new **ApplicationTarget** bit in [**DXGK\_SEGMENTFLAGS2**](https://msdn.microsoft.com/library/windows/hardware/ff562044) structure that needs to be set on segments that the kernel mode driver wishes to be included in the budgeting logic. For example, on a discrete graphics processing unit (GPU) with 1 segment of VRAM thatâ€™s suitable for application usage, and 1 segment of VRAM thatâ€™s used for special-purpose resources automatically, the driver would likely only mark the primary VRAM segment as **ApplicationTarget**. For integrated GPUs, the main aperture segment will usually be the one marked. There is no limit to how many segments can be marked as **ApplicationTarget**. The kernel will aggregate these together and present the application with a unified size.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Process%20residency%20budgets%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




