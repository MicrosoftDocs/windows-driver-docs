---
title: Removing an ISR
description: Removing an ISR
ms.assetid: 23d84edb-763f-4383-b05c-832b4249b604
keywords: ["interrupt service routines WDK kernel , removing ISRs", "interrupt objects WDK kernel , removing ISRs", "ISRs WDK kernel , removing ISRs", "removing ISRs WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Removing an ISR


Drivers can remove an ISR that is registered with [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378) by calling [**IoDisconnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff549093). **IoDisconectInterruptEx** takes a single *Parameters* parameter, which is a pointer to an [**IO\_DISCONNECT\_INTERRUPT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff550569) structure. The values that are used for the members of the structure depend on the version that is used to register the ISR.

The driver must save certain information when it registers the ISR to later remove it. For the CONNECT\_LINE\_BASED and CONNECT\_FULLY\_SPECIFIED versions, the driver must save the value that is supplied in the **LineBased.InterruptObject** or **FullySpecified.InterruptObject** member of [**IO\_CONNECT\_INTERRUPT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff550541). For the CONNECT\_MESSAGE\_BASED version, the driver must save the values supplied in the **Version** and **MessageBased.ConnectionContext** members of **IO\_CONNECT\_INTERRUPT\_PARAMETERS**.

 

 




