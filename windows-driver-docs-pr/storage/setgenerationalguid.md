---
title: SetGenerationalGuid
description: SetGenerationalGuid
ms.assetid: cf8e57e5-afdf-4bc2-9849-5df3fbbdd6c5
---

# SetGenerationalGuid


The **SetGenerationalGuid** method assigns a new GUID value to the information in the initiator HBA's caches.

Initiator HBAs often cache authentication information such as preshared keys that are associated with particular initiator identifiers, group keys that are associated by default with initiator identifiers that have no key, and CHAP secrets. The initiator maintains a GUID that identifies the version of the information that is currently in its caches.

Services, such as the iSCSI discovery service, and management applications that update an initiator's cached information should change this GUID to indicate that the cache has been modified. When an iSCSI service or management application restarts, it can check the initiator HBA's GUID to verify that its cached information is synchronized with the cached information on the initiator.

Applications and services can use the following iSCSI WMI methods to manage an initiators' cached configuration data:

[ClearCache](clearcache.md)

[GetPresharedKeyForId](getpresharedkeyforid.md)

[SetGroupPresharedKey](setgrouppresharedkey.md)

[SetPresharedKeyForId](setpresharedkeyforid.md)

[SetTunnelModeOuterAddress](settunnelmodeouteraddress.md)

The **SetGenerationalGuid** method belongs to the unpublished [MSiSCSI\_SecurityConfigOperations WMI class](msiscsi-securityconfigoperations-wmi-class.md). For a description of the parameters of the **SetGenerationalGuid** method, see the member descriptions for the [**SetGenerationalGuid\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565681) and [**SetGenerationalGuid\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565687) structures. Miniport drivers that implement the MSiSCSI\_SecurityConfigOperations WMI class must support this method if the HBA caches information.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SetGenerationalGuid%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




