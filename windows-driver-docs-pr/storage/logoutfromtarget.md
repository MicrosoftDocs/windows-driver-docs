---
title: LogoutFromTarget
description: LogoutFromTarget
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# LogoutFromTarget


The **LogoutFromTarget** method instructs the miniport driver that manages the iSCSI initiator HBA to log off a target and removes the target's logical units from the local computer's device stack.

Miniport drivers that implement the [MSiSCSI\_Operations WMI class](msiscsi-operations-wmi-class.md) are not required to support this method.

The MSiSCSI\_Operations WMI class is unpublished. For a description of the parameters of the **LogoutFromTarget** method, see the member descriptions for the [**LogoutFromTarget\_IN**](/windows-hardware/drivers/ddi/iscsiop/ns-iscsiop-_logoutfromtarget_in) and [**LogoutFromTarget\_OUT**](/windows-hardware/drivers/ddi/iscsiop/ns-iscsiop-_logoutfromtarget_out) structures.

 

