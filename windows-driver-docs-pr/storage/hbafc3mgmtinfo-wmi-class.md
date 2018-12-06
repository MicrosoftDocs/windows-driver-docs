---
title: HBAFC3MgmtInfo WMI Class
description: HBAFC3MgmtInfo WMI Class
ms.assetid: 7c3e5b7e-aed9-4d82-91d9-e0c7b8f5ddf6
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# HBAFC3MgmtInfo WMI Class


## <span id="ddk_hbafc3mgmtinfo_wmi_class_kr"></span><span id="DDK_HBAFC3MGMTINFO_WMI_CLASS_KR"></span>


A WMI client uses the HBAFC3MgmtInfo class to query an HBA miniport driver for FC3 management information associated with a Fibre Channel adapter. FC3 refers to the common services layer of the Fibre Channel protocol. It defines a set of services which are common across multiple ports of a node. For an explanation of the common services layer, see the T11 committee's *Fibre Channel HBA API* specification.

The HBAFC3MgmtInfo class is defined as follows in *Hbaapi.mof*:

```cpp
class HBAFC3MgmtInfo {
  [Description ("Unique identifier for the adapter. This"
    "identifier must be unique among all adapters. "
    "The same value for the identifier must be used "
    "for the same adapter in other classes that expose "
    "adapter information") : amended,
   WmiRefClass("MSFC_FibreChannelAdapter"),
   WmiRefProperty("UniqueAdapterId"), WmiDataId(1) 
     uint64  UniqueAdapterId;
// CIM_FibreChannelAdapter REF
  [HBAType("HBA_WWN"), WmiDataId(2)] uint8  wwn[8];
  [WmiDataId(3)] uint32  unittype;
  [WmiDataId(4)] uint32  PortId;
  [WmiDataId(5)] uint32  NumberOfAttachedNodes;
  [WmiDataId(6)] uint16  IPVersion;
  [WmiDataId(7)] uint16  UDPPort;
  [WmiDataId(8)] uint8  IPAddress[16];
  [WmiDataId(9)] uint16 reserved;
  [WmiDataId(10)] uint16  TopologyDiscoveryFlags;
  [WmiDataId(11)] uint32  reserved1;
};
```

When compiled by the WMI tool suite, this class definition produces the [**HBAFC3MgmtInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556032) data structure. There are no methods associated with this WMI class.

 

 





