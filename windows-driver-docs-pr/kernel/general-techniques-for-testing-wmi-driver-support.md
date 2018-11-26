---
title: General Techniques for Testing WMI Driver Support
description: General Techniques for Testing WMI Driver Support
ms.assetid: 4d1a9198-2cc7-491d-a803-80f846882a6e
keywords: ["WMI WDK kernel , testing", "testing WMI support WDK kernel", "WMI WDM provider logs WDK", "errors WDK WMI", "provider logs WDK WMI", "events WDK WMI", "WMI WDK kernel , errors"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# General Techniques for Testing WMI Driver Support





### WMI Client Tools

There are several tools you can use to test WMI support in your driver.

<a href="" id="wbemtest"></a>Wbemtest  
The operating system includes the Wbemtest tool, which provides a GUI you can use to query for WMI classes and class instances, change property values, execute methods, and receive event notifications. Connect to the "root\\wmi" namespace to test your driver's support.

<a href="" id="wmic"></a>Wmic  
Microsoft Windows XP and later operating systems include the Wmic tool, which provides a command shell you can use to issue WMI-related commands to test your driver.

<a href="" id="wmimofck"></a>Wmimofck  
The **wmimofck** command can be used to check the syntax of your binary MOF files. You can also use the **wmimofck -t** command to generate a VBScript file. You can use this script to test your driver's handling of WMI class instance queries. The **wmimofck -w** command generates webpages that can test querying and setting classes, executing methods, and receiving events. Note that the webpages do not support executing methods that use complex parameters or return values (such as an array of embedded classes). In such cases you can use Wbemtest instead. See [Using wmimofck.exe](using-wmimofck-exe.md) for more information about Wmimofck.

You can also test your driver's WMI support by writing a custom WMI client application, using the WMI user-mode API.

For more information about this user-mode API, which allows applications to provide or consume WMI information, refer to the Windows Management Instrumentation information in the Microsoft Windows SDK documentation.

A WMI client application performs the following tasks to test a driver:

-   Connects to WMI.

    To connect to WMI, the application can call the Component Object Model (COM) function, **CoCreateInstance**, to retrieve a pointer to the **IWbemLocator** interface. The application then calls the **IWbemLocator::ConnectServer** method to connect to WMI. From this call, the application receives a pointer to the **IWbemServices** interface.

-   Accesses information in the driver.

    To access information and to register for events, the application uses the methods of the **IWbemServices** interface.

### <a href="" id="ddk-wmi-irps-and-the-system-event-log-kg"></a>WMI IRPs and the System Event Log

WMI errors that occur strictly in kernel-mode are logged to the system event log. You can use the Event Viewer to examine the system event log. (See [Logging Errors](logging-errors.md) for more information.)

The two main sources of such errors are malformed replies to WMI requests and incorrect parameters to event notifications. For example, if the driver returns a malformed [**WMIREGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff565832) data structure in response to an [**IRP\_MN\_REGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551731) or [**IRP\_MN\_REGINFO\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff551734) request, the system will log that to the system event log. The system would also log an invalid call to [**IoWMIWriteEvent**](https://msdn.microsoft.com/library/windows/hardware/ff550520) and [**WmiFireEvent**](https://msdn.microsoft.com/library/windows/hardware/ff565807) to issue a WMI event notification.

### <a href="" id="ddk-wmi-wdm-provider-log-kg"></a>WMI WDM Provider Log

WMI errors that occur while being handled by the WMI WDM provider (Wmiprov.dll) are logged to the log file for the WMI WDM Provider, Wmiprov.log. This is a text file can be found in %windir%\\system32\\wbem\\logs\\wmiprov.log. Errors, such as a bad or missing MOF resource for the driver, are logged here. In the case of a bad MOF resource, the file %windir%\\system32\\mofcomp.log might have additional information related to the error.

In versions of Windows earlier than Windows Vista, you can change the logging settings for all WMI providers by using the Wmimgmt.msc application. (In Windows 98/Me, use Wbemcntl instead.) You can disable or reenable logging, change the directory where WMI log files are kept, as well as set the maximum size for such files. For more information, see [WMI Log Files](https://msdn.microsoft.com/library/aa394564).

 

 




