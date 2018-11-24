---
title: MPIO\_EventEntry WMI Class
description: MPIO\_EventEntry WMI Class
ms.assetid: 37160002-fe65-4d02-80f5-375f169b7d11
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MPIO\_EventEntry WMI Class


An MPIO driver uses the MPIO\_EventEntry WMI class to report any MPIO-related events. This class is currently not implemented.

```cpp
class MPIO_EventEntry : WMIEvent
{
        [key, read]
        string InstanceName;

        [read]
        boolean Active;

        //
        // Current system time at time of logging.
        //
        [WmiDataId(1),
         read,
         Description("Time Stamp") : amended,
         WmiTimeStamp
        ] uint64 TimeStamp;

        //
        // Indicates severity of event being logged.
        //
        [WmiDataId(2),
        read,
        Values{"Fatal Error",
               "Error",
               "Warning",
               "Information"} : amended,

        DefineValues{"MPIO_FATAL_ERROR",
                     "MPIO_ERROR",
                     "MPIO_WARNING",
                     "MPIO_INFORMATION"},

        ValueMap{"1", "2", "3", "4"}
        ] uint32 Severity;

        //
        // Multi-path disk&#39;s name that this event is being logged for.
        //
        [WmiDataId(3),
        read,
        MaxLen(63),
        Description("Component") : amended
        ] string Component;

        //
        // Description of event.
        //
        [WmiDataId(4),
        read,
        MaxLen(63),
        Description("Event Description") : amended
        ] string EventDescription;
};
```

There are no methods associated with this WMI class.

 

 





