---
title: RemoveConnectionFromSession
description: RemoveConnectionFromSession
ms.assetid: ae23713a-c75d-4669-a643-44e95dbb713c
---

# RemoveConnectionFromSession


The **RemoveConnectionFromSession** method instructs the miniport driver that manages an iSCSI initiator HBA to remove a connection from a logon session.

The iSCSI initiator (that is, the virtual miniport driver) does not support sessions with multiple connections. Do not use **RemoveConnectionFromSession** with the iSCSI initiator.

The **RemoveConnectionFromSession** method will not remove the last connection from a session. You should close sessions with a single connection with the [LogoutFromTarget](logoutfromtarget.md) method.

**RemoveConnectionFromSession** belongs to the unpublished [MSiSCSI\_Operations WMI class](msiscsi-operations-wmi-class.md). For a description of the parameters of the **RemoveConnectionFromSession** method, see the member descriptions for the [**RemoveConnectionFromSession\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff563974) and [**RemoveConnectionFromSession\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff563976) structures.

Miniport drivers that implement the MSiSCSI\_Operations WMI class must support this method.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20RemoveConnectionFromSession%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




