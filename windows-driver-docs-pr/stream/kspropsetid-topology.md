---
title: KSPROPSETID\_Topology
description: KSPROPSETID\_Topology
MS-HAID:
- 'ks-prop\_db1354a0-c7ab-43ee-9a5d-03207d7dd6f1.xml'
- 'stream.kspropsetid\_topology'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d0c51bcf-ced3-4863-9359-9fa326122262
---

# KSPROPSETID\_Topology


## <span id="ddk_kspropsetid_topology_ks"></span><span id="DDK_KSPROPSETID_TOPOLOGY_KS"></span>


Clients use requests in the KSPROPSETID\_Topology property set to examine a KS filter's internal topology.

Each node in the topology has a zero-based node ID: KS filters with *n* nodes number them from 0 to *n-1*. The whole KS filter itself may be treated as a node and has the special node ID number KSFILTER\_NODE.

Stream minidrivers do not need to handle the properties in this property set. The stream class driver handles them on behalf of the minidriver.

Microsoft defines a standard set of node types of the form KSNODETYPE\_XXX in the *ksmedia.h* header file. When using the properties in this set, clients refer to a node by its zero-based index in this sequence.

The KSPROPSETID\_Topology property set includes:

[**KSPROPERTY\_TOPOLOGY\_CATEGORIES**](ksproperty-topology-categories.md)

[**KSPROPERTY\_TOPOLOGY\_CONNECTIONS**](ksproperty-topology-connections.md)

[**KSPROPERTY\_TOPOLOGY\_NAME**](ksproperty-topology-name.md)

[**KSPROPERTY\_TOPOLOGY\_NODES**](ksproperty-topology-nodes.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPSETID_Topology%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




