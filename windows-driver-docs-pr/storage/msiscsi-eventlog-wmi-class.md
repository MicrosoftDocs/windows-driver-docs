---
title: MSiSCSI_EventLog WMI Class
description: MSiSCSI\_EventLog WMI Class
ms.date: 10/17/2018
---

# MSiSCSI\_EventLog WMI Class


The MSiSCSI\_EventLog WMI class is used to log any iSCSI events to system event logs. This class is defined as follows in *Mgmt.mof.*

```cpp
class MSiSCSI_Eventlog : __ExtrinsicEvent
{
    [key] 
    string InstanceName;
 
    boolean Active;
 
    [WmiDataId(1),
     EVENTLOG_MESSAGE_QUALIFIERS
    ]
    uint32 Type;

    [WmiDataId(2),
     Description("If zero, then this event is not logged to system eventlog") : amended
    ]
    uint32 LogToEventlog;

    [WmiDataId(3),
     Description("Size of Additional Data") : amended
    ]
    uint32 Size;

    [WmiDataId(4),
     WmiSizeIs("Size"),
     Description("Additional data to include in eventlog message, typically iSCSI Header") : amended
    ]
    uint8 AdditionalData[];    
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_EventLog**](/windows-hardware/drivers/ddi/iscsimgt/ns-iscsimgt-_msiscsi_eventlog) data structure.

 

