---
title: Miscellaneous rule set (WDM)
description: Use these rules to verify that your driver correctly follows a general set of requirements for the proper handling of registry keys, strings and device object pointers.
ms.date: 05/21/2018
ms.localizationpriority: medium
---

# Miscellaneous rule set (WDM)


Use these rules to verify that your driver correctly follows a general set of requirements for the proper handling of registry keys, strings and device object pointers.

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
<td align="left"><p><a href="wdm-adddevice.md" data-raw-source="[&lt;strong&gt;AddDevice&lt;/strong&gt;](wdm-adddevice.md)"><strong>AddDevice</strong></a></p></td>
<td align="left"><p>The <a href="wdm-adddevice.md" data-raw-source="[&lt;strong&gt;AddDevice&lt;/strong&gt;](wdm-adddevice.md)"><strong>AddDevice</strong></a> rule specifies that the driver's <a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device" data-raw-source="[&lt;strong&gt;AddDevice&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device)"><strong>AddDevice</strong></a> routine calls <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack" data-raw-source="[&lt;strong&gt;IoAttachDeviceToDeviceStack&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack)"><strong>IoAttachDeviceToDeviceStack</strong></a> only after calling <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice" data-raw-source="[&lt;strong&gt;IoCreateDevice&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice)"><strong>IoCreateDevice</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-danglingdeviceobjectreference.md" data-raw-source="[&lt;strong&gt;DanglingDeviceObjectReference&lt;/strong&gt;](wdm-danglingdeviceobjectreference.md)"><strong>DanglingDeviceObjectReference</strong></a></p></td>
<td align="left"><p>The <a href="wdm-danglingdeviceobjectreference.md" data-raw-source="[&lt;strong&gt;DanglingDeviceObjectReference&lt;/strong&gt;](wdm-danglingdeviceobjectreference.md)"><strong>DanglingDeviceObjectReference</strong></a> rule specifies that the driver calls <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobject" data-raw-source="[&lt;strong&gt;ObDereferenceObject&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobject)"><strong>ObDereferenceObject</strong></a> with the same device object pointer that <a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iogetattacheddevicereference" data-raw-source="[&lt;strong&gt;IoGetAttachedDeviceReference&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iogetattacheddevicereference)"><strong>IoGetAttachedDeviceReference</strong></a> returned.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-pnpsamedeviceobject.md" data-raw-source="[&lt;strong&gt;PnpSameDeviceObject&lt;/strong&gt;](wdm-pnpsamedeviceobject.md)"><strong>PnpSameDeviceObject</strong></a></p></td>
<td align="left"><p>The <a href="wdm-pnpsamedeviceobject.md" data-raw-source="[&lt;strong&gt;PnpSameDeviceObject&lt;/strong&gt;](wdm-pnpsamedeviceobject.md)"><strong>PnpSameDeviceObject</strong></a> rule specifies that the driver calls <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack" data-raw-source="[&lt;strong&gt;IoAttachDeviceToDeviceStack&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack)"><strong>IoAttachDeviceToDeviceStack</strong></a> with a pointer to a valid target device object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-targetrelationneedsref.md" data-raw-source="[&lt;strong&gt;TargetRelationNeedsRef&lt;/strong&gt;](wdm-targetrelationneedsref.md)"><strong>TargetRelationNeedsRef</strong></a></p></td>
<td align="left"><p>The <a href="wdm-targetrelationneedsref.md" data-raw-source="[&lt;strong&gt;TargetRelationNeedsRef&lt;/strong&gt;](wdm-targetrelationneedsref.md)"><strong>TargetRelationNeedsRef</strong></a> rule specifies that when processing a <em>TargetDeviceRelation</em> query, the driver's <a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch" data-raw-source="[&lt;strong&gt;DispatchPnP&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)"><strong>DispatchPnP</strong></a> routine calls one of the following functions to reference the child device's PDO:</p>
<ul>
<li><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-obfreferenceobject" data-raw-source="[&lt;strong&gt;ObReferenceObject&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-obfreferenceobject)"><strong>ObReferenceObject</strong></a></p></li>
<li><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-obreferenceobjectbyhandle" data-raw-source="[&lt;strong&gt;ObReferenceObjectByHandle&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-obreferenceobjectbyhandle)"><strong>ObReferenceObjectByHandle</strong></a></p></li>
<li><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-obreferenceobjectbypointer" data-raw-source="[&lt;strong&gt;ObReferenceObjectByPointer&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-obreferenceobjectbypointer)"><strong>ObReferenceObjectByPointer</strong></a></p></li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-unsafeallocatepool.md" data-raw-source="[&lt;strong&gt;UnSafeAllocatePool&lt;/strong&gt;](wdm-unsafeallocatepool.md)"><strong>UnSafeAllocatePool</strong></a></p></td>
<td align="left"><p><a href="wdm-unsafeallocatepool.md" data-raw-source="[&lt;strong&gt;UnSafeAllocatePool&lt;/strong&gt;](wdm-unsafeallocatepool.md)"><strong>UnSafeAllocatePool</strong></a> is an important security rule that checks that a driver is not using deprecated DDIs to allocate memory.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-zwregistrycreate.md" data-raw-source="[&lt;strong&gt;ZwRegistryCreate&lt;/strong&gt;](wdm-zwregistrycreate.md)"><strong>ZwRegistryCreate</strong></a></p></td>
<td align="left"><p>The <a href="wdm-zwregistrycreate.md" data-raw-source="[&lt;strong&gt;ZwRegistryCreate&lt;/strong&gt;](wdm-zwregistrycreate.md)"><strong>ZwRegistryCreate</strong></a> rule specifies that after calling <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatekey" data-raw-source="[&lt;strong&gt;ZwCreateKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatekey)"><strong>ZwCreateKey</strong></a>, the driver can call the following registry functions only while holding an open handle to the registry key (that is, before any calls to <a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose" data-raw-source="[&lt;strong&gt;ZwClose&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose)"><strong>ZwClose</strong></a> or <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwdeletekey" data-raw-source="[&lt;strong&gt;ZwDeleteKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwdeletekey)"><strong>ZwDeleteKey</strong></a> to close or delete the handle to the registry key):</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-zwregistryopen.md" data-raw-source="[&lt;strong&gt;ZwRegistryOpen&lt;/strong&gt;](wdm-zwregistryopen.md)"><strong>ZwRegistryOpen</strong></a></p></td>
<td align="left"><p>The <a href="storport-zwregistryopen.md" data-raw-source="[&lt;strong&gt;ZwRegistryOpen&lt;/strong&gt;](storport-zwregistryopen.md)"><strong>ZwRegistryOpen</strong></a> rule specifies that after calling <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenkey" data-raw-source="[&lt;strong&gt;ZwOpenKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenkey)"><strong>ZwOpenKey</strong></a>, the driver calls the following registry functions only while holding an open handle to a registry key (that is, before calling <a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose" data-raw-source="[&lt;strong&gt;ZwClose&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose)"><strong>ZwClose</strong></a> or <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwdeletekey" data-raw-source="[&lt;strong&gt;ZwDeleteKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwdeletekey)"><strong>ZwDeleteKey</strong></a>):</p></td>
</tr>
</tbody>
</table>

 

**To select the Miscellaneous rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **Miscellaneous**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **Miscellaneous.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:Miscellaneous.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md) and [Static Driver Verifier commands (MSBuild)](./-static-driver-verifier-commands--msbuild-.md).

