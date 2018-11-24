---
title: Irql rule set (KMDF)
description: Use these rules to verify that your driver makes DDI calls at the required IRQL.A driver that does not follow the IRQL rules can cause serious problems during operation that can lead to deadlock conditions or computer crashes.
ms.assetid: B02D196F-E8D5-4FE9-8983-AD08EAE00DE5
ms.date: 05/21/2018
ms.localizationpriority: medium
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
<td align="left"><p><a href="kmdf-kmdfirql.md" data-raw-source="[&lt;strong&gt;KmdfIrql&lt;/strong&gt;](kmdf-kmdfirql.md)"><strong>KmdfIrql</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-kmdfirql.md" data-raw-source="[&lt;strong&gt;KmdfIrql&lt;/strong&gt;](kmdf-kmdfirql.md)"><strong>KmdfIrql</strong></a> rule specifies that a driver calls a framework method at an IRQL that is less than or equal to the maximum IRQL for that method.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-kmdfirql2.md" data-raw-source="[&lt;strong&gt;KmdfIrql2&lt;/strong&gt;](kmdf-kmdfirql2.md)"><strong>KmdfIrql2</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-kmdfirql2.md" data-raw-source="[&lt;strong&gt;KmdfIrql2&lt;/strong&gt;](kmdf-kmdfirql2.md)"><strong>KmdfIrql2</strong></a> rule specifies that a driver calls a framework method at an IRQL that is less than or equal to the maximum IRQL for that method.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-usbkmdfirql.md" data-raw-source="[&lt;strong&gt;UsbKmdfIrql&lt;/strong&gt;](kmdf-usbkmdfirql.md)"><strong>UsbKmdfIrql</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-usbkmdfirql.md" data-raw-source="[&lt;strong&gt;UsbKmdfIrql&lt;/strong&gt;](kmdf-usbkmdfirql.md)"><strong>UsbKmdfIrql</strong></a> rule specifies that a KMDF driver does not call USB-specific device driver interfaces (DDI) at the incorrect IRQL level.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-usbkmdfirql2.md" data-raw-source="[&lt;strong&gt;UsbKmdfIrql2&lt;/strong&gt;](kmdf-usbkmdfirql2.md)"><strong>UsbKmdfIrql2</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-usbkmdfirql2.md" data-raw-source="[&lt;strong&gt;UsbKmdfIrql2&lt;/strong&gt;](kmdf-usbkmdfirql2.md)"><strong>UsbKmdfIrql2</strong></a> rule specifies that a KMDF driver should not call USB-specific DDIs at the incorrect IRQL level.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="usbkmdfirqlexplicit.md" data-raw-source="[&lt;strong&gt;UsbKmdfIrqlExplicit&lt;/strong&gt;](usbkmdfirqlexplicit.md)"><strong>UsbKmdfIrqlExplicit</strong></a></p></td>
<td align="left"><p>The <a href="usbkmdfirqlexplicit.md" data-raw-source="[&lt;strong&gt;UsbKmdfIrqlExplicit&lt;/strong&gt;](usbkmdfirqlexplicit.md)"><strong>UsbKmdfIrqlExplicit</strong></a> rule verifies that KMDF DDIs are called at the correct IRQL level. This rule applies to all EvtIoCallback functions.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdfrequestsendsyncatdispatch.md" data-raw-source="[&lt;strong&gt;WdfRequestSendSyncAtDispatch&lt;/strong&gt;](wdfrequestsendsyncatdispatch.md)"><strong>WdfRequestSendSyncAtDispatch</strong></a></p></td>
<td align="left"><p>The <a href="wdfrequestsendsyncatdispatch.md" data-raw-source="[&lt;strong&gt;WdfRequestSendSyncAtDispatch&lt;/strong&gt;](wdfrequestsendsyncatdispatch.md)"><strong>WdfRequestSendSyncAtDispatch</strong></a> rule verifies that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550027" data-raw-source="[&lt;strong&gt;WdfRequestSend&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550027)"><strong>WdfRequestSend</strong></a> function is sent at the correct IRQL priority level.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdfrequestsendsyncatdispatch2.md" data-raw-source="[&lt;strong&gt;WdfRequestSendSyncAtDispatch2&lt;/strong&gt;](wdfrequestsendsyncatdispatch2.md)"><strong>WdfRequestSendSyncAtDispatch2</strong></a></p></td>
<td align="left"><p>The <a href="wdfrequestsendsyncatdispatch2.md" data-raw-source="[&lt;strong&gt;WdfRequestSendSyncAtDispatch2&lt;/strong&gt;](wdfrequestsendsyncatdispatch2.md)"><strong>WdfRequestSendSyncAtDispatch2</strong></a> rule verifies that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550027" data-raw-source="[&lt;strong&gt;WdfRequestSend&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550027)"><strong>WdfRequestSend</strong></a> function is sent at the correct IRQL priority level.</p></td>
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

 

 





