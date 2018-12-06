---
title: Getting Error Injection Capabilities
description: Getting Error Injection Capabilities
ms.assetid: d4ff0d9c-bb17-4dff-8008-bf8d59e44621
keywords:
- error injection capabilities WDK WHEA
- retrieving error injection capabilities WDK WHEA
- errors WDK WHEA , error injection
- WHEA WDK , error injection
- Windows Hardware Error Architecture WDK , error injection
- injecting hardware errors WDK WHEA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Getting Error Injection Capabilities


A user-mode application can get information about the error injection capabilities of the hardware platform by calling the [**WHEAErrorInjectionMethods::GetErrorInjectionCapabilitiesRtn**](https://msdn.microsoft.com/library/windows/hardware/ff559516) method. This method returns a [**WHEA\_ERROR\_INJECTION\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff560460) structure that describes the error injection capabilities that are supported by the hardware platform.

The following code example shows how to retrieve the error injection capabilities information.

```cpp
IWbemServices *pIWbemServices;
BSTR ClassName;
BSTR MethodName;
HRESULT Result;
IWbemClassObject *pOutParameters;
VARIANT Parameter;
ULONG Status;
WHEA_ERROR_INJECTION_CAPABILITIES ErrorInjectionCapabilities;

// The following example assumes that the application
// has previously connected to WMI on the local machine
// and that the pIWbemServices variable contains the
// pointer that was returned from the call to the
// IWbemLocator::ConnectServer method.

// Specify the class and method to execute
ClassName = SysAllocString(L"WHEAErrorInjectionMethods");
MethodName = SysAllocString(L"GetErrorInjectionCapabilitiesRtn");

// Call the GetErrorInjectionCapabilitiesRtn method indirectly
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
VariantClear(Parameter);

// Get the capabilities from the output parameters object
Result =
  pOutParameters->Get(
    L"Capabilities",
    0,
    &Parameter,
    NULL,
    NULL
    );
ErrorInjectionCapabilities.AsULONG = Parameter.ulval;
VariantClear(Parameter);

// Process the error injection capabilities data
...

// Free up resources
SysFreeString(ClassName);
SysFreeString(MethodName);
pOutParameters->Release();
```

 

 




