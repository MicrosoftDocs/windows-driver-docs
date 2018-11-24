---
title: SetGenerationalGuid
description: SetGenerationalGuid
ms.assetid: cf8e57e5-afdf-4bc2-9849-5df3fbbdd6c5
ms.localizationpriority: medium
ms.date: 10/17/2018
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

 

 





