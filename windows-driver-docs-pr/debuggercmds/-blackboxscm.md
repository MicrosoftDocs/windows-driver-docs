---
title: blackboxscm
description: The blackboxscmextension displays service control manager (scm) secondary boot data.
keywords: ["blackboxscm Windows Debugging"]
ms.date: 01/02/2019
topic_type:
- apiref
ms.topic: reference
api_name:
- blackboxscm
api_type:
- NA
---

# !blackboxscm

The **!blackboxscm** extension displays information from Service Control Manager (SCM) when it is available in a kernel mode dump file. The extension will display the names of any services which have outstanding Service Control Requests.    The information is retrieved from cached data in the kernel mode dump which was saved at the time the bugcheck occurred, and may not always be available.


Syntax

```dbgcmd
!blackboxscm  
```

## <span id="Parameters"></span>Parameters

*None*   


## <span id="DLL"></span><span id="dll"></span>DLL

ext.dll


## <span id="Remarks"></span>Remarks

The commands have been dispatched to the LPHANDLER_FUNCTION_EX callback function of the specific service.  
Outstanding requests such as SERVICE_CONTROL_SHUTDOWN or SERVICE_CONTROL_PRESHUTDOWN could be delaying the orderly shutdown or restart of the computer.

### Example Command Output 

In many dump files, just a single service is returned.

```dbgcmd
2: kd> !ext.blackboxscm
    Name: gpsvc
    Code: 15
```

The returned data provides information on two fields.

*Name* - The name of the service that was active at the time that the dump occurred.

*Code* - The Decimal value of the dwControl which is outstanding

In this example, the code 15 (or  0x0000000F) is defined as SERVICE_CONTROL_PRESHUTDOWN.


### Multiple Services

When multiple services are listed,  only the first service that is listed is typically of interest for failure analysis.  This is because the SCM (Service Control Manager) waits serially for completion of these requests, so only the first service has actually received a control request.

For more information about SCM, see [Service Control Manager](/windows/desktop/Services/service-control-manager).


### <span id="Additional_Information"></span>Additional Information

dwControl values are defined in winsvc.h and documented as parameters to [LPHANDLER_FUNCTION_EX callback function](/windows/win32/api/winsvc/nc-winsvc-lphandler_function_ex#parameters).

 
