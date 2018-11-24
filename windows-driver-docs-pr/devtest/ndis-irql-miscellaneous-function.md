---
title: Irql\_Miscellaneous\_Function rule (ndis)
description: The Irql\_Miscellaneous\_Function rule specifies that the NDIS functions must be called at correct IRQL levels.
ms.assetid: ae1d0243-1db9-428f-a112-f438e2322ff2
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

|              |      |
|--------------|------|
| Driver model | NDIS |

How to test
-----------

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>Irql_Miscellaneous_Function</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh454281" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**NdisAllocateFromNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff560708)
[**NdisAllocateGenericObject**](https://msdn.microsoft.com/library/windows/hardware/ff561603)
[**NdisAllocateIoWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff561604)
[**NdisAllocateMemoryWithTagPriority**](https://msdn.microsoft.com/library/windows/hardware/ff561606)
[**NdisAnsiStringToUnicodeString**](https://msdn.microsoft.com/library/windows/hardware/ff561619)
[**NdisCloseConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff561642)
[**NdisCloseFile**](https://msdn.microsoft.com/library/windows/hardware/ff561645)
[**NdisDeleteNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff561739)
[**NdisDeregisterDeviceEx**](https://msdn.microsoft.com/library/windows/hardware/ff561741)
[**NdisEqualMemory**](https://msdn.microsoft.com/library/windows/hardware/ff561760)
[**NdisEqualString**](https://msdn.microsoft.com/library/windows/hardware/ff561771)
[**NdisEqualUnicodeString**](https://msdn.microsoft.com/library/windows/hardware/ff561775)
[**NdisFreeGenericObject**](https://msdn.microsoft.com/library/windows/hardware/ff561850)
[**NdisFreeIoWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff561855)
[**NdisFreeMemory**](https://msdn.microsoft.com/library/windows/hardware/ff562577)
[**NdisFreeString**](https://msdn.microsoft.com/library/windows/hardware/ff562604)
[**NdisFreeToNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff562607)
[**NdisGeneratePartialCancelId**](https://msdn.microsoft.com/library/windows/hardware/ff562623)
[**NdisGetCurrentProcessorCounts**](https://msdn.microsoft.com/library/windows/hardware/ff562625)
[**NdisGetRoutineAddress**](https://msdn.microsoft.com/library/windows/hardware/ff562665)
[**NdisGetSharedDataAlignment**](https://msdn.microsoft.com/library/windows/hardware/ff562671)
[**NdisGetVersion**](https://msdn.microsoft.com/library/windows/hardware/ff562680)
[**NdisInitAnsiString**](https://msdn.microsoft.com/library/windows/hardware/ff562730)
[**NdisInitializeNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff562736)
[**NdisInitializeString**](https://msdn.microsoft.com/library/windows/hardware/ff562741)
[**NdisInitUnicodeString**](https://msdn.microsoft.com/library/windows/hardware/ff562745)
[**NdisMapFile**](https://msdn.microsoft.com/library/windows/hardware/ff562785)
[**NdisOpenConfigurationEx**](https://msdn.microsoft.com/library/windows/hardware/ff563717)
[**NdisOpenConfigurationKeyByIndex**](https://msdn.microsoft.com/library/windows/hardware/ff563721)
[**NdisOpenConfigurationKeyByName**](https://msdn.microsoft.com/library/windows/hardware/ff563725)
[**NdisOpenFile**](https://msdn.microsoft.com/library/windows/hardware/ff563728)
[**NdisQueryAdapterInstanceName**](https://msdn.microsoft.com/library/windows/hardware/ff563745)
[**NdisQueryDepthSList**](https://msdn.microsoft.com/library/windows/hardware/ff563753)
[**NdisQueueIoWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff563775)
[**NdisReadConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff564511)
[**NdisReadNetworkAddress**](https://msdn.microsoft.com/library/windows/hardware/ff564512)
[**NdisReEnumerateProtocolBindings**](https://msdn.microsoft.com/library/windows/hardware/ff564516)
[**NdisRegisterDeviceEx**](https://msdn.microsoft.com/library/windows/hardware/ff564518)
[**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550)
[**NdisSystemProcessorCount**](https://msdn.microsoft.com/library/windows/hardware/ff564579)
[**NdisUnicodeStringToAnsiString**](https://msdn.microsoft.com/library/windows/hardware/ff564635)
[**NdisUnmapFile**](https://msdn.microsoft.com/library/windows/hardware/ff564641)
[**NdisUpcaseUnicodeString**](https://msdn.microsoft.com/library/windows/hardware/ff564644)
[**NdisWaitEvent**](https://msdn.microsoft.com/library/windows/hardware/ff564651)
[**NdisWriteConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff564659)
[**NdisWriteErrorLogEntry**](https://msdn.microsoft.com/library/windows/hardware/ff564663)
[**NdisWriteEventLogEntry**](https://msdn.microsoft.com/library/windows/hardware/ff564672)
[**KeGetCurrentProcessorNumber**](https://msdn.microsoft.com/library/windows/hardware/ff552063)








