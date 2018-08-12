---
title: Warning rule set (WDM)
description: Use these rules to verify that your driver can correctly processes IRPs in various contexts and follows Microsoft recommended best practices.
ms.assetid: 29374BBE-D1DF-48C0-80A9-96CBAC6D8A22
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Warning rule set (WDM)


Use these rules to verify that your driver can correctly processes IRPs in various contexts and follows Microsoft recommended best practices.

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
<td align="left"><p>[<strong>CheckDeviceObjectFlags</strong>](wdm-checkdeviceobjectflags.md)</p></td>
<td align="left"><p>The [<strong>CheckDeviceObjectFlags</strong>](wdm-checkdeviceobjectflags.md) rule specifies that a bus driver must check that the device object flags for DO_POWER_PAGABLE and DO_POWER_INRUSH are set consistently for the FDO and the child PDOs. This rule only applies to bus drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>CompletionEventChecking</strong>](wdm-completioneventchecking.md)</p></td>
<td align="left"><p>The [<strong>CompletionEventChecking</strong>](wdm-completioneventchecking.md) rule specifies that a driver does not call [<strong>IoMarkIrpPending</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549422) and [<strong>KeSetEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553253) in a completion routine for the same IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DeleteDevice</strong>](wdm-deletedevice.md)</p></td>
<td align="left"><p>The [<strong>DeleteDevice</strong>](wdm-deletedevice.md) rule specifies that drivers should not rely on the I/O Manager or PnP Manager to keep the DeviceObject alive after a call to [<strong>IoDeleteDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549083).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MultRemoveLock</strong>](wdm-multremovelock.md)</p></td>
<td align="left"><p>The [<strong>MultRemoveLock</strong>](wdm-multremovelock.md) rule verifies that [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204) is called with only one unique Remove Lock. This is a warning rule.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PagedCode</strong>](wdm-pagedcode.md)</p></td>
<td align="left"><p>The [<strong>PagedCode</strong>](wdm-pagedcode.md) rule specifies that the driver calls the [<strong>PAGED_CODE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff558773) macro only when it is executing at <strong>IRQL &lt;= APC_LEVEL</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PagedCodeAtPowerTrans</strong>](wdm-pagedcodeatpowertrans.md)</p></td>
<td align="left"><p>The [<strong>PagedCodeAtPowerTrans</strong>](wdm-pagedcodeatpowertrans.md) rule specifies that a driver should not call [<strong>PAGED_CODE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff558773) while responding to a system IRP_MJ_POWER Irp (IRP_MN_SET_POWER) and to a device IRP_MJ_POWER Irp (IRP_MN_SET_POWER).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ReservedDDIs</strong>](wdm-reservedddis.md)</p></td>
<td align="left"><p>The [<strong>ReservedDDIs</strong>](wdm-reservedddis.md) rule verifies that drivers do not call any reserved functions.</p></td>
</tr>
</tbody>
</table>

 

**To select the Warning rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **Warning**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **Warning.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:Warning.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 





