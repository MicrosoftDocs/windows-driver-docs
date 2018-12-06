---
title: BDA Filter Category GUIDs
description: BDA Filter Category GUIDs
ms.assetid: fbd4bf91-8309-423a-97ea-7e4f90cd3b68
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





