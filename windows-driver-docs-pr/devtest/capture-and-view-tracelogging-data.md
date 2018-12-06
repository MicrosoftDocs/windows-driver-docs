---
title: Capture and view TraceLogging data
description: Capture and view TraceLogging data
ms.assetid: E5C18352-B05B-42BF-B5B8-12ABA0E6131C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Capture and view TraceLogging data


You can capture and view TraceLoggging data using the latest internal versions of the Windows Performance Tools (WPT). Before publishing your instrumentation, you should test your TraceLogging provider code to ensure that your event data is generated and is producing meaningful data at the appropriate times.

The process of verifying that the instrumentation is correct, involves these two steps:

-   Capture trace with Windows Performance Recorder (wpr.exe or wprui.exe).
-   View trace with the Windows Performance Analyzer (wpa.exe).

**Note**  For Windows Phone, you can also use Tracelog.exe and Xperf.exe to capture trace. See "To capture trace on Phone (using Tracelog and XPerf)" below.



### <span id="Prerequisites"></span><span id="prerequisites"></span><span id="PREREQUISITES"></span>Prerequisites

The WPR and WPA tools must be compatible with the version of the TraceLogging that you are linked against. If you are unable to capture or decode your events, it could be because the tools do not match and are not compatible.

### <span id="To_capture_trace_data_with_WPR"></span><span id="to_capture_trace_data_with_wpr"></span><span id="TO_CAPTURE_TRACE_DATA_WITH_WPR"></span>To capture trace data with WPR

1.  Create or edit a WPR profile (.wprp) for your TraceLoggingProvider.

    You can use the following example. Save the contents to a file with the .wprp file name extension. Replace the TODO sections with the appropriate values for your provider. For example, if you registered your provider by GUID, specify the GUID in this file.

    **Note**  For kernel mode providers, add NonPagedMemory="true" to the EventProvider Id element, see the comment in the following XML example.




Sample WPRP file:

```
<?xml version="1.0" encoding="utf-8"?>
<!-- TODO: 
1. Find and replace "WorkshopTraceLoggingProvider" with your component name.
2. See TODO below to update GUID for your event provider
-->
<WindowsPerformanceRecorder Version="1.0" Author="Microsoft Corporation" 
    Copyright="Microsoft Corporation" Company="Microsoft Corporation">
  <Profiles>
    <EventCollector Id="EventCollector_WorkshopTraceLoggingProvider" 
      Name="WorkshopTraceLoggingProviderCollector">
      <BufferSize Value="64" />
      <Buffers Value="4" />
    </EventCollector>

<!-- TODO: 
 1. Update Name attribute in EventProvider xml element with your provider GUID, 
    or if you specify an EventSource C# provider or call TraceLoggingRegister(...) 
    without a GUID, use star(*) before your provider name, 
    eg: Name="*MyEventSourceProvider" which will enable your provider appropriately.
 2. This sample lists more than 1 EventProvider xml element and references them again 
    in a Profile with EventProviderId xml element. For your component wprp, enable 
    the required number of providers and fix the Profile xml element appropriately
--> 
    <EventProvider Id="EventProvider_WorkshopTraceLoggingProvider" 
      Name="f9bc6c5d-4b98-43b5-90a1-1d0c8f45bf5a" />
<!-- For Kernel Mode providers, add NonPagedMemory="true" attribute to the 
  EventProvider Id element:

  Example:
  <EventProvider Id="EventProvider_UMDFReflector" 
    Name="263dd596-513b-4fd9-969c-022b691bb130" NonPagedMemory="true"/> 

-->

    <Profile Id="WorkshopTraceLoggingProvider.Verbose.File" 
      Name="WorkshopTraceLoggingProvider" Description="WorkshopTraceLoggingProvider" 
      LoggingMode="File" DetailLevel="Verbose">
      <Collectors>
        <EventCollectorId Value="EventCollector_WorkshopTraceLoggingProvider">
          <EventProviders>
<!-- TODO:
 1. Fix your EventProviderId with Value same as the Id attribute on EventProvider 
    xml element above
-->
            <EventProviderId Value="EventProvider_WorkshopTraceLoggingProvider" />
          </EventProviders>
        </EventCollectorId>
      </Collectors>
    </Profile>

    <Profile Id="WorkshopTraceLoggingProvider.Light.File" 
      Name="WorkshopTraceLoggingProvider" 
      Description="WorkshopTraceLoggingProvider" 
      Base="WorkshopTraceLoggingProvider.Verbose.File" 
      LoggingMode="File" 
      DetailLevel="Light" />

    <Profile Id="WorkshopTraceLoggingProvider.Verbose.Memory" 
      Name="WorkshopTraceLoggingProvider" 
      Description="WorkshopTraceLoggingProvider" 
      Base="WorkshopTraceLoggingProvider.Verbose.File" 
      LoggingMode="Memory" 
      DetailLevel="Verbose" />

    <Profile Id="WorkshopTraceLoggingProvider.Light.Memory" 
      Name="WorkshopTraceLoggingProvider" 
      Description="WorkshopTraceLoggingProvider" 
      Base="WorkshopTraceLoggingProvider.Verbose.File" 
      LoggingMode="Memory" 
      DetailLevel="Light" />

  </Profiles>
</WindowsPerformanceRecorder>
```


2.  For kernel mode providers, you need to add the NonPagedMemory="true" attribute to the EventProvider Id element.

    ```
    <EventProvider Id="EventProvider_myTraceLoggingProviderKM" 
      Name="263dd596-513b-4fd9-969c-022b691bb130" NonPagedMemory="true"/>
    ```

3.  Save the file with the file name extension (.WPRP).
4.  Start the capture using WPR from a Command Prompt window.

    ```
    <path to wpr>\wpr.exe -start GeneralProfile -start  yourTraceLoggingProvider.wprp
    ```

    The GeneralProfile will capture system events. For general debugging, it is a good idea to capture system events along with the events from your provider.

5.  Run your test scenario (load and unload the driver or component to trigger events).
6.  Stop trace capture and merge all recordings.

    ```
    <path to wpr>\wpr.exe -stop GeneralProfile -stop  yourTraceCaptureFile.etl description
    ```

You can also use Windows Performance Recorder user interface (Wprui.exe) to collect trace data.

```
<path to wpr>\wprui.exe
```

1.  On the WPR window, if the options are hidden, click **More Options**.
2.  Click **Add Profile** and browse to the location of your .wprp file.
3.  Select the .wprp file and click **Open**. WPR will validate the XML schema of your profile.
4.  Click **Start** and run your test scenario.
5.  Click **Save** to merge the results and save them to a file. If you use the WPR user interface, you are also given the option to open the .etl log file in WPA.

### <span id="To_capture_trace_on_Phone__using_Tracelog_and_XPerf_"></span><span id="to_capture_trace_on_phone__using_tracelog_and_xperf_"></span><span id="TO_CAPTURE_TRACE_ON_PHONE__USING_TRACELOG_AND_XPERF_"></span>To capture trace on Phone (using Tracelog and XPerf)

1.  Start trace capture of your provider.

    ```
    cmdd tracelog '-start test -f c:\test.etl -guid #providerguid'
    ```

2.  Run your test scenarios to log events.
3.  Stop trace capture.

    ```
    cmdd tracelog '-stop test'
    ```

4.  Merge trace results.

    ```
    cmdd xperf -merge c:\test.etl c:\testmerged.etl
    ```

5.  Retrieve the merged log file.

    ```
    getd c:\testmerged.etl
    ```

### <span id="View_TraceLogging_data_using_WPA"></span><span id="view_tracelogging_data_using_wpa"></span><span id="VIEW_TRACELOGGING_DATA_USING_WPA"></span>View TraceLogging data using WPA

Currently, WPA is the only viewer you can use to view the etl files that TraceLogging produces.

1.  Start WPA.

    ```
    <path to wpr>\wpa.exe
    ```

2.  Load the trace file (.etl).
3.  View your provider events. In the Graph Explorer, expand **System Activity**.
4.  Double-click **Generic Events** to view them in the Analysis view.
5.  In the Analysis view, locate the events from your provider to verify that logging is working.

    In the **Provider Name** column of the Generic Events table, find and select the row with your provider name.

    You can click the column header to sort by column name, which might make it easier to find your provider. When find your provider, right click on the name and select **Filter to Selection**.









