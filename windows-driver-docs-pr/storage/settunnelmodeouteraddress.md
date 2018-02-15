---
title: SetTunnelModeOuterAddress
description: SetTunnelModeOuterAddress
ms.assetid: 0f67a15c-5077-460a-923c-8d86cc79a1bb
---

# SetTunnelModeOuterAddress


The **SetTunnelModeOuterAddress** allows a management application to specify the tunnel-mode outer address that a port uses on an initiator HBA.

In tunnel mode, an inner-encrypted IP packet is nested within an outer IP packet that contains the address of the security gateway. The **SetTunnelModeOuterAddress** method allows a management application to indicate the address of the security gateway that is associated with IP packets that pass through the indicated port.

The initiator HBA or HBA miniport driver should maintain the default tunnel-mode outer address in nonvolatile storage if nonvolatile storage is available

**SetTunnelModeOuterAddress** belongs to the unpublished [MSiSCSI\_SecurityConfigOperations WMI class](msiscsi-securityconfigoperations-wmi-class.md). For a description of the parameters of the **SetTunnelModeOuterAddress** method, see the member descriptions for the [**SetTunnelModeOuterAddress\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff566187) and [**SetTunnelModeOuterAddress\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566190) structures.

Miniport drivers that implement the MSiSCSI\_SecurityConfigOperations WMI class must support **SetTunnelModeOuterAddress**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SetTunnelModeOuterAddress%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




