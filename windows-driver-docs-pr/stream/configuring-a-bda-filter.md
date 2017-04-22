---
title: Configuring a BDA Filter
author: windows-driver-content
description: Configuring a BDA Filter
ms.assetid: 4af9efc3-8073-4111-9ad0-8b2fba4d1545
keywords:
- method sets WDK BDA , filter configuration
- property sets WDK BDA , filter configuration
- KSMETHODSETID_BdaDeviceConfiguration
- filter configuration WDK BDA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Configuring a BDA Filter


## <a href="" id="ddk-configuring-a-bda-filter-ksg"></a>


A BDA minidriver processes method requests of the [KSMETHODSETID\_BdaDeviceConfiguration](https://msdn.microsoft.com/library/windows/hardware/ff563404) method set to configure a filter instance for the minidriver in the current filter graph.

In the following code snippet, two of the methods of the KSMETHODSETID\_BdaDeviceConfiguration method set are dispatched directly to the BDA support library and the remaining method is first intercepted by the BDA minidriver before dispatching to the BDA support library.

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Configuring%20a%20BDA%20Filter%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


