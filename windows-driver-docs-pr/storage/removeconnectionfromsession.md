---
title: RemoveConnectionFromSession
description: RemoveConnectionFromSession
ms.assetid: ae23713a-c75d-4669-a643-44e95dbb713c
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# RemoveConnectionFromSession


The **RemoveConnectionFromSession** method instructs the miniport driver that manages an iSCSI initiator HBA to remove a connection from a logon session.

The iSCSI initiator (that is, the virtual miniport driver) does not support sessions with multiple connections. Do not use **RemoveConnectionFromSession** with the iSCSI initiator.

The **RemoveConnectionFromSession** method will not remove the last connection from a session. You should close sessions with a single connection with the [LogoutFromTarget](logoutfromtarget.md) method.

**RemoveConnectionFromSession** belongs to the unpublished [MSiSCSI\_Operations WMI class](msiscsi-operations-wmi-class.md). For a description of the parameters of the **RemoveConnectionFromSession** method, see the member descriptions for the [**RemoveConnectionFromSession\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff563974) and [**RemoveConnectionFromSession\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff563976) structures.

Miniport drivers that implement the MSiSCSI\_Operations WMI class must support this method.

 

 





