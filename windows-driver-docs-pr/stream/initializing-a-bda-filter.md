---
title: Initializing a BDA Filter
author: windows-driver-content
description: Initializing a BDA Filter
ms.assetid: 716978f5-4bdd-4673-8c4a-14dc76947fba
keywords: ["BDA minidrivers WDK AVStream , filter initialization", "initializing BDA filters", "initial filter instance WDK BDA"]
---

# Initializing a BDA Filter


## <a href="" id="ddk-initializing-a-bda-filter-ksg"></a>


A network provider filter uses the create dispatch routine of the BDA device's initial filter descriptor to create an initial filter instance of the BDA device when the network provider creates a filter graph. This initial filter descriptor was set as a filter factory and associated with the BDA filter template for the BDA device when the BDA device started. The initial filter instance that is created should expose at least one input. Typically, the initial filter instance exposes an input pin for each possible input pin in the initial filter descriptor but exposes no output pins. See [Starting a BDA Minidriver](starting-a-bda-minidriver.md) and [Creating Dispatch Tables](creating-dispatch-tables.md) for more information.

The BDA filter's create routine should allocate memory for its filter object, should set member variables for the filter object, and then should call the [**BdaInitFilter**](https://msdn.microsoft.com/library/windows/hardware/ff556464) support function to initialize the filter instance. In this call, the BDA filter's create routine passes a pointer to the [**KSFILTER**](https://msdn.microsoft.com/library/windows/hardware/ff562522) structure for the initial filter to create and a pointer to the [**BDA\_FILTER\_TEMPLATE**](https://msdn.microsoft.com/library/windows/hardware/ff556523) structure that describes possibilities for the filter's template topology for the initial filter instance.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Initializing%20a%20BDA%20Filter%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


