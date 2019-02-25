---
title: Diagnostics and Debugging
description: Diagnostics and Debugging
ms.assetid: 6c5c1b4a-338d-4550-903d-c6905ce743f9
keywords:
- RDBSS WDK file systems , diagnostics
- Redirected Drive Buffering Subsystem WDK file systems , diagnostics
- diagnostics WDK RDBSS
- debugging drivers WDK RDBSS
- driver debugging WDK RDBSS
- RDBSS WDK file systems , debugging
- Redirected Drive Buffering Subsystem WDK file systems , debugging
- dereference tracking WDK RDBSS
- reference tracking WDK RDBSS
- assert routine WDK RDBSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Diagnostics and Debugging


## <span id="ddk_diagnostics_and_debugging_if"></span><span id="DDK_DIAGNOSTICS_AND_DEBUGGING_IF"></span>


RDBSS provides a number of routines for diagnostic and debugging purposes. These routines fall into two categories:

-   Assert and debug routines

-   Reference and dereference tracking routines

These routines include the items in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Routine</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553384" data-raw-source="[&lt;strong&gt;RxAssert&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553384)"><strong>RxAssert</strong></a></p></td>
<td align="left"><p>This routine sends an assert string in checked builds of RDBSS to a kernel debugger if one is installed. When the rxAssert.h include file is used, Windows kernel <strong>RtlAssert</strong> calls will be redefined to call this <a href="https://msdn.microsoft.com/library/windows/hardware/ff553384" data-raw-source="[&lt;strong&gt;RxAssert&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553384)"><strong>RxAssert</strong></a> routine as well.</p>
<p>For retail builds, calls to this routine will bug check.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554385" data-raw-source="[&lt;strong&gt;RxDbgBreakPoint&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554385)"><strong>RxDbgBreakPoint</strong></a></p></td>
<td align="left"><p>This routine raises an exception that is handled by the kernel debugger if one is installed; otherwise, it is handled by the debug system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554655" data-raw-source="[&lt;strong&gt;RxpTrackDereference&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554655)"><strong>RxpTrackDereference</strong></a></p></td>
<td align="left"><p>This routine is used to track a request to reference SRV_CALL, NET_ROOT, V_NET_ROOT, FOBX, FCB, and SRV_OPEN structures in checked builds. A log of these reference requests can be accessed by the logging system and WMI. This routine does not perform the dereference operation.</p>
<p>For retail builds, this routine does nothing.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554659" data-raw-source="[&lt;strong&gt;RxpTrackReference&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554659)"><strong>RxpTrackReference</strong></a></p></td>
<td align="left"><p>This routine is used to track a request to dereference SRV_CALL, NET_ROOT, V_NET_ROOT, FOBX, FCB, and SRV_OPEN structures in checked builds. A log of these dereference requests can be accessed by the logging system and WMI. This routine does not perform the reference operation.</p>
<p>For retail builds, this routine does nothing.</p></td>
</tr>
</tbody>
</table>

 

In addition to the routines listed in the previous table, a number of macros that call these routines are defined for debugging. These macros, which are listed in the following table, provide a wrapper around the [**RxReference**](https://msdn.microsoft.com/library/windows/hardware/ff554688) or [**RxDereference**](https://msdn.microsoft.com/library/windows/hardware/ff554388) routines used for file structure management operations on SRV\_CALL, NET\_ROOT, V\_NET\_ROOT, FOBX, FCB, and SRV\_OPEN structures. These macros first call the corresponding [**RxpTrackReference**](https://msdn.microsoft.com/library/windows/hardware/ff554659) or [**RxpTrackDereference**](https://msdn.microsoft.com/library/windows/hardware/ff554655) routine to log diagnostic information before calling the corresponding **RxReference** or **RxDeference** routine. A log of the reference and dereference requests can be accessed by the RDBSS logging system and WMI.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Macro</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>RxDereferenceAndFinalizeNetFcb</strong> (<em>Fcb ,RxContext</em>, <em>RecursiveFinalize</em>, <em>ForceFinalize</em>)</p></td>
<td align="left"><p>This macro is used to track dereference operations on FCB structures.</p>
<p>Note that this macro manipulates the reference count and also returns the status of the finalize call.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RxDereferenceNetFcb</strong> (<em>Fcb</em>)</p></td>
<td align="left"><p>This macro is used to track dereference operations on FCB structures.</p>
<p>Note that this macro manipulates the reference count and also returns the status of the final dereference call.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RxDereferenceNetFobx</strong> (<em>Fobx,LockHoldingState</em>)</p></td>
<td align="left"><p>This macro is used to track dereference operations on FOBX structures.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RxDereferenceNetRoot</strong> (<em>NetRoot</em>, <em>LockHoldingState</em>)</p></td>
<td align="left"><p>This macro is used to track dereference operations on NET_ROOT structures.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RxDereferenceSrvCall</strong> (<em>SrvCall</em>, <em>LockHoldingState</em>)</p></td>
<td align="left"><p>This macro is used to track dereference operations on SRV_CALL structures.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RxDereferenceSrvOpen</strong> ( <em>SrvOpen</em>, <em>LockHoldingState</em>)</p></td>
<td align="left"><p>This macro is used to track dereference operations on SRV_OPEN structures.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RxDereferenceVNetRoot</strong> ( <em>VNetRoot</em>, <em>LockHoldingState</em>)</p></td>
<td align="left"><p>This macro is used to track dereference operations on NET_ROOT structures.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RxReferenceNetFcb</strong> (<em>Fcb</em>)</p></td>
<td align="left"><p>This macro is used to track reference operations on FCB structures.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RxReferenceNetFobx</strong> (<em>Fobx</em>)</p></td>
<td align="left"><p>This macro is used to track reference operations on FOBX structures.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RxReferenceNetRoot</strong> (<em>NetRoot</em>)</p></td>
<td align="left"><p>This macro is used to track reference operations on NET_ROOT structures.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RxReferenceSrvCall</strong> (<em>SrvCall</em>)</p></td>
<td align="left"><p>This macro is used to track reference operations on SRV_CALL structures that are not at DPC level.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RxReferenceSrvCallAtDpc</strong> (<em>SrvCall</em>)</p></td>
<td align="left"><p>This macro is used to track reference operations on SRV_CALL structures at DPC level.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RxReferenceSrvOpen</strong> (<em>SrvOpen</em>)</p></td>
<td align="left"><p>This macro is used to track reference operations on SRV_OPEN structures.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RxReferenceVNetRoot</strong> (<em>VNetRoot</em>)</p></td>
<td align="left"><p>This macro is used to track reference operations on V_NET_ROOT structures.</p></td>
</tr>
</tbody>
</table>

 

 

 




