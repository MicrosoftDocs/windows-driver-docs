---
title: VirtualStorport rule set (Storport)
description: Use these rules to verify that your driver correctly calls DDIs that are of particular interest to Storport virtual miniport (VMiniport) drivers.
ms.assetid: 7223AFF1-7EB7-4E25-BC50-8A7BF4E4BE59
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>[<strong>DoubleExFreePool</strong>](storport-doubleexfreepool.md)</p></td>
<td align="left"><p>This rule verifies that the driver does not attempt to free the same block of pool memory twice.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DoubleKeSetEvent</strong>](storport-doublekesetevent.md)</p></td>
<td align="left"><p>This rule verifies that <strong>KeSetEvent</strong> is not called twice on the same event object. If the same event object is passed to the routine, the driver fails the rule.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IoFreeIrp</strong>](storport-iofreeirp.md)</p></td>
<td align="left"><p>This rule verifies that an IRP that was allocated by <strong>IoAllocateIrp</strong> either will be freed by <strong>IoFreeIrp</strong> or its completion routine will get set by <strong>IoSetCompletionRoutine</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>StorPortVirtualDevice</strong>](storport-storportvirtualdevice.md)</p></td>
<td align="left"><p>This rule verifies that upon exit from the [<strong>HwStorFindAdapter</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557390) routine, the <strong>VirtualDevice</strong> field in the [<strong>PORT_CONFIGURATION_INFORMATION (Storport)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563901) structure has been set to <strong>FALSE</strong>. The rule applies only to physical StorPort miniports.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>StorPortVirtualDevice2</strong>](storport-storportvirtualdevice2.md)</p></td>
<td align="left"><p>This rule verifies that upon exit from the [<strong>HwStorFindAdapter</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557390) routine, the <strong>VirtualDevice</strong> field in the [<strong>PORT_CONFIGURATION_INFORMATION (Storport)</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563901) structure has been set to <strong>TRUE</strong>. The rule applies only to virtual StorPort miniports.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WithinCriticalRegion</strong>](storport-withincriticalregion.md)</p></td>
<td align="left"><p>This rule verifies that the driver's calls to certain synchronization functions are made only while normal kernel APC delivery is disabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ZwRegistryCreate</strong>](storport-zwregistrycreate.md)</p></td>
<td align="left"><p>This rule verifies that the handle to a registry key created with [<strong>ZwCreateKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566425) is subsequently used correctly by other <em>ZwXxx</em> routines. The [<strong>ZwOpenKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567014) routine must not be called on an already open handle. The routines [<strong>ZwEnumerateKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566447), [<strong>ZwEnumerateValueKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566453), [<strong>ZwFlushKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566457), [<strong>ZwQueryKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567060), [<strong>ZwQueryValueKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567069), [<strong>ZwSetValueKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567109), [<strong>ZwClose</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566417), and [<strong>ZwDeleteKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566437) must not be called on a handle that isn't open. The handle must also be closed before returning.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ZwRegistryOpen</strong>](storport-zwregistryopen.md)</p></td>
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

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 





