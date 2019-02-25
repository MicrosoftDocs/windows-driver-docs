---
title: DeleteInitiatorNodeName
description: DeleteInitiatorNodeName
ms.assetid: 955ff574-a73b-42fa-8302-1012de5c9fee
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DeleteInitiatorNodeName


The **DeleteInitiatorNodeName** method informs the miniport driver that manages an HBA initiator that the indicated iSCSI node name is no longer valid. Under some circumstances, initiator HBAs use the node name in challenge handshake authentication protocol (CHAP) authentication.

Miniport drivers that implement the [MSiSCSI\_Operations WMI class](msiscsi-operations-wmi-class.md) are not required to support this method.

The MSiSCSI\_Operations WMI Class is unpublished. For a description of the parameters of the **DeleteInitiatorNodeName** method, see the member descriptions for the [**DeleteInitiatorNodeName\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff552505) and [**DeleteInitiatorNodeName\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff552506) structures.

 

 





