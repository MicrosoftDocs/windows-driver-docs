---
title: Registering the Minifilter Driver
author: windows-driver-content
description: Registering the Minifilter Driver
ms.assetid: 943082c9-dcff-478f-80ba-2a2e72f6ead2
keywords: ["registering minifilter drivers"]
---

# Registering the Minifilter Driver


## <span id="ddk_registering_the_minifilter_if"></span><span id="DDK_REGISTERING_THE_MINIFILTER_IF"></span>


Every minifilter driver must call [**FltRegisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544305) from its **DriverEntry** routine to add itself to the global list of registered minifilter drivers and to provide the filter manager with a list of callback routines and other information about the driver.

In the MiniSpy sample, the minifilter driver is registered as shown in the following code example:

```
NTSTATUS status;
status = FltRegisterFilter(
           DriverObject,                  //Driver
           &amp;FilterRegistration,           //Registration
           &amp;MiniSpyData.FilterHandle);    //RetFilter
```

**FltRegisterFilter** has two input parameters. The first, *Driver*, is the driver object pointer that the minifilter driver received as the *DriverObject* input parameter to its **DriverEntry** routine. The second, *Registration*, is a pointer to an [**FLT\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff544811) structure that contains entry points to the minifilter driver's callback routines.

In addition, **FltRegisterFilter** has an output parameter, *RetFilter*, that receives an opaque filter pointer for the minifilter driver. This filter pointer is a required input parameter for many **Flt***Xxx* support routines, including [**FltStartFiltering**](https://msdn.microsoft.com/library/windows/hardware/ff544569) and [**FltUnregisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544606).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Registering%20the%20Minifilter%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


