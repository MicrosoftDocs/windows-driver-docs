---
title: GetPresharedKeyForId
description: GetPresharedKeyForId
ms.assetid: cd83d1dc-7aa8-4514-a108-50aee91d272b
---

# GetPresharedKeyForId


The **GetPresharedKeyForId** method reports whether the Internet key exchange (IKE) identification payload for a particular initiator identifier (ID is configured to use a preshared key.

When an initiator uses a preshared key in a key exchange, it associates the key with an identifier for the initiator and passes the identifier and its associated key to the target in the data portion of an identification packet (also known as the *identification payload*). The initiator passes the identifier and its associated key during phase 1 of an aggressive or main-mode IKE, as described in [RFC 2407](http://go.microsoft.com/fwlink/p/?linkid=64840). The identification payload permits the target to identify the initiator in a way that is secure and to choose a security policy that is appropriate for a connection with that particular initiator.

However, not every authentication negotiation uses preshared keys. The **GetPresharedKeyForId** method allows a user-mode service or management application to determine if the IKE identification payload for a particular identifier is configured with a preshared key.

This WMI method belongs to the unpublished [MSiSCSI\_SecurityConfigOperations WMI class](msiscsi-securityconfigoperations-wmi-class.md). For a description of the parameters of the **GetPresharedKeyForId** method, see the member descriptions for the [**GetPresharedKeyForId\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff554973) and [**GetPresharedKeyForId\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff554975) structures.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20GetPresharedKeyForId%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




