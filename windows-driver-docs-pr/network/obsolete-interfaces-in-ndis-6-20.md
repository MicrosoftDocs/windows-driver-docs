---
title: Obsolete Interfaces in NDIS 6.20
description: Obsolete Interfaces in NDIS 6.20
ms.assetid: 11c3abd5-651e-4f9c-9f0b-ced6c00947f1
keywords: ["NDIS 6.20 WDK , obsolete NDIS 6.1 interfaces", "obsolete NDIS 6.1 interfaces WDK NDIS 6.20"]
---

# Obsolete Interfaces in NDIS 6.20


## <a href="" id="ddk-obsolete-interfaces-in-ndis-6-20-ng"></a>


Some NDIS 6.1 application interface elements are obsolete for NDIS 6.20 drivers.

The following table lists NDIS 6.1 interface elements and their NDIS 6.20 replacements.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Obsolete interface</th>
<th align="left">Use instead</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>LOCK_STATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557067)</p></td>
<td align="left"><p>[<strong>LOCK_STATE_EX</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557070)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NDIS_CURRENT_PROCESSOR_NUMBER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564915)</p></td>
<td align="left"><p>[<strong>NdisCurrentProcessorIndex</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561737)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>NDIS_MAX_PROCESSOR_COUNT</strong>(constant)</p></td>
<td align="left"><p>[<strong>NdisGroupMaxProcessorCount</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562689)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NDIS_RW_LOCK</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567277)</p></td>
<td align="left"><p>[<strong>NDIS_RW_LOCK_EX</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567279)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>MAXIMUM_PROCESSORS</strong>(constant)</p></td>
<td align="left"><p>[<strong>NdisGroupMaxProcessorCount</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562689)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NdisSystemProcessorCount</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564579)</p></td>
<td align="left"><p>[<strong>NdisGroupMaxProcessorCount</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562689)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NdisSystemActiveProcessorCount</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564577)</p></td>
<td align="left"><p>[<strong>NdisGroupActiveProcessorCount</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562685)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NdisGetProcessorInformation</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562661)</p></td>
<td align="left"><p>[<strong>NdisGetProcessorInformationEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562662)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NdisMQueueDpc</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563637)</p></td>
<td align="left"><p>[<strong>NdisMQueueDpcEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563640)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Do not use the <em>TargetProcessors</em> parameter of MINIPORT_ISR_HANDLER ( [<em>MiniportInterrupt</em>](https://msdn.microsoft.com/library/windows/hardware/ff559395))</p></td>
<td align="left"><p>[<strong>NdisMQueueDpcEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563640)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Do not use the <em>TargetProcessors</em> parameter of MINIPORT_MSI_ISR_HANDLER ( [<em>MiniportMessageInterrupt</em>](https://msdn.microsoft.com/library/windows/hardware/ff559407))</p></td>
<td align="left"><p>[<strong>NdisMQueueDpcEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563640)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NDIS_NBL_MEDIA_SPECIFIC_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566515)</p></td>
<td align="left"><p>[<strong>NDIS_NBL_MEDIA_SPECIFIC_INFORMATION_EX</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566518)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_GEN_PHYSICAL_MEDIUM](https://msdn.microsoft.com/library/windows/hardware/ff569621)</p></td>
<td align="left"><p>[OID_GEN_PHYSICAL_MEDIUM_EX](https://msdn.microsoft.com/library/windows/hardware/ff569622)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_PNP_ADD_WAKE_UP_PATTERN](https://msdn.microsoft.com/library/windows/hardware/ff569773)</p></td>
<td align="left"><p>[OID_PM_ADD_WOL_PATTERN](https://msdn.microsoft.com/library/windows/hardware/ff569764)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_PNP_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569774)</p></td>
<td align="left"><p>[OID_PM_CURRENT_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569765)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_PNP_ENABLE_WAKE_UP](https://msdn.microsoft.com/library/windows/hardware/ff569775)</p></td>
<td align="left"><p>[OID_PM_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569768)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_PNP_REMOVE_WAKE_UP_PATTERN](https://msdn.microsoft.com/library/windows/hardware/ff569779)</p></td>
<td align="left"><p>[OID_PM_REMOVE_WOL_PATTERN](https://msdn.microsoft.com/library/windows/hardware/ff569771)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_PNP_WAKE_UP_PATTERN_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569783)</p></td>
<td align="left"><p>[OID_PM_WOL_PATTERN_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569772)</p></td>
</tr>
</tbody>
</table>

 

 

 





