---
title: Configuring a BDA Filter
description: Configuring a BDA Filter
ms.assetid: 4af9efc3-8073-4111-9ad0-8b2fba4d1545
keywords:
- method sets WDK BDA , filter configuration
- property sets WDK BDA , filter configuration
- KSMETHODSETID_BdaDeviceConfiguration
- filter configuration WDK BDA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuring a BDA Filter





A BDA minidriver processes method requests of the [KSMETHODSETID\_BdaDeviceConfiguration](https://msdn.microsoft.com/library/windows/hardware/ff563404) method set to configure a filter instance for the minidriver in the current filter graph.

In the following code snippet, two of the methods of the KSMETHODSETID\_BdaDeviceConfiguration method set are dispatched directly to the BDA support library and the remaining method is first intercepted by the BDA minidriver before dispatching to the BDA support library.

```cpp
//
//  BDA Device Configuration Method Set
//
//  Defines the dispatch routines for the filter level
//  topology configuration methods
//
DEFINE_KSMETHOD_TABLE(BdaDeviceConfigurationMethods)
{
    DEFINE_KSMETHOD_ITEM_BDA_CREATE_PIN_FACTORY(
        BdaMethodCreatePin,
        NULL
        ),
    DEFINE_KSMETHOD_ITEM_BDA_DELETE_PIN_FACTORY(
        BdaMethodDeletePin,
        NULL
        ),
    DEFINE_KSMETHOD_ITEM_BDA_CREATE_TOPOLOGY(
        CFilter::CreateTopology,
        NULL
        )
};
/*
** CreateTopology()
**
** Keeps track of topology association between input and output pins
**
*/
NTSTATUS
CFilter::
CreateTopology(
    IN PIRP         pIrp,
    IN PKSMETHOD    pKSMethod,
    PVOID           pvIgnored
    )
{
    NTSTATUS            Status = STATUS_SUCCESS;
    CFilter *           pFilter;
    ULONG               ulPinType;
    PKSFILTER           pKSFilter;

    ASSERT( pIrp);
    ASSERT( pKSMethod);

    //  Obtain a "this" pointer for the method.
    //
    //  Because this function is called directly from the property 
    //  dispatch table, get pointer to the underlying object.
    //
    pFilter = FilterFromIRP( pIrp);
    ASSERT( pFilter);
    if (!pFilter)
    {
        Status = STATUS_INVALID_PARAMETER;
        goto errExit;
    }

    //  Let the BDA support library create the standard topology.
    //  It will also validate the method, instance count, etc.
    //
    Status = BdaMethodCreateTopology( pIrp, pKSMethod, pvIgnored);
    if (Status != STATUS_SUCCESS)
    {
        goto errExit;
    }

    //  This is where the filter can keep track of associated pins.
    //
errExit:
    return Status;
}
```

The KSMETHOD\_BDA\_CREATE\_TOPOLOGY method request calls the minidriver's CFilter::CreateTopology method. This method calls the BDA support library function [**BdaMethodCreateTopology**](https://msdn.microsoft.com/library/windows/hardware/ff556471) to create a topology between filter pins. This function actually creates a topology structure in Ring 3, which reflects, for other property sets, the known connections of the filter. A BDA minidriver should intercept the KSMETHOD\_BDA\_CREATE\_TOPOLOGY method request as shown in the preceding code snippet if that minidriver must send special instructions to the hardware when connecting particular pin types--for example, if the BDA device performs hardware demultiplexing and creates an arbitrary number of output pins fanned off from a single input pin.

 

 




