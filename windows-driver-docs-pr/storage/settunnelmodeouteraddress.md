---
title: SetTunnelModeOuterAddress
description: SetTunnelModeOuterAddress
ms.date: 10/17/2018
---

# SetTunnelModeOuterAddress


The **SetTunnelModeOuterAddress** allows a management application to specify the tunnel-mode outer address that a port uses on an initiator HBA.

In tunnel mode, an inner-encrypted IP packet is nested within an outer IP packet that contains the address of the security gateway. The **SetTunnelModeOuterAddress** method allows a management application to indicate the address of the security gateway that is associated with IP packets that pass through the indicated port.

The initiator HBA or HBA miniport driver should maintain the default tunnel-mode outer address in nonvolatile storage if nonvolatile storage is available

**SetTunnelModeOuterAddress** belongs to the unpublished [MSiSCSI\_SecurityConfigOperations WMI class](msiscsi-securityconfigoperations-wmi-class.md). For a description of the parameters of the **SetTunnelModeOuterAddress** method, see the member descriptions for the [**SetTunnelModeOuterAddress\_IN**](/windows-hardware/drivers/ddi/iscsiop/ns-iscsiop-_settunnelmodeouteraddress_in) and [**SetTunnelModeOuterAddress\_OUT**](/windows-hardware/drivers/ddi/iscsiop/ns-iscsiop-_settunnelmodeouteraddress_out) structures.

Miniport drivers that implement the MSiSCSI\_SecurityConfigOperations WMI class must support **SetTunnelModeOuterAddress**.

 

