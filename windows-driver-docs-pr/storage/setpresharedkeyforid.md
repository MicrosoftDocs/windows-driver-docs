---
title: SetPresharedKeyForId
description: SetPresharedKeyForId
ms.assetid: d966fd05-31ac-4774-b970-e4ce3d02a5ba
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SetPresharedKeyForId


The **SetPresharedKeyForId** method allows a management application to associate a particular preshared key with the identifier (ID) that an initiator uses to identify itself during phase 1 of an aggressive or main-mode Internet key exchange (IKE).

When an initiator uses a preshared key in a key exchange, it associates the key with an identifier for the initiator (and with an IP address) and passes the identifier and its associated key to the target in the data portion of an identification packet (also known as the *identification payload*). The initiator passes the identifier and its associated key during phase 1 of an aggressive or main-mode IKE, as described in [RFC 2407](http://go.microsoft.com/fwlink/p/?linkid=64840). The identification payload permits the target to identify the initiator in a way that is secure and to choose a security policy that is appropriate for a connection with that particular initiator.

After the **SetPresharedKeyForId** method specifies the preshared key, the initiator should store it in nonvolatile storage if nonvolatile storage is available. But the initiator should also keep the preshared key in working memory, so that it will be quickly available during IKE phase 1 negotiation. This improves the efficiency of the key exchange. If nonvolatile memory is not available to the initiator, the initiator service will store the key on behalf of the initiator.

A management application can use the **SetPresharedKeyForId** method to associate a preshared key with a particular initiator identifier. To associate a default key with all of an initiator's identifiers, the application can call the [SetGroupPresharedKey](setgrouppresharedkey.md) method. If an explicit association exists between an identifier and a key, the key that the explicit association specifies takes precedence over the default key.

**SetPresharedKeyForId** belongs to the unpublished [MSiSCSI\_SecurityConfigOperations WMI class](msiscsi-securityconfigoperations-wmi-class.md). For a description of the parameters of the **SetPresharedKeyForId** method, see the member descriptions for the [**SetPresharedKeyForId\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565806) and [**SetPresharedKeyForId\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565810) structures.

Miniport drivers that implement the MSiSCSI\_SecurityConfigOperations WMI class must support **SetPresharedKeyForId**.

 

 





