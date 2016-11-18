---
title: Obtaining a Function Instance Object
author: windows-driver-content
description: Obtaining a Function Instance Object
MS-HAID:
- 'WIA\_wsd\_scan\_9446ed50-f28b-42a2-8245-8f426ac04999.xml'
- 'image.obtaining\_a\_function\_instance\_object'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2c750281-031b-4b9f-9012-3b341ebe1cd9
---

# Obtaining a Function Instance Object


The WIA minidriver must identify the current hardware device and the service that it is running on. To identify these items, the minidriver obtains at run time the Function Instance object from the Function Discovery service and reads the device properties.

To use Function Discovery COM interfaces, the minidriver code must include the *FunctionDiscovery.h* main header file, which is available in the Windows Vista SDK, as the following example shows.

```
//
// Web Services Function Discovery main header:
//
#include <FunctionDiscovery.h>
```

During initialization, as might happen in the [**IStiUSD::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff543824) method, the minidriver should query Function Discovery to obtain the appropriate Function Instance object that represents the hardware device. To complete this query, use the following procedure (and the associated code examples):

### Step 1: Create the Function Discovery object

```
//
// Function Discovery object
//
IFunctionDiscovery *pFunctionDiscovery = NULL;
CoCreateInstance(__uuidof(FunctionDiscovery),
                 NULL,
                 CLSCTX_INPROC_SERVER,
                 __uuidof(IFunctionDiscovery),
  (void**)&pFunctionDiscovery);
```

### Step 2: Create an Instance Collection Query object

```
IFunctionInstanceCollectionQuery *pfiCollectionQuery = NULL;
pFunctionDiscovery->CreateInstanceCollectionQuery(FCTN_CATEGORY_PNP,
   NULL,
   FALSE,
   NULL,
   NULL,
   &pfiCollectionQuery);
```

### <a href="" id="step-3--add-a-constraint-to-the-instance-collection-query-object-to-sp"></a>Step 3: Add a constraint to the Instance Collection Query object to specify the PNPX ID (its value is retrieved with IStiDeviceControl::GetMyDevicePortName) as the query constraint

```
PROPVARIANT PropVar = {0};
//
// Note that the wszDevicePath value is obtained by the WIA minidriver 
// calling IStiDeviceControl::GetMyDevicePortName during IStiUSD::Initialize
//
PropVariantInit(&PropVar);
PropVar.vt = VT_LPWSTR;
PropVar.pwszVal = (LPWSTR)wszDevicePath; 
pfiCollectionQuery->AddPropertyConstraint(PKEY_PNPX_ID, &PropVar, QC_EQUALS);
```

### Step 4: Execute the query

```
IFunctionInstanceCollection *pfiCollection = NULL;
pfiCollectionQuery->Execute(&pfiCollection);
```

### Step 5: Retrieve the Function Instance object that is returned

```
//
// Function Instance object that represents our device instance
//
IFunctionInstance *pFunctionInstance;

pfiCollection->Item(0, &m_pFunctionInstance);
```

For a code example that contains the declaration of a sample class (CWSDDevice), see [Code Sample for Obtaining a Function Instance Object](code-example-for-obtaining-a-function-instance-object.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Obtaining%20a%20Function%20Instance%20Object%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


