---
title: VirtualStorport rule set (Storport)
description: Use these rules to verify that your driver correctly calls DDIs that are of particular interest to Storport virtual miniport (VMiniport) drivers.
ms.date: 05/21/2018
ms.localizationpriority: medium
---

# VirtualStorport rule set (Storport)


Use these rules to verify that your driver correctly calls DDIs that are of particular interest to Storport virtual miniport (VMiniport) drivers.

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
<td align="left"><p><a href="storport-doubleexfreepool.md" data-raw-source="[&lt;strong&gt;DoubleExFreePool&lt;/strong&gt;](storport-doubleexfreepool.md)"><strong>DoubleExFreePool</strong></a></p></td>
<td align="left"><p>This rule verifies that the driver does not attempt to free the same block of pool memory twice.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storport-doublekesetevent.md" data-raw-source="[&lt;strong&gt;DoubleKeSetEvent&lt;/strong&gt;](storport-doublekesetevent.md)"><strong>DoubleKeSetEvent</strong></a></p></td>
<td align="left"><p>This rule verifies that <strong>KeSetEvent</strong> is not called twice on the same event object. If the same event object is passed to the routine, the driver fails the rule.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="storport-iofreeirp.md" data-raw-source="[&lt;strong&gt;IoFreeIrp&lt;/strong&gt;](storport-iofreeirp.md)"><strong>IoFreeIrp</strong></a></p></td>
<td align="left"><p>This rule verifies that an IRP that was allocated by <strong>IoAllocateIrp</strong> either will be freed by <strong>IoFreeIrp</strong> or its completion routine will get set by <strong>IoSetCompletionRoutine</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storport-storportvirtualdevice.md" data-raw-source="[&lt;strong&gt;StorPortVirtualDevice&lt;/strong&gt;](storport-storportvirtualdevice.md)"><strong>StorPortVirtualDevice</strong></a></p></td>
<td align="left"><p>This rule verifies that upon exit from the <a href="/windows-hardware/drivers/ddi/storport/nc-storport-hw_find_adapter" data-raw-source="[&lt;strong&gt;HwStorFindAdapter&lt;/strong&gt;](/windows-hardware/drivers/ddi/storport/nc-storport-hw_find_adapter)"><strong>HwStorFindAdapter</strong></a> routine, the <strong>VirtualDevice</strong> field in the <a href="/previous-versions/windows/hardware/drivers/ff563901(v=vs.85)" data-raw-source="[&lt;strong&gt;PORT_CONFIGURATION_INFORMATION (Storport)&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff563901(v=vs.85))"><strong>PORT_CONFIGURATION_INFORMATION (Storport)</strong></a> structure has been set to <strong>FALSE</strong>. The rule applies only to physical StorPort miniports.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="storport-storportvirtualdevice2.md" data-raw-source="[&lt;strong&gt;StorPortVirtualDevice2&lt;/strong&gt;](storport-storportvirtualdevice2.md)"><strong>StorPortVirtualDevice2</strong></a></p></td>
<td align="left"><p>This rule verifies that upon exit from the <a href="/windows-hardware/drivers/ddi/storport/nc-storport-hw_find_adapter" data-raw-source="[&lt;strong&gt;HwStorFindAdapter&lt;/strong&gt;](/windows-hardware/drivers/ddi/storport/nc-storport-hw_find_adapter)"><strong>HwStorFindAdapter</strong></a> routine, the <strong>VirtualDevice</strong> field in the <a href="/previous-versions/windows/hardware/drivers/ff563901(v=vs.85)" data-raw-source="[&lt;strong&gt;PORT_CONFIGURATION_INFORMATION (Storport)&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff563901(v=vs.85))"><strong>PORT_CONFIGURATION_INFORMATION (Storport)</strong></a> structure has been set to <strong>TRUE</strong>. The rule applies only to virtual StorPort miniports.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storport-withincriticalregion.md" data-raw-source="[&lt;strong&gt;WithinCriticalRegion&lt;/strong&gt;](storport-withincriticalregion.md)"><strong>WithinCriticalRegion</strong></a></p></td>
<td align="left"><p>This rule verifies that the driver's calls to certain synchronization functions are made only while normal kernel APC delivery is disabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="storport-zwregistrycreate.md" data-raw-source="[&lt;strong&gt;ZwRegistryCreate&lt;/strong&gt;](storport-zwregistrycreate.md)"><strong>ZwRegistryCreate</strong></a></p></td>
<td align="left"><p>This rule verifies that the handle to a registry key created with <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatekey" data-raw-source="[&lt;strong&gt;ZwCreateKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatekey)"><strong>ZwCreateKey</strong></a> is subsequently used correctly by other <em>ZwXxx</em> routines. The <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenkey" data-raw-source="[&lt;strong&gt;ZwOpenKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenkey)"><strong>ZwOpenKey</strong></a> routine must not be called on an already open handle. The routines <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwenumeratekey" data-raw-source="[&lt;strong&gt;ZwEnumerateKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwenumeratekey)"><strong>ZwEnumerateKey</strong></a>, <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwenumeratevaluekey" data-raw-source="[&lt;strong&gt;ZwEnumerateValueKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwenumeratevaluekey)"><strong>ZwEnumerateValueKey</strong></a>, <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwflushkey" data-raw-source="[&lt;strong&gt;ZwFlushKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwflushkey)"><strong>ZwFlushKey</strong></a>, <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwquerykey" data-raw-source="[&lt;strong&gt;ZwQueryKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwquerykey)"><strong>ZwQueryKey</strong></a>, <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwqueryvaluekey" data-raw-source="[&lt;strong&gt;ZwQueryValueKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwqueryvaluekey)"><strong>ZwQueryValueKey</strong></a>, <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwsetvaluekey" data-raw-source="[&lt;strong&gt;ZwSetValueKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwsetvaluekey)"><strong>ZwSetValueKey</strong></a>, <a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose" data-raw-source="[&lt;strong&gt;ZwClose&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose)"><strong>ZwClose</strong></a>, and <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwdeletekey" data-raw-source="[&lt;strong&gt;ZwDeleteKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwdeletekey)"><strong>ZwDeleteKey</strong></a> must not be called on a handle that isn't open. The handle must also be closed before returning.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storport-zwregistryopen.md" data-raw-source="[&lt;strong&gt;ZwRegistryOpen&lt;/strong&gt;](storport-zwregistryopen.md)"><strong>ZwRegistryOpen</strong></a></p></td>
<td align="left"><p>This rule verifies that the handle to the registry key opened via <strong>ZwOpenKey</strong> is subsequently used correctly by other ZwXxx routines. The routines <strong>ZwEnumerateKey</strong>, <strong>ZwEnumerateValueKey</strong>, <strong>ZwFlushKey</strong>, <strong>ZwQueryKey</strong>, <strong>ZwQueryValueKey</strong>, <strong>ZwSetValueKey</strong>, <strong>ZwClose</strong>, and <strong>ZwDeleteKey</strong> must not be called on a handle that isn't open. The handle must also be closed before returning.</p></td>
</tr>
</tbody>
</table>

 

**To select the VirtualStorport rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **VirtualStorport**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **VirtualStorport.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:VirtualStorport.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md) and [Static Driver Verifier commands (MSBuild)](./-static-driver-verifier-commands--msbuild-.md).

