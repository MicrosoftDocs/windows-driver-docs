---
title: Registering the Minifilter Driver
description: Registering the Minifilter Driver
keywords:
- registering minifilter drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering the Minifilter Driver


## <span id="ddk_registering_the_minifilter_if"></span><span id="DDK_REGISTERING_THE_MINIFILTER_IF"></span>


Every minifilter driver must call [**FltRegisterFilter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltregisterfilter) from its **DriverEntry** routine to add itself to the global list of registered minifilter drivers and to provide the filter manager with a list of callback routines and other information about the driver.

In the MiniSpy sample, the minifilter driver is registered as shown in the following code example:

```cpp
NTSTATUS status;
status = FltRegisterFilter(
           DriverObject,                  //Driver
           &FilterRegistration,           //Registration
           &MiniSpyData.FilterHandle);    //RetFilter
```

**FltRegisterFilter** has two input parameters. The first, *Driver*, is the driver object pointer that the minifilter driver received as the *DriverObject* input parameter to its **DriverEntry** routine. The second, *Registration*, is a pointer to an [**FLT\_REGISTRATION**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_registration) structure that contains entry points to the minifilter driver's callback routines.

In addition, **FltRegisterFilter** has an output parameter, *RetFilter*, that receives an opaque filter pointer for the minifilter driver. This filter pointer is a required input parameter for many **Flt**_Xxx_ support routines, including [**FltStartFiltering**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltstartfiltering) and [**FltUnregisterFilter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltunregisterfilter).

 

