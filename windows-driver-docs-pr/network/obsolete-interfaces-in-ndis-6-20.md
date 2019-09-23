---
title: Obsolete Interfaces in NDIS 6.20
description: Obsolete Interfaces in NDIS 6.20
ms.assetid: 11c3abd5-651e-4f9c-9f0b-ced6c00947f1
keywords:
- NDIS 6.20 WDK , obsolete NDIS 6.1 interfaces
- obsolete NDIS 6.1 interfaces WDK NDIS 6.20
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obsolete Interfaces in NDIS 6.20





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
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_lock_state" data-raw-source="[&lt;strong&gt;LOCK_STATE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_lock_state)"><strong>LOCK_STATE</strong></a></p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_lock_state_ex" data-raw-source="[&lt;strong&gt;LOCK_STATE_EX&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_lock_state_ex)"><strong>LOCK_STATE_EX</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/ndis-current-processor-number" data-raw-source="[&lt;strong&gt;NDIS_CURRENT_PROCESSOR_NUMBER&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-current-processor-number)"><strong>NDIS_CURRENT_PROCESSOR_NUMBER</strong></a></p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndiscurrentprocessorindex" data-raw-source="[&lt;strong&gt;NdisCurrentProcessorIndex&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndiscurrentprocessorindex)"><strong>NdisCurrentProcessorIndex</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>NDIS_MAX_PROCESSOR_COUNT</strong>(constant)</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisgroupmaxprocessorcount" data-raw-source="[&lt;strong&gt;NdisGroupMaxProcessorCount&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisgroupmaxprocessorcount)"><strong>NdisGroupMaxProcessorCount</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_rw_lock" data-raw-source="[&lt;strong&gt;NDIS_RW_LOCK&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_rw_lock)"><strong>NDIS_RW_LOCK</strong></a></p></td>
<td align="left"><p><a href="https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff567279(v=vs.85)" data-raw-source="[&lt;strong&gt;NDIS_RW_LOCK_EX&lt;/strong&gt;](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff567279(v=vs.85))"><strong>NDIS_RW_LOCK_EX</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>MAXIMUM_PROCESSORS</strong>(constant)</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisgroupmaxprocessorcount" data-raw-source="[&lt;strong&gt;NdisGroupMaxProcessorCount&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisgroupmaxprocessorcount)"><strong>NdisGroupMaxProcessorCount</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndissystemprocessorcount" data-raw-source="[&lt;strong&gt;NdisSystemProcessorCount&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndissystemprocessorcount)"><strong>NdisSystemProcessorCount</strong></a></p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisgroupmaxprocessorcount" data-raw-source="[&lt;strong&gt;NdisGroupMaxProcessorCount&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisgroupmaxprocessorcount)"><strong>NdisGroupMaxProcessorCount</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndissystemactiveprocessorcount" data-raw-source="[&lt;strong&gt;NdisSystemActiveProcessorCount&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndissystemactiveprocessorcount)"><strong>NdisSystemActiveProcessorCount</strong></a></p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisgroupactiveprocessorcount" data-raw-source="[&lt;strong&gt;NdisGroupActiveProcessorCount&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisgroupactiveprocessorcount)"><strong>NdisGroupActiveProcessorCount</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisgetprocessorinformation" data-raw-source="[&lt;strong&gt;NdisGetProcessorInformation&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisgetprocessorinformation)"><strong>NdisGetProcessorInformation</strong></a></p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisgetprocessorinformationex" data-raw-source="[&lt;strong&gt;NdisGetProcessorInformationEx&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisgetprocessorinformationex)"><strong>NdisGetProcessorInformationEx</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismqueuedpc" data-raw-source="[&lt;strong&gt;NdisMQueueDpc&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismqueuedpc)"><strong>NdisMQueueDpc</strong></a></p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismqueuedpcex" data-raw-source="[&lt;strong&gt;NdisMQueueDpcEx&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismqueuedpcex)"><strong>NdisMQueueDpcEx</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Do not use the <em>TargetProcessors</em> parameter of MINIPORT_ISR_HANDLER ( <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_isr" data-raw-source="[&lt;em&gt;MiniportInterrupt&lt;/em&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_isr)"><em>MiniportInterrupt</em></a>)</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismqueuedpcex" data-raw-source="[&lt;strong&gt;NdisMQueueDpcEx&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismqueuedpcex)"><strong>NdisMQueueDpcEx</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Do not use the <em>TargetProcessors</em> parameter of MINIPORT_MSI_ISR_HANDLER ( <a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_message_interrupt" data-raw-source="[&lt;em&gt;MiniportMessageInterrupt&lt;/em&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_message_interrupt)"><em>MiniportMessageInterrupt</em></a>)</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismqueuedpcex" data-raw-source="[&lt;strong&gt;NdisMQueueDpcEx&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismqueuedpcex)"><strong>NdisMQueueDpcEx</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_nbl_media_media_specific_information" data-raw-source="[&lt;strong&gt;NDIS_NBL_MEDIA_SPECIFIC_INFORMATION&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_nbl_media_media_specific_information)"><strong>NDIS_NBL_MEDIA_SPECIFIC_INFORMATION</strong></a></p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_nbl_media_specific_information_ex" data-raw-source="[&lt;strong&gt;NDIS_NBL_MEDIA_SPECIFIC_INFORMATION_EX&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_nbl_media_specific_information_ex)"><strong>NDIS_NBL_MEDIA_SPECIFIC_INFORMATION_EX</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-physical-medium" data-raw-source="[OID_GEN_PHYSICAL_MEDIUM](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-physical-medium)">OID_GEN_PHYSICAL_MEDIUM</a></p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-physical-medium-ex" data-raw-source="[OID_GEN_PHYSICAL_MEDIUM_EX](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-physical-medium-ex)">OID_GEN_PHYSICAL_MEDIUM_EX</a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-pnp-add-wake-up-pattern" data-raw-source="[OID_PNP_ADD_WAKE_UP_PATTERN](https://docs.microsoft.com/windows-hardware/drivers/network/oid-pnp-add-wake-up-pattern)">OID_PNP_ADD_WAKE_UP_PATTERN</a></p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-pm-add-wol-pattern" data-raw-source="[OID_PM_ADD_WOL_PATTERN](https://docs.microsoft.com/windows-hardware/drivers/network/oid-pm-add-wol-pattern)">OID_PM_ADD_WOL_PATTERN</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-pnp-capabilities" data-raw-source="[OID_PNP_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/network/oid-pnp-capabilities)">OID_PNP_CAPABILITIES</a></p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-pm-current-capabilities" data-raw-source="[OID_PM_CURRENT_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/network/oid-pm-current-capabilities)">OID_PM_CURRENT_CAPABILITIES</a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-pnp-enable-wake-up" data-raw-source="[OID_PNP_ENABLE_WAKE_UP](https://docs.microsoft.com/windows-hardware/drivers/network/oid-pnp-enable-wake-up)">OID_PNP_ENABLE_WAKE_UP</a></p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-pm-parameters" data-raw-source="[OID_PM_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-pm-parameters)">OID_PM_PARAMETERS</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-pnp-remove-wake-up-pattern" data-raw-source="[OID_PNP_REMOVE_WAKE_UP_PATTERN](https://docs.microsoft.com/windows-hardware/drivers/network/oid-pnp-remove-wake-up-pattern)">OID_PNP_REMOVE_WAKE_UP_PATTERN</a></p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-pm-remove-wol-pattern" data-raw-source="[OID_PM_REMOVE_WOL_PATTERN](https://docs.microsoft.com/windows-hardware/drivers/network/oid-pm-remove-wol-pattern)">OID_PM_REMOVE_WOL_PATTERN</a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-pnp-wake-up-pattern-list" data-raw-source="[OID_PNP_WAKE_UP_PATTERN_LIST](https://docs.microsoft.com/windows-hardware/drivers/network/oid-pnp-wake-up-pattern-list)">OID_PNP_WAKE_UP_PATTERN_LIST</a></p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-pm-wol-pattern-list" data-raw-source="[OID_PM_WOL_PATTERN_LIST](https://docs.microsoft.com/windows-hardware/drivers/network/oid-pm-wol-pattern-list)">OID_PM_WOL_PATTERN_LIST</a></p></td>
</tr>
</tbody>
</table>

 

 

 





