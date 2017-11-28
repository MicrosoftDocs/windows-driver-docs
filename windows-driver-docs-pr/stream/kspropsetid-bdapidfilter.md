---
title: KSPROPSETID\_BdaPIDFilter
description: KSPROPSETID\_BdaPIDFilter
ms.assetid: 9a2655cb-d7e9-4f61-803a-63fe3fd3501b
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPSETID_BdaPIDFilter%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




