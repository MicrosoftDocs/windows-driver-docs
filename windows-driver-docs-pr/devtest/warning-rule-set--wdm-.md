---
title: Warning rule set (WDM)
description: Use these rules to verify that your driver can correctly processes IRPs in various contexts and follows Microsoft recommended best practices.
ms.assetid: 29374BBE-D1DF-48C0-80A9-96CBAC6D8A22
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Warning%20rule%20set%20%28WDM%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




