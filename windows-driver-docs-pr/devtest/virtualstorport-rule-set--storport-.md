---
title: VirtualStorport rule set (Storport)
description: Use these rules to verify that your driver correctly calls DDIs that are of particular interest to Storport virtual miniport (VMiniport) drivers.
ms.assetid: 7223AFF1-7EB7-4E25-BC50-8A7BF4E4BE59
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20VirtualStorport%20rule%20set%20%28Storport%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




