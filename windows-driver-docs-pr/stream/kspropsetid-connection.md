---
title: KSPROPSETID\_Connection
description: KSPROPSETID\_Connection
ms.assetid: 1be062ab-7396-4876-ab28-8a03e55df1d3
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_Connection


## <span id="ddk_kspropsetid_connection_ks"></span><span id="DDK_KSPROPSETID_CONNECTION_KS"></span>


Clients use the properties in the KSPROPSETID\_Connection property set to examine or set the state of a connection on a pin. Pin instances handle these properties.

Stream class minidrivers do not have to handle [**KSPROPERTY\_CONNECTION\_STATE**](ksproperty-connection-state.md) or [**KSPROPERTY\_CONNECTION\_PROPOSEDATAFORMAT**](ksproperty-connection-proposedataformat.md) properties directly. The stream class driver handles them, using stream request blocks (SRB) to query for more information where necessary.

The KSPROPSETID\_Connection property set includes:

[**KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING**](ksproperty-connection-allocatorframing.md)

[**KSPROPERTY\_CONNECTION\_ALLOCATORFRAMING\_EX**](ksproperty-connection-allocatorframing-ex.md)

[**KSPROPERTY\_CONNECTION\_ACQUIREORDERING**](ksproperty-connection-acquireordering.md)

[**KSPROPERTY\_CONNECTION\_DATAFORMAT**](ksproperty-connection-dataformat.md)

[**KSPROPERTY\_CONNECTION\_PRIORITY**](ksproperty-connection-priority.md)

[**KSPROPERTY\_CONNECTION\_PROPOSEDATAFORMAT**](ksproperty-connection-proposedataformat.md)

[**KSPROPERTY\_CONNECTION\_STARTAT**](ksproperty-connection-startat.md)

[**KSPROPERTY\_CONNECTION\_STATE**](ksproperty-connection-state.md)

 

 





