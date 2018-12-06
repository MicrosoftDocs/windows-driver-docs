---
title: MS\_SM\_EventControl WMI Class
description: MS\_SM\_EventControl WMI Class
ms.assetid: d5c6a308-2782-4846-81f9-f4932d8caac6
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MS\_SM\_EventControl WMI Class


The MS\_SM\_EventControl WMI class defines WMI methods that allow WMI clients to control the delivery of link, port, and target events. This WMI class has no data blocks. Therefore, the WMI tool suite generates declarations for structures that hold parameter data for the methods that belong to the class, but it does not generate a structure declaration that corresponds to the class itself.

The MOF syntax for each method that belongs to this class is described in the reference page for the method. The following topics describe these methods and their accompanying structures:

[**SM\_AddTarget**](sm-addtarget.md)

[**SM\_RemoveTarget**](sm-removetarget.md)

[**SM\_AddPort**](sm-addport.md)

[**SM\_RemovePort**](sm-removeport.md)

[**SM\_AddLink**](sm-addlink.md)

[**SM\_RemoveLink**](sm-removelink.md)

The MS\_SM\_EventControl class is defined as follows in *Hbaapi.mof*:

```cpp
class MS_SM_EventControl 
{ 
    [key] 
    string  InstanceName; 
    boolean Active; 

    //
    // These methods are used to control delivery of MS_SM_TargetEvents
//
    [ Implemented, WmiMethodId(1) ]
    void SM_AddTarget(
            [in, HBAType("HBA_WWN") ] uint8 HbaPortWWN[8],
            [in, HBAType("HBA_WWN") ] uint8 DiscoveredPortWWN[8],
            [in, HBAType("HBA_WWN") ] uint8 DomainPortWWN[8],
            [in ] uint32  AllTargets,
            [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus
            );

    [ Implemented, WmiMethodId(2) ]
    void SM_RemoveTarget(
            [in, HBAType("HBA_WWN") ] uint8 HbaPortWWN[8],
            [in, HBAType("HBA_WWN") ] uint8 DiscoveredPortWWN[8],
            [in, HBAType("HBA_WWN") ] uint8 DomainPortWWN[8],
            [in ] uint32  AllTargets,
            [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus
            );


//
// These methods are used to control delivery of MS_SM_PortEvents
//
    [ Implemented, WmiMethodId(3) ]
    void SM_AddPort(
            [in, HBAType("HBA_WWN") ] uint8 PortWWN[8],
            [in, EVENT_TYPES_QUALIFIERS ] uint32 EventType,
            [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus
            );

    [ Implemented, WmiMethodId(4) ]
    void SM_RemovePort(
            [in, HBAType("HBA_WWN") ] uint8 PortWWN[8],
            [in, EVENT_TYPES_QUALIFIERS ] uint32 EventType,
            [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus
            );

//
// These methods are used to control delivery of MSFC_LinkEvents
//
    [ Implemented, WmiMethodId(10) ]
    void SM_AddLink(
            [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus
            );

    [ Implemented, WmiMethodId(11) ]
    void SM_RemoveLink(
            [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus
            );
};
```

 

 





