---
title: SetPresharedKeyForId
description: SetPresharedKeyForId
ms.assetid: d966fd05-31ac-4774-b970-e4ce3d02a5ba
---

# SetPresharedKeyForId


The **SetPresharedKeyForId** method allows a management application to associate a particular preshared key with the identifier (ID) that an initiator uses to identify itself during phase 1 of an aggressive or main-mode Internet key exchange (IKE).

When an initiator uses a preshared key in a key exchange, it associates the key with an identifier for the initiator (and with an IP address) and passes the identifier and its associated key to the target in the data portion of an identification packet (also known as the *identification payload*). The initiator passes the identifier and its associated key during phase 1 of an aggressive or main-mode IKE, as described in [RFC 2407](http://go.microsoft.com/fwlink/p/?linkid=64840). The identification payload permits the target to identify the initiator in a way that is secure and to choose a security policy that is appropriate for a connection with that particular initiator.

After the **SetPresharedKeyForId** method specifies the preshared key, the initiator should store it in nonvolatile storage if nonvolatile storage is available. But the initiator should also keep the preshared key in working memory, so that it will be quickly available during IKE phase 1 negotiation. This improves the efficiency of the key exchange. If nonvolatile memory is not available to the initiator, the initiator service will store the key on behalf of the initiator.

A management application can use the **SetPresharedKeyForId** method to associate a preshared key with a particular initiator identifier. To associate a default key with all of an initiator's identifiers, the application can call the [SetGroupPresharedKey](setgrouppresharedkey.md) method. If an explicit association exists between an identifier and a key, the key that the explicit association specifies takes precedence over the default key.

**SetPresharedKeyForId** belongs to the unpublished [MSiSCSI\_SecurityConfigOperations WMI class](msiscsi-securityconfigoperations-wmi-class.md). For a description of the parameters of the **SetPresharedKeyForId** method, see the member descriptions for the [**SetPresharedKeyForId\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565806) and [**SetPresharedKeyForId\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565810) structures.

Miniport drivers that implement the MSiSCSI\_SecurityConfigOperations WMI class must support **SetPresharedKeyForId**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SetPresharedKeyForId%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




