---
title: Removing an ISR
author: windows-driver-content
description: Removing an ISR
MS-HAID:
- 'Intrupts\_83dc0f3a-5906-48fa-92ee-e833fe5c2913.xml'
- 'kernel.removing\_an\_isr'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 23d84edb-763f-4383-b05c-832b4249b604
keywords: ["interrupt service routines WDK kernel , removing ISRs", "interrupt objects WDK kernel , removing ISRs", "ISRs WDK kernel , removing ISRs", "removing ISRs WDK kernel"]
---

# Removing an ISR


Drivers can remove an ISR that is registered with [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378) by calling [**IoDisconnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff549093). **IoDisconectInterruptEx** takes a single *Parameters* parameter, which is a pointer to an [**IO\_DISCONNECT\_INTERRUPT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff550569) structure. The values that are used for the members of the structure depend on the version that is used to register the ISR.

The driver must save certain information when it registers the ISR to later remove it. For the CONNECT\_LINE\_BASED and CONNECT\_FULLY\_SPECIFIED versions, the driver must save the value that is supplied in the **LineBased.InterruptObject** or **FullySpecified.InterruptObject** member of [**IO\_CONNECT\_INTERRUPT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff550541). For the CONNECT\_MESSAGE\_BASED version, the driver must save the values supplied in the **Version** and **MessageBased.ConnectionContext** members of **IO\_CONNECT\_INTERRUPT\_PARAMETERS**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Removing%20an%20ISR%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


