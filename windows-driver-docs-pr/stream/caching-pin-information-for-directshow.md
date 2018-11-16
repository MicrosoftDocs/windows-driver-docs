---
title: Caching Pin Information for DirectShow
description: Caching Pin Information for DirectShow
ms.assetid: 1e6a973b-32d2-4ac2-9cd6-f4d3c329cecf
keywords:
- pin data cache WDK BDA
- cache WDK AVStream
- DirectShow pin data cache WDK AVStream
- updating pin data cache WDK AVStream
- Broadcast Driver Architecture WDK AVStream , pin data cache
- BDA WDK AVStream , pin data cache
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Caching Pin Information for DirectShow





An application can use the DirectShow **IFilterMapper2** interface to automatically search for filters that meet certain criteria. This application can use the list of proposed filters that **IFilterMapper2** returns to automatically build filter graphs with filters that receive and render television signals. To quickly find filters that meet the criteria specified, **IFilterMapper2** uses information about a filter and its pins that was previously entered into a cache. The discussion in the following paragraphs refers to this cache as the *pin data cache*.

The information contained in the pin data cache includes a list of mediums and media types for each pin that the filter can expose. **IFilterMapper2** uses this cache information to determine whether a possible filter can connect to a pin on a filter that is already in the graph. Making this determination eliminates the overhead of creating an instance of a filter only to determine that connecting to the filter is prevented because a medium or media type does not match. If the pin data cache for a filter is not up-to-date, a filter could be wrongly eliminated as a candidate for connection in a filter graph.

Whenever a BDA minidriver determines that its pin data cache that DirectShow uses is not up-to-date, that minidriver must update the pin data cache so that pin information for BDA filter instances of the minidriver's BDA component is accurately exposed in a filter graph. A BDA minidriver updates DirectShow's pin data cache as described in the following scenarios:

-   A BDA minidriver may or may not be required to update DirectShow's pin data cache when the minidriver initially creates BDA filter instances depending on how that minidriver presents BDA filters as DirectShow filters in user mode. A BDA minidriver's information (INF) file specifies the mechanism that the minidriver uses to present its BDA filters as DirectShow filters.

    BDA minidrivers typically use the [kernel-streaming (KS) proxy module](https://msdn.microsoft.com/library/windows/hardware/ff560877) (*Ksproxy.ax*) to present their BDA filters as DirectShow filters. KS proxy automatically updates DirectShow's pin data cache to expose pin information for BDA filters whenever instances of those filters are initially created. Therefore, BDA minidrivers that use KS proxy are not required to perform any action to update DirectShow's pin data cache when they initially create instances of filters. If a BDA filter is exposed to user mode through KS proxy, the cached information automatically includes the mediums and media types for the pin factories that exist on the filter instance immediately after the filter's create dispatch routine returns.

    Some BDA minidrivers do not use KS proxy to present their BDA filters as DirectShow filters. For example, BDA receiver minidrivers that implement BDA filters to receive or process analog television signals use either the *KSTVTune.ax* or *KSXBar.ax* modules to present these BDA filters as DirectShow filters. Because these modules do not use standard KS proxy interface methods to update DirectShow's pin data cache, BDA minidrivers for these types of BDA filters must update DirectShow's pin data cache when those minidrivers initially create instances of filters. To ensure that DirectShow's pin data cache is updated when instances of these filters are created, a BDA minidriver calls the [**BdaFilterFactoryUpdateCacheData**](https://msdn.microsoft.com/library/windows/hardware/ff556455) function immediately after calling the [**BdaInitFilter**](https://msdn.microsoft.com/library/windows/hardware/ff556464) function inside the implementation of the filter's create dispatch routine. In this call, the minidriver passes pin information to update all initial pins on the filter.

-   Pins can be created on a BDA filter dynamically after the filter's create dispatch routine completes. If the initially created instance of a BDA filter does not expose instances of all the pins that are listed in the BDA filter's template topology ([**BDA\_FILTER\_TEMPLATE**](https://msdn.microsoft.com/library/windows/hardware/ff556523)), then the BDA minidriver must call **BdaFilterFactoryUpdateCacheData** to force information about all pins listed in the filter's template topology.

**Note**   Updating DirectShow's pin data cache has significant overhead because it touches and modifies the registry. In addition, updating DirectShow's pin data cache impacts the amount of time required for DirectShow to automatically build filter graphs. Therefore, a BDA minidriver should call **BdaFilterFactoryUpdateCacheData** for all possible pins only when it determines that its pin data cache that DirectShow uses is not up-to-date.

 

If possible, a BDA minidriver should call **BdaFilterFactoryUpdateCacheData** whenever a driver, firmware, or hardware update has occurred.

 

 




