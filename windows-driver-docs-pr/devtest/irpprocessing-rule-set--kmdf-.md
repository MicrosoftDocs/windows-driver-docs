---
title: IrpProcessing rule set (KMDF)
description: Use these rules to verify that your driver correctly processes I/O request packets (IRP).
ms.assetid: B403F21E-FE35-4A57-92DB-C78FDC1488BD
ms.date: 05/21/2018
ms.localizationpriority: medium
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
<td align="left"><p><a href="kmdf-fwdirptoioqueuevalid.md" data-raw-source="[&lt;strong&gt;FwdIrpToIoQueueValid&lt;/strong&gt;](kmdf-fwdirptoioqueuevalid.md)"><strong>FwdIrpToIoQueueValid</strong></a></p></td>
<td align="left"><p>The rule <a href="kmdf-fwdirptoioqueuevalid.md" data-raw-source="[&lt;strong&gt;FwdIrpToIoQueueValid&lt;/strong&gt;](kmdf-fwdirptoioqueuevalid.md)"><strong>FwdIrpToIoQueueValid</strong></a> specifies that the driver sends an IRP to an I/O queue, using <a href="https://msdn.microsoft.com/library/windows/hardware/hh451105" data-raw-source="[&lt;strong&gt;WdfDeviceWdmDispatchIrpToIoQueue&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451105)"><strong>WdfDeviceWdmDispatchIrpToIoQueue</strong></a> method from either the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406404" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpDispatch&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/hh406404)"><em>EvtDeviceWdmIrpDispatch</em></a> callback or the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540925" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpPreprocess&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540925)"><em>EvtDeviceWdmIrpPreprocess</em></a> callback.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-setcompletionroutinefromdispatch.md" data-raw-source="[&lt;strong&gt;SetCompletionRoutineFromDispatch&lt;/strong&gt;](kmdf-setcompletionroutinefromdispatch.md)"><strong>SetCompletionRoutineFromDispatch</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-setcompletionroutinefromdispatch.md" data-raw-source="[&lt;strong&gt;SetCompletionRoutineFromDispatch&lt;/strong&gt;](kmdf-setcompletionroutinefromdispatch.md)"><strong>SetCompletionRoutineFromDispatch</strong></a> rule verifies that the driver does not specify a completion routine on an IRP from their <a href="https://msdn.microsoft.com/library/windows/hardware/hh406404" data-raw-source="[&lt;em&gt;EvtDeviceWdmIrpDispatch&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/hh406404)"><em>EvtDeviceWdmIrpDispatch</em></a> callback function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-miniportonlywdmdevice.md" data-raw-source="[&lt;strong&gt;MiniportOnlyWdmDevice&lt;/strong&gt;](kmdf-miniportonlywdmdevice.md)"><strong>MiniportOnlyWdmDevice</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-miniportonlywdmdevice.md" data-raw-source="[&lt;strong&gt;MiniportOnlyWdmDevice&lt;/strong&gt;](kmdf-miniportonlywdmdevice.md)"><strong>MiniportOnlyWdmDevice</strong></a> rule specifies that WDF drivers should not use <a href="https://msdn.microsoft.com/library/windows/hardware/ff548397" data-raw-source="[&lt;strong&gt;IoCreateDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548397)"><strong>IoCreateDevice</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff548407" data-raw-source="[&lt;strong&gt;IoCreateDeviceSecure&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548407)"><strong>IoCreateDeviceSecure</strong></a> functions to create bare WDM device objects. This will cause a the computer to crash if someone tries to send an IRP to the WDM device. This is because IRP dispatch entries of the device are set to WDF-specific entries, but the framework hasn’t created a WDF device. However, miniport drivers can use the DDIs because driver dispatch entry points aren’t set for them.</p></td>
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

 

 





