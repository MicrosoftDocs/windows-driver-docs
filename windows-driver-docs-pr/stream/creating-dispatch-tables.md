---
title: Creating Dispatch Tables
description: Creating Dispatch Tables
ms.assetid: 0771aeac-68b2-4dec-8887-a0b313899ce8
keywords:
- BDA minidrivers WDK AVStream , dispatch tables
- dispatch tables WDK AVStream
- filter dispatch tables WDK BDA
- pin dispatch tables WDK BDA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Dispatch Tables





You must create a filter dispatch table for a filter descriptor ([**KSFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562553)) of a BDA minidriver so that the network provider filter can open and initialize an instance of the filter and later release the filter instance. You must also create a pin dispatch table for each pin descriptor ([**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534)) in the array of pin types that are available in the filter's template topology. The network provider filter uses a pin dispatch table to open and initialize a pin and later release the pin. The following code snippet shows examples of filter and pin dispatch tables:

```cpp
//
//  Filter Dispatch Table
//
//  Lists the dispatch routines for major events at the filter
//  level.
//
const
KSFILTER_DISPATCH
FilterDispatch =
{
    CFilter::Create,        // Create
    CFilter::FilterClose,   // Close
    NULL,                   // Process
    NULL                    // Reset
};

//
//  Input Pin Dispatch Table
//  Lists the dispatch routines for major events at the pin level.
//
const
KSPIN_DISPATCH
AntennaPinDispatch =
{
    CAntennaPin::PinCreate,         // Create
    CAntennaPin::PinClose,          // Close
    NULL,                           // Process signal data
    NULL,                           // Reset
    NULL,                           // SetDataFormat
    CAntennaPin::PinSetDeviceState, // SetDeviceState
    NULL,                           // Connect
    NULL,                           // Disconnect
    NULL,                           // Clock
    NULL                            // Allocator
};
```

 

 




