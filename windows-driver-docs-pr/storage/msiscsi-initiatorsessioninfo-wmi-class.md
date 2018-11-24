---
title: MSiSCSI\_InitiatorSessionInfo WMI Class
description: MSiSCSI\_InitiatorSessionInfo WMI Class
ms.assetid: 73053af8-80b0-4cab-8e27-c651be8f0e8c
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSiSCSI\_InitiatorSessionInfo WMI Class


## <span id="ddk_msiscsi_initiatorsessioninfo_wmi_class_kr"></span><span id="DDK_MSISCSI_INITIATORSESSIONINFO_WMI_CLASS_KR"></span>


The MSiSCSI\_InitiatorSessionInfo WMI class exposes information that is associated with the sessions and collections that belong to the indicated HBA initiator.

Because this class is associated with a particular instance of a storage miniport driver, the miniport driver must register the class using the name of the particular physical device object (PDO) that the miniport driver manages.

The MSiSCSI\_InitiatorSessionInfo class is defined in *Mgmt.mof*.

```cpp
class MSiSCSI_InitiatorSessionInfo {
  [read,key] String  InstanceName;
  [read] boolean  Active;
  [WmiDataId(1), DisplayName("Adapter Id") : amended, 
    DisplayInHex, description("Id that is globally unique to
    each instance of each adapter. Using the address of the 
    Adapter Extension is a good idea.") : amended]
    uint64  UniqueAdapterId;
  [WmiDataId(2), read, DisplayName("Count of Elements in 
    SessionsList array") : amended,
    cpp_quote(
    "\n    // Number of elements in SessionList array\n"),
    Description("Number of elements in SessionList array") : 
    amended] 
    uint32  SessionCount;
  [WmiDataId(3), read, DisplayName("List Of Sessions") :
    amended, Description("Variable length array of sessions.
    SessionCount specifies the number of elements in the 
    array") : amended, WmiSizeIs("SessionCount")]  
    ISCSI_SessionStaticInfo  SessionsList[];
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_InitiatorSessionInfo**](https://msdn.microsoft.com/library/windows/hardware/ff563054) data structure.

 

 





