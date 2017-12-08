---
title: blackboxscm
description: The blackboxscmextension displays service control manager (scm) secondary boot data.
keywords: ["blackboxscm Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 12/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- blackboxscm
api_type:
- NA
---

# !blackboxscm


The **!blackboxscm** extension displays service control manager (scm) information when it is available in a kernel mode dump file in the secondary boot data.


Syntax

```
!blackboxscm  
```

## <span id="Parameters"></span>Parameters
*None*   


## <span id="DLL"></span><span id="dll"></span>DLL

ext.dll


## <span id="Remarks"></span>Remarks

Driver developers can call the [BugCheckSecondaryDumpDataCallback routine](https://msdn.microsoft.com/library/windows/hardware/ff540679) to add secondary boot information to dump files. Driver developers (and the OS) can decide when to add this information to the dump file. This means that not all kernel mode dump files will contain secondary boot information. When this data is available the !blackboxscm command, can display the name and last known state of the service(s).

### Example Command Output - Single Service

In many dump files, just a single service is returned.

```
2: kd> !ext.blackboxscm
    Name: gpsvc
    Code: 15
```

The returned data provides information on two things.

*Name* - The name of the service that was active at the time that the dump occurred.

*Code* - The status code of the service as described in TBD.


### Example Command Output - Single Service

In some situations, such as TBD TBD TBD, multiple services will be returned.

```
TBD TBD TBD 

2: kd> !ext.blackboxscm
    Name: gpsvc
    Code: 15
Name: tbd 
    Code: 10
Name: foo
    Code: 12

```

When multiple services are listed, it is important to note that the service state may not be valid for all of the services listed. In the shutdown process, the process for updating the status of the services is suspended. After this point in time, the reported service state can not be trusted. 

For example in the scenario below,  the reported state for service C and D would be questionable and should not be trusted.


```
Service A Code: 15
Service B Code: 12
** Services Shutdown Event **
Service C Code: ?? (Questionable state information)
Service D Code: ?? (Questionable state information)
```
To further examine the credibility of the service states, we can bucket states into static and transitory (changing) states. 

States with "ed:" such as such as Started, Stopped and Paused can be considered static states. 

States with "ing" such as Starting, Stopping and Pausing can be considered transitory states.

The validity of static states is TBD TBD TBD when compared to transitory states.


### <span id="Additional_Information"></span>Additional Information

[BugCheckSecondaryDumpDataCallback routine](https://msdn.microsoft.com/library/windows/hardware/ff540679)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!blackboxscm%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




