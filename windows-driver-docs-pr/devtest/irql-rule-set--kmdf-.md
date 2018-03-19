---
title: Irql rule set (KMDF)
description: Use these rules to verify that your driver makes DDI calls at the required IRQL.A driver that does not follow the IRQL rules can cause serious problems during operation that can lead to deadlock conditions or computer crashes.
ms.assetid: B02D196F-E8D5-4FE9-8983-AD08EAE00DE5
---

# Irql rule set (KMDF)


Use these rules to verify that your driver makes DDI calls at the required IRQL.

A driver that does not follow the IRQL rules can cause serious problems during operation that can lead to deadlock conditions or computer crashes.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>KmdfIrql</strong>](kmdf-kmdfirql.md)</p></td>
<td align="left"><p>The [<strong>KmdfIrql</strong>](kmdf-kmdfirql.md) rule specifies that a driver calls a framework method at an IRQL that is less than or equal to the maximum IRQL for that method.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>KmdfIrql2</strong>](kmdf-kmdfirql2.md)</p></td>
<td align="left"><p>The [<strong>KmdfIrql2</strong>](kmdf-kmdfirql2.md) rule specifies that a driver calls a framework method at an IRQL that is less than or equal to the maximum IRQL for that method.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>UsbKmdfIrql</strong>](kmdf-usbkmdfirql.md)</p></td>
<td align="left"><p>The [<strong>UsbKmdfIrql</strong>](kmdf-usbkmdfirql.md) rule specifies that a KMDF driver does not call USB-specific device driver interfaces (DDI) at the incorrect IRQL level.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>UsbKmdfIrql2</strong>](kmdf-usbkmdfirql2.md)</p></td>
<td align="left"><p>The [<strong>UsbKmdfIrql2</strong>](kmdf-usbkmdfirql2.md) rule specifies that a KMDF driver should not call USB-specific DDIs at the incorrect IRQL level.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>UsbKmdfIrqlExplicit</strong>](usbkmdfirqlexplicit.md)</p></td>
<td align="left"><p>The [<strong>UsbKmdfIrqlExplicit</strong>](usbkmdfirqlexplicit.md) rule verifies that KMDF DDIs are called at the correct IRQL level. This rule applies to all EvtIoCallback functions.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WdfRequestSendSyncAtDispatch</strong>](wdfrequestsendsyncatdispatch.md)</p></td>
<td align="left"><p>The [<strong>WdfRequestSendSyncAtDispatch</strong>](wdfrequestsendsyncatdispatch.md) rule verifies that the [<strong>WdfRequestSend</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550027) function is sent at the correct IRQL priority level.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WdfRequestSendSyncAtDispatch2</strong>](wdfrequestsendsyncatdispatch2.md)</p></td>
<td align="left"><p>The [<strong>WdfRequestSendSyncAtDispatch2</strong>](wdfrequestsendsyncatdispatch2.md) rule verifies that the [<strong>WdfRequestSend</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550027) function is sent at the correct IRQL priority level.</p></td>
</tr>
</tbody>
</table>

 

**To select the Irql rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **Irql**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **Irql.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:Irql.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 





