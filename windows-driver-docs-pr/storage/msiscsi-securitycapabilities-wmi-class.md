---
title: MSiSCSI\_SecurityCapabilities WMI Class
description: MSiSCSI\_SecurityCapabilities WMI Class
ms.assetid: 50f7aa98-0743-4775-808b-c5a90dc1d0fe
---

# MSiSCSI\_SecurityCapabilities WMI Class


## <span id="ddk_msiscsi_securitycapabilities_wmi_class_kr"></span><span id="DDK_MSISCSI_SECURITYCAPABILITIES_WMI_CLASS_KR"></span>


The MSiSCSI\_SecurityCapabilities WMI class describes the security capabilities of an initiator.

A miniport driver must implement the MSiSCSI\_SecurityCapabilities class if the HBA it manages supports IPsec.

Because the MSiSCSI\_SecurityCapabilities class is associated with a particular instance of a storage miniport driver, the miniport driver must register the class using the name of the particular physical device object (PDO) that the miniport driver manages.

The MSiSCSI\_SecurityCapabilities class is defined in *Config.mof*.

```
class MSiSCSI_SecurityCapabilities {
  [key] string  InstanceName;
  boolean  Active;
  [read, DisplayName("Protect iSCSI") : amended, 
    WmiDataId(1), description("TRUE if the HBA can use IPsec 
    to protect iSCSI traffic") : amended]
    boolean  ProtectiScsiTraffic;
  [read, WmiDataId(2), DisplayName("Protect iSNS") : 
    amended, description("TRUE if the HBA can use IPsec to 
    protect iSNS traffic") : amended] 
    boolean  ProtectiSNSTraffic;
  [read, WmiDataId(3), DisplayName("Certificates Supported") 
    : amended, description("TRUE if HBA supports 
    certificates") : amended] 
    boolean  CertificatesSupported;
  [read, WmiDataId(4), DisplayName("Encryption Types 
    Available") : amended, description("Count of encryption 
    types available")] 
    uint32  EncryptionAvailableCount;
  [read, WmiDataId(5), 
    WmiSizeIs("EncryptionAvailableCount"), 
    ENCRYPTION_TYPES_QUALIFIERS, DisplayName("Encryption 
    Types") : amended] 
    uint32  EncryptionAvailable[];
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_SecurityCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff563130) data structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSiSCSI_SecurityCapabilities%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




