---
Description: Support for base-driver commands (WpdServiceSampleDriver)
title: Support for base-driver commands (WpdServiceSampleDriver)
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Support for base-driver commands (WpdServiceSampleDriver)


The base driver module (*WpdBaseDriver.cpp*) for the sample processes two commands: WPD\_COMMAND\_COMMON\_GET\_OBJECT\_IDS\_FROM\_ PERSISTENT\_UNIQUE\_IDS and WPD\_COMMAND\_COMMON\_SAVE\_CLIENT\_INFORMATION.

However, *WpdBaseDriver.cpp* is also the starting point for all command processing in our driver. This means that all commands are first processed by the **WpdBaseDriver::DispatchMessage** method. This method examines the category of a given command and then forwards it to the enumeration-, property-, capability-, or service-command handler.

The following table describes the two commands that are supported by the base driver module, together with the handler for the command that is supported by the base driver module.

|                                                                       |                                      |                                                                                                                       |
|-----------------------------------------------------------------------|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Command                                                               | Handler                              | Description                                                                                                           |
| WPD\_COMMAND\_COMMON\_GET\_OBJECT\_IDS\_FROM\_PERSISTENT\_UNIQUE\_IDS | OnGetOjectIDsFromPersistentUniqueIDs | Issued when an application tries to retrieve the object identifier that matches a given persistent-unique identifier. |
| WPD\_COMMAND\_COMMON\_SAVE\_CLIENT\_INFORMATION                       | OnSaveClientInfo                     | Issued when an application tries to open a connection to a device or a service.                                       |

 

## <span id="related_topics"></span>Related topics


****
[The WpdServiceSampleDriver](the-wpdservicesampledriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 





