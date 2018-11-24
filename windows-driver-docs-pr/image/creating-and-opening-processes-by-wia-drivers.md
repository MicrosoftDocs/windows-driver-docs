---
title: Creating and Opening Processes by WIA Drivers
description: Creating and Opening Processes by WIA Drivers
ms.assetid: c939eb25-b92b-41ef-ade0-98c2a707fee6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating and Opening Processes by WIA Drivers





WIA drivers should not start other processes on the system. The two most important reasons for this are the following:

1.  Calling **CreateProcess** (described in the Microsoft Windows SDK documentation) starts the process under the same account in which the service was launched. In Windows XP, this is the **LocalSystem** account, which is a significant security risk.

2.  Calling **CreateProcessAsUser** (described in the Windows SDK documentation) can be difficult in a Fast User Switching (FUS) or Terminal Services (TS) environment. Incorrectly implemented components at this level can easily lead to successful escalation of privilege or information disclosure attacks.

The **LocalService** account does not have sufficient privileges to start other processes. Therefore, on Microsoft Windows Server 2003 and later, WIA drivers cannot create processes.

If another process is required for device functionality, it is recommended that it be implemented as a system service or local COM server. See the Microsoft documentation for specific security information related to the creation of system services and COM servers.

 

 




