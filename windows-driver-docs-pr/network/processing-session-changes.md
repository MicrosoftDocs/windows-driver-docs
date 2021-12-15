---
title: Processing Session Changes
description: Processing Session Changes
keywords:
- user interaction WDK Native 802.11 IHV Extensions DLL
- session changes WDK Native 802.11 IHV Extensions DLL
ms.date: 04/20/2017
---

# Processing Session Changes




 

If the user's session changes state, such as when the user logs in or out, the operating system notifies the IHV Extensions DLL about the session change by calling the [*Dot11ExtIhvProcessSessionChange*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_process_session_change) function. The operating system passes the reason for the session change to the *uEventType* parameter.

If the *uEventType* parameter is set to WTS\_SESSION\_LOGOFF, the user has logged off of the current session. In this situation, all pending user interface (UI) requests must be canceled internally by the IHV Extensions DLL, and the DLL must free any allocated resources for each pending UI request.

 

 
