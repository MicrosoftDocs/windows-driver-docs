---
title: IrpProcessing rule set (KMDF)
description: Use these rules to verify that your driver correctly processes I/O request packets (IRP).
ms.assetid: B403F21E-FE35-4A57-92DB-C78FDC1488BD
---

# IrpProcessing rule set (KMDF)


Use these rules to verify that your driver correctly processes I/O request packets (IRP).

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
<td align="left"><p>[<strong>FwdIrpToIoQueueValid</strong>](kmdf-fwdirptoioqueuevalid.md)</p></td>
<td align="left"><p>The rule [<strong>FwdIrpToIoQueueValid</strong>](kmdf-fwdirptoioqueuevalid.md) specifies that the driver sends an IRP to an I/O queue, using [<strong>WdfDeviceWdmDispatchIrpToIoQueue</strong>](https://msdn.microsoft.com/library/windows/hardware/hh451105) method from either the [<em>EvtDeviceWdmIrpDispatch</em>](https://msdn.microsoft.com/library/windows/hardware/hh406404) callback or the [<em>EvtDeviceWdmIrpPreprocess</em>](https://msdn.microsoft.com/library/windows/hardware/ff540925) callback.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetCompletionRoutineFromDispatch</strong>](kmdf-setcompletionroutinefromdispatch.md)</p></td>
<td align="left"><p>The [<strong>SetCompletionRoutineFromDispatch</strong>](kmdf-setcompletionroutinefromdispatch.md) rule verifies that the driver does not specify a completion routine on an IRP from their [<em>EvtDeviceWdmIrpDispatch</em>](https://msdn.microsoft.com/library/windows/hardware/hh406404) callback function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>MiniportOnlyWdmDevice</strong>](kmdf-miniportonlywdmdevice.md)</p></td>
<td align="left"><p>The [<strong>MiniportOnlyWdmDevice</strong>](kmdf-miniportonlywdmdevice.md) rule specifies that WDF drivers should not use [<strong>IoCreateDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548397) and [<strong>IoCreateDeviceSecure</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548407) functions to create bare WDM device objects. This will cause a the computer to crash if someone tries to send an IRP to the WDM device. This is because IRP dispatch entries of the device are set to WDF-specific entries, but the framework hasn’t created a WDF device. However, miniport drivers can use the DDIs because driver dispatch entry points aren’t set for them.</p></td>
</tr>
</tbody>
</table>

 

**To select the IrpProcessing rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **IrpProcessing**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **IrpProcessing.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:IrpProcessing.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20IrpProcessing%20rule%20set%20%28KMDF%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




