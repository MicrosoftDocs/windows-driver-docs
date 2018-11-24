---
title: Reset (surprise remove) steps 15-20
description: The steps of reset (surprise-remove), which are Steps 15 through 20, are described below. The steps correspond to the diagram shown in UE hang detection and recovery flow.
ms.assetid: E72714A9-9B06-4609-820C-F25DC6BC0696
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reset (surprise remove): steps 15-20


The steps of reset (surprise-remove), which are Steps 15 through 20, are described below. The steps correspond to the diagram shown in [UE hang detection and recovery flow](wdi-ue-hang-detection-and-recovery-flow.md).

Once the Reset Recovery can proceed, the bus causes PnP to generate a surprise-remove IRP. When NDIS receives the surprise-remove IRP, it calls back WDI for a surprise-remove PnP event callback. WDI forwards the surprise-remove as a WDI command to the LE, where the LE returns the hung WDI command. The rest of flow is identical to a real device surprise-remove on a bus (for example, USB).

Cleanup commands flow to the LE to facilitate the return of resources. In this state, the LE should not touch the hardware.

| Step | Action                                                                                                                                                               |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 15   | NDIS calls back the PnP event for surprise-remove.                                                                                                                   |
| 16   | WDI calls back the LE for surprise-remove.                                                                                                                           |
| 17   | The LE returns the hung WDI command. The LE only needs a slot for outstanding WDI commands because WDI serializes WDI commands to the LE, except Diagnose and Abort. |
| 18   | WDI ignores the return of the hung WDI command because it has returned the original NDIS command.                                                                    |
| 19   | The LE returns WDI surprise-remove.                                                                                                                                  |
| 20   | WDI returns NDIS PnP callbacks for surprise-remove.                                                                                                                  |

 

## Related topics


[UE hang detection: steps 1-14](wdi-ue-hang-detection--step-1-to-step-14.md)

[UE hang detection and recovery flow](wdi-ue-hang-detection-and-recovery-flow.md)

 

 






