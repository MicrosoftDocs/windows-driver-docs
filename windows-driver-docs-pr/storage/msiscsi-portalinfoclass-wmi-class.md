---
title: MSiSCSI\_PortalInfoClass WMI Class
description: MSiSCSI\_PortalInfoClass WMI Class
ms.date: 10/17/2018
---

# MSiSCSI\_PortalInfoClass WMI Class


## <span id="ddk_msiscsi_portalinfoclass_wmi_class_kr"></span><span id="DDK_MSISCSI_PORTALINFOCLASS_WMI_CLASS_KR"></span>


The MSiSCSI\_PortalInfoClass WMI class exposes information about a collection of iSCSI portals.

Because this class is associated with a particular instance of a storage miniport driver, the miniport driver must register the class using the name of the particular physical device object (PDO) that the miniport driver manages.

The MSiSCSI\_PortalInfoClass class is defined in *Mgmt.mof*.

```cpp
class MSiSCSI_PortalInfoClass {
  [read,key] String  InstanceName;
  [read] boolean  Active;
  [WmiDataId(1), read, DisplayName("Count of Elements in
    iScsiPortalInfo array") : amended,
    cpp_quote(
    "\n    // Number of elements in  iScsiPortalInfo
    array\n"),
    Description("Number of elements in iScsiPortalInfo
    array") : amended] 
    uint32  PortalInfoCount;
  [WmiDataId(2), read, DisplayName("List Of Portals") :
    amended, Description("Variable length array of
    iScsiPortalInfo. PortalInfoCount specifies the 
    number of elements in the array") : amended,
    WmiSizeIs("PortalInfoCount")] 
    ISCSI_PortalInfo  PortalInformation[];
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_PortalInfoClass**](/windows-hardware/drivers/ddi/iscsimgt/ns-iscsimgt-_msiscsi_portalinfoclass) data structure.

 

