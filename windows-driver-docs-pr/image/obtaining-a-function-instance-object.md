---
title: Obtaining a Function Instance Object
description: Obtaining a Function Instance Object
ms.assetid: 2c750281-031b-4b9f-9012-3b341ebe1cd9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining a Function Instance Object


The WIA minidriver must identify the current hardware device and the service that it is running on. To identify these items, the minidriver obtains at run time the Function Instance object from the Function Discovery service and reads the device properties.

To use Function Discovery COM interfaces, the minidriver code must include the *FunctionDiscovery.h* main header file, which is available in the Windows Vista SDK, as the following example shows.

```cpp
//
// Web Services Function Discovery main header:
//
#include <FunctionDiscovery.h>
```

During initialization, as might happen in the [**IStiUSD::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff543824) method, the minidriver should query Function Discovery to obtain the appropriate Function Instance object that represents the hardware device. To complete this query, use the following procedure (and the associated code examples):

### Step 1: Create the Function Discovery object

```cpp
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

```cpp
IFunctionInstanceCollectionQuery *pfiCollectionQuery = NULL;
pFunctionDiscovery->CreateInstanceCollectionQuery(FCTN_CATEGORY_PNP,
   NULL,
   FALSE,
   NULL,
   NULL,
   &pfiCollectionQuery);
```

### <a href="" id="step-3--add-a-constraint-to-the-instance-collection-query-object-to-sp"></a>Step 3: Add a constraint to the Instance Collection Query object to specify the PNPX ID (its value is retrieved with IStiDeviceControl::GetMyDevicePortName) as the query constraint

```cpp
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

```cpp
IFunctionInstanceCollection *pfiCollection = NULL;
pfiCollectionQuery->Execute(&pfiCollection);
```

### Step 5: Retrieve the Function Instance object that is returned

```cpp
//
// Function Instance object that represents our device instance
//
IFunctionInstance *pFunctionInstance;

pfiCollection->Item(0, &m_pFunctionInstance);
```

For a code example that contains the declaration of a sample class (CWSDDevice), see [Code Sample for Obtaining a Function Instance Object](code-example-for-obtaining-a-function-instance-object.md).

 

 




