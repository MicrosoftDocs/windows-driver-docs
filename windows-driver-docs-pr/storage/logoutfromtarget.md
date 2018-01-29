---
title: LogoutFromTarget
description: LogoutFromTarget
ms.assetid: 29be7228-2b18-4f88-8a5a-e7406ef91b1c
---

# LogoutFromTarget


The **LogoutFromTarget** method instructs the miniport driver that manages the iSCSI initiator HBA to log off a target and removes the target's logical units from the local computer's device stack.

Miniport drivers that implement the [MSiSCSI\_Operations WMI class](msiscsi-operations-wmi-class.md) are not required to support this method.

The MSiSCSI\_Operations WMI class is unpublished. For a description of the parameters of the **LogoutFromTarget** method, see the member descriptions for the [**LogoutFromTarget\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff562191) and [**LogoutFromTarget\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff562194) structures.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20LogoutFromTarget%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




