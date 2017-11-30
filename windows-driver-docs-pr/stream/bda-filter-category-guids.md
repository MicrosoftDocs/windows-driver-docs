---
title: BDA Filter Category GUIDs
description: BDA Filter Category GUIDs
ms.assetid: fbd4bf91-8309-423a-97ea-7e4f90cd3b68
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# BDA Filter Category GUIDs


## <span id="ddk_bda_filter_category_guids_ks"></span><span id="DDK_BDA_FILTER_CATEGORY_GUIDS_KS"></span>


A BDA minidriver uses the BDA filter category GUIDs to specify the types of BDA filters to create. A BDA minidriver assigns these GUIDs in the array to which the **Categories** member of a [**KSFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562553) structure points. The *Bdamedia.h* header file defines these GUIDs.

The following filter category GUIDs are available in BDA:

<span id="KSCATEGORY_BDA_RECEIVER_COMPONENT"></span><span id="kscategory_bda_receiver_component"></span>KSCATEGORY\_BDA\_RECEIVER\_COMPONENT  
A BDA minidriver assigns this GUID to specify to create a BDA receiver filter.

<span id="KSCATEGORY_BDA_NETWORK_TUNER"></span><span id="kscategory_bda_network_tuner"></span>KSCATEGORY\_BDA\_NETWORK\_TUNER  
A BDA minidriver assigns this GUID to specify to create a BDA network tuner filter.

<span id="KSCATEGORY_BDA_NETWORK_EPG"></span><span id="kscategory_bda_network_epg"></span>KSCATEGORY\_BDA\_NETWORK\_EPG  
A BDA minidriver assigns this GUID to specify to create a BDA electronic program guide (EPG) filter.

<span id="KSCATEGORY_BDA_IP_SINK"></span><span id="kscategory_bda_ip_sink"></span>KSCATEGORY\_BDA\_IP\_SINK  
A BDA minidriver assigns this GUID to specify to create a BDA IP sink filter.

<span id="KSCATEGORY_BDA_NETWORK_PROVIDER"></span><span id="kscategory_bda_network_provider"></span>KSCATEGORY\_BDA\_NETWORK\_PROVIDER  
A BDA minidriver assigns this GUID to specify to create a BDA network provider filter.

<span id="KSCATEGORY_BDA_TRANSPORT_INFORMATION"></span><span id="kscategory_bda_transport_information"></span>KSCATEGORY\_BDA\_TRANSPORT\_INFORMATION  
A BDA minidriver assigns this GUID to specify to create a BDA transport information filter (TIF).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20BDA%20Filter%20Category%20GUIDs%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




