---
title: Process residency budgets
description: In Windows Display Driver Model (WDDM) v2, processes will be assigned budgets for how much memory they can keep resident.
ms.assetid: 9A93E110-4D3F-4D08-8379-222A2D7DEFBB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Process residency budgets


In Windows Display Driver Model (WDDM) v2, processes will be assigned budgets for how much memory they can keep resident. This budget can change over time, but generally will only be imposed when the system is under memory pressure. Prior to Microsoft Direct3D 12, the budget is handled by the user mode driver in the form of *Trim* notifications and *MakeResident* failures with **STATUS\_NO\_MEMORY**. *TrimToBudget* notification, [*Evict*](https://msdn.microsoft.com/library/windows/hardware/dn906355), and failed [*MakeResident*](https://msdn.microsoft.com/library/windows/hardware/dn906357) calls all return the latest budget in the form of an integer **NumBytesToTrim** value that indicates how much needs to be trimmed in order to fit in the new budget.

For Direct3D 12 applications, the budget is handled completely by the application. The size of the budget is meant as a cue to let the application know what to size itself to. By using the budget size as a hint, the application can decide how many resources to keep resident, what resolution and quality of resources to keep.

To properly manage these budgets, the kernel needs to know what memory should participate in the budget. There is a new **ApplicationTarget** bit in [**DXGK\_SEGMENTFLAGS2**](https://msdn.microsoft.com/library/windows/hardware/ff562044) structure that needs to be set on segments that the kernel mode driver wishes to be included in the budgeting logic. For example, on a discrete graphics processing unit (GPU) with 1 segment of VRAM that's suitable for application usage, and 1 segment of VRAM that's used for special-purpose resources automatically, the driver would likely only mark the primary VRAM segment as **ApplicationTarget**. For integrated GPUs, the main aperture segment will usually be the one marked. There is no limit to how many segments can be marked as **ApplicationTarget**. The kernel will aggregate these together and present the application with a unified size.

 

 





