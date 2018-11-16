---
title: Injecting a Hardware Error
description: Injecting a Hardware Error
ms.assetid: c27c79d9-c0b2-433b-b3f4-7674c361f1aa
keywords:
- injecting hardware errors WDK WHEA
- errors WDK WHEA , injecting, WHEA WDK , injecting
- Windows Hardware Error Architecture WDK , injecting
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Injecting a Hardware Error


A user-mode application can inject a hardware error into the hardware platform by calling the [**WHEAErrorInjectionMethods::InjectError**](https://msdn.microsoft.com/library/windows/hardware/ff559518) method. An application injects hardware errors into the hardware platform to test and validate the system's hardware error handling functionality.

The following code example shows how to inject a hardware error.

```cpp
IWbemServices *pIWbemServices;
ULONG ErrorType;
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

// The following also assumes that ErrorType has
// previously been initialized with the type of error
// to be injected into the hardware platform.

// Specify the class and method to execute
ClassName = SysAllocString(L"WHEAErrorInjectionMethods");
MethodName = SysAllocString(L"InjectErrorRtn");

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

// Set the ErrorType parameter
Parameter.vt = VT_UI4;
Parameter.ulVal = ErrorType;
Result =
  pInParameters->Put(
    L"ErrorType",
    0,
    &Parameter,
    0
    );
VariantClear(&Parameter);

// Set the additional parameters - in this case
// they are all set to zero. If additional data
// is required by the PSHED plug-in to perform
// the error injection operation, these parameters
// should be set with the necessary data.
Parameter.vt = VT_UI8;
Parameter.ullVal = (ULONGLONG)0;
Result =
  pInParameters->Put(
    L"Parameter1",
    0,
    &Parameter,
    0
    );
Result =
  pInParameters->Put(
    L"Parameter2",
    0,
    &Parameter,
    0
    );
Result =
  pInParameters->Put(
    L"Parameter3",
    0,
    &Parameter,
    0
    );
Result =
  pInParameters->Put(
    L"Parameter4",
    0,
    &Parameter,
    0
    );
VariantClear(&Parameter);

// Call the InjectErrorRtn method indirectly by
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

// For injected errors that are fatal or otherwise
// unrecoverable, the call to the InjectErrorRtn method
// might not return before the Windows kernel generates
// a bug check in response to the error condition.

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
VariantClear(Parameter);

// Free up resources
SysFreeString(ClassName);
SysFreeString(MethodName);
pInParameters->Release();
pInParametersClass->Release();
pClass->Release();
pOutParameters->Release();
```

 

 




