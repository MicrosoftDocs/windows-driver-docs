---
title: Hyper-V Extensible Switch Forwarding Context Data Types
description: Hyper-V Extensible Switch Forwarding Context Data Types
ms.assetid: B5377411-C6F0-47BE-BD45-534AC784ED76
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hyper-V Extensible Switch Forwarding Context Data Types


The [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure for each packet that traverses the Hyper-V extensible switch data path contains out-of-band (OOB) data. This data specifies the source port from where the packet originated, as well as one or more destination ports for packet delivery. This OOB data is known as the *extensible switch forwarding context*.

The following data types have been declared to access the extensible switch forwarding context within a packet's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure:

<a href="" id="ndis-switch-forwarding-detail-net-buffer-list-info"></a>[**NDIS\_SWITCH\_FORWARDING\_DETAIL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh598211)  
This is a 64-bit union that contains the forwarding characteristics of a packet. This data includes the identifiers for the source port and network adapter connection from which the packet originated. This data also includes the number of unused elements that are available in the destination port array.

The extensible switch extension can access this data by using the [**NET\_BUFFER\_LIST\_SWITCH\_FORWARDING\_DETAIL**](https://msdn.microsoft.com/library/windows/hardware/hh598259) macro.

<a href="" id="ndis-switch-forwarding-destination-array"></a>[**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598211)  
This structure defines the destination port array for the packet. Each element in this array is formatted as an [**NDIS\_SWITCH\_PORT\_DESTINATION**](https://msdn.microsoft.com/library/windows/hardware/hh598224) structure.

The [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/hh598211) structure contains members that specify the current number of the total number of elements as well as the number of used elements in the array.

The extensible switch extension can obtain this array by calling the [*GetNetBufferListDestinations*](https://msdn.microsoft.com/library/windows/hardware/hh598157) function. If the driver adds or modifies elements in the array for a packet with multiple destination ports, it must call the [*UpdateNetBufferListDestinations*](https://msdn.microsoft.com/library/windows/hardware/hh598303) function. This function commits those changes to the destination port array in the packet's forwarding context.

**Note**  To commit changes to a packet with only one destination port, it is more efficient for the driver to call the [*AddNetBufferListDestination*](https://msdn.microsoft.com/library/windows/hardware/hh598133) function.

 

<a href="" id="ndis-switch-port-destination"></a>[**NDIS\_SWITCH\_PORT\_DESTINATION**](https://msdn.microsoft.com/library/windows/hardware/hh598224)  
This structure defines a destination port for the packet. For packets with a single destination port, there is only one [**NDIS\_SWITCH\_PORT\_DESTINATION**](https://msdn.microsoft.com/library/windows/hardware/hh598224) element in the destination port array. For packets with multiple destination ports, there are one or more of these elements in the array.

After the extensible switch extension has called [*GetNetBufferListDestinations*](https://msdn.microsoft.com/library/windows/hardware/hh598157) to obtain the packet's destination port array, it can access individual elements in the array by using the [**NDIS\_SWITCH\_PORT\_DESTINATION\_AT\_ARRAY\_INDEX**](https://msdn.microsoft.com/library/windows/hardware/hh598225) macro.

 

 





