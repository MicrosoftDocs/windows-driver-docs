---
title: DeleteInitiatorNodeName
description: DeleteInitiatorNodeName
ms.assetid: 955ff574-a73b-42fa-8302-1012de5c9fee
---

# DeleteInitiatorNodeName


The **DeleteInitiatorNodeName** method informs the miniport driver that manages an HBA initiator that the indicated iSCSI node name is no longer valid. Under some circumstances, initiator HBAs use the node name in challenge handshake authentication protocol (CHAP) authentication.

Miniport drivers that implement the [MSiSCSI\_Operations WMI class](msiscsi-operations-wmi-class.md) are not required to support this method.

The MSiSCSI\_Operations WMI Class is unpublished. For a description of the parameters of the **DeleteInitiatorNodeName** method, see the member descriptions for the [**DeleteInitiatorNodeName\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff552505) and [**DeleteInitiatorNodeName\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff552506) structures.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20DeleteInitiatorNodeName%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




