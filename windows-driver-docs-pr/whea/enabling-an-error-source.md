---
title: Enabling an Error Source
description: Enabling an Error Source
ms.assetid: a65357fa-e600-47fe-8719-b67c36542711
keywords:
- error sources WDK WHEA , enabling
- Windows Hardware Error Architecture WDK , enabling error sources
- WHEA WDK , enabling error sources
- errors WDK WHEA , enabling error sources
- hardware error sources WDK WHEA , enabling
- enabling an error source WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enabling an Error Source


A user-mode application can enable an [error source](hardware-errors-and-error-sources.md) by calling the [**WHEAErrorSourceMethods::EnableErrorSourceRtn**](https://msdn.microsoft.com/library/windows/hardware/ff559525) method.

The following code example shows how to enable an error source.

```cpp
IWbemServices *pIWbemServices;
ULONG ErrorSourceID;
BSTR ClassName;
BSTR MethodName;
HRESULT Result;
IWbemClassObject *pClass;
IWbemClassObject *pInParametersClass;
IWbemClassObject *pInParameters;
IWbemClassObject *pOutParameters;
VARIANT Parameter;
ULONG Status;

// The following example assumes that the application
// has previously connected to WMI on the local machine
// and that the pIWbemServices variable contains the
// pointer that was returned from the call to the
// IWbemLocator::ConnectServer method.

// The following also assumes that the ErrorSourceID
// variable has previously been initialized with the
// identifier of the error source to be enabled.

// Specify the class and method to execute
ClassName = SysAllocString(L"WHEAErrorSourceMethods");
MethodName = SysAllocString(L"EnableErrorSourceRtn");

// Get the class object for the method definition
Result =
  pIWbemServices->GetObject(
    ClassName,
    0,
    NULL,
    &pClass,
    NULL
    );

// Get the input parameter class object for the method
Result =
  pClass->GetMethod(
    MethodName,
    0,
    &pInParametersClass,
    NULL
    );

// Create an instance of the input parameter class
Result =
  pInParametersClass->SpawnInstance(
    0,
    &pInParameters
    );

// Set the ErrorSourceId parameter
Parameter.vt = VT_UI4;
Parameter.ulVal = ErrorSourceId;
Result =
  pInParameters->Put(
    L"ErrorSourceId",
    0,
    &Parameter,
    0
    );
VariantClear(&Parameter);

// Call the EnableErrorSourceRtn method indirectly by
// calling the IWbemServices::ExecMethod method.
Result =
  pIWbemServices->ExecMethod(
    ClassName,
    MethodName,
    0,
    NULL,
    &pInParameters,
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

// Free up resources
SysFreeString(ClassName);
SysFreeString(MethodName);
pInParameters->Release();
pInParametersClass->Release();
pClass->Release();
pOutParameters->Release();
```

A user-mode application can disable an [error source](hardware-errors-and-error-sources.md) by calling the [**WHEAErrorSourceMethods::DisableErrorSourceRtn**](https://msdn.microsoft.com/library/windows/hardware/ff559523) method. For more information about disabling an error source, see [Disabling an Error Source](disabling-an-error-source.md).

 

 




