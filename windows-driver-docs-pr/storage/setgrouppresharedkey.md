---
title: SetGroupPresharedKey
description: SetGroupPresharedKey
ms.assetid: 7dedcc62-4ad6-42d5-a461-b0a69c9c97cd
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SetGroupPresharedKey


The **SetGroupPresharedKey** method allows a management application to configure an initiator HBA to use the indicated preshared key whenever a key is required but no key is currently associated with the identifier (ID) for a session

When an initiator uses a preshared key in a key exchange, it associates the key with an identifier for the initiator and passes the identifier and its associated key to the target in the data portion of an identification packet (also known as the *identification payload*). The initiator passes the identifier and its associated key during phase 1 of an aggressive or main-mode Internet key exchange (IKE), as described in [RFC 2407](http://go.microsoft.com/fwlink/p/?linkid=64840). The identification payload permits the target to identify the initiator in a way that is secure and to choose a security policy that is appropriate for a connection with that particular initiator.

The **SetGroupPresharedKey** method configures an initiator to use the default preshared key for identifiers that are not already associated with a key. To establish an explicit association between a key and a particular initiator identifier, a management application must call the [SetPresharedKeyForId](setpresharedkeyforid.md) method. If an explicit association exists between an identifier and a key, the key that the association takes precedence over the default key.

After the **SetGroupPresharedKey** method specifies the default key, the initiator should store this key in nonvolatile storage if nonvolatile storage is available. But the initiator should also keep the key in working memory, so that it will be quickly available during IKE phase 1 negotiation. This improves the efficiency of the key exchange.

**SetGroupPresharedKey** belongs to the unpublished [MSiSCSI\_SecurityConfigOperations WMI class](msiscsi-securityconfigoperations-wmi-class.md). For a description of the parameters of the **SetGroupPresharedKey** method, see the member descriptions for the [**SetGroupPresharedKey\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565695) and [**SetGroupPresharedKey\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565697) structures.

Miniport drivers that implement the MSiSCSI\_SecurityConfigOperations WMI class must support **SetGroupPresharedKey**.

 

 





