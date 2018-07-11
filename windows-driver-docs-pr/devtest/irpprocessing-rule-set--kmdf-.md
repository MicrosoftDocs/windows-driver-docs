---
title: IrpProcessing rule set (KMDF)
description: Use these rules to verify that your driver correctly processes I/O request packets (IRP).
ms.assetid: B403F21E-FE35-4A57-92DB-C78FDC1488BD
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 





