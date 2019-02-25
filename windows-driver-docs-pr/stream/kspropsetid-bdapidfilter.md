---
title: KSPROPSETID\_BdaPIDFilter
description: KSPROPSETID\_BdaPIDFilter
ms.assetid: 9a2655cb-d7e9-4f61-803a-63fe3fd3501b
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_BdaPIDFilter


## <span id="ddk_kspropsetid_bdapidfilter_ks"></span><span id="DDK_KSPROPSETID_BDAPIDFILTER_KS"></span>


KSPROPSETID\_BdaPIDFilter is the BDA packet identifier (PID) filter property set. It is used to filter out unwanted substreams from the received broadcast MPEG2 transport stream. This property set controls the properties of a PID filter node.

The following properties are available:

<span id="KSPROPERTY_BDA_PIDFILTER_MAP_PIDS"></span><span id="ksproperty_bda_pidfilter_map_pids"></span>[**KSPROPERTY\_BDA\_PIDFILTER\_MAP\_PIDS**](ksproperty-bda-pidfilter-map-pids.md)  
Informs the PID filter node about the list of MPEG2 PIDs of transport stream packets that should be passed to the downstream filter or node.

<span id="KSPROPERTY_BDA_PIDFILTER_UNMAP_PIDS"></span><span id="ksproperty_bda_pidfilter_unmap_pids"></span>[**KSPROPERTY\_BDA\_PIDFILTER\_UNMAP\_PIDS**](ksproperty-bda-pidfilter-unmap-pids.md)  
Informs the PID filter node about packets identified with specific PIDs to filter from the input stream.

<span id="KSPROPERTY_BDA_PIDFILTER_LIST_PIDS"></span><span id="ksproperty_bda_pidfilter_list_pids"></span>[**KSPROPERTY\_BDA\_PIDFILTER\_LIST\_PIDS**](ksproperty-bda-pidfilter-list-pids.md)  
Returns an array of PIDs that identify groups of packets that the PID filter node delivers from the input stream to the output stream.

 

 





