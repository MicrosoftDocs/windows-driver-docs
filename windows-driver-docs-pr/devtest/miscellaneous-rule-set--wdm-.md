---
title: Miscellaneous rule set (WDM)
description: Use these rules to verify that your driver correctly follows a general set of requirements for the proper handling of registry keys, strings and device object pointers.
ms.assetid: 50E8BFFE-AC38-4023-9FFB-DC53B749A603
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Miscellaneous%20rule%20set%20%28WDM%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




