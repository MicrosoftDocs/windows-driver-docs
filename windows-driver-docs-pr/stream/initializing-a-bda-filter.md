---
title: Initializing a BDA Filter
description: Initializing a BDA Filter
ms.assetid: 716978f5-4bdd-4673-8c4a-14dc76947fba
keywords:
- BDA minidrivers WDK AVStream , filter initialization
- initializing BDA filters
- initial filter instance WDK BDA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing a BDA Filter





A network provider filter uses the create dispatch routine of the BDA device's initial filter descriptor to create an initial filter instance of the BDA device when the network provider creates a filter graph. This initial filter descriptor was set as a filter factory and associated with the BDA filter template for the BDA device when the BDA device started. The initial filter instance that is created should expose at least one input. Typically, the initial filter instance exposes an input pin for each possible input pin in the initial filter descriptor but exposes no output pins. See [Starting a BDA Minidriver](starting-a-bda-minidriver.md) and [Creating Dispatch Tables](creating-dispatch-tables.md) for more information.

The BDA filter's create routine should allocate memory for its filter object, should set member variables for the filter object, and then should call the [**BdaInitFilter**](https://msdn.microsoft.com/library/windows/hardware/ff556464) support function to initialize the filter instance. In this call, the BDA filter's create routine passes a pointer to the [**KSFILTER**](https://msdn.microsoft.com/library/windows/hardware/ff562522) structure for the initial filter to create and a pointer to the [**BDA\_FILTER\_TEMPLATE**](https://msdn.microsoft.com/library/windows/hardware/ff556523) structure that describes possibilities for the filter's template topology for the initial filter instance.

 

 




