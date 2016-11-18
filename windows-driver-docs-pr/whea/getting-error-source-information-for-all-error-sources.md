---
title: Getting Error Source Information for All Error Sources
author: windows-driver-content
description: Getting Error Source Information for All Error Sources
MS-HAID:
- 'whea\_5b2f202a-27a8-4c09-9cab-498964260af2.xml'
- 'whea.getting\_error\_source\_information\_for\_all\_error\_sources'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 78e3a015-128d-44d1-b0ec-4da43c359090
keywords: ["error sources WDK WHEA , getting information", "errors WDK WHEA , error sources", "WHEA WDK , getting error source information", "Windows Hardware Error Architecture WDK , getting error source information", "hardware error sources WDK WHEA , getting informati"]
---

# Getting Error Source Information for All Error Sources


A user-mode application can get information about all of the [error sources](hardware-errors-and-error-sources.md) in the system by calling the [**WHEAErrorSourceMethods::GetAllErrorSourcesRtn**](https://msdn.microsoft.com/library/windows/hardware/ff559527) method. This method returns an array of [**WHEA\_ERROR\_SOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff560505) structures that describes all of the error sources that are supported by the hardware platform.

The following code example shows how to get the error source information for all of the error sources in the system.

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Getting%20Error%20Source%20Information%20for%20All%20Error%20Sources%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


