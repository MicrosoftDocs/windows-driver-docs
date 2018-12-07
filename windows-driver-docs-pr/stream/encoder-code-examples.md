---
title: Encoder Code Examples
description: Encoder Code Examples
ms.assetid: cbe773ad-2222-4d62-8e1e-6d47418a3e7c
keywords:
- variable bit rates WDK encoder
- encoder devices WDK AVStream
- AVStream WDK , encoder devices
- uncompressed data streams WDK AVStream
- encoded streams WDK AVStream
- audio encoder devices WDK AVStream
- video encoder devices WDK AVStream
- ENCAPIPARAM_BITRATE_MODE
- ENCAPIPARAM_BITRATE
- bit rates WDK encoder
- registry WDK encoder
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Encoder Code Examples


The following code examples are based on the [AVStream Simulated Hardware Sample Driver (AVSHwS)](http://go.microsoft.com/fwlink/p/?linkid=256083). They demonstrate the following:

-   How to specify the encoder's supported bit rates

-   How to specify the bit rate encoding modes supported by an encoder

-   How to specify metadata values at run time under the encoder device's *Device Parameters\\Capabilities* registry key

### **Implementing Supported Bit Rates**

The following code snippets demonstrate how to implement support for the [ENCAPIPARAM\_BITRATE](https://msdn.microsoft.com/library/windows/hardware/ff559520) property. Use a [**KSPROPERTY\_STEPPING\_LONG**](https://msdn.microsoft.com/library/windows/hardware/ff565631) structure to specify a stepping granularity of 400 bits per second (bps) with a 400-bps lower-bound and 4,000,000-bps upper-bound.

```cpp
const KSPROPERTY_STEPPING_LONG BitRateRanges [] = {
    {
        400,
        0,
        400,
        4000000
    }
};
```

If you access the encoder filter's property page by right-clicking on the filter in a tool such as GraphEdit, you will see the **Bit Rate** slider bar where these values are used.

Next, specify the default encoding bit rate of the encoder filter when an instance of it is created. Note that the data type used is a ULONG that corresponds to the property value type required by the ENCAPIPARAM\_BITRATE property. This value is the default encoding "Bit Rate" that is displayed in the encoder's property page:

```cpp
const ULONG BitRateValues [] = {
    1000000
};
```

Specify the list of legal ranges and a default value for the ENCAPIPARAM\_BITRATE property:

```cpp
 const KSPROPERTY_MEMBERSLIST BitRateMembersList [] = {
    {
        {
            KSPROPERTY_MEMBER_STEPPEDRANGES,
            sizeof (BitRateRanges),
            SIZEOF_ARRAY (BitRateRanges),
            0
        },
        BitRateRanges
    },
    {
        {
            KSPROPERTY_MEMBER_VALUES,
            sizeof (BitRateValues),
            SIZEOF_ARRAY (BitRateValues),
            KSPROPERTY_MEMBER_FLAG_DEFAULT
        },
        BitRateValues
    }
};
```

```cpp
 const KSPROPERTY_VALUES BitRateValuesSet = {
    {
        STATICGUIDOF (KSPROPTYPESETID_General),
        VT_UI4,
        0
    },
    SIZEOF_ARRAY (BitRateMembersList),
    BitRateMembersList
};
```

Specify the single property defined for the ENCAPIPARAM\_BITRATE property set:

```cpp
DEFINE_KSPROPERTY_TABLE(ENCAPI_BitRate) {
    DEFINE_KSPROPERTY_ITEM (
        0,
        GetBitRateHandler, //Get-property handler supported
        sizeof (KSPROPERTY),
        sizeof (ULONG),
        SetBitRateHandler, //Set-property handler supported
        &BitRateValuesSet,
        0,
        NULL,
        NULL,
        sizeof (ULONG)
        )
};
```

**Note**   The *get*-property handler returns the encoding bit rate, and the *Set*-property handler must test that the incoming passed-in value is valid before using it.

 

### **Implementing Supported Encoding Bit Rate Modes**

The following code snippets demonstrate how to implement support for the [ENCAPIPARAM\_BITRATE\_MODE](https://msdn.microsoft.com/library/windows/hardware/ff559524) property.

Define the encoding modes supported by the encoder:

```cpp
 const VIDEOENCODER_BITRATE_MODE BitRateModeValues [] = {
    ConstantBitRate,
    VariableBitRateAverage
};
```

Specify the default encoding bit rate mode as average variable bit rate:

```cpp
const VIDEOENCODER_BITRATE_MODE BitRateModeDefaultValues [] = {
    VariableBitRateAverage
};
```

Specify the list of legal ranges and default value for the ENCAPIPARAM\_BITRATE\_MODE property:

```cpp
const KSPROPERTY_MEMBERSLIST BitRateModeMembersList [] = {
    {
        {
            KSPROPERTY_MEMBER_VALUES,
            sizeof (BitRateModeValues),
            SIZEOF_ARRAY (BitRateModeValues),
            0
        },
        BitRateModeValues
    },
    {
        {
            KSPROPERTY_MEMBER_VALUES,
            sizeof (BitRateModeDefaultValues),
            SIZEOF_ARRAY (BitRateModeDefaultValues),
            KSPROPERTY_MEMBER_FLAG_DEFAULT
        },
        BitRateModeDefaultValues
    }
};

const KSPROPERTY_VALUES BitRateModeValuesSet = {
    {
        STATICGUIDOF (KSPROPTYPESETID_General),
        VT_I4,
        0
    },
    SIZEOF_ARRAY (BitRateModeMembersList),
    BitRateModeMembersList
};
```

Specify the single property defined for the ENCAPIPARAM\_BITRATE\_MODE property set:

```cpp
DEFINE_KSPROPERTY_TABLE(ENCAPI_BitRateMode) {
    DEFINE_KSPROPERTY_ITEM (
        0,
        GetBitRateModeHandler, //Get-property handler supported
        sizeof (KSPROPERTY),
        sizeof (VIDEOENCODER_BITRATE_MODE),
        SetBitRateModeHandler, //Set-property handler supported
        &BitRateModeValuesSet,
        0,
        NULL,
        NULL,
        sizeof (VIDEOENCODER_BITRATE_MODE)
        )
};
```

**Note**   The *get*-property handler should return the encoding bit rate mode, and the *Set*-property handler must test that the incoming passed-in value is valid before using it.

 

The property sets are then specified as the [**KSFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562553) structure's automation table.

```cpp
DEFINE_KSPROPERTY_SET_TABLE(PropertyTable) {
    DEFINE_KSPROPERTY_SET(
        &ENCAPIPARAM_BITRATE_MODE,
        SIZEOF_ARRAY (ENCAPI_BitRateMode),
        ENCAPI_BitRateMode,
        0,
        NULL
        ),
    DEFINE_KSPROPERTY_SET(
        &ENCAPIPARAM_BITRATE,
        SIZEOF_ARRAY (ENCAPI_BitRate),
        ENCAPI_BitRate,
        0,
        NULL
        )
};

DEFINE_KSAUTOMATION_TABLE(FilterTestTable) {
    DEFINE_KSAUTOMATION_PROPERTIES(PropertyTable),
    DEFINE_KSAUTOMATION_METHODS_NULL,
    DEFINE_KSAUTOMATION_EVENTS_NULL
};

const 
KSFILTER_DESCRIPTOR 
FilterDescriptor = {
    ...,
    &FilterTestTable, // Automation Table
    ...,
    ...
};
```

### <a href="" id="specifying-the-encoder-s-capabilities-in-the-registry"></a>**Specifying the Encoder's Capabilities in the Registry**

The following code sample demonstrates how to create a *Capabilities* registry key under the *Device Parameters* registry key, and how to create and specify sub keys and values under the *Capabilities* key. Execute this code when the driver initializes.

**Note:** The following code assumes the presence of a single hardware encoder per physical device. If your hardware contains more than one encoder then you must iterate through the list returned in the call to the **IoGetDeviceInterfaces** function and register the capabilities for each encoder.

```cpp
/**************************************************************************
CreateDwordValueInCapabilityRegistry()

IN Pdo: PhysicalDeviceObject
IN categoryGUID: Category GUID eg KSCATEGORY_CAPTURE

1. Get Symbolic name for interface
2. Open registry key for storing information about a 
   particular device interface instance
3. Create Capabilities key under "Device Parameters" key
4. Create a DWORD value "TestCapValueDWORD" under Capabilities

Must be running at IRQL = PASSIVE_LEVEL in the context of a system thread
**************************************************************************/
NTSTATUS CreateDwordValueInCapabilityRegistry(IN PDEVICE_OBJECT pdo, IN GUID categoryGUID)

{

    // 1. Get Symbolic name for interface
    // pSymbolicNameList can contain multiple strings if pdo is NULL. 
    // Driver should parse this list of string to get 
    // the one corresponding to current device interface instance. 
    PWSTR  pSymbolicNameList = NULL;

    NTSTATUS ntStatus = IoGetDeviceInterfaces(
        &categoryGUID,
        pdo,
        DEVICE_INTERFACE_INCLUDE_NONACTIVE,
        &pSymbolicNameList);
    if (NT_SUCCESS(ntStatus) && (NULL != pSymbolicNameList))
    {
        HANDLE hDeviceParametersKey = NULL;
        UNICODE_STRING symbolicName;

        // 2. Open registry key for storing information about a 
        // particular device interface instance
        RtlInitUnicodeString(&symbolicName, pSymbolicNameList);
        ntStatus = IoOpenDeviceInterfaceRegistryKey(
            &symbolicName,
            KEY_READ|KEY_WRITE,
            &hDeviceParametersKey);
        if (NT_SUCCESS(ntStatus))
        {
            OBJECT_ATTRIBUTES objAttribSubKey;
            UNICODE_STRING subKey;
 
            // 3. Create Capabilities key under "Device Parameters" key
            RtlInitUnicodeString(&subKey,L"Capabilities");
            InitializeObjectAttributes(&objAttribSubKey,
                &subKey,
                OBJ_KERNEL_HANDLE,
                hDeviceParametersKey,
                NULL);
 
            HANDLE hCapabilityKeyHandle = NULL;
 
            ntStatus = ZwCreateKey(&hCapabilityKeyHandle,
                    KEY_READ|KEY_WRITE|KEY_SET_VALUE,
                    &objAttribSubKey,
                    0,
                    NULL,
                    REG_OPTION_NON_VOLATILE,
                    NULL);
            if (NT_SUCCESS(ntStatus))
            {
                OBJECT_ATTRIBUTES objAttribDwordKeyVal;
                UNICODE_STRING subValDword;
 
                // 4. Create a DWORD value "TestCapValueDWORD" under Capabilities 
                RtlInitUnicodeString(&subValDword,L"TestCapValueDWORD");
 
                ULONG data = 0xaaaaaaaa;
 
                ntStatus = ZwSetValueKey(hCapabilityKeyHandle,&subValDword,0,REG_DWORD,&data,sizeof(ULONG));
                ZwClose(hCapabilityKeyHandle);
            }
        }
        ZwClose(hDeviceParametersKey);
        ExFreePool(pSymbolicNameList);
    }
 
    return ntStatus;
}
```

 

 




