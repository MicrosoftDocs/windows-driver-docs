---
title: WdfFiTester Overview
description: WdfFiTester Overview
ms.assetid: 87acefcd-8db3-4b1e-972a-13fba629d52d
---

# WdfFiTester Overview


You can configure WdfFiTester to fail any KMDF device driver interface (DDI) function calls that return an NTSTATUS code. There are 190 system-supplied functions in KMDF version 1.11 that return an NTSTATUS code. For a list of these functions, see [KMDF Functions that Return NSTATUS Codes](wdftester-functions-that-return-nstatus-codes.md).

The code that handles a KMDF function call typically has the pattern shown in the following code example:

```
//
// Create the device object.
//
status = WdfDeviceCreate(
                         &DeviceInit,
                         &attributes,
                         &device
                         );
if (!NT_SUCCESS(status)) {
 return status;
    }
```

The KMDF function returns an NTSTATUS code and the driver checks for the return code before it proceeds. However, many driver problems occur because of a missing or incorrect check for the return code. These errors might cause unexpected behavior in the driver or could cause a bug check.

For example, a bug check might occur if a function has a (**\_\_out**) pointer parameter that is expected to be valid upon function exit, but, instead, is **NULL**. The bug check can occur if the driver uses the parameter and the driver does not check the return status from the function call correctly.

For each DDI that has been configured for fault injection, the WdfFiTester tool returns an NTSTATUS code of STATUS\_UNSUCCESSFUL. The driver is expected to handle the failure.

Because the tool uses the WMI interface, you can run it from a script (vbscript or jscript) or any other user-mode application (C, C++, or C# ) that can make calls to WMI.

Apart from other operations, with the tool's WMI interface you can get a list of DDIs that were called by a specific KMDF driver, and that are waiting on a WMI event that fires every time a DDI fault injection completes successfully.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20WdfFiTester%20Overview%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




