---
title: PnpSurpriseRemove rule (wdm)
description: The PnpSurpriseRemove rule specifies that the driver does not call IoDeleteDevice or IoDetachDevice while processing an IRP\_MN\_SURPRISE\_REMOVAL request.
ms.assetid: 58553c78-04c3-423c-bf68-69d5a8fbfa9b
keywords: ["PnpSurpriseRemove rule (wdm)"]
topic_type:
- apiref
api_name:
- PnpSurpriseRemove
api_type:
- NA
---

# PnpSurpriseRemove rule (wdm)


The **PnpSurpriseRemove** rule specifies that the driver does not call IoDeleteDevice or IoDetachDevice while processing an [**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760) request.

The PnP manager sends the [**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760) request to notify drivers that a device is no longer available for I/O operations and that it has probably been unexpectedly removed from the computer.

-   All PnP drivers must handle [**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760) request.
-   The driver must not call [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083) or [**IoDetachDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549087) on device objects until the IRP\_MN\_SURPRISE\_REMOVAL IRP succeeds and all open handles to the device are closed.
-   The PnP manager then sends an [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request to the device stack. In response to the remove IRP, drivers detach their device objects from the stack and delete them.

For more information about how a driver should respond to [**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760) request, see [**Handling an IRP\_MN\_SURPRISE\_REMOVAL Request**](https://msdn.microsoft.com/library/windows/hardware/ff546699)

|              |     |
|--------------|-----|
| Driver model | WDM |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>PnpSurpriseRemove</strong> rule.</p>
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
[**IoDetachDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549087)
See also
--------

[**Handling an IRP\_MN\_SURPRISE\_REMOVAL Request**](https://msdn.microsoft.com/library/windows/hardware/ff546699)
[Analyzing a Driver Using Verification and Code Analysis Tools](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver)
[**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760)
[**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20PnpSurpriseRemove%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




