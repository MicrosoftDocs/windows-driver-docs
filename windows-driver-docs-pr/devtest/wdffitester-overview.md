---
title: WdfFiTester Overview
description: WdfFiTester Overview
ms.assetid: 87acefcd-8db3-4b1e-972a-13fba629d52d
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





