---
title: MSiSCSI\_HBAInformation WMI Class
description: MSiSCSI\_HBAInformation WMI Class
ms.assetid: 24c44f97-5ff3-46fa-a5bf-aa76f7f0d3f2
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSiSCSI\_HBAInformation WMI Class


## <span id="ddk_msiscsi_hbainformation_wmi_class_kr"></span><span id="DDK_MSISCSI_HBAINFORMATION_WMI_CLASS_KR"></span>


The iSCSI initiator service uses the MSiSCSI\_HBAInformation WMI class to communicate with your adapter. You should have a separate instance of this class for each instance of the miniport driver that is loaded.

Because this class is associated with a particular instance of a storage miniport driver, the miniport driver must register the class using the name of the particular physical device object (PDO) that the miniport driver manages.

The MSiSCSI\_HBAInformation class is defined as follows in *Mgmt.mof*.

```cpp
class MSiSCSI_HBAInformation {
  [key] string  InstanceName;
  boolean  Active;
  [WmiDataId(1), DisplayName("Adapter Id") : amended, 
    DisplayInHex, description("Id that is globally unique to
    each instance of each adapter. Using the address of the
    Adapter Extension is a good idea.") : amended] 
    uint64  UniqueAdapterId;
  [WmiDataId(2), DisplayName("Integrated Networking") : 
    amended, description("TRUE if TCP/IP traffic is 
    integrated with the Windows networking TCP/IP stack via 
    a software only initiator") : amended] 
    boolean  IntegratedTCPIP;
  [WmiDataId(3), Displayname("Requires Binary Addresses") :
    amended, description("TRUE if HBA requires binary ip
    addresses. If unchecked then DNS must be available on
    HBA.") : amended] 
    boolean  RequiresBinaryIpAddresses;
  [read, WmiDataId(4), DisplayName("Minimum iSCSI 
    Version")
    : amended, description("Minimum version number of the
    iScsi spec supported by HBA") : amended] 
    uint8  VersionMin;
  [read, WmiDataId(5), DisplayName("Maximum iSCSI
    Version") 
    : amended, description("Maximum version number of the 
    iSCSI spec supported by HBA") : amended] 
    uint8  VersionMax;
  [read, WmiDataId(6), DisplayName("Multifunction Device") : 
    amended, description("TRUE if this adapter is a 
    multifunction device, that is it also exposes a netcard 
    interface") : amended] 
    boolean  MultifunctionDevice;
  [read, WmiDataId(7), DisplayName("Valid Cache") : amended, 
    description("TRUE if the adapter caches are valid") : 
    amended] boolean  CacheValid;
  [read, WmiDataId(8), Displayname("Number of ports") : 
    amended, description("Number of ports attached to HBA") 
    : amended] uint32  NumberOfPorts;
  [read, WmiDataId(9), Displayname("Status") : amended, 
    description("Current status of HBA") : amended, 
    Values{ "Working", "Degraded", "Critical", "Failed"},
    ValueMap{ "0",     "1",        "2",        "3" },
    cpp_quote(
    "#define ISCSI_HBA_STATUS_WORKING           0\n"
    "#define ISCSI_HBA_STATUS_DEGRADED          1\n"
    "#define ISCSI_HBA_STATUS_CRITICAL          2\n"
    "#define ISCSI_HBA_STATUS_FAILED            3\n"
    )] uint32  Status;
  [read, WmiDataId(10), DisplayName("Functionality 
    Supported") : amended, Description("Bit flags that 
    indicate various functionality supported") : amended, 
    BitValueMap{"0x00000001",
                "0x00000002",
                "0x00000004",
                "0x00000008",
                "0x00000010",
                "0x00000020"
                },
    BitValues{"Preshared Key Cache",
              "iSCSI Authentication Cache",
              "Tunnel Mode",
              "CHAP authentication via RADIUS",
              "Discovery via iSNS",
              "Discovery via SLP"
              } : amended,
    cpp_quote(
    "\n"
    "//\n"
    "// Flags that define the functionality 
    supported by he HBA\n"
    "//\n"
    "#define ISCSI_HBA_PRESHARED_KEY_CACHE  0x00000001\n"
    "#define ISCSI_HBA_ISCSI_AUTHENTICATION_CACHE 
     x00000002\n"
    "#define ISCSI_HBA_IPSEC_TUNNEL_MODE    0x00000004\n"
    "#define ISCSI_HBA_CHAP_VIA_RADIUS      0x00000008\n"
    "#define ISCSI_HBA_ISNS_DISCOVERY       0x00000010\n"
    "#define ISCSI_HBA_SLP_DISCOVERY        0x00000020\n"
    "\n")] 
    uint32  FunctionalitySupported;
  [read, WmiDataId(11), DisplayName("Generational Guid") : 
    amended, Description("Generational Guid") : amended] 
    uint8  GenerationalGuid[16];
  [read, WmiDataId(12), DisplayName("Max CDB Length") : 
    amended, Description("Max CDB Length") : amended] 
    uint32  MaxCDBLength;
  [read, WmiDataId(13), DisplayName("Bi-directional SCSI 
    command supported") : amended, Description("Bi-
    directional SCSI command supported") : amended] 
    boolean  BiDiScsiCommands;
  [read, WmiDataId(14), DisplayName("Manufacturer") : 
    amended, description("A text string describing the 
    manufacturer of HBA") : amended, MaxLen(255)] 
    string  VendorID;
  [read, WmiDataId(15), Displayname("Model") : amended, 
    description("A text string set by the manufacturer 
    describing the model of HBA") : amended, MaxLen(255)] 
    string  VendorModel;
  [read, WmiDataId(16), Displayname("Version") : amended, 
    description("A text string set by the manufacturer 
    describing the version of HBA") : amended,
    MaxLen(255)] 
    string  VendorVersion;
  [read, WmiDataId(17), displayName("Firmware Version") : 
    amended, description("A text string set by the 
    manufacturer describing the firmware version of HBA") :    amended, MaxLen(255)] 
    string  FirmwareVersion;
  [read, WmiDataId(18), displayName("ASIC Version") : 
    amended, description("A text string set by the 
    manufacturer describing the firmware version of HBA") : 
    amended, MaxLen(255)] 
    string  AsicVersion;
  [read, WmiDataId(19), displayName("Option Rom Version") :
  amended, description("A text string set by the
  manufacturer describing the option rom version of HBA")
  : amended, MaxLen(255)] 
  string  OptionRomVersion;
  [read, WmiDataId(20), Displayname("Serial Number") :
    amended, description("A text string set by the
    manufacturer describing the serial number of HBA") :
    amended, MaxLen(255)] 
    string  SerialNumber;
  [read, WmiDataId(21), Displayname("Driver Name") :
    amended, description("A text string specifying the name
    of the driver for the HBA") : amended, MaxLen(255)] 
    string  DriverName;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_HBAInformation**](https://msdn.microsoft.com/library/windows/hardware/ff563012) data structure.

 

 





