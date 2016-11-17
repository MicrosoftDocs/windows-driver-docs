---
title: Getting Error Injection Capabilities
author: windows-driver-content
description: Getting Error Injection Capabilities
MS-HAID:
- 'whea\_0ae41111-71db-403b-9b2f-254942b2cc72.xml'
- 'whea.getting\_error\_injection\_capabilities'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d4ff0d9c-bb17-4dff-8008-bf8d59e44621
keywords: ["error injection capabilities WDK WHEA", "retrieving error injection capabilities WDK WHEA", "errors WDK WHEA , error injection", "WHEA WDK , error injection", "Windows Hardware Error Architecture WDK , error injection", "injecting hardware errors WDK WHEA"]
---

# Getting Error Injection Capabilities


A user-mode application can get information about the error injection capabilities of the hardware platform by calling the [**WHEAErrorInjectionMethods::GetErrorInjectionCapabilitiesRtn**](https://msdn.microsoft.com/library/windows/hardware/ff559516) method. This method returns a [**WHEA\_ERROR\_INJECTION\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff560460) structure that describes the error injection capabilities that are supported by the hardware platform.

The following code example shows how to retrieve the error injection capabilities information.

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Getting%20Error%20Injection%20Capabilities%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


