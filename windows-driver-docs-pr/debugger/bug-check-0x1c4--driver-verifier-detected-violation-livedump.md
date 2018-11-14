---
title: Bug Check 0x1C4 DRIVER_VERIFIER_DETECTED_VIOLATION_LIVEDUMP
description: The DRIVER_VERIFIER_DETECTED_VIOLATION_LIVEDUMP bug check has a value of 0x000001C4.
ms.assetid: B5C00570-477C-4C0C-B8B9-A7796FC33D63
keywords: ["Bug Check 0x1C4 DRIVER_VERIFIER_DETECTED_VIOLATION_LIVEDUMP", "DRIVER_VERIFIER_DETECTED_VIOLATION_LIVEDUMP"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DRIVER_VERIFIER_DETECTED_VIOLATION_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1C4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION\_LIVEDUMP


The DRIVER\_VERIFIER\_DETECTED\_VIOLATION\_LIVEDUMP bug check has a value of 0x000001C4. This indicates that a device driver attempting to corrupt the system has been detected. This is because the driver was specified in the registry as being suspect (by the administrator) and the kernel has enabled substantial checking of this driver. For more information, see [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448).

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## DRIVER\_VERIFIER\_DETECTED\_VIOLATION\_LIVEDUMP Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">1</td>
<td align="left"><p>The subclass of driver violation.</p>
<div class="code">
<code>0x00081001: ID of the &amp;#39;KsDeviceMutex&amp;#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00081002: ID of the &#39;KsStreamPointerClone&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00081003: ID of the &#39;KsStreamPointerLock&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved 

        0x00081004: ID of the &#39;KsStreamPointerUnlock&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00081005: ID of the &#39;KsCallbackReturn&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00081006: ID of the &#39;KsIrqlDeviceCallbacks&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00081007: ID of the &#39;KsIrqlFilterCallbacks&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00081008: ID of the &#39;KsIrqlPinCallbacks&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00081009: ID of the &#39;KsIrqlDDIs&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x0008100A: ID of the &#39;KsFilterMutex&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x0008100B: ID of the &#39;KsProcessingMutex&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00082001: ID of the &#39;KsTimedPinSetDeviceState&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00082002: ID of the &#39;KsTimedDeviceCallbacks&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00082003: ID of the &#39;KsTimedFilterCallbacks&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00082004: ID of the &#39;KsTimedPinCallbacks&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00082005: ID of the &#39;KsTimedProcessingMutex&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00071001: ID of the &#39;PcIrqlDDIs&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00071003: ID of the &#39;PcIrqlIport&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00071004: ID of the &#39;PcUnmapAllocatedPages&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00071005: ID of the &#39;PcAllocatedPages&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00071006: ID of the &#39;PcRegisterAdapterPower&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00071007: ID of the &#39;PcAddAdapterDevice&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00071008: ID of the &#39;PcPropertyRequest&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00071009: ID of the &#39;PcAllocateAndMapPages&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x0007100A: ID of the &#39;PcPoRequestPowerIrp&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00072001: ID of the &#39;PcTimedWaveRtStreamSetState&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00020002: ID of the &#39;IrqlApcLte&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00020003: ID of the &#39;IrqlDispatch&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00020004: ID of the &#39;IrqlExAllocatePool&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00020005: ID of the &#39;IrqlExApcLte1&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00020006: ID of the &#39;IrqlExApcLte2&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00020007: ID of the &#39;IrqlExApcLte3&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00020008: ID of the &#39;IrqlExPassive&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00020009: ID of the &#39;IrqlIoApcLte&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x0002000A: ID of the &#39;IrqlIoPassive1&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x0002000B: ID of the &#39;IrqlIoPassive2&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x0002000C: ID of the &#39;IrqlIoPassive3&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x0002000D: ID of the &#39;IrqlIoPassive4&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x0002000E: ID of the &#39;IrqlIoPassive5&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x0002000F: ID of the &#39;IrqlKeApcLte1&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00020010: ID of the &#39;IrqlKeApcLte2&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00020011: ID of the &#39;IrqlKeDispatchLte&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00020015: ID of the &#39;IrqlKeReleaseSpinLock&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00020016: ID of the &#39;IrqlKeSetEvent&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00020019: ID of the &#39;IrqlMmApcLte&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x0002001A: ID of the &#39;IrqlMmDispatch&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x0002001B: ID of the &#39;IrqlObPassive&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x0002001C: ID of the &#39;IrqlPsPassive&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x0002001D: ID of the &#39;IrqlReturn&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x0002001E: ID of the &#39;IrqlRtlPassive&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x0002001F: ID of the &#39;IrqlZwPassive&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00020022: ID of the &#39;IrqlIoDispatch&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00040003: ID of the &#39;CriticalRegions&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00040006: ID of the &#39;QueuedSpinLock&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00040007: ID of the &#39;QueuedSpinLockRelease&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00040009: ID of the &#39;SpinLock&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x0004000A: ID of the &#39;SpinlockRelease&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x0004000E: ID of the &#39;GuardedRegions&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x0004100B: ID of the &#39;RequestedPowerIrp&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x0004100F: ID of the &#39;IoSetCompletionExCompleteIrp&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00043006: ID of the &#39;PnpRemove&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00091001: ID of the &#39;NdisOidComplete&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00091002: ID of the &#39;NdisOidDoubleComplete&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x0009100E: ID of the &#39;NdisOidDoubleRequest&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00092003: ID of the &#39;NdisTimedOidComplete&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x0009200D: ID of the &#39;NdisTimedDataSend&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x0009200F: ID of the &#39;NdisTimedDataHang&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00092010: ID of the &#39;NdisFilterTimedPauseComplete&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00092011: ID of the &#39;NdisFilterTimedDataSend&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00092012: ID of the &#39;NdisFilterTimedDataReceive&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00093004: ID of the &#39;WlanAssociation&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00093005: ID of the &#39;WlanConnectionRoaming&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00093006: ID of the &#39;WlanDisassociation&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00093101: ID of the &#39;WlanAssert&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Reserved  
            Parameter 4 - Reserved  

        0x00094007: ID of the &#39;WlanTimedAssociation&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00094008: ID of the &#39;WlanTimedConnectionRoaming&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x00094009: ID of the &#39;WlanTimedConnectRequest&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x0009400B: ID of the &#39;WlanTimedLinkQuality&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo). 

        0x0009400C: ID of the &#39;WlanTimedScan&#39; rule that was violated.
            Parameter 2 - A pointer to the string describing the violated rule condition.
            Parameter 3 - Address of internal rule state (second argument to !ruleinfo).
            Parameter 4 - Address of supplemental states (third argument to !ruleinfo).</code>
</div></td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">See parameter 1</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">See parameter 1</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">See parameter 1</td>
</tr>
</tbody>
</table>










