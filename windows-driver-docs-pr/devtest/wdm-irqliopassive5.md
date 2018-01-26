---
title: IrqlIoPassive5 rule (wdm)
description: The IrqlIoPassive5 rule specifies that the driver calls specific I/O Manager routines only when it is executing at IRQL�  PASSIVE\_LEVEL.
ms.assetid: 07037cf2-37eb-4045-9588-ac10e79b9c5c
keywords: ["IrqlIoPassive5 rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlIoPassive5
api_type:
- NA
---

# IrqlIoPassive5 rule (wdm)


The **IrqlIoPassive5** rule specifies that the driver calls specific I/O Manager routines only when it is executing at IRQL = PASSIVE\_LEVEL.

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x0002000E) |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlIoPassive5</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li>[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)</li>
<li>[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)</li>
<li>[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)</li>
</ol>
<p>For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281).</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208) option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**IoGetConfigurationInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549157)
[**IoGetDeviceObjectPointer**](https://msdn.microsoft.com/library/windows/hardware/ff549198)
[**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220)
[**IoGetFileObjectGenericMapping**](https://msdn.microsoft.com/library/windows/hardware/ff549231)
[**IoInitializeTimer**](https://msdn.microsoft.com/library/windows/hardware/ff549344)
[**IoIsWdmVersionAvailable**](https://msdn.microsoft.com/library/windows/hardware/ff549382)
[**IoRegisterDriverReinitialization**](https://msdn.microsoft.com/library/windows/hardware/ff549511)
[**IoRegisterShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549541)
[**IoRemoveShareAccess**](https://msdn.microsoft.com/library/windows/hardware/ff549587)
[**IoSetShareAccess**](https://msdn.microsoft.com/library/windows/hardware/ff550324)
[**IoUnregisterShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff550409)
[**IoUpdateShareAccess**](https://msdn.microsoft.com/library/windows/hardware/ff550412)
[**IoWMIAllocateInstanceIds**](https://msdn.microsoft.com/library/windows/hardware/ff550429)
[**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20IrqlIoPassive5%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




