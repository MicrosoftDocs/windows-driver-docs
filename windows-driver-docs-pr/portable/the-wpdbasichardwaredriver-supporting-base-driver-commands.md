---
Description: Support for base-driver commands (WpdBasicHardwareDriverSample)
title: Support for base-driver commands (WpdBasicHardwareDriverSample)
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Support for base-driver commands (WpdBasicHardwareDriverSample)


The base driver module for the sample (*WpdBaseDriver.cpp*) processes a single command (WPD\_COMMAND\_COMMON\_GET\_OBJECT\_IDS\_FROM\_ PERSISTENT\_UNIQUE\_IDS). However, this module is also the starting point for all command processing in the sample driver. This means that all commands are first processed by the **WpdBaseDriver::DispatchMessage** method. This method examines the category of a given command and then forwards it to the enumeration-, property-, or capability-command handler.

The one change that occurred in the **WpdBaseDriver::DispatchMessage** method was that the code that checks for resource-related commands was removed. Because the sample driver does not support resources, it was no longer necessary to process related commands; any application that sends non-implemented commands receives the E\_NOTIMPL error.

The information in the following table describes the command that is supported by the base driver module, together with the handler for the command.

| Command                                                               | Handler                              | Description                                                                                                              |
|-----------------------------------------------------------------------|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| WPD\_COMMAND\_COMMON\_GET\_OBJECT\_IDS\_FROM\_PERSISTENT\_UNIQUE\_IDS | OnGetOjectIDsFromPersistentUniqueIDs | Issued when an application attempts to retrieve the object identifier that matches a given persistent-unique identifier. |

 

## <span id="related_topics"></span>Related topics


****
[The WpdBasicHardwareDriverSample](the-wpdbasichardwaredriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 





