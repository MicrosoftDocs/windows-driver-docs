---
title: WexLogger
description: WexLogger
ms.assetid: D9F4AD08-19EA-4a6c-AD25-886FBEA334B8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WexLogger


The WexLogger provides a consistent API for logging which spans native code, managed code and script. It also scales from running Unit Tests in a command prompt all the way up to long-haul stress testing.

## Logging Through the Verify Framework


Most logging within a test case should be performed via the [Verify](verify.md) framework. This will ensure that tests are authored in a clearer, more sequential and human-readable fashion. However, in some cases, test authors will find that they need more granular control around what is written to the logs: hence the need for the WexLogger API.

## Logging Within TAEF


For test cases running within TAEF, there is no logger initialization necessary by the test author. You can immediately start using the Log API that is exposed to the language that you are authoring your tests in.

In native C++ code, it will look like this:

```cpp
using namespace WEX::Logging;
using namespace WEX::Common;
Log::Comment(L"Rendering to the BufferView");
Log::Comment(L"Render succeeded");

Log::Comment(String().Format(L"Look, a number! %d", aNumber));

#define LOG_OUTPUT(fmt, ...) Log::Comment(String().Format(fmt, __VA_ARGS__))
LOG_OUTPUT(L"Look, a number! %d", aNumber);
```

In managed code, it will look like this:

```cpp
Log.Comment("Rendering to the BufferView");
Log.Comment("Render succeeded");
```

In JScript, it will look like this:

```cpp
var log = new ActiveXObject("WEX.Logger.Log");
log.Comment("Rendering to the BufferView");
log.Comment("Render succeeded");
```

## Logging Outside TAEF


The majority of the time, logging initialization and completion will be performed by TAEF, so the WexLogger will be ready to use for the duration of the test case as stated above, and will finish properly. However, if a client would like to use the WexLogger outside TAEF, they will be responsible for manually calling **LogController::InitializeLogging()** and **LogController::FinalizeLogging()**. This requirement exists for native and managed code only; scripts do not have this additional requirement. See the Static LogController Methods table below for more information on the LogController API.

Refer to the [Generating WTT Logs](#generating-wtt-logs) section for information on how to generate WTT Logs outside TAEF.

## WexLogger API


**Here is the list of native C++ Log methods available.**

There are equivalent versions available to managed code and script.

| Native C++ Log Methods                                                                                                              | Functionality                                                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Assert(const wchar\_t\* pszAssert)                                                                                                  | Log a test assert.                                                                                                                                                                           |
| Assert(const wchar\_t\* pszAssert, const wchar\_t\* pszContext)                                                                     | Log a test assert, with context.                                                                                                                                                             |
| Assert(const wchar\_t\* pszAssert, const wchar\_t\* pszFile, const wchar\_t\* pszFunction, int line)                                | Log a test assert with file, function and line information.                                                                                                                                  |
| Assert(const wchar\_t\* pszAssert, const wchar\_t\* pszContext, const wchar\_t\* pszFile, const wchar\_t\* pszFunction, int line)   | Log a test assert, with context, and also file, function and line information.                                                                                                               |
| Bug(const wchar\_t\* pszBugDatabase, int bugId)                                                                                     | Log a known bug number.                                                                                                                                                                      |
| Bug(const wchar\_t\* pszBugDatabase, int bugId, const wchar\_t\* pszContext)                                                        | Log a known bug number, with context.                                                                                                                                                        |
| Comment(const wchar\_t\* pszComment)                                                                                                | Log a test comment.                                                                                                                                                                          |
| Comment(const wchar\_t\* pszComment, const wchar\_t\* pszContext)                                                                   | Log a test comment, with context                                                                                                                                                             |
| EndGroup(const wchar\_t\* pszGroupName)                                                                                             | Log the end of a group of tests, or of a specific test.                                                                                                                                      |
| EndGroup(const wchar\_t\* pszGroupName, const wchar\_t\* pszContext)                                                                | Log the end of a group of tests, or of a specific test, with context.                                                                                                                        |
| Error(const wchar\_t\* pszError)                                                                                                    | Log a test error.                                                                                                                                                                            |
| Error(const wchar\_t\* pszError, const wchar\_t\* pszContext)                                                                       | Log a test error, with context.                                                                                                                                                              |
| Error(const wchar\_t\* pszError, const wchar\_t\* pszFile, const wchar\_t\* pszFunction, int line)                                  | Log a test error with file, function and line information.                                                                                                                                   |
| Error(const wchar\_t\* pszError, const wchar\_t\* pszContext, const wchar\_t\* pszFile, const wchar\_t\* pszFunction, int line)     | Log a test error, with context, and also file, function and line information.                                                                                                                |
| File(const wchar\_t\* pszFileName)                                                                                                  | Log a test file to be saved. Files are saved to either &lt;WTTRunWorkingDir&gt;\\WexLogFileOutput (if WTTRunWorkingDir is set), or &lt;CurrentDirectory\\&gt;WexLogFileOutput.               |
| File(const wchar\_t\* pszFileName, const wchar\_t\* pszContext)                                                                     | Log a test file to be saved, with context. Files are saved to either &lt;WTTRunWorkingDir&gt;\\WexLogFileOutput (if WTTRunWorkingDir is set), or &lt;CurrentDirectory\\&gt;WexLogFileOutput. |
| Property(const wchar\_t\* pszName, const wchar\_t\* pszValue)                                                                       | Log a name/value property pair. The value can be in xml format.                                                                                                                              |
| Property(const wchar\_t\* pszName, const wchar\_t\* pszValue, const wchar\_t\* pszContext)                                          | Log a name/value property pair, with context. The value can be in xml format.                                                                                                                |
| Result(TestResults::Result testResult)                                                                                              | Log a test result.                                                                                                                                                                           |
| Result(TestResults::Result testResult, const wchar\_t\* pszComment)                                                                 | Log a test result with an associated comment.                                                                                                                                                |
| Result(TestResults::Result testResult, const wchar\_t\* pszComment, const wchar\_t\* pszContext)                                    | Log a test result with an associated comment, with context.                                                                                                                                  |
| StartGroup(const wchar\_t\* pszGroupName)                                                                                           | Log the start of a group of tests, or of a specific test.                                                                                                                                    |
| StartGroup(const wchar\_t\* pszGroupName, TestResults::Result defaultTestResult)                                                    | Log the start of a group of tests, or of a specific test; also sets the default test result.                                                                                                 |
| StartGroup(const wchar\_t\* pszGroupName, const wchar\_t\* pszContext)                                                              | Log the start of a group of tests, or of a specific test, with context.                                                                                                                      |
| StartGroup(const wchar\_t\* pszGroupName, const wchar\_t\* pszContext, TestResults::Result defaultTestResult)                       | Log the start of a group of tests, or of a specific test; also sets the default test result.                                                                                                 |
| Warning(const wchar\_t\* pszWarning)                                                                                                | Log a test warning.                                                                                                                                                                          |
| Warning(const wchar\_t\* pszWarning, const wchar\_t\* pszContext)                                                                   | Log a test warning, with context.                                                                                                                                                            |
| Warning(const wchar\_t\* pszWarning, const wchar\_t\* pszFile, const wchar\_t\* pszFunction, int line)                              | Log a test warning with file, function and line information.                                                                                                                                 |
| Warning(const wchar\_t\* pszWarning, const wchar\_t\* pszContext, const wchar\_t\* pszFile, const wchar\_t\* pszFunction, int line) | Log a test warning, with context, and also file, function and line information.                                                                                                              |
| Xml(const wchar\_t\* pszXml)                                                                                                        | Log xml data. No check is made to verify that it is well-formed.                                                                                                                             |
| Xml(const wchar\_t\* pszXml, const wchar\_t\* pszContext)                                                                           | Log xml data, with context. No check is made to verify that it is well-formed.                                                                                                               |
| MiniDump()                                                                                                                          | Log the current process mini dump.                                                                                                                                                           |



**Note:** "Context" is an extra string that you can optionally provide with a **WexLogger** API call to provide more context or detail. For example, you may choose to always pass in "ImageComparator" as your context when making any **WexLogger** API calls from your ImageComparator class methods.

Here are the possible valid values for the native C++ **TestResults::Result** enumeration. There are equivalent versions available to managed code and script.

| Native C++ TestResults::Result enumeration | Functionality        |
|--------------------------------------------|----------------------|
| Passed                                     | The test passed      |
| NotRun                                     | The test was not run |
| Skipped                                    | The test was skipped |
| Blocked                                    | The test was blocked |
| Failed                                     | The test failed      |



**Here is the list of native C++ LogContoller methods available:**

| Native C++ LogController Methods                                                                       | Functionality                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static HRESULT InitializeLogging()                                                                     | Initialize logging functionality.                                                                                                                                                                                                                                                                               |
| static HRESULT InitializeLogging(WexLoggerErrorCallback pfnErrorCallback)                              | Initialize logging functionality, and specify the WexLoggerErrorCallback function you would like to use to be notified of internal logger errors.                                                                                                                                                               |
| static HRESULT InitializeLogging(const wchar\_t\* pszLogName)                                          | Initialize logging functionality, and specify the name of the log file you would like to use. **Note:** The log name is only taken into account if [WttLogging is enabled](#generating-wtt-logs).                                                                                                             |
| static HRESULT InitializeLogging(const wchar\_t\* pszLogName, WexLoggerErrorCallback pfnErrorCallback) | Initialize logging functionality, specify the name of the log file you would like to use, and specify the WexLoggerErrorCallback function you would like to use to be notified of internal logger errors. **Note:** The log name is only taken into account if [WttLogging is enabled](#generating-wtt-logs). |
| static bool IsInitialized()                                                                            | Returns whether or not the LogController has been initialized for this process.                                                                                                                                                                                                                                 |
| static const unsigned short\* GetLogName()                                                             | Returns the name that was specified for the log in the InitializeLogging call (if any).                                                                                                                                                                                                                         |
| static HRESULT FinalizeLogging()                                                                       | Finish logging functionality.                                                                                                                                                                                                                                                                                   |



**Note:** See the C++ Error Handling section below for more information on the **WexLoggerErrorCallback** mechanism and how to use it outside the TAEF framework.

**Note:** It is only necessary to call InitializeLogging/FinalizeLogging when using the **WexLogger** outside the TAEF framework, as TAEF already handles logging initialization/completion.

**Note:** It is not necessary to initialize/complete logging functionality when using the **WexLogger** from script.

**Here is the list of native C++ RemoteLogContoller methods available:**

| Native C++ RemoteLogController Methods                                                                             | Functionality                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static HRESULT GenerateConnectionData(WEX::Common::NoThrowString& connectionData)                                  | Generates the connection data that must be used within the parent and child processes to allow the child process to log back to the parent process.                                                          |
| static HRESULT GenerateConnectionData(const wchar\_t\* pszMachineName, WEX::Common::NoThrowString& connectionData) | Used when launching child processes on a remote machine. Generates the connection data that must be used within the parent and child processes to allow the child process to log back to the parent process. |
| static HRESULT InitializeLogging(WEX::Common::NoThrowString connectionData)                                        | Initializes logging functionality within the parent process so the child process can log back to it.                                                                                                         |



**Note:** See the [Remote Logging From Child Processes](#remote-logging-from-child-processes) section below for more information on remote logging.

Here is the list of managed Log methods available.

| Managed Log Methods                                                             | Functionality                                                                                                                                                                |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Assert(IFormatProvider provider, string format, params object\[\] args)         | Log a test assert using a culture-specific formatting information provider, a format string, and an object array that contains zero or more objects to format.               |
| Assert(IFormatProvider provider, string format, params object\[\] args)         | Log a test assert using a culture-specific formatting information provider, a format string, and an object array that contains zero or more objects to format.               |
| Assert(string message)                                                          | Log a test assert.                                                                                                                                                           |
| Assert(string format, object arg0)                                              | Log a test assert using a format string and an object to format.                                                                                                             |
| Assert(string format, params object\[\] args)                                   | Log a test assert using a format string, and an object array that contains zero or more objects to format.                                                                   |
| Assert(string message, string context)                                          | Log a test assert, with context.                                                                                                                                             |
| Assert(string message, string file, string function, int line)                  | Log a test assert, and also file, function and line information.                                                                                                             |
| Assert(string message, string context, string file, string function, int line)  | Log a test assert, with context, and also file, function and line information.                                                                                               |
| Bug(string bugDatabase, int bugId)                                              | Log a known bug number.                                                                                                                                                      |
| Bug(string bugDatabase, int bugId, string context)                              | Log a known bug number, with context.                                                                                                                                        |
| Comment(IFormatProvider provider, string format, params object\[\] args)        | Log a test comment using a culture-specific formatting information provider, a format string, and an object array that contains zero or more objects to format.              |
| Comment(string message)                                                         | Log a test comment                                                                                                                                                           |
| Comment(string format, object arg0)                                             | Log a test comment using a format string and an object to format.                                                                                                            |
| Comment(string format, params object\[\] args)                                  | Log a test comment using a format string and an object array that contains zero or more objects to format.                                                                   |
| Comment(string message, string context)                                         | Log a test comment, with context                                                                                                                                             |
| EndGroup(string groupName)                                                      | Log the end of a group of tests, or of a specific test.                                                                                                                      |
| EndGroup(string groupName, string context)                                      | Log the end of a group of tests, or of a specific test, with context.                                                                                                        |
| Error(IFormatProvider provider, string format, params object\[\] args)          | Log a test error using a culture-specific formatting information provider, a format string, and an object array that contains zero or more objects to format.                |
| Error(string message)                                                           | Log a test error.                                                                                                                                                            |
| Error(string format, object arg0)                                               | Log a test error using a format string and an object to format.                                                                                                              |
| Error(string message, string context)                                           | Log a test error, with context.                                                                                                                                              |
| Error(IFormatProvider provider, string format, params object\[\] args)          | Log a test error using a format string and an object array that contains zero or more objects to format.                                                                     |
| Error(string message, string file, string function, int line)                   | Log a test error with file, function and line information.                                                                                                                   |
| Error(string message, string context, string file, string function, int line)   | Log a test error, with context, and also file, function and line information.                                                                                                |
| File(string fileName)                                                           | Log a test file to be saved. Files are saved to either WTTRunWorkingDir\\WexLogFileOutput (if WTTRunWorkingDir is set), or CurrentDirectory\\WexLogFileOutput.               |
| File(string fileName, string context)                                           | Log a test file to be saved, with context. Files are saved to either WTTRunWorkingDir\\WexLogFileOutput (if WTTRunWorkingDir is set), or CurrentDirectory\\WexLogFileOutput. |
| MiniDump()                                                                      | Log the current process mini dump.                                                                                                                                           |
| Property(string name, string value)                                             | Log a name/value property pair. The value can be in xml format.                                                                                                              |
| Property(string name, string value, string context)                             | Log a name/value property pair, with context. The value can be in xml format.                                                                                                |
| Result(TestResult testResult)                                                   | Log a test result.                                                                                                                                                           |
| Result(TestResult testResult, string comment)                                   | Log a test result with an associated comment.                                                                                                                                |
| Result(TestResult testResult, string comment, string context)                   | Log a test result with an associated comment, with context.                                                                                                                  |
| StartGroup(string groupName)                                                    | Log the start of a group of tests, or of a specific test.                                                                                                                    |
| StartGroup(string groupName, string context)                                    | Log the start of a group of tests, or of a specific test, with context.                                                                                                      |
| Warning(IFormatProvider provider, string format, params object\[\] args)        | Log a test warning using a culture-specific formatting information provider, a format string, and an object array that contains zero or more objects to format.              |
| Warning(string message)                                                         | Log a test warning.                                                                                                                                                          |
| Warning(string format, object arg0)                                             | Log a test warning using a format string and an object to format.                                                                                                            |
| Warning(string format, params object\[\] args)                                  | Log a test warning using a format string and an object array that contains zero or more objects to format.                                                                   |
| Warning(string message, string context)                                         | Log a test warning, with context.                                                                                                                                            |
| Warning(string message, string file, string function, int line)                 | Log a test warning with file, function and line information.                                                                                                                 |
| Warning(string message, string context, string file, string function, int line) | Log a test warning, with context, and also file, function and line information.                                                                                              |
| Xml(string xmlData)                                                             | Log xml data. No check is made to verify that it is well-formed.                                                                                                             |
| Xml(string xmlData, string context)                                             | Log xml data, with context. No check is made to verify that it is well-formed.                                                                                               |



**Here is the list of managed LogContoller methods available:**

| Managed LogController Methods                 | Functionality                                                                                                                                                                                       |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static void InitializeLogging()               | Initialize logging functionality.                                                                                                                                                                   |
| static void InitializeLogging(String logName) | Initialize logging functionality, and specify the name of the log file you would like to use. **Note:** The log name is only taken into account if [WttLogging is enabled](#generating-wtt-logs). |
| static bool IsInitialized()                   | Returns whether or not the LogController has been initialized for this process.                                                                                                                     |
| static String GetLogName()                    | Returns the name that was specified for the log in the InitializeLogging call (if any).                                                                                                             |
| static void FinalizeLogging()                 | Finish logging functionality.                                                                                                                                                                       |



**Note:** See the Managed Code Error and Exception section below for more information on how to handle errors and exceptions when using the managed layer of the **WexLogger** outside the TAEF framework.

**Note:** It is only necessary to call InitializeLogging/FinalizeLogging when using the **WexLogger** outside the TAEF framework, as TAEF already handles logging initialization/completion.

**Note:** It is not necessary to initialize/complete logging functionality when using the **WexLogger** from script.

**Here is the list of managed RemoteLogContoller methods available:**

| Managed RemoteLogController Methods                      | Functionality                                                                                                                                                                                                |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static String GenerateConnectionData()                   | Generates the connection data that must be used within the parent and child processes to allow the child process to log back to the parent process.                                                          |
| static String GenerateConnectionData(string machineName) | Used when launching child processes on a remote machine. Generates the connection data that must be used within the parent and child processes to allow the child process to log back to the parent process. |
| static void InitializeLogging(String connectionData)     | Initializes logging functionality within the parent process so the child process can log back to it.                                                                                                         |



**Note:** See the [Remote Logging From Child Processes](#remote-logging-from-child-processes) section below for more information on remote logging.

## Remote Logging From Child Processes


WexLogger provides the ability for one or more child processes to log back to a single parent process, resulting in the generation of consolidated test results within a single log file.

The child processes can either be running on the same machine as the parent process, or remotely on a different machine. For remote-machine logging to work, it is up to the WexLogger client to add TCP firewall exclusions for all child processes on the remote machine. However, if the child processes are running on the same machine as the parent, no firewall modifications are necessary.

The following steps are necessary to set up each remote logging connection:

**Parent Process**

1.  Call **RemoteLogController::GenerateConnectionData()** to generate the connection data that must be used by both processes to initiate a logging connection.

    **Note:** Be sure to check the return value of this call.

    ```cpp
        NoThrowString connectionData;
        Throw::IfFailed(RemoteLogController::GenerateConnectionData(connectionData));

    ```

2.  Communicate the connection data with the child process either by setting it in its environment block, or by passing it as an argument at the command prompt. For example:

    **Pass as a named argument at the command prompt that WexLogger understands:**  
    /wexlogger\_connectiondata=*\[connection data\]*

    **Note:** If this option is used, then step 1 in the **Child Process** section below **is not** necessary.

    **Pass as a named environment variable that WexLogger understands:**  
    \[YourAppName\_cmd\]=/wexlogger\_connectiondata=*\[connection data\]*

    **Note:** If this option is used, then step 1 in the **Child Process** section below **is not** necessary.

    **Pass to process in an arbitrary format (some other command parameter, environment variable, etc.)**  
    **Note:** If this option is used, then step 1 in the **Child Process** section below **is** necessary.

    **Note:** As a convenience, the value "/wexlogger\_connectiondata=" is defined as a constant in both the native and managed RemoteLogControllers:

    -   **WEX::Logging::c\_szWexLoggerRemoteConnectionData**, in LogController.h

    -   **RemoteLogController.WexLoggerRemoteConnectionData**, in Wex.Logger.Interop.dll

3.  Launch the child process with the connection data
4.  Call **RemoteLogController::InitalizeLogging(*\[connection data created in step 1\]*)**. This call must be made after the child process is launched, since it will time out if the child does not call **LogController::InitializeLogging()** in a timely manner.

    **Note:** Be sure to check the return value of this call.

    ```cpp
    // ...launch child process with connection data...
    Throw::IfFailed(RemoteLogController::InitializeLogging(connectionData));
    ```

5.  Wait on the child process, etc.

**Child Process**

1.  If the connection data was **not** passed to the child process as a named argument at the command prompt that WexLogger understands (see step 2 above), then you must set an environment variable as such:

    \[YourAppName\_cmd\]=/wexlogger\_connectiondata=*\[connection data\]*

    **For example:**

    ```cpp
    // App name is mytestapp.exe
    ::SetEnvironmentVariable(L"mytestapp_cmd", String(c_szWexLoggerRemoteConnectionData).Append(connectionData));
    ```

2.  Call **LogController::InitializeLogging()** to initialize logging for this process. Internally, this will leverage the environment variable set in step 1 above (or in step 2 of the **Parent Process** section) to initiate a logging connection back to the parent process.
3.  Log, etc; all traces will be sent back to the parent process.
4.  Call **LogController::FinalizeLogging()** to finish logging for this process.

## Determining Test Outcome


Although there is a method provided to explicitly state the intended outcome of a test case (**Log::Result()**), there is no **need** for a test case to use this method in most cases.

For example, if a test case does not explicitly call **Log::Result()**, and **does not** log an error (via **Log::Error()**), by default it is considered a passing test case; if it **does** log an error, it is a failing test case.

However, if a test case **does** explicitly call **Log::Result(TestResults::TestPassed)**, but also **does** log an error within the test case, the test will still be counted as a failure since an error occurred within the test.

Inside the TAEF framework, this behavior can be overridden by tagging your test with a different default test result. More information on this can be found in the "Authoring TAEF Tests" document.

This behavior can also be overridden by explicitly calling **Log::StartGroup()** for your own test groups/test cases, with a default test result of your choice.

## Generating WTT Logs


Three methods exist to generate WTT logs via the **WexLogger**. All of them require that **WttLog.dll** is present in the run directory, or in your path.

-   If you are running in the lab, with the wtt client installed, wtt logs will automatically be generated for you. This is due to the fact that the WexLogger looks for the existence of two environment variables that should only exist in a lab environment: 'WttTaskGuid' and 'WTTRunWorkingDir'. If both of these exist, then wtt logging is automatically enabled.
-   If running within TAEF outside a lab environment, pass /enablewttlogging at the command prompt to your test case. Example:

    ``` syntax
    te my.test.dll /enablewttlogging
    ```

-   If you are consuming WexLogger outside the TAEF framework, and you are not running in a lab environment, you must set the **&lt;YOUR\_PROCESS\_NAME&gt;\_CMD** environment variable to contain this option before calling **LogController::InitializeLogging()**. Example:
    ```cpp
    Environment.SetEnvironmentVariable("<YOUR_PROCESS_NAME>_CMD", "/enablewttlogging");
    LogController.InitializeLogging();
    ```

    ```cpp
    Environment.SetEnvironmentVariable("consoleapplication4_cmd", "/enablewttlogging");
    LogController.InitializeLogging();
    ```

-   If you would like to append to an existing wtt log file rather than overwrite it, also specify the /appendwttlogging option in addition to /enablewttlogging.

    ``` syntax
    te my.test.dll /enablewttlogging /appendwttlogging
    ```

    ```cpp
    Environment.SetEnvironmentVariable("<YOUR_PROCESS_NAME>_CMD", "/enablewttlogging /appendwttlogging");
    LogController.InitializeLogging();
    ```

    ```cpp
    Environment.SetEnvironmentVariable("consoleapplication4_cmd", "/enablewttlogging /appendwttlogging");
    LogController.InitializeLogging();
    ```

It is also possible to completely override or append to the default WttLogger device string by specifying one of the following command options:

/WttDeviceString:&lt;new device string&gt;   
Completely overrides the WttDeviceString used by WexLogger when it initializes WttLogger.

/WttDeviceStringSuffix:&lt;value to append to the device string&gt;   
Appends the specified value to the default WttDeviceString used by WexLogger when it initializes WttLogger. Ignored if '/WttDeviceString' is also specified.

The following table lists how WexLogger TestResults map to WttLogger results:

| WexLogger | WttLogger                      |
|-----------|--------------------------------|
| Passed    | WTT\_TESTCASE\_RESULT\_PASS    |
| NotRun    | WTT\_TESTCASE\_RESULT\_BLOCKED |
| Skipped   | WTT\_TESTCASE\_RESULT\_SKIPPED |
| Blocked   | WTT\_TESTCASE\_RESULT\_BLOCKED |
| Failed    | WTT\_TESTCASE\_RESULT\_FAIL    |



## Logger Dependencies


The native C++ logger (**Wex.Logger.dll**) is dependent upon **Wex.Common.dll** and **Wex.Communication.dll**.

The managed logger (**Wex.Logger.Interop.dll**) is dependent upon **Wex.Logger.dll**, **Wex.Common.dll** and **Wex.Communication.dll**.

Additionally, **WttLog.dll** is required when Wtt Logging is enabled.

## Additional Error Data


In the event that an error is logged, you can enable WexLogger to include one or more of the following items in addition to the error itself:

-   MiniDump
-   ScreenCapture
-   StackTrace

``` syntax
te my.test.dll /minidumponerror
```

``` syntax
te my.test.dll /screencaptureonerror /stacktraceonerror
```

With one or more of these options enabled, you will receive extra output every time Log::Error() is called.

Note: If you are consuming WexLogger outside the TAEF framework, you must set the **&lt;YOUR\_PROCESS\_NAME&gt;\_CMD** environment variable to contain these options before calling **LogController::InitializeLogging()**. Example:

```cpp
Environment.SetEnvironmentVariable("<YOUR_PROCESS_NAME>_CMD", "/screencaptureonerror /minidumponerror /stacktraceonerror");
LogController.InitializeLogging();
```

```cpp
Environment.SetEnvironmentVariable("consoleapplication4_cmd", "/screencaptureonerror /minidumponerror /stacktraceonerror");
LogController.InitializeLogging();
```

## C++ Error Handling


In order to shield test case authors from the burden of checking return values for each Log API call, the WexLogger reports unexpected error conditions via the use of an optional callback mechanism; a **WexLoggerErrorCallback** function. Upon initializaiton of the **WexLogger** (via **LogController::InitializeLogging()**), clients may choose to specify a **WexLoggerErrorCallback** function to call if unexpected error conditions occur within the **WexLogger**. The **WexLoggerErrorCallback** function must use the following signature:

```cpp
void __stdcall MyLoggerErrorCallback(const unsigned short* pszMessage, HRESULT hr);
```

A common use for the WexLoggerErrorCallback function would be to write out the error messages to the console (if your test harness is a console application). For example, the TAEF framework is a client of the **WexLogger**, and implements a **WexLoggerErrorCallback** which writes red text to the console when WexLogger errors occur.

## .NET 4.0 Compatibility


Wex.Logger.Interop is compiled as a NetFx 2/3/3.5 binary, so that it can be loaded into both NetFx 2/3/3.5 and NetFx 4 processes. This allows TAEF to run all managed assemblies above NetFx 2. If you're using Wex.Logger outside TAEF, then you need to add a [config file](https://msdn.microsoft.com/library/ms229689.aspx) for your exe to configure the NetFx 4 runtime to load NetFx 2/3/3.5 binaries into it's process. The config file should contain the following:

```cpp
<configuration> 
    <startup useLegacyV2RuntimeActivationPolicy="true">
        <supportedRuntime version="v4.0"/>
    </startup>
</configuration>
```

## Managed Code Error and Exception Handling


In order to shield test case authors from the burden of checking return values for each **Log** API call, the managed layer of the WexLogger reports unexpected error conditions via the use of the **LoggerController.WexLoggerError** event. You may subscribe to this event at any time by implementing your own **WexLoggerErrorEventHandler** and using the following familiar syntax for C# event subscription:

```cpp
LogController.WexLoggerError += new WexLoggerEventHandler(My_WexLoggerErrorHandler);
```

Here's an example of what your event handler might look like:

```cpp
static void LogController_WexLoggerError(object sender, WexLoggerErrorEventArgs e)
{
    ConsoleColor originalColor = Console.ForegroundColor;
    Console.ForegroundColor = ConsoleColor.Red;
    Console.WriteLine("LogController_WexLoggerError: " + e.Message);
    Console.ForegroundColor = originalColor;
}
```

Additionally, the **LogController::InitializeLogging()** and **LogController::FinalizeLogging()** methods themselves throw WexLoggerException in the event of failure. This provides detailed information on the error, and also allows you to abort the test run before it begins. Test case authors will never need to worry about catching these exceptions - they should be expected/handled during WexLogger initializaiton/completion only.









