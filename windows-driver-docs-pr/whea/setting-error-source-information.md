---
title: Setting Error Source Information
author: windows-driver-content
description: Setting Error Source Information
MS-HAID:
- 'whea\_db940098-6984-4efe-92ef-89b7c60c048c.xml'
- 'whea.setting\_error\_source\_information'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 87c61c3e-768a-4784-b9ec-1ec85d65ea81
keywords: ["error sources WDK WHEA , setting information", "errors WDK WHEA , error sources", "WHEA WDK , setting error source information", "Windows Hardware Error Architecture WDK , setting error source information", "hardware error sources WDK WHEA , setting information"]
---

# Setting Error Source Information


A user-mode application can set the information for a particular [error source](hardware-errors-and-error-sources.md) that is supported by the hardware platform by calling the [**WHEAErrorSourceMethods::SetErrorSourceInfoRtn**](https://msdn.microsoft.com/library/windows/hardware/ff559531) method. In this situation, the application provides a [**WHEA\_ERROR\_SOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff560505) structure that describes the information to be set for the specified error source.

The following code example shows how to set the error source information for a particular error source.

```
IWbemServices *pIWbemServices;
WHEA_ERROR_SOURCE_DESCRIPTOR ErrorSourceInfo;
BSTR ClassName;
BSTR MethodName;
HRESULT Result;
IWbemClassObject *pClass;
IWbemClassObject *pInParametersClass;
IWbemClassObject *pInParameters;
IWbemClassObject *pOutParameters;
VARIANT Parameter;
SAFEARRAY *Array;
PVOID ArrayData;
ULONG Status;

// The following example assumes that the application
// has previously connected to WMI on the local machine
// and that the pIWbemServices variable contains the
// pointer that was returned from the call to the
// IWbemLocator::ConnectServer method.

// The following also assumes that the ErrorSourceInfo
// contains the error source information to be set.

// Note that the SetErrorSourceInfoRtn method determines
// the identifier of the error source for which the
// information is being set from the ErrorSourceId
// member of the WHEA_ERROR_SOURCE_DESCRIPTOR structure.

// Specify the class and method to execute
ClassName = SysAllocString(L"WHEAErrorSourceMethods");
MethodName = SysAllocString(L"SetErrorSourceInfoRtn");

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

// Create a safe array for the error source information
Array =
  SafeArrayCreateVector(
    VT_UI1,
    0,
    sizeof(WHEA_ERROR_SOURCE_DESCRIPTOR)
    );

// Get access to the data buffer
Result =
  SafeArrayAccessData(
    Array,
    &ArrayData
    );

// Copy the error source information
*(PWHEA_ERROR_SOURCE_DESCRIPTOR)ArrayData =
  ErrorSourceInfo;

// Release access to the data buffer
SafeArrayUnaccessData(Array);

// Set the ErrorSourceInfo parameter
Parameter.vt = VT_ARRAY | VT_UI1;
Parameter.parray = Array;
Result =
  pInParameters->Put(
    L"ErrorSourceInfo",
    0,
    &Parameter,
    0
    );
VariantClear(&Parameter);

// Set the Length parameter
Parameter.vt = VT_UI4;
Parameter.ulVal = sizeof(WHEA_ERROR_SOURCE_DESCRIPTOR);
Result =
  pInParameters->Put(
    L"Length",
    0,
    &Parameter,
    0
    );
VariantClear(&Parameter);

// Call the SetErrorSourceInfoRtn method indirectly
// by calling the IWbemServices::ExecMethod method.
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

An application typically sets the information for an error source when it modifies the error source's configuration. An application can modify the configuration of an error source by performing the following steps:

1.  Retrieve the WHEA\_ERROR\_SOURCE\_DESCRIPTOR structure that describes the particular error source.

    For more information about getting information about all of the [error sources](hardware-errors-and-error-sources.md) in the system, see [Getting Error Source Information for All Error Sources](getting-error-source-information-for-all-error-sources.md).

    For more information about getting information about a particular error source in the system, see [Getting Error Source Information for a Specific Error Source](getting-error-source-information-for-a-specific-error-source.md).

2.  Modify the contents of the WHEA\_ERROR\_SOURCE\_DESCRIPTOR structure to change the configuration of the error source.

3.  Set the error source information for the error source by calling the [**WHEAErrorSourceMethods::SetErrorSourceInfoRtn**](https://msdn.microsoft.com/library/windows/hardware/ff559531) method

Any changes that are made to the configuration of an error source will not take effect until after the system is restarted.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Setting%20Error%20Source%20Information%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


