---
title: Miscellaneous rule set (WDM)
description: Use these rules to verify that your driver correctly follows a general set of requirements for the proper handling of registry keys, strings and device object pointers.
ms.assetid: 50E8BFFE-AC38-4023-9FFB-DC53B749A603
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
<td align="left"><p>[<strong>AddDevice</strong>](wdm-adddevice.md)</p></td>
<td align="left"><p>The [<strong>AddDevice</strong>](wdm-adddevice.md) rule specifies that the driver's [<strong>AddDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine calls [<strong>IoAttachDeviceToDeviceStack</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548300) only after calling [<strong>IoCreateDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548397).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DanglingDeviceObjectReference</strong>](wdm-danglingdeviceobjectreference.md)</p></td>
<td align="left"><p>The [<strong>DanglingDeviceObjectReference</strong>](wdm-danglingdeviceobjectreference.md) rule specifies that the driver calls [<strong>ObDereferenceObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557724) with the same device object pointer that [<strong>IoGetAttachedDeviceReference</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549145) returned.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PnpSameDeviceObject</strong>](wdm-pnpsamedeviceobject.md)</p></td>
<td align="left"><p>The [<strong>PnpSameDeviceObject</strong>](wdm-pnpsamedeviceobject.md) rule specifies that the driver calls [<strong>IoAttachDeviceToDeviceStack</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548300) with a pointer to a valid target device object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>TargetRelationNeedsRef</strong>](wdm-targetrelationneedsref.md)</p></td>
<td align="left"><p>The [<strong>TargetRelationNeedsRef</strong>](wdm-targetrelationneedsref.md) rule specifies that when processing a <em>TargetDeviceRelation</em> query, the driver's [<strong>DispatchPnP</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine calls one of the following functions to reference the child device's PDO:</p>
<ul>
<li><p>[<strong>ObReferenceObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff558678)</p></li>
<li><p>[<strong>ObReferenceObjectByHandle</strong>](https://msdn.microsoft.com/library/windows/hardware/ff558679)</p></li>
<li><p>[<strong>ObReferenceObjectByPointer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff558686)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ZwRegistryCreate</strong>](wdm-zwregistrycreate.md)</p></td>
<td align="left"><p>The [<strong>ZwRegistryCreate</strong>](wdm-zwregistrycreate.md) rule specifies that after calling [<strong>ZwCreateKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566425), the driver can call the following registry functions only while holding an open handle to the registry key (that is, before any calls to [<strong>ZwClose</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566417) or [<strong>ZwDeleteKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566437) to close or delete the handle to the registry key):</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ZwRegistryOpen</strong>](wdm-zwregistryopen.md)</p></td>
<td align="left"><p>The [<strong>ZwRegistryOpen</strong>](storport-zwregistryopen.md) rule specifies that after calling [<strong>ZwOpenKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567014), the driver calls the following registry functions only while holding an open handle to a registry key (that is, before calling [<strong>ZwClose</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566417) or [<strong>ZwDeleteKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566437)):</p></td>
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

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 





