---
title: SMP Example MOFs (Windows Drivers)
description: Learn more about SMP Example MOFs.
ms.date: 10/14/2022
---

# SMP Example MOFs

A master MOF: sample\_master.mof

```mof
    // BEGIN OF FILE
    
    // Required MOFs
    #pragma include("msft_qualifiers.mof")
    #pragma include("storagewmi_provider.mof")
    
    // Your SMP MOFs
    #pragma include("sample_storageprovider.mof")
    // #pragma include("sample_storagesubsystem.mof")
    // other supported classes…
    
    // END OF FILE
```

Individual class MOF: sample\_storageprovider.mof

```mof
    // BEGIN OF FILE
    
    class SAMPLE_StorageProvider : MSFT_StorageProvider
    {
        // No need to copy base class properties.
    
        // If you support Discover, copy it over.
        // Keep all qualifiers.
        // Qualifier strings are omitted below.
        [Required, Description(…),
                ValueMap {…},
                Values {…}]
        UInt32 Discover(
            [In, Required, Description(…),
                ValueMap {…},
                Values {…}]
            UInt16 DiscoveryLevel,
        
            [In, Description(…)]
            MSFT_StorageObject REF RootObject,
    
            [Out, Description(…)]
            MSFT_StorageJob REF CreatedStorageJob,
    
            [Out, Description(…),
                  EmbeddedInstance("MSFT_StorageExtendedStatus")]
            String ExtendedStatus
        );
    
        // other supported methods…
    };
    
    // END OF FILE
```
