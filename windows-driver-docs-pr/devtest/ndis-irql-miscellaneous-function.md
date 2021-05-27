---
title: Irql\_Miscellaneous\_Function rule (ndis)
description: The Irql\_Miscellaneous\_Function rule specifies that the NDIS functions must be called at correct IRQL levels.
ms.date: 05/21/2018
keywords: ["Irql_Miscellaneous_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_Miscellaneous_Function
api_type:
- NA
ms.localizationpriority: medium
---

# Irql\_Miscellaneous\_Function rule (ndis)


The Irql\_Miscellaneous\_Function rule specifies that the NDIS functions must be called at correct IRQL levels.

This rule verifies the following functions:

**KeGetCurrentProcessorNumber**
**NdisAllocateFromNPagedLookasideList**
**NdisAllocateGenericObject**
**NdisAllocateIoWorkItem**
**NdisAllocateMemoryWithTagPriority**
**NdisAnsiStringToUnicodeString**
**NdisCloseConfiguration**
**NdisCloseFile**
**NdisDeleteNPagedLookasideList**
**NdisDeregisterDeviceEx**
**NdisEqualMemory**
**NdisEqualUnicodeString**
**NdisFreeGenericObject**
**NdisFreeIoWorkItem**
**NdisFreeMemory**
**NdisFreeSpinLock**
**NdisFreeString**
**NdisFreeToNPagedLookasideList**
**NdisGeneratePartialCancelId**
**NdisGetCurrentProcessorCounts**
**NdisGetDriverHandle**
**NdisGetRoutineAddress**
**NdisGetSharedDataAlignment**
**NdisGetVersion**
**NdisInitAnsiString**
**NdisInitializeListHead**
**NdisInitializeNPagedLookasideList**
**NdisInitializeSListHead**
**NdisInitializeString**
**NdisInitUnicodeString**
**NdisMapFile**
**NdisOpenConfigurationEx**
**NdisOpenConfigurationKeyByIndex**
**NdisOpenConfigurationKeyByName**
**NdisOpenFile**
**NdisQueryAdapterInstanceName**
**NdisQueryDepthSList**
**NdisQueueIoWorkItem**
**NdisReadConfiguration**
**NdisReadNetworkAddress**
**NdisReEnumerateProtocolBindings**
**NdisSetOptionalHandlers**
**NdisSystemProcessorCount**
**NdisUnicodeStringToAnsiString**
**NdisUnmapFile**
**NdisUpcaseUnicodeString**
**NdisWaitEvent**
**NdisWriteConfiguration**
**NdisWriteErrorLogEntry**
**NdisWriteEventLogEntry**

**Driver model: NDIS**

## How to test

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>Irql_Miscellaneous_Function</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](./using-static-driver-verifier-to-find-defects-in-drivers.md#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](./using-static-driver-verifier-to-find-defects-in-drivers.md#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](./using-static-driver-verifier-to-find-defects-in-drivers.md#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

## Applies to

[**NdisAllocateFromNPagedLookasideList**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatefromnpagedlookasidelist)  
[**NdisAllocateGenericObject**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocategenericobject)  
[**NdisAllocateIoWorkItem**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocateioworkitem)  
[**NdisAllocateMemoryWithTagPriority**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatememorywithtagpriority)  
[**NdisAnsiStringToUnicodeString**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisansistringtounicodestring)  
[**NdisCloseConfiguration**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscloseconfiguration)  
[**NdisCloseFile**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclosefile)  
[**NdisDeleteNPagedLookasideList**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisdeletenpagedlookasidelist)  
[**NdisDeregisterDeviceEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisderegisterdeviceex)  
[**NdisEqualMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisequalmemory)  
[**NdisEqualString**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisequalstring)  
[**NdisEqualUnicodeString**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisequalunicodestring)  
[**NdisFreeGenericObject**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreegenericobject)  
[**NdisFreeIoWorkItem**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreeioworkitem)  
[**NdisFreeMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreememory)  
[**NdisFreeString**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreestring)  
[**NdisFreeToNPagedLookasideList**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreetonpagedlookasidelist)  
[**NdisGeneratePartialCancelId**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgeneratepartialcancelid)  
[**NdisGetCurrentProcessorCounts**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgetcurrentprocessorcounts)  
[**NdisGetRoutineAddress**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgetroutineaddress)  
[**NdisGetSharedDataAlignment**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgetshareddataalignment)  
[**NdisGetVersion**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgetversion)  
[**NdisInitAnsiString**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisinitansistring)  
[**NdisInitializeNPagedLookasideList**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisinitializenpagedlookasidelist)  
[**NdisInitializeString**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisinitializestring)  
[**NdisInitUnicodeString**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisinitunicodestring)  
[**NdisMapFile**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismapfile)  
[**NdisOpenConfigurationEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisopenconfigurationex)  
[**NdisOpenConfigurationKeyByIndex**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisopenconfigurationkeybyindex)  
[**NdisOpenConfigurationKeyByName**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisopenconfigurationkeybyname)  
[**NdisOpenFile**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisopenfile)  
[**NdisQueryAdapterInstanceName**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisqueryadapterinstancename)  
[**NdisQueryDepthSList**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisquerydepthslist)  
[**NdisQueueIoWorkItem**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisqueueioworkitem)  
[**NdisReadConfiguration**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreadconfiguration)  
[**NdisReadNetworkAddress**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreadnetworkaddress)  
[**NdisReEnumerateProtocolBindings**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreenumerateprotocolbindings)  
[**NdisRegisterDeviceEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisregisterdeviceex)  
[**NdisSetOptionalHandlers**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers)  
[**NdisSystemProcessorCount**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissystemprocessorcount)  
[**NdisUnicodeStringToAnsiString**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisunicodestringtoansistring)  
[**NdisUnmapFile**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisunmapfile)  
[**NdisUpcaseUnicodeString**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisupcaseunicodestring)  
[**NdisWaitEvent**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiswaitevent)  
[**NdisWriteConfiguration**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiswriteconfiguration)  
[**NdisWriteErrorLogEntry**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiswriteerrorlogentry)  
[**NdisWriteEventLogEntry**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiswriteeventlogentry)  
[**KeGetCurrentProcessorNumber**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-kegetcurrentprocessornumber)
