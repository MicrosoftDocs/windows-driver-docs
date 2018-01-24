---
title: IrqlIoApcLte rule (wdm)
description: The IrqlIoApcLte rule specifies that the driver calls the following I/O manager routines only when it is executing at IRQL�  APC\_LEVEL IoDeleteDeviceIoGetInitialStackIoRaiseHardErrorIoRaiseInformationalHardError.
ms.assetid: 1f0b2b9c-f67c-4e34-b079-6a2769f62879
keywords: ["IrqlIoApcLte rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlIoApcLte
api_type:
- NA
---

# IrqlIoApcLte rule (wdm)


The **IrqlIoApcLte** rule specifies that the driver calls the following I/O manager routines only when it is executing at IRQL &lt;= APC\_LEVEL:

-   [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083)

-   [**IoGetInitialStack**](https://msdn.microsoft.com/library/windows/hardware/ff549247)

-   [**IoRaiseHardError**](https://msdn.microsoft.com/library/windows/hardware/ff549482)

-   [**IoRaiseInformationalHardError**](https://msdn.microsoft.com/library/windows/hardware/ff549488)

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                                                                                                                        |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00020009), [**Bug Check 0xA: IRQL\_NOT\_LESS\_OR\_EQUAL**](https://msdn.microsoft.com/library/windows/hardware/ff560129) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlIoApcLte</strong> rule.</p>
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

Applies to
----------

[**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083)
[**IoGetInitialStack**](https://msdn.microsoft.com/library/windows/hardware/ff549247)
[**IoRaiseHardError**](https://msdn.microsoft.com/library/windows/hardware/ff549482)
[**IoRaiseInformationalHardError**](https://msdn.microsoft.com/library/windows/hardware/ff549488)
See also
--------

[**Managing Hardware Priorities**](https://msdn.microsoft.com/library/windows/hardware/ff554368)
[**Preventing Errors and Deadlocks While Using Spin Locks**](https://msdn.microsoft.com/library/windows/hardware/ff559854)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20IrqlIoApcLte%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




