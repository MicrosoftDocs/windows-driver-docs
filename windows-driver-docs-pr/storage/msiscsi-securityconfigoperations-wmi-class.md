---
title: MSiSCSI\_SecurityConfigOperations WMI Class
description: MSiSCSI\_SecurityConfigOperations WMI Class
ms.assetid: 27056bae-ba73-409f-b55e-453ed46a61d2
---

# MSiSCSI\_SecurityConfigOperations WMI Class


## <span id="ddk_msiscsi_securityconfigoperations_wmi_class_kr"></span><span id="DDK_MSISCSI_SECURITYCONFIGOPERATIONS_WMI_CLASS_KR"></span>


The MSiSCSI\_SecurityConfigOperations WMI class defines the security configuration methods that an initiator must implement to support either Internet protocol security (IPsec) or challenge handshake authentication protocol (CHAP).

In addition, initiators that support Internet key exchange (IKE) with preshared keys must implement the following methods:

-   [SetPresharedKeyForId](setpresharedkeyforid.md)

-   [GetPresharedKeyForId](getpresharedkeyforid.md)

-   [SetGroupPresharedKey](setgrouppresharedkey.md)

Initiators that support a nonvolatile cache for IPsec preshared keys and iSCSI authentication credentials (that is, a user name and password) must implement the [ClearCache](clearcache.md) method. The initiator must also indicate that it uses a cache by setting the appropriate flags in the [MSiSCSI\_HBAInformation WMI class](msiscsi-hbainformation-wmi-class.md). In particular, if the initiator caches the preshared key, it should set the ISCSI\_HBA\_PRESHARED\_KEY\_CACHE flag in the **FunctionalitySupported** member of the class; and if the initiator caches iSCSI authentication data, it should set the ISCSI\_HBA\_ISCSI\_AUTHENTICATION\_CACHE flag.

Because the MSiSCSI\_SecurityConfigOperations class is associated with a particular instance of a storage miniport driver, the miniport driver must register the class using the name of the particular physical device object (PDO) that the miniport driver manages.

For the initiator to be compatible with the iSCSI discovery service, it must implement the [SetGenerationalGuid](setgenerationalguid.md) method.

The managed object format (MOF) syntax for each method that belongs to this class is described in the reference page for the method. The following topics describe these methods and their accompanying structures:

[ClearCache](clearcache.md)

[GetPresharedKeyForId](getpresharedkeyforid.md)

[SetGenerationalGuid](setgenerationalguid.md)

[SetGroupPresharedKey](setgrouppresharedkey.md)

[SetPresharedKeyForId](setpresharedkeyforid.md)

[SetTunnelModeOuterAddress](settunnelmodeouteraddress.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSiSCSI_SecurityConfigOperations%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




