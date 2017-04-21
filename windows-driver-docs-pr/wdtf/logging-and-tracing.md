---
title: WDTF Object Logging
author: windows-driver-content
description: WDTF Object Logging
ms.assetid: A99E62D1-31A2-46B5-841B-F3969854E39A
keywords:
- logging WDK WDTF
- tracing WDK WDTF
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDTF Object Logging


## <a href="" id="wdtf-logging"></a>


WDTF Object *Logging* is a feature in WDTF that enables WDTF objects to write log messages to a common log file automatically. The name of the object logging file is called TestTextLog.log. WDTF Object logging has two key benefits. It simplifies test script authoring by using WDTF object methods to log the high level method call, the method's parameters, and the method's result. WDTF Object logging also improves diagnosability by providing a consistent mechanism for writing common log messages.

By default WDTF object logging is disabled. You enable object logging by calling the [**IWDTFConfig2::EnableObjectLogging**](https://msdn.microsoft.com/library/windows/hardware/hh406389) method. After you enable logging, you can temporarily disable or re-enable it for specific actions or collections of actions by calling the methods [**IWDTFAction2::EnableObjectLogging**](https://msdn.microsoft.com/library/windows/hardware/hh406319), [**IWDTFAction2::DisableObjectLogging**](https://msdn.microsoft.com/library/windows/hardware/hh406315), [**IWDTFActions2::EnableObjectLogging**](https://msdn.microsoft.com/library/windows/hardware/hh406357), and [**IWDTFActions2::DisableObjectLogging**](https://msdn.microsoft.com/library/windows/hardware/hh406349).

The log messages that the WDTF writes to the log file have common patterns.

```
<OBJECT_NAME> : <TYPE> : - <METHOD_NAME>(<METHOD_PARAMS>) <Additional Info>
<OBJECT_NAME> : <TYPE> : Target: <DisplayName>
```

The following example shows the logging output for a call to **DeviceDepot.Query("Volume::")** when logging is enabled for an example system.

```
[ Ouput ]

WDTF_TARGETS    : INFO  :  - Query("Volume::")
WDTF_TARGETS    : INFO  :          Target: Generic volume
WDTF_TARGETS    : INFO  :          Target: Generic volume
WDTF_TARGETS    : INFO  :          Target: HL-DT-ST RW/DVD MU10N ATA Device
WDTF_TARGETS    : INFO  :          Target: Generic volume
WDTF_TARGETS    : INFO  :          Target: Generic volume
WDTF_TARGETS    : INFO  :          Target: Generic volume
```

If object logging is enabled, object error logging is enabled by default. Otherwise, error logging defaults to disabled. Like object logging, you can enable/disable error logging by calling the methods [**IWDTFConfig2::EnableObjectErrorLogging**](https://msdn.microsoft.com/library/windows/hardware/hh406387), [**IWDTFConfig2::DisableObjectErrorLogging**](https://msdn.microsoft.com/library/windows/hardware/hh406383), [**IWDTFAction2::EnableObjectErrorLogging**](https://msdn.microsoft.com/library/windows/hardware/hh406317), [**IWDTFAction2::DisableObjectErrorLogging**](https://msdn.microsoft.com/library/windows/hardware/hh406313), [**IWDTFActions2::EnableObjectErrorLogging**](https://msdn.microsoft.com/library/windows/hardware/hh406353), and [**IWDTFActions2::DisableObjectErrorLogging**](https://msdn.microsoft.com/library/windows/hardware/hh406346).

The log messages that the WDTF writes to the log file for error logging have the following patterns. Look for the keyword "ERROR" to jump to the first error in the log.

``` syntax
<OBJECT_NAME> : <TYPE> : - <METHOD_NAME>(<METHOD_PARAMS>) <Additional Info>
<OBJECT_NAME> : <TYPE> : Target: <DisplayName>
<OBJECT_NAME> : ERROR : Status: <ErrorString>
```

You still have the option to write a custom message to the log file by calling the [**IWDTFLog2::OutputInfo**](https://msdn.microsoft.com/library/windows/hardware/hh451016) or [**IWDTFLog2::OutputError**](https://msdn.microsoft.com/library/windows/hardware/hh451014) method.

For a list of the available objects, see [WDTF Object Name tags](wdtf-object-name-tags.md).

## Related topics
[WDTF Object Name tags](wdtf-object-name-tags.md)  
[Enabling and Viewing WDTF Traces](viewing-wdtf-traces.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdtf\dtf%5D:%20WDTF%20Object%20Logging%20%20RELEASE:%20%289/13/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


