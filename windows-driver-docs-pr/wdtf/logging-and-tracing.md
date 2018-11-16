---
title: WDTF Object Logging
description: WDTF Object Logging
ms.assetid: A99E62D1-31A2-46B5-841B-F3969854E39A
keywords:
- logging WDK WDTF
- tracing WDK WDTF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDTF Object Logging





WDTF Object *Logging* is a feature in WDTF that enables WDTF objects to write log messages to a common log file automatically. The name of the object logging file is called TestTextLog.log. WDTF Object logging has two key benefits. It simplifies test script authoring by using WDTF object methods to log the high level method call, the method's parameters, and the method's result. WDTF Object logging also improves diagnosability by providing a consistent mechanism for writing common log messages.

By default WDTF object logging is disabled. You enable object logging by calling the [**IWDTFConfig2::EnableObjectLogging**](https://msdn.microsoft.com/library/windows/hardware/hh406389) method. After you enable logging, you can temporarily disable or re-enable it for specific actions or collections of actions by calling the methods [**IWDTFAction2::EnableObjectLogging**](https://msdn.microsoft.com/library/windows/hardware/hh406319), [**IWDTFAction2::DisableObjectLogging**](https://msdn.microsoft.com/library/windows/hardware/hh406315), [**IWDTFActions2::EnableObjectLogging**](https://msdn.microsoft.com/library/windows/hardware/hh406357), and [**IWDTFActions2::DisableObjectLogging**](https://msdn.microsoft.com/library/windows/hardware/hh406349).

The log messages that the WDTF writes to the log file have common patterns.

```cpp
<OBJECT_NAME> : <TYPE> : - <METHOD_NAME>(<METHOD_PARAMS>) <Additional Info>
<OBJECT_NAME> : <TYPE> : Target: <DisplayName>
```

The following example shows the logging output for a call to **DeviceDepot.Query("Volume::")** when logging is enabled for an example system.

```cpp
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



