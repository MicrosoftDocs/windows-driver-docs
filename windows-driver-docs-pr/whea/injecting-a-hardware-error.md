---
title: Injecting a Hardware Error
author: windows-driver-content
description: Injecting a Hardware Error
MS-HAID:
- 'whea\_dbc7cc61-4f9c-4380-b394-997ad0d9e219.xml'
- 'whea.injecting\_a\_hardware\_error'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c27c79d9-c0b2-433b-b3f4-7674c361f1aa
keywords: ["injecting hardware errors WDK WHEA", "errors WDK WHEA , injecting, WHEA WDK , injecting", "Windows Hardware Error Architecture WDK , injecting"]
---

# Injecting a Hardware Error


A user-mode application can inject a hardware error into the hardware platform by calling the [**WHEAErrorInjectionMethods::InjectError**](https://msdn.microsoft.com/library/windows/hardware/ff559518) method. An application injects hardware errors into the hardware platform to test and validate the system's hardware error handling functionality.

The following code example shows how to inject a hardware error.

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Injecting%20a%20Hardware%20Error%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


