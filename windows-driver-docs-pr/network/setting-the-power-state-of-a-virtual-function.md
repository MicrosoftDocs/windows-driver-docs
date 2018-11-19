---
title: Setting the Power State of a Virtual Function
description: Setting the Power State of a Virtual Function
ms.assetid: 7504677D-9B3A-47A2-9990-7BBF50A832EA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the Power State of a Virtual Function


An overlying driver issues an object identifier (OID) set request of [OID\_SRIOV\_SET\_VF\_POWER\_STATE](https://msdn.microsoft.com/library/windows/hardware/hh451896) to change the power state of a specified PCI Express (PCIe) Virtual Function (VF) on the network adapter. Because changing the power state is a privileged operation, overlying drivers issue this OID set request to the miniport driver of the PCIe Physical Function (PF) on the network adapter. The PF miniport driver then sets the specified power state on the VF.

For example, the virtualization stack manages the power state of the Hyper-V child partition that is attached to the VF. The stack changes the power state by issuing the [OID\_SRIOV\_SET\_VF\_POWER\_STATE](https://msdn.microsoft.com/library/windows/hardware/hh451896) to the PF miniport driver.

Before it issues the OID set request of [OID\_SRIOV\_SET\_VF\_POWER\_STATE](https://msdn.microsoft.com/library/windows/hardware/hh451896), the overlying driver must set the members of [**NDIS\_SRIOV\_SET\_VF\_POWER\_STATE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451683) structure in the following way:

-   The **VFId** member must be set to the identifier of the VF from which the information is to be read.

-   The **PowerState** member must be set to the power state that the VF should transition to.

-   If the network adapter must have its WAKE\# signal (on the PCI Express bus) or PME\# signal (on the PCI bus) asserted as it goes into the low-power state, the **WakeEnable** member must be set to TRUE. Otherwise, this member must be set to FALSE.

When the PF miniport driver is issued this OID set request, it must follow these guidelines:

-   The PF miniport driver must verify that the VF, specified by the **VFId** member of the [**NDIS\_SRIOV\_SET\_VF\_POWER\_STATE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451683) structure, has resources that have been previously allocated. The PF miniport driver allocates resources for a VF during an OID method request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451814). If the specified VF is not in an allocated state, the driver must fail the OID request.

-   The power state operation must only affect the specified VF. The operation must not affect other VFs or the PF on the same network adapter.

 

 





