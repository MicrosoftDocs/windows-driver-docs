---
title: GetPresharedKeyForId
description: GetPresharedKeyForId
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GetPresharedKeyForId


The **GetPresharedKeyForId** method reports whether the Internet key exchange (IKE) identification payload for a particular initiator identifier (ID is configured to use a preshared key.

When an initiator uses a preshared key in a key exchange, it associates the key with an identifier for the initiator and passes the identifier and its associated key to the target in the data portion of an identification packet (also known as the *identification payload*). The initiator passes the identifier and its associated key during phase 1 of an aggressive or main-mode IKE, as described in [RFC 2407](https://go.microsoft.com/fwlink/p/?linkid=64840). The identification payload permits the target to identify the initiator in a way that is secure and to choose a security policy that is appropriate for a connection with that particular initiator.

However, not every authentication negotiation uses preshared keys. The **GetPresharedKeyForId** method allows a user-mode service or management application to determine if the IKE identification payload for a particular identifier is configured with a preshared key.

This WMI method belongs to the unpublished [MSiSCSI\_SecurityConfigOperations WMI class](msiscsi-securityconfigoperations-wmi-class.md). For a description of the parameters of the **GetPresharedKeyForId** method, see the member descriptions for the [**GetPresharedKeyForId\_IN**](/windows-hardware/drivers/ddi/iscsiop/ns-iscsiop-_getpresharedkeyforid_in) and [**GetPresharedKeyForId\_OUT**](/windows-hardware/drivers/ddi/iscsiop/ns-iscsiop-_getpresharedkeyforid_out) structures.

 

