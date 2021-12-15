---
title: Warning rule set (WDM)
description: Use these rules to verify that your driver can correctly processes IRPs in various contexts and follows Microsoft recommended best practices.
ms.date: 05/21/2018
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
<td align="left"><p><a href="wdm-checkdeviceobjectflags.md" data-raw-source="[&lt;strong&gt;CheckDeviceObjectFlags&lt;/strong&gt;](wdm-checkdeviceobjectflags.md)"><strong>CheckDeviceObjectFlags</strong></a></p></td>
<td align="left"><p>The <a href="wdm-checkdeviceobjectflags.md" data-raw-source="[&lt;strong&gt;CheckDeviceObjectFlags&lt;/strong&gt;](wdm-checkdeviceobjectflags.md)"><strong>CheckDeviceObjectFlags</strong></a> rule specifies that a bus driver must check that the device object flags for DO_POWER_PAGABLE and DO_POWER_INRUSH are set consistently for the FDO and the child PDOs. This rule only applies to bus drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-completioneventchecking.md" data-raw-source="[&lt;strong&gt;CompletionEventChecking&lt;/strong&gt;](wdm-completioneventchecking.md)"><strong>CompletionEventChecking</strong></a></p></td>
<td align="left"><p>The <a href="wdm-completioneventchecking.md" data-raw-source="[&lt;strong&gt;CompletionEventChecking&lt;/strong&gt;](wdm-completioneventchecking.md)"><strong>CompletionEventChecking</strong></a> rule specifies that a driver does not call <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending" data-raw-source="[&lt;strong&gt;IoMarkIrpPending&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending)"><strong>IoMarkIrpPending</strong></a> and <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-kesetevent" data-raw-source="[&lt;strong&gt;KeSetEvent&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesetevent)"><strong>KeSetEvent</strong></a> in a completion routine for the same IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-deletedevice.md" data-raw-source="[&lt;strong&gt;DeleteDevice&lt;/strong&gt;](wdm-deletedevice.md)"><strong>DeleteDevice</strong></a></p></td>
<td align="left"><p>The <a href="wdm-deletedevice.md" data-raw-source="[&lt;strong&gt;DeleteDevice&lt;/strong&gt;](wdm-deletedevice.md)"><strong>DeleteDevice</strong></a> rule specifies that drivers should not rely on the I/O Manager or PnP Manager to keep the DeviceObject alive after a call to <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iodeletedevice" data-raw-source="[&lt;strong&gt;IoDeleteDevice&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodeletedevice)"><strong>IoDeleteDevice</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-multremovelock.md" data-raw-source="[&lt;strong&gt;MultRemoveLock&lt;/strong&gt;](wdm-multremovelock.md)"><strong>MultRemoveLock</strong></a></p></td>
<td align="left"><p>The <a href="wdm-multremovelock.md" data-raw-source="[&lt;strong&gt;MultRemoveLock&lt;/strong&gt;](wdm-multremovelock.md)"><strong>MultRemoveLock</strong></a> rule verifies that <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ioacquireremovelock" data-raw-source="[&lt;strong&gt;IoAcquireRemoveLock&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioacquireremovelock)"><strong>IoAcquireRemoveLock</strong></a> is called with only one unique Remove Lock. This is a warning rule.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-pagedcode.md" data-raw-source="[&lt;strong&gt;PagedCode&lt;/strong&gt;](wdm-pagedcode.md)"><strong>PagedCode</strong></a></p></td>
<td align="left"><p>The <a href="wdm-pagedcode.md" data-raw-source="[&lt;strong&gt;PagedCode&lt;/strong&gt;](wdm-pagedcode.md)"><strong>PagedCode</strong></a> rule specifies that the driver calls the <a href="/windows-hardware/drivers/kernel/paged_code"><strong>PAGED_CODE</strong></a> macro only when it is executing at <strong>IRQL &lt;= APC_LEVEL</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-pagedcodeatpowertrans.md" data-raw-source="[&lt;strong&gt;PagedCodeAtPowerTrans&lt;/strong&gt;](wdm-pagedcodeatpowertrans.md)"><strong>PagedCodeAtPowerTrans</strong></a></p></td>
<td align="left"><p>The <a href="wdm-pagedcodeatpowertrans.md" data-raw-source="[&lt;strong&gt;PagedCodeAtPowerTrans&lt;/strong&gt;](wdm-pagedcodeatpowertrans.md)"><strong>PagedCodeAtPowerTrans</strong></a> rule specifies that a driver should not call <a href="/windows-hardware/drivers/kernel/paged_code"><strong>PAGED_CODE</strong></a> while responding to a system IRP_MJ_POWER Irp (IRP_MN_SET_POWER) and to a device IRP_MJ_POWER Irp (IRP_MN_SET_POWER).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-reservedddis.md" data-raw-source="[&lt;strong&gt;ReservedDDIs&lt;/strong&gt;](wdm-reservedddis.md)"><strong>ReservedDDIs</strong></a></p></td>
<td align="left"><p>The <a href="wdm-reservedddis.md" data-raw-source="[&lt;strong&gt;ReservedDDIs&lt;/strong&gt;](wdm-reservedddis.md)"><strong>ReservedDDIs</strong></a> rule verifies that drivers do not call any reserved functions.</p></td>
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

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md) and [Static Driver Verifier commands (MSBuild)](./-static-driver-verifier-commands--msbuild-.md).

