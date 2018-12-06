---
title: Getting Error Source Information for All Error Sources
description: Getting Error Source Information for All Error Sources
ms.assetid: 78e3a015-128d-44d1-b0ec-4da43c359090
keywords:
- error sources WDK WHEA , getting information
- errors WDK WHEA , error sources
- WHEA WDK , getting error source information
- Windows Hardware Error Architecture WDK , getting error source information
- hardware error sources WDK WHEA , getting informati
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Getting Error Source Information for All Error Sources


A user-mode application can get information about all of the [error sources](hardware-errors-and-error-sources.md) in the system by calling the [**WHEAErrorSourceMethods::GetAllErrorSourcesRtn**](https://msdn.microsoft.com/library/windows/hardware/ff559527) method. This method returns an array of [**WHEA\_ERROR\_SOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff560505) structures that describes all of the error sources that are supported by the hardware platform.

The following code example shows how to get the error source information for all of the error sources in the system.

```cpp
IWbemServices *pIWbemServices;
BSTR ClassName;
BSTR MethodName;
HRESULT Result;
IWbemClassObject *pOutParameters;
VARIANT Parameter;
ULONG Status;
ULONG Count;
ULONG Length;
SAFEARRAY *Array;
PWHEA_ERROR_SOURCE_DESCRIPTOR ErrorSourceList;

// The following example assumes that the application
// has previously connected to WMI on the local machine
// and that the pIWbemServices variable contains the
// pointer that was returned from the call to the
// IWbemLocator::ConnectServer method.

// Specify the class and method to execute
ClassName = SysAllocString(L"WHEAErrorSourceMethods");
MethodName = SysAllocString(L"GetAllErrorSourcesRtn");

// Call the GetAllErrorSourcesRtn method indirectly
// by calling the IWbemServices::ExecMethod method.
Result =
  pIWbemServices->ExecMethod(
    ClassName,
    MethodName,
    0,
    NULL,
    NULL,
    &pOutParameters,
    NULL
    );

// Get the status from the output parameters object
Result =
  pOutParameters->Get(
    L"Status",
    0,
    &Parameter,
    NULL,
    NULL
    );
Status = Parameter.ulval;
VariantClear(&Parameter);

// Get the count from the output parameters object
Result =
  pOutParameters->Get(
    L"Count",
    0,
    &Parameter,
    NULL,
    NULL
    );
Count = Parameter.ulval;
VariantClear(&Parameter);

// Get the length from the output parameters object
Result =
  pOutParameters->Get(
    L"Length",
    0,
    &Parameter,
    NULL,
    NULL
    );
Length = Parameter.ulval;
VariantClear(&Parameter);

// Get the data buffer from the output parameters object
Result =
  pOutParameters->Get(
    L"ErrorSourceArray",
    0,
    &Parameter,
    NULL,
    NULL
    );
Array = Parameter.parray;

// Get access to the data buffer
Result =
  SafeArrayAccessData(
    Array,
    &ErrorSourceList
    );

// Process the error source information.
...

// If the error source information is to be saved
// for later use, the data in the ErrorSourceList
// array must be copied to an application-allocated
// array of WHEA_ERROR_SOURCE_DESCRIPTOR structures
// before freeing up the resources.
...

// Free the array containing the error source information
SafeArrayUnaccessData(Array);
VariantClear(&Parameter);

// Free up resources
SysFreeString(ClassName);
SysFreeString(MethodName);
pOutParameters->Release();
```

 

 




