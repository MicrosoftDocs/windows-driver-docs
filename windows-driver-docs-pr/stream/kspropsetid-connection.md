---
title: KSPROPSETID\_Connection
description: KSPROPSETID\_Connection
MS-HAID:
- 'ks-prop\_fc940ef1-e39a-4db2-bd68-ba850830d989.xml'
- 'stream.kspropsetid\_connection'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1be062ab-7396-4876-ab28-8a03e55df1d3
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPSETID_Connection%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




