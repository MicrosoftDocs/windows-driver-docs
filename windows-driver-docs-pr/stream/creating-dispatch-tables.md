---
title: Creating Dispatch Tables
author: windows-driver-content
description: Creating Dispatch Tables
ms.assetid: 0771aeac-68b2-4dec-8887-a0b313899ce8
keywords: ["BDA minidrivers WDK AVStream , dispatch tables", "dispatch tables WDK AVStream", "filter dispatch tables WDK BDA", "pin dispatch tables WDK BDA"]
---

# Creating Dispatch Tables


## <a href="" id="ddk-creating-dispatch-tables-ksg"></a>


You must create a filter dispatch table for a filter descriptor ([**KSFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562553)) of a BDA minidriver so that the network provider filter can open and initialize an instance of the filter and later release the filter instance. You must also create a pin dispatch table for each pin descriptor ([**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534)) in the array of pin types that are available in the filter's template topology. The network provider filter uses a pin dispatch table to open and initialize a pin and later release the pin. The following code snippet shows examples of filter and pin dispatch tables:

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Creating%20Dispatch%20Tables%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


