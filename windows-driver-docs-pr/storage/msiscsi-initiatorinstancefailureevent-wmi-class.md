---
title: MSiSCSI_InitiatorInstanceFailureEvent WMI Class
description: MSiSCSI\_InitiatorInstanceFailureEvent WMI Class
ms.date: 10/17/2018
---

# MSiSCSI\_InitiatorInstanceFailureEvent WMI Class


## <span id="ddk_msiscsi_initiatorinstancefailureevent_wmi_class_kr"></span><span id="DDK_MSISCSI_INITIATORINSTANCEFAILUREEVENT_WMI_CLASS_KR"></span>


The MSiSCSI\_InitiatorInstanceFailureEvent WMI Class fires an event when an initiator instance failure occurs.

Because this class is associated with a particular instance of a storage miniport driver, the miniport driver must register the class using the name of the particular physical device object (PDO) that the miniport driver manages.

The MSiSCSI\_InitiatorInstanceFailureEvent class is defined in *Mgmt.mof*.

```cpp
class MSiSCSI_InitiatorInstanceFailureEvent : WMIEvent {
  [read,key] String  InstanceName;
  [read] boolean  Active;
  [read, WmiDataId(1),
    ISCSI_INITIATOR_NODE_FAILURE_TYPE_QUALIFIERS, 
    WmiVersion(1)] 
    ISCSI_INITIATOR_NODE_FAILURE_TYPE  FailureType;
  [read, WmiDataId(2), WmiVersion(1),
    MaxLen(MAX_ISCSI_NAME_LEN)] 
    string  RemoteNodeName;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_InitiatorInstanceFailureEvent**](/windows-hardware/drivers/ddi/iscsimgt/ns-iscsimgt-_msiscsi_initiatorinstancefailureevent) data structure.

 

