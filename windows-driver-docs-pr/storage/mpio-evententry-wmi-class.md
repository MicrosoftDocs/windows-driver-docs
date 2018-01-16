---
title: MPIO\_EventEntry WMI Class
description: MPIO\_EventEntry WMI Class
ms.assetid: 37160002-fe65-4d02-80f5-375f169b7d11
---

# MPIO\_EventEntry WMI Class


An MPIO driver uses the MPIO\_EventEntry WMI class to report any MPIO-related events. This class is currently not implemented.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MPIO_EventEntry%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




