---
title: What are the WPP extended format specification strings
description: What are the WPP extended format specification strings
ms.date: 01/27/2021
ms.localizationpriority: medium
---

# What are the WPP extended format specification strings

WPP includes predefined format specification strings that you can use in trace messages in addition to the standard format strings that are defined for **printf**.

You can use the **%!FLAGS!**, **%!FUNC!** and **%!LEVEL!** strings in a [trace message prefix](trace-message-prefix.md), and in any tracing function or macro, such as [**DoTraceMessage**](/previous-versions/windows/hardware/previsioning-framework/ff544918(v=vs.85)).

You can use the other extended strings in any tracing function.

## Default configuration options for tracewpp

WPP uses "defaultwpp.ini" for the default configuration settings. This default INI file is included as part of the Windows SDK in the WppConfig Rev1 directory. Refer to this INI file for the latest information on the WPP default behavior, as well as for additional information on customization.

### Software tracing

|Format string|Description|
|----|----|
|%!FILE!|Displays the name of the source file from which the trace message was generated. This variable can also be used in the [trace message prefix](trace-message-prefix.md)|.
|%!FLAGS!|Displays the value of the [trace flags](trace-flags.md) that enable the trace message. This variable can also be used in the  [trace message prefix](trace-message-prefix.md).|
|%!FUNC!|Displays the function that generated the trace message. This variable can also be used in the [trace message prefix](trace-message-prefix.md).|
|%!LEVEL!|Displays the name of the [trace level](trace-level.md)  that enables the trace message. This variable can also be used in the [trace message prefix](trace-message-prefix.md).|
|%!LINE!|Displays the line number of the line in the code that generated the trace prefix. This variable can also be used in the [trace message prefix](trace-message-prefix.md).|

### General use

|Format string|Description|
|----|----|
|%!bool!|Displays TRUE or FALSE|
|%!irql!|Displays the name of the current IRQL.|
|%!sid!|Represents a pointer to Security Identifier (pSID). Displays the SID.|
|**GUIDs**| |
|%!GUID!|Represents a pointer to a GUID (pGUID). Displays the GUID that is pointed to.|
|%!CLSID!|Class ID. Represents a pointer to a class ID GUID. Displays the string associated with the GUID. WPP locates the string in the registry when it formats the trace messages.|
|%!LIBID!|Type library. Represents the GUID of a COM type library. Displays the string associated with the GUID. WPP locates the string in the registry when it formats the trace messages.|
|%!IID!|Interface ID. Represents a pointer to an interface ID GUID. Displays the string associated with the GUID. WPP locates the string in the registry when it formats the trace messages.|
|**Time**| |
|%!delta!|Displays the difference between two time values, in milliseconds. It is a LONGLONG value that is displayed in **day~h:m:s** format.|
|%!WAITTIME!|Displays the time that was spent waiting for something to be completed, in milliseconds. It is a LONGLONG value that is displayed in **day~h:m:s** format. Designed to be used with **%!due!**.|
|%!due!|Displays the time that something is expected to be completed, in milliseconds. It is a LONGLONG value that is displayed in **day~h:m:s** format. Designed to be used with **%!WAITTIME!**.|
|%!TIMESTAMP! </br>%!datetime! </br> %!TIME!|Displays the value of system time at a particular moment. These are LONGLONG (SINT64) values that are displayed in SYSTEMTIME format.</br>You can use these variables to represent different time values in your program and to distinguish among them.|

### Return codes

|Format string|Description|
|----|----|
|%!STATUS!|Represents a status value and displays the string associated with the status code.|
|%!WINERROR!|Represents a Windows error code and displays the string associated with the error.|
|%!HRESULT!|Represents an error or warning and displays the code in HRESULT format.|

### Network
|Format string|Description|
|----|----|
|%!IPADDR!|Represents a pointer to an IP address. Displays the IP address.|
|%!PORT!|Displays a port number.|
