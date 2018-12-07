---
title: Disabling an Error Source
description: Disabling an Error Source
ms.assetid: a481ac98-0ff1-4583-a81a-1d2e4f968111
keywords:
- error sources WDK WHEA , disabling
- Windows Hardware Error Architecture WDK , disabling error sources
- WHEA WDK , disabling error sources
- errors WDK WHEA , disabling error sources
- hardware error sources WDK WHEA , disabling
- disabling an error sourc
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Disabling an Error Source


A user-mode application can disable an [error source](hardware-errors-and-error-sources.md) by calling the [**WHEAErrorSourceMethods::DisableErrorSourceRtn**](https://msdn.microsoft.com/library/windows/hardware/ff559523) method.

The following code example shows how to disable an error source.

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
// identifier of the error source to be disabled.

// Specify the class and method to execute
ClassName = SysAllocString(L"WHEAErrorSourceMethods");
MethodName = SysAllocString(L"DisableErrorSourceRtn");

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

// Call the DisableErrorSourceRtn method indirectly by
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

A user-mode application can re-enable an [error source](hardware-errors-and-error-sources.md) by calling the [**WHEAErrorSourceMethods::EnableErrorSourceRtn**](https://msdn.microsoft.com/library/windows/hardware/ff559525) method. For more information about how to enable an error source, see [Enabling an Error Source](enabling-an-error-source.md).

 

 




