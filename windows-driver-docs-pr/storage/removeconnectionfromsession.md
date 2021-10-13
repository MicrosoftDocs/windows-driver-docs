---
title: RemoveConnectionFromSession
description: RemoveConnectionFromSession
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# RemoveConnectionFromSession


The **RemoveConnectionFromSession** method instructs the miniport driver that manages an iSCSI initiator HBA to remove a connection from a logon session.

The iSCSI initiator (that is, the virtual miniport driver) does not support sessions with multiple connections. Do not use **RemoveConnectionFromSession** with the iSCSI initiator.

The **RemoveConnectionFromSession** method will not remove the last connection from a session. You should close sessions with a single connection with the [LogoutFromTarget](logoutfromtarget.md) method.

**RemoveConnectionFromSession** belongs to the unpublished [MSiSCSI\_Operations WMI class](msiscsi-operations-wmi-class.md). For a description of the parameters of the **RemoveConnectionFromSession** method, see the member descriptions for the [**RemoveConnectionFromSession\_IN**](/windows-hardware/drivers/ddi/iscsiop/ns-iscsiop-_removeconnectionfromsession_in) and [**RemoveConnectionFromSession\_OUT**](/windows-hardware/drivers/ddi/iscsiop/ns-iscsiop-_removeconnectionfromsession_out) structures.

Miniport drivers that implement the MSiSCSI\_Operations WMI class must support this method.

 

