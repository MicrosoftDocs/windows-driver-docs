---
title: AddConnectionToSession
description: AddConnectionToSession
ms.assetid: c2762e75-8732-4c48-83a9-24ccd39218eb
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# AddConnectionToSession


The **AddConnectionToSession** method instructs the miniport driver that manages an iSCSI initiator HBA to add a new connection to a logon session.

Miniport drivers that support the [MSiSCSI\_Operations class](msiscsi-operations-wmi-class.md) must provide at least a stub for this method, but the implementation of the method's functionality is optional. If the method does not implement the add connection functionality, it should return an error.

**AddConnectionToSession** belongs to the unpublished MSiSCSI\_Operations WMI Class. For a description of the parameters of the **AddConnectionToSession** method, see the member descriptions for the [**AddConnectionToSession\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff550122) and [**AddConnectionToSession\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff550123) structures.

 

 





